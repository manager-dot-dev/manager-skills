---
name: shadow-work
description: When the user notices their team consistently misses commitments despite apparent capacity, or wants to understand hidden capacity drains. Also use when the user says "team is always busy but nothing ships," "invisible work," "untracked work," "support requests consuming the team," "glue work," or "capacity planning is wrong."
metadata:
  version: 1.0.0
---

# Shadow Work

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

---

## What Shadow Work Is

Shadow work is the untracked capacity drain that makes teams consistently miss commitments without anyone understanding why. It falls into three types — each requires a different response.

---

## Type 1: Invisible Production Support

Ad-hoc incident triage, alert investigation, and support-team requests that never enter the ticket system.

Without tracking, patterns go unnoticed. The same 15-minute manual fix burns hundreds of hours annually while the root cause stays unfixed. The team appears to have capacity but consistently underdelivers — and has no data to show why.

**What to do:**
- Create a lightweight category for tracking unplanned support work — even just a tag in your ticketing system
- After 4–6 weeks of tracking, run a frequency analysis: what are the top 5 recurring issues? Prioritize fixing those root causes in the next planning cycle
- Rotate hot-fix responsibilities across the team rather than letting one person absorb them

---

## Type 2: Glue Work

Code reviews, mentoring, documentation, and coordination that lands disproportionately on senior engineers.

Glue work is rarely promotion-worthy in most performance review frameworks, which means it creates two problems simultaneously: the engineers doing it get burned out without recognition, and the engineers not doing it get promoted without learning it.

**What to do:**
- Make glue work visible in performance conversations — track and name it explicitly
- Actively distribute these skills downward through pairing and live review sessions; don't let them concentrate
- When fighting for a senior engineer's promotion, document the glue work they did — it is organizational value that often goes uncounted

---

## Type 3: The Shadow Backlog

Work that happens outside the official roadmap: PMs making off-the-record fix requests, engineers taking longer routes they know are right, unplanned integrations negotiated directly with other teams.

This can consume 40% of real capacity while quietly breaking capacity planning and eroding trust between business and engineering. Leadership sees a team that commits and misses — without understanding where the capacity went.

**What to do:**
- Make the shadow backlog explicit. In planning, ask: "What are we likely to get asked to do that we haven't scoped?" Budget 10–20% of capacity for it rather than pretending it doesn't exist
- For PMs making off-the-record requests: redirect to the official backlog. One-off favors that bypass planning are a symptom of a broken PM–EM relationship
- Periodically present the shadow backlog to stakeholders as evidence for capacity arguments

---

## The Remote Amplification Problem

For remote teams, shadow work is doubly invisible: your manager can't observe it either. This means you have no natural evidence when advocating for a team member's raise or promotion, and no visibility when capacity is being consumed.

Building lightweight tracking habits is therefore a management infrastructure investment, not overhead — it protects the team's ability to get credit for real work done.

---

## Related Skills

- `roadmap-planning` — Shadow work should be explicitly budgeted in capacity planning, not ignored
- `working-with-pm` — Off-the-record requests are a PM–EM relationship problem, not just a capacity problem
- `retaining-developers` — Senior engineers absorbing invisible glue work without recognition are in the "unappreciated" retention state
