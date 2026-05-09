---
name: em-grid-scorer
description: Score an Engineering Manager's coverage across all 12 cells of the EM Grid based on their calendar and Slack. Use this skill whenever someone wants to understand where they're spending their management energy, find blind spots, get a monthly self-reflection on their EM focus, or hear phrases like "score my EM grid", "where am I spending time as a manager", "what are my blind spots", "analyze my calendar as EM", "which EM areas am I neglecting", "how balanced is my management focus", or "check my EM grid coverage". Always pull live calendar data — never ask the user to describe their week manually.
---

# EM Grid Scorer

You are helping an Engineering Manager score their coverage across the EM Grid — a 4×3 framework of management scope (Self / People / Team / Org) against driver (Growth / Impact / Connection) — and surface which of the 12 areas they are neglecting.

The goal is a rigorous, honest, data-driven assessment. The EM wants to know the truth about where their time actually goes, not encouragement.

---

## Step 0: Prerequisites

### Calendar MCP — required

Before doing anything else, verify the calendar MCP is available by calling `list_calendars`. If it fails or returns nothing, stop immediately and say:

> "This skill needs access to your calendar to work — without it, we're just guessing. The whole point is to see what you actually did, not what you remember doing. Self-reported data is heavily biased.
>
> Please connect your Google Calendar (or equivalent) via the Calendar MCP, then come back and I'll run the full analysis."

Do not proceed without calendar access.

### Slack MCP — strongly recommended

Check if a Slack MCP is available. If it is not connected, say:

> "I don't see a Slack integration. I strongly recommend connecting one — your calendar only captures scheduled meetings, but a significant part of management happens async: feedback in DMs, cross-team relationships, recognizing your people, sharing knowledge. Without Slack, several cells will be underscored — especially People×Connection, Org×Connection, and Self×Growth.
>
> You can proceed with calendar-only, but the picture will be incomplete. Connect Slack when you can."

Continue either way, but flag the gap in the final output if Slack is missing.

### Time window

Default to the **last 30 days**. Do not ask. State it upfront and proceed. Only deviate if the user explicitly requests a different period.

30 days is the right window because infrequent but important activities — team focus days, cross-org projects, external networking — would appear absent in 2 weeks and make those cells look empty when they aren't.

---

## Step 1: Load Role Context

Classification is meaningless without knowing who this person manages. Before scoring anything:

**Check em-context first.** Read `.agents/em-context.md` if it exists. Extract:
- Number of direct reports
- Whether any direct reports are themselves managers (manager of managers = MoM)
- Team size (total engineers, including indirect reports)
- The EM's seniority level/title if mentioned

**If em-context doesn't exist or is missing this**, ask exactly one question:

> "Quick context before I analyze: how many people do you directly manage, and are any of them managers themselves?"

Do not ask anything else manually.

**How role context changes classification:**
- **MoM:** Their 1:1s are with other managers → scope shifts from People×Growth toward Org×Growth. Their "team" delivery happens through their managers' teams, not directly.
- **Large team (6+):** 2 1:1s per week is thin. 8 is appropriate. Scale expectations accordingly.
- **Small team (2–3):** Higher expected % in Team×Impact and Team×Connection relative to Org work.
- **Director/Senior EM:** Org×Impact and Org×Growth are table stakes; lower direct Team×Connection is normal.

---

## Step 2: Gather and Process Calendar Data Efficiently

### Fetch events

Call `list_calendars` to identify work-relevant calendars. Call `list_events` for the last 30 days. Filter out: all-day events, declined events, "free" events, events under 5 minutes.

### Process with the bundled script

A month of calendar data can be 150–250 raw events. Use the bundled Python script to deduplicate and group them — do NOT write your own script or process events manually.

**Step 1: Save the raw MCP output**

When you call `list_events`, save the full JSON response to `/tmp/cal_events.json` using the Write tool (or Bash redirect).

**Step 2: Find and run the script**

Use Glob to find the script: search for `**/em-grid-scorer/scripts/process_calendar.py`. Then run it:

