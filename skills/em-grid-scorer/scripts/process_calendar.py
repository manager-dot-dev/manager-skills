#!/usr/bin/env python3
"""
EM Grid Calendar Processor

Reads a calendar events JSON file (from the Google Calendar MCP list_events tool),
deduplicates recurring events, groups by title pattern + attendee category, and
outputs a clean summary for EM Grid classification.

Usage:
    python process_calendar.py <events_json_file> <em_email> [report_email ...]

    <events_json_file>  Path to the JSON file saved from list_events MCP output.
                        Pass - to read from stdin.
    <em_email>          The EM's own email address.
    [report_email ...]  Email addresses of direct reports (space-separated).

Output:
    Prints a human-readable summary of unique event patterns to stdout.
    Also writes full JSON output to /tmp/em_grid_calendar_groups.json.

Example:
    python process_calendar.py /tmp/cal.json anton@company.com \
        alice@company.com bob@company.com carol@company.com
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta


MIN_DURATION_MINUTES = 5


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def extract_events(data):
    """Return the flat list of event dicts from whatever structure the MCP returns."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("events", "items", "results", "data", "value"):
            val = data.get(key)
            if isinstance(val, list):
                return val
        # Some MCPs wrap in a top-level 'result' or 'content' key
        for key in ("result", "content", "response"):
            val = data.get(key)
            if val:
                return extract_events(val)
    return []


def parse_dt(dt_str):
    """Parse an ISO 8601 datetime string, handling Z and offset formats."""
    if not dt_str:
        return None
    s = str(dt_str).strip()
    s = s.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        return None


def get_duration_minutes(event):
    """Return duration in minutes. Returns 0 for all-day events or parse failures."""
    start = event.get("start") or {}
    end = event.get("end") or {}

    start_str = start.get("dateTime") or start.get("datetime")
    end_str = end.get("dateTime") or end.get("datetime")

    # All-day events use 'date' not 'dateTime'
    if not start_str or not end_str:
        return 0

    start_dt = parse_dt(start_str)
    end_dt = parse_dt(end_str)
    if not start_dt or not end_dt:
        return 0

    delta = end_dt - start_dt
    minutes = int(delta.total_seconds() / 60)
    return max(0, minutes)


# ---------------------------------------------------------------------------
# Event filtering
# ---------------------------------------------------------------------------

def is_declined_by_em(event, em_email):
    """True if the EM's own RSVP is 'declined'."""
    em_lower = em_email.lower()
    for attendee in event.get("attendees") or []:
        if (attendee.get("email") or "").lower() == em_lower:
            if attendee.get("responseStatus") == "declined":
                return True
    return False


def is_free_time(event):
    """True if the event is marked as free (transparency = transparent)."""
    return (event.get("transparency") or "").lower() == "transparent"


def is_all_day(event):
    """True if the event has no time component (all-day)."""
    start = event.get("start") or {}
    return "dateTime" not in start and "datetime" not in start


def should_include(event, em_email):
    """Return True if the event should be counted in the analysis."""
    if is_all_day(event):
        return False
    if is_free_time(event):
        return False
    if is_declined_by_em(event, em_email):
        return False
    if get_duration_minutes(event) < MIN_DURATION_MINUTES:
        return False
    # Skip events with status = cancelled
    if (event.get("status") or "").lower() == "cancelled":
        return False
    return True


# ---------------------------------------------------------------------------
# Title normalisation
# ---------------------------------------------------------------------------