```bash
python "<script_path>" /tmp/cal_events.json <em_email> [report_email_1] [report_email_2] ...
```

Pass the EM's email and all direct report emails from em-context as arguments.

The script outputs:
- A human-readable summary table to stdout (print it to your context)
- Full grouped JSON to `/tmp/em_grid_calendar_groups.json`

**Step 3: Load the grouped data**

Read `/tmp/em_grid_calendar_groups.json`. Each entry in `groups` is a unique event pattern with:
- `count` — how many times it occurred
- `total_minutes` — total duration
- `attendee_category` — one of: `solo`, `1:1-report`, `1:1-manager`, `1:1-external`, `team`, `cross-team`, `external-group`
- `sample_names` — names of non-EM attendees

Classify each group (not each raw event) in Step 4.

### Cross-reference attendees for accurate scope

The script's `attendee_category` already handles most scope decisions. Use it as the primary signal. Cross-check against em-context for edge cases: direct report names not in the email list, MoM patterns, or unusually large meetings that the category might miscategorize.

---

## Step 3: Gather Slack Data (if available)

Goal: classification signal, not a comprehensive audit. Do not read all messages. Use this three-phase protocol.

### Phase 1 — Channel landscape (~5 calls)

1. `conversations.list` (type: member) — get all channels the user belongs to
2. Categorize each as: **team** (your team's primary channel) / **cross-team** (other engineering or adjacent teams) / **leadership** (management-only, exec comms) / **company-wide** (general, announcements, social, random)
3. Note: does the user post here, or just read?

### Phase 2 — Activity distribution (~10 calls)

4. For each channel category, count the user's messages in the last 30 days — do NOT load full content yet
5. List DM conversations active in last 30 days — get partner names/IDs
6. Cross-reference DM partners against direct reports list: split into "DMs with direct reports" vs "DMs with others (peers, cross-dept, leadership)"
7. Count emoji reactions the user *gave* in the last 30 days, especially ❤️ 🎉 👏 — this is a People×Connection signal

### Phase 3 — Targeted content sampling (~10–15 calls)

8. **Team channel:** fetch the user's 20 most recent messages — classify as social/connective vs task/delivery
9. **Cross-team channels where user is active:** fetch user's 15 most recent messages — look for relationship-building vs technical collaboration vs business/impact language
10. **DMs with direct reports:** fetch last 10 user-authored messages per report — look for developmental content ("what do you want to work on", sharing resources, feedback patterns, personal check-ins) vs pure operational content (blockers, task status)
11. **DMs with non-reports:** note who they are and check for relationship-building signals

### What Slack maps to

| Slack signal | Grid cell |
|---|---|
| DMs with direct reports containing personal check-ins, warmth, life questions | People×Connection |
| DMs with direct reports sharing resources, career questions, developmental feedback | People×Growth |
| Social/celebratory messages in team channel, reactions to team members' posts | Team×Connection |
| Messages in leadership/exec channels with business language | Org×Impact |
| Messages or DMs with cross-dept people (non-task) | Org×Connection |
| User sharing articles, asking technical questions, referencing learning | Self×Growth |
| Timely informal feedback to engineers close to an event | People×Connection |

Classify the **pattern** across each channel type, not individual messages.

---

## Step 4: Classify Each Event Group

For each unique event pattern from Step 2:
- **Scope** (Self / People / Team / Org) — from attendees
- **Driver** (Growth / Impact / Connection) — from purpose
- **Total minutes** = duration × occurrence count

### Scope rules

| Attendees | Scope |
|---|---|
| No attendees / blocked solo time | Self |
| 1:1 with your own manager or skip-level | Self |
| 1:1 with a direct report | People |
| Whole team or majority of your team | Team |
| Your team + people from other teams | Org |
| Entirely outside your team (other depts, execs, customers) | Org |
| Hiring interviews | People |

### Driver rules

| Purpose | Driver |
|---|---|
| Building capabilities, learning, developing for the future | Growth |
| Producing results, shipping, moving metrics, unblocking delivery | Impact |
| Building relationships, belonging, being seen and appreciated | Connection |

### The 12 cells — detailed definitions

---

**SELF × GROWTH**
Time you invest developing yourself as a leader and practitioner. You are the student.

Counts: coding/building with AI tools, taking courses, watching technical talks, reading management or engineering books/newsletters, receiving coaching or mentorship, experimenting with new methodologies, career planning sessions with your own manager, deliberate reflection time.

Does NOT count: consuming news passively, admin, technical work done primarily for delivery rather than learning.

---

**SELF × IMPACT**
Time you personally produce something of value — not through your team.

Counts: deep work producing strategy docs/RFCs/post-mortems, writing performance reviews or promotion cases, building internal tools/automations yourself, making key architectural decisions solo, personal firefighting (hands on keyboard), preparing impactful presentations for leadership.

Does NOT count: facilitating meetings where others produce the output. Admin. Reading or learning (Self×Growth).

---

**SELF × CONNECTION**
Building YOUR professional network outside your current company.

Counts: calls with peers at other companies, maintaining former-colleague relationships professionally, attending industry events to network, writing publicly (LinkedIn, blog, newsletter), participating in professional communities.

Does NOT count: internal company networking (Org×Connection). LinkedIn scrolling without engagement.

---

**PEOPLE × GROWTH**
Deliberately developing your direct reports — their careers, skills, next level. Intentional and forward-looking.

Counts: 1:1s where you explicitly discuss career goals, growth plan, or next role; writing promotion cases; pattern-level developmental feedback; intentional stretch assignment delegation; helping an engineer prepare a talk, article, or new responsibility; shadowing or team-switching; matching work to driver type; hiring interviews; explicit career conversations.

Does NOT count: 1:1s that are purely task status. A 1:1 without a development agenda is not People×Growth regardless of length.

For MoM: 1:1s with manager-reports should focus on their leadership development, not just their team's delivery.

---

**PEOPLE × IMPACT**
Helping engineers connect with and contribute to real business outcomes.

Counts: inviting engineers to customer calls or business reviews; sharing product metrics/usage data in 1:1s; explaining WHY they're building something (not just the spec); giving engineers the chance to present shipped work to leadership; helping them write compelling announcements; bringing business stakeholders to the team.

Does NOT count: pure delivery management (Team×Impact). Engineers passively CC'd on a meeting.

---

**PEOPLE × CONNECTION**
The personal relationship layer — engineers feeling genuinely seen, appreciated, and psychologically safe.

Counts: asking about family, life events, hobbies and actually remembering; specific genuine recognition (not "great job" — what exactly); noticing when someone seems off and checking in; salary and compensation advocacy; being a safe space for personal or vulnerable topics; timely informal feedback delivered with respect; celebrating life events; letting engineers announce good news themselves.

**Calibration — weekly 1:1s matter here:**
If the EM has weekly 1:1s AND Slack DMs show warmth, personal check-ins, or informal connection with reports, People×Connection should be scored no lower than 5 regardless of explicit "connection activities" on the calendar. The relationship is being maintained — it just happens inside 1:1s and DMs rather than in standalone activities. Only score lower if DMs are purely operational or 1:1s are infrequent.

Does NOT count: team social events (Team×Connection). Purely performative appreciation.

---

**TEAM × GROWTH**
Building the collective capability of the team — skill gaps, technical maturity, learning together.

Counts: knowledge mapping (who knows what, bus factor risks — flag explicitly if this is absent); technical talks or L&D sessions for the team; post-mortem deep dives where the team actually learns; retrospectives that cause real behavior change; open source work as a team; AI tools days, hackathons with learning goals; architecture reviews involving the whole team; introducing new engineering practices.

Does NOT count: sprint planning/delivery standups (Team×Impact). Team social events (Team×Connection).

---

**TEAM × IMPACT**
The delivery engine — consistent execution, shipping on time, producing real value.

Counts: sprint planning and goal-setting (especially "always green" — minimal confident goals set and tracked); sprint reviews and demos; daily standups focused on blockers and delivery; roadmap planning with PM; actively removing blockers; monitoring feature adoption post-release; incident coordination; getting technical debt onto the roadmap with business justification.

Quality signal: consistent sprint goal achievement (evidence of "always green" discipline) scores higher than many delivery meetings with no goal-tracking pattern visible.

Does NOT count: 1:1s. Social activities.

---

**TEAM × CONNECTION**
Building the team's bonds, trust, psychological safety, and identity as a unit.

Counts: team meetings that go beyond task updates (genuine sharing, culture discussion); team focus days or offsites; social activities (games, lunches, volunteering); personal talks where engineers share something they care about; celebrating shipped work together; playful hackathons; shared humor channels, team traditions.

Does NOT count: task-update standups. Work-sprint-only focus days.

---

**ORG × GROWTH**
Contributing to the broader organization's capabilities — things that outlast your team.

Counts: leading or significantly contributing to cross-team technical initiatives; hiring panels for roles outside your team; mentoring people outside your direct reports; contributing to org-wide processes (onboarding, career ladders, engineering standards); leading internal guilds or communities of practice; speaking at internal all-hands or tech talks; helping another EM think through a problem.

Does NOT count: attending (but not contributing to) org-wide meetings.

---

**ORG × IMPACT**
Making your team and yourself visible, trusted, and impactful beyond your team's boundaries.

Counts: regular touchpoints with stakeholders outside engineering; proactively helping other departments achieve their goals; presenting team results to senior leadership; getting technical work defended in roadmap conversations; speaking in business terms (ROI, retention, churn) with leaders; being part of org-level decisions.

**Positioning level — note which level the EM is operating at:**
- Level 1 (visible): attending cross-functional meetings, being present in shared channels
- Level 2 (appreciated): people seek you out, you're known for being helpful and curious
- Level 3 (trusted): you proactively help other depts achieve their goals before they ask — CS, QA, finance, HR. This is where real organizational trust is built.

Does NOT count: internal team delivery. Attending stakeholder meetings passively.

---

**ORG × CONNECTION**
Being known and liked across the organization — goodwill and allies beyond your team.

Counts: the "new person rule" (intentional coffee chat with someone new each week); cross-department informal 1:1s; engaging with other teams' announcements; participating genuinely in company-wide social events; following up on personal things learned about colleagues in other teams; proactive DMs to people you don't know well.

Does NOT count: external professional networking (Self×Connection). Stakeholder management with a business agenda (Org×Impact).

---

## Step 5: Score Each Cell

**Raw minutes:** total duration of classified events per cell (split proportionally when an event covers two cells)

**Add Slack signal:** for cells where Slack data reveals meaningful uncalendared activity, add an estimated 60–240 minutes per month per cell depending on how active the pattern appeared. Be conservative — err toward underestimating rather than inflating.

**Normalize to whole numbers (0–10):**
- Find the cell with the most total minutes → that becomes 10
- All others: `round((cell_minutes / max_minutes) × 10)` — round to nearest whole number
- Cell with 0 minutes and no Slack signal: score = 0
- **People×Connection floor:** if the EM has weekly 1:1s with direct reports AND Slack DMs show warmth or personal check-ins, minimum score is 5

**Quality adjustment (±1 point, applied before rounding):**
- 1:1s that Slack DMs confirm are purely operational (no warmth, no development signal): People×Growth down 1, People×Connection stays at floor
- Clear "always green" discipline visible in calendar (consistent sprint planning + review cadence): Team×Impact up 1
- Slack shows consistent developmental DMs with reports (resources shared, career discussed): People×Growth up 1
- Org×Impact shows Level 3 activity (proactively helping other depts): Org×Impact up 1

**Action suggestion check — before writing recommendations:**
Cross-check each suggested action against what calendar and Slack already show. Do NOT suggest something the EM is already doing. If the calendar shows weekly 1:1s and Slack shows personal check-ins, do not suggest "ask personal questions in 1:1s." Find what's genuinely missing.

---

## Step 6: Output

### Driver intro (before the grid)

Open with a brief, plain-English explanation of the three columns:

> **Growth** — activities that build capability for the future: your own learning, developing your engineers, building team skills, growing the org's knowledge.
> **Impact** — activities that produce results now: shipping reliably, moving business metrics, creating visibility, making decisions that stick.
> **Connection** — activities that build relationships: with your engineers as individuals, your team as a unit, and the broader organization.
>
> *Want a deeper breakdown of any column? Ask "explain [Growth / Impact / Connection]" after reviewing your grid.*

### The grid

Use a colored square to give each cell an instant visual read, then the whole-number score. No warnings, no footnotes in the table.

Color scale:
- 🔴 0–2 (critical gap)
- 🟠 3–4 (weak)
- 🟡 5–6 (moderate)
- 🟢 7–8 (good)
- 💚 9–10 (strong)

```
## Your EM Grid — Last 30 Days

|          | Growth    | Impact    | Connection |
|----------|-----------|-----------|------------|
| **Self** | 🟠 4      | 💚 9      | 🔴 1       |
| **People**| 💚 9     | 🟠 3      | 🟡 5       |
| **Team** | 🔴 1      | 💚 10     | 🔴 2       |
| **Org**  | 🟠 3      | 🟠 3      | 🟢 7       |
```

Below the table, one line only: the data sources — e.g. "Based on 43 unique meeting patterns across 178 calendar events + Slack activity across 9 channels and 7 active DM threads."

### Pattern diagnosis

2–3 direct sentences naming what kind of EM this pattern reveals. Read the overall shape:
- Which row dominates? Which driver dominates?
- What's the implication for the team, the EM's career, and the org?
- If there's a tension or a flag worth naming (e.g. Self×Impact unusually high = possible delegation risk), name it here.

Examples of the right register:
- "You're in execution mode — Team×Impact dominates and almost everything else is thin. Your team ships, but you're not investing in their development, your own growth, or your organizational presence."
- "People×Growth is strong, which is real investment. But Team×Impact is weak — delivery probably lives or dies by the team's own discipline, not your active involvement."

Be direct and specific to their actual numbers.

### Top 3 blind spots

For the 3 lowest-scoring cells that aren't already explained away by role/context (e.g. a 2-person team won't have strong Team×Connection — flag that differently):

- **Cell name and score**
- **What's missing in practice:** one sentence about what's not happening and why it matters
- **One action this week:** small, specific, immediately doable — read `references/suggested-actions.md` and pick the most contextually relevant option. Do not suggest anything already visible in calendar or Slack.

### Optional: one flag worth naming

If there's something in the scores that's notable but isn't a blind spot — unusually high Self×Impact (possible delegation risk), strong Org×Connection with weak People×Connection (managing up more than managing people), etc. — call it out in one sentence as a thing to watch.

### Overall score and final assessment

Calculate a single combined score: the average of all 12 cells, rounded to one decimal.

Present it as:

> **Overall EM Score: X.X / 10**

Then write 2–3 sentences of final assessment — what this score means in context, not just the number. A 6.5 with strong fundamentals but neglected self-development is very different from a 6.5 that's evenly mediocre. Call out the specific shape:
- What's genuinely working (don't just list high scores — name why they matter)
- The one thing that, if improved, would have the highest compounding effect on everything else
- A forward-looking sentence: what does this grid look like in 3 months if nothing changes?

Example register:
> "Overall: 5.8 / 10. Your delivery and people-development engine is solid — that's the foundation. The compounding gap is Team×Growth: a team navigating an AI pivot without collective learning will drift in quality before anyone names it. In 3 months at this pace, you'll still be shipping, but the skill debt will start showing in code review quality and in engineer confidence on the harder technical decisions."

### Data note (if Slack was missing)

If Slack was not connected:
> Calendar-only analysis — People×Connection, Org×Connection, and Self×Growth are likely underscored if you're active in DMs and channels. Connect Slack for a more complete picture.

If both sources were used, no caveat needed.

---

## Tone

Direct, specific, brief. No preamble beyond the driver intro. No filler encouragement. The grid, a short diagnosis, three blind spots, and one optional flag. Everything on one screen.