# Patterns to strip from titles to get a canonical group key
_STRIP_PATTERNS = [
    # Sprint / iteration numbers: "Sprint 42", "S42", "Iteration 7"
    (r"\b(sprint|iteration|iter|week|s)\s*\d+\b", r"\1 N", re.IGNORECASE),
    # Quarter references: "Q1 2024", "Q3"
    (r"\bq[1-4](\s+\d{4})?\b", "QN", re.IGNORECASE),
    # Date patterns: "2024-01-15", "Jan 15", "15/01"
    (r"\b\d{4}-\d{2}-\d{2}\b", ""),
    (r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\s+\d{1,2}\b", "", re.IGNORECASE),
    (r"\b\d{1,2}/\d{1,2}(/\d{2,4})?\b", ""),
    # Ticket IDs: "PROJ-123", "ENG-4567"
    (r"\b[A-Z]{2,10}-\d+\b", ""),
    # Version numbers: "v1.2", "v3"
    (r"\bv\d+(\.\d+)*\b", "", re.IGNORECASE),
    # "with <Name>" patterns
    (r"\bwith\s+[A-Z][a-z]+\b", "with EM", 0),
    # Trailing/leading punctuation and extra spaces
    (r"[\-–—:|]\s*$", ""),
    (r"^\s*[\-–—:|]\s*", ""),
]

# Compiled once
_COMPILED_STRIPS = [
    (re.compile(pat, flags if len(t) == 3 else 0), repl)
    for t in _STRIP_PATTERNS
    for pat, repl, *flags in [(t[0], t[1], t[2] if len(t) == 3 else 0)]
]

_1ON1_RE = re.compile(r"1\s*[:/]\s*1|one.on.one|1-on-1", re.IGNORECASE)
_STANDUP_RE = re.compile(r"\bstand.?up\b|\bdaily\b|\bmorning\s+sync\b", re.IGNORECASE)
_PLANNING_RE = re.compile(r"\bplanning\b", re.IGNORECASE)
_RETRO_RE = re.compile(r"\bretro(spective)?\b", re.IGNORECASE)
_REVIEW_RE = re.compile(r"\b(sprint|demo|ship|release)\s*(review|demo|showcase)\b", re.IGNORECASE)
_INTERVIEW_RE = re.compile(r"\binterview\b", re.IGNORECASE)
_ALLHANDS_RE = re.compile(r"\ball.hands?\b|\btown.?hall\b|\bcompany.?meeting\b", re.IGNORECASE)
_FOCUS_RE = re.compile(r"\bfocus\s*(time|block|hours?)\b|\bdeep\s+work\b|\bno\s+meetings?\b|\bblocked?\b", re.IGNORECASE)


def normalize_title(raw_title):
    """Return a canonical group key for an event title."""
    if not raw_title:
        return "Untitled"

    title = raw_title.strip()

    # Shortcut for known patterns before stripping
    if _1ON1_RE.search(title):
        return "1:1"
    if _STANDUP_RE.search(title):
        return "Daily Standup"
    if _RETRO_RE.search(title):
        return "Retrospective"
    if _PLANNING_RE.search(title):
        return "Sprint Planning"
    if _REVIEW_RE.search(title):
        return "Sprint Review / Demo"
    if _INTERVIEW_RE.search(title):
        return "Interview"
    if _ALLHANDS_RE.search(title):
        return "All Hands / Company Meeting"
    if _FOCUS_RE.search(title):
        return "Focus / Deep Work Block"

    # General stripping
    for pattern, repl in _COMPILED_STRIPS:
        title = pattern.sub(repl, title)

    title = re.sub(r"\s+", " ", title).strip()
    return title if title else raw_title.strip()


# ---------------------------------------------------------------------------
# Attendee categorisation
# ---------------------------------------------------------------------------

def get_domain(email):
    """Return the domain part of an email, or empty string."""
    email = (email or "").lower().strip()
    return email.split("@")[-1] if "@" in email else ""


def categorize_attendees(event, em_email, direct_reports_set):
    """
    Returns one of:
        solo            - no other attendees
        1:1-report      - one-on-one with a direct report
        1:1-manager     - one-on-one with someone not a report (likely manager / peer)
        1:1-external    - one-on-one with someone outside the company
        team            - mostly direct reports (>=50% of non-EM attendees)
        cross-team      - mixed internal people, most not reports
        external-group  - group meeting with external participants
    """
    em_lower = em_email.lower()
    em_domain = get_domain(em_lower)

    # Other attendees who accepted (or have no RSVP = tentative/no response counts)
    others = [
        a for a in (event.get("attendees") or [])
        if (a.get("email") or "").lower() != em_lower
        and a.get("responseStatus") != "declined"
    ]

    if not others:
        return "solo"

    if len(others) == 1:
        other_email = (others[0].get("email") or "").lower()
        if other_email in direct_reports_set:
            return "1:1-report"
        if get_domain(other_email) != em_domain:
            return "1:1-external"
        return "1:1-manager"

    # Multiple attendees
    emails = [(a.get("email") or "").lower() for a in others]
    report_count = sum(1 for e in emails if e in direct_reports_set)
    external_count = sum(1 for e in emails if get_domain(e) != em_domain and get_domain(e))

    if external_count > 0:
        return "external-group"
    if len(others) > 0 and report_count / len(others) >= 0.5:
        return "team"
    return "cross-team"


def get_sample_names(event, em_email, max_names=3):
    """Return up to max_names display names of non-EM attendees."""
    em_lower = em_email.lower()
    names = []
    for a in (event.get("attendees") or []):
        if (a.get("email") or "").lower() == em_lower:
            continue
        name = a.get("displayName") or a.get("email") or ""
        if name:
            names.append(name.split("@")[0])  # strip domain for readability
        if len(names) >= max_names:
            break
    return names


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------

def process(events_data, em_email, direct_reports):
    """
    Filter, deduplicate, and group calendar events.

    Returns a dict with:
        total_raw       - number of events in the input
        total_filtered  - number after filtering
        skipped         - breakdown of why events were skipped
        unique_patterns - number of unique (title, attendee_category) groups
        groups          - ordered dict of group_key -> group stats
    """
    all_events = extract_events(events_data)
    direct_reports_set = {e.lower() for e in direct_reports}

    filtered = []
    skipped = {"all_day": 0, "too_short": 0, "declined": 0, "free": 0, "cancelled": 0}

    for event in all_events:
        if is_all_day(event):
            skipped["all_day"] += 1
            continue
        duration = get_duration_minutes(event)
        if duration < MIN_DURATION_MINUTES:
            skipped["too_short"] += 1
            continue
        if is_declined_by_em(event, em_email):
            skipped["declined"] += 1
            continue
        if is_free_time(event):
            skipped["free"] += 1
            continue
        if (event.get("status") or "").lower() == "cancelled":
            skipped["cancelled"] += 1
            continue

        filtered.append({
            "raw_title": event.get("summary") or "",
            "duration": duration,
            "attendees": event.get("attendees") or [],
            "description_snippet": (event.get("description") or "")[:150],
        })

    # Group by (normalized_title, attendee_category)
    groups = defaultdict(lambda: {
        "count": 0,
        "total_minutes": 0,
        "attendee_category": "",
        "sample_names": [],
        "raw_titles": [],
    })

    for ev in filtered:
        norm = normalize_title(ev["raw_title"])
        cat = categorize_attendees({"attendees": ev["attendees"]}, em_email, direct_reports_set)
        key = f"{norm} [{cat}]"

        g = groups[key]
        g["count"] += 1
        g["total_minutes"] += ev["duration"]
        g["attendee_category"] = cat

        raw = ev["raw_title"]
        if raw and raw not in g["raw_titles"]:
            g["raw_titles"].append(raw)

        if not g["sample_names"]:
            g["sample_names"] = get_sample_names({"attendees": ev["attendees"]}, em_email)

    # Sort by total minutes descending
    sorted_groups = dict(
        sorted(groups.items(), key=lambda x: x[1]["total_minutes"], reverse=True)
    )

    return {
        "em_email": em_email,
        "direct_reports": list(direct_reports),
        "total_raw": len(all_events),
        "total_filtered": len(filtered),
        "skipped": skipped,
        "unique_patterns": len(sorted_groups),
        "groups": sorted_groups,
    }


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def print_summary(result):
    print(f"\nEM: {result['em_email']}")
    print(f"Direct reports loaded: {len(result['direct_reports'])}")
    print(f"Raw events: {result['total_raw']}  |  After filtering: {result['total_filtered']}  |  Unique patterns: {result['unique_patterns']}")
    print(f"Skipped: {result['skipped']}")
    print()

    header = f"{'Pattern':<52} {'N':>4} {'Min':>7}  {'Category':<16}  {'Sample names'}"
    print(header)
    print("-" * len(header))

    for pattern, g in result["groups"].items():
        names_str = ", ".join(g["sample_names"][:2]) if g["sample_names"] else ""
        raw_examples = " / ".join(g["raw_titles"][:2]) if g["raw_titles"] else ""
        display_names = names_str or raw_examples
        print(
            f"{pattern[:50]:<52} {g['count']:>4} {g['total_minutes']:>7}  "
            f"{g['attendee_category']:<16}  {display_names[:40]}"
        )

    print()
    print(f"Full JSON written to /tmp/em_grid_calendar_groups.json")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    events_file = sys.argv[1]
    em_email = sys.argv[2]
    direct_reports = sys.argv[3:]

    if events_file == "-":
        data = json.load(sys.stdin)
    else:
        with open(events_file, encoding="utf-8") as f:
            data = json.load(f)

    result = process(data, em_email, direct_reports)

    print_summary(result)

    # Write full JSON for Claude to reference
    output_path = "/tmp/em_grid_calendar_groups.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
