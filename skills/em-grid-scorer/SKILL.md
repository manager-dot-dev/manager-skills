---
name: em-grid-scorer
description: Score an Engineering Manager's coverage across all 12 cells of the EM Grid based on their calendar and Slack. Use this skill whenever someone wants to understand where they're spending their management energy, find blind spots, get a monthly self-reflection on their EM focus, or hear phrases like "score my EM grid", "where am I spending time as a manager", "what are my blind spots", "analyze my calendar as EM", "which EM areas am I neglecting", "how balanced is my management focus", or "check my EM grid coverage". Always pull live calendar data — never ask the user to describe their week manually.
---

# EM Grid Scorer

You are helping an Engineering Manager score their coverage across the EM Grid — a 4×3 framework of management scope (Self / People / Team / Org) against driver (Growth / Impact / Connection) — and surface which of the 12 areas they are neglecting.

The goal is a rigorous, honest, data-driven assessment. Do not be vague or encouraging for its own sake. The EM wants to know the truth about where their time actually goes.

---

## Step 0: Prerequisites

### Calendar MCP — required

Before doing anything else, verify the calendar MCP is available by calling `list_calendars`. If it fails or returns nothing, stop immediately and explain:

> "This skill needs access to your calendar to work — without it, we're just guessing. The whole point is to see what you actually did, not what you remember doing. Self-reported data is heavily biased.
>
> Please connect your Google Calendar (or equivalent) via the Calendar MCP, then come back and I'll run the full analysis."

Do not proceed without calendar access.

### Slack MCP — strongly recommended

Check if a Slack MCP is available. If it is, proceed with Slack data collection in Step 3. If it is not connected, say:

> "I don't see a Slack integration. I strongly recommend connecting one — calendar only captures scheduled meetings, but a big portion of your management work happens async: feedback in DMs, cross-team connections, recognizing people, sharing knowledge. Without Slack, scores for People×Connection, Org×Connection, and Self×Growth will likely be underestimated.
>
> You can still proceed with calendar-only, but the picture will be incomplete — especially for the connection-type cells. Connect Slack when you can for a more accurate read."

Continue either way — but flag the gap in the final output if Slack is missing.

### Time window

Default to the **last 30 days**. Do not ask the user to choose — just use 30 days and state it upfront. Only deviate if the user explicitly asks for a different period.

30 days is the right window because: some important activities (team focus days, cross-team projects, org-level work) are infrequent enough that 2 weeks would miss them entirely and make those cells look empty when they aren't.

---

## Step 1: Load Role Context

Before classifying anything, you need to understand who this person manages. Classification is meaningless without it — a 1:1 with a direct report who manages 5 engineers themselves is very different from a 1:1 with an IC.

**Check em-context first.** Read `.agents/em-context.md` if it exists. Extract:
- Number of direct reports
- Whether any direct reports are themselves managers (manager of managers = MoM)
- Team size (total engineers, including indirect)
- The EM's own level/title if mentioned

**If em-context doesn't exist or doesn't have this information**, do not ask the user a long list of questions. Ask exactly one thing:

> "Quick context before I analyze: how many people do you directly manage, and are any of them managers themselves?"

Use the answer to calibrate classification throughout. Do not ask anything else manually.

**How role context affects classification:**
- **Manager of managers:** Their 1:1s are likely with other EMs → scope shifts from People×Growth to Org×Growth. Their Team×Impact may be indirect (through their reports' teams).
- **Large team (6+):** Having only 2 1:1s per week looks thin. Having 8 looks appropriate.
- **Small team (2-3):** Higher expected % of time in Team×Impact and Team×Connection relative to Org.
- **Director/Senior EM:** Org×Impact and Org×Growth are more expected; lower Team×Connection involvement is normal.

---

## Step 2: Gather and Process Calendar Data Efficiently

### Fetch events

Call `list_calendars` to identify work-relevant calendars (skip personal, holiday, birthday). Then call `list_events` for the last 30 days across those calendars.

Filter out:
- All-day events (holidays, OOO, reminders)
- Events the user declined
- Events marked as "free"
- Events under 5 minutes

### Deduplicate recurring events — critical for efficiency

A month of calendar data can contain 150–250 raw events, but most EMs have highly repetitive calendars. Do not classify each event individually. Instead:

1. **Normalize titles** by stripping variable parts: names, dates, sprint numbers, ticket IDs
   - "1:1 with Alice", "1:1 with Bob", "1:1 - Carol" → all become `1:1 (direct report)` if those names are direct reports
   - "Sprint 42 Planning", "Sprint 43 Planning" → `Sprint Planning`
   - "Sync with [external person]" → `External Sync`

2. **Group by normalized title + attendee pattern** (solo / 1:1-with-report / whole-team / cross-team / external)

3. **Classify each unique group once**, then multiply by the number of occurrences and total duration

4. This reduces 200 raw events to roughly 20–40 unique patterns — classify those, not 200 individual rows

### Cross-reference attendees

For accurate scope assignment, compare event attendees against:
- Direct reports (from em-context or Step 1 answer)
- The EM's own manager (if known from em-context)
- Email domains: same company domain = internal, different = external

This determines whether a meeting is Self / People / Team / Org scope — don't guess from title alone when attendee data is available.

---

## Step 3: Gather Slack Data (if available)

The goal is classification signal, not a comprehensive audit. Do not read every message. Use this efficient extraction protocol.

### Phase 1 — Channel landscape (~5 calls)

1. `conversations.list` (type: member) → get all channels/groups the user is a member of
2. Categorize each channel:
   - **Team channel**: contains your team name, engineering team, or your direct reports are the primary members
   - **Cross-team channel**: engineering-adjacent channels with people from other teams
   - **Leadership/exec channel**: management-only, exec comms, leadership sync
   - **Company-wide**: all-hands, announcements, social, random, general
3. For each channel, note: does the user post here, or just read?

### Phase 2 — Activity distribution (~10 calls)

4. For each channel category, get the user's message count in the last 30 days (use `conversations.history` with pagination, count only messages authored by the user — do NOT load full content yet)
5. List DM conversations active in last 30 days (`conversations.list` type: im) → get the partner's display name or ID for each
6. Cross-reference DM partners against the direct reports list from em-context: split into "DMs with direct reports" vs "DMs with others"

### Phase 3 — Targeted content sampling (~10–15 calls)

7. For the **team channel**: fetch the user's 20 most recent messages. Look for: social/personal content (celebrations, check-ins, GIFs, reactions) vs task/delivery content
8. For **cross-team channels where user is active**: fetch user's 15 most recent messages. Look for: relationship-building vs technical collaboration vs business/impact language
9. For **DMs with direct reports**: fetch last 10 messages per report in the last 30 days. Look for: developmental content ("what do you want to work on", sharing resources, feedback patterns) vs operational content (task updates, blockers)
10. For **DMs with non-reports**: note who they are (cross-dept peers, leadership, external) and check for relationship-building signals
11. Count reactions the user has **given** in the last 30 days (especially ❤️ 🎉 👏 in team/people channels — this is a People×Connection signal)

### What Slack data maps to

| Slack signal | Grid cell |
|---|---|
| DMs with direct reports that are personal, supportive, or developmental | People×Connection or People×Growth |
| Social/celebratory messages in team channel | Team×Connection |
| Messages in leadership/exec channels with business language | Org×Impact |
| Messages or DMs with cross-dept people (not task-related) | Org×Connection |
| User sharing articles, learning content, asking technical questions | Self×Growth |
| Reactions given to direct reports (❤️ 🎉 👏) | People×Connection |
| Cross-team channel activity with technical substance | Org×Growth |

Do not try to classify individual messages — classify the **pattern** across each channel type.

---

## Step 4: Classify Each Event Group

For each unique event pattern from Step 2, determine:
- **Scope** (Self / People / Team / Org) — from attendees
- **Driver** (Growth / Impact / Connection) — from purpose
- **Total minutes** = duration × occurrence count

### Scope rules — attendees are the clearest signal

| Attendees | Scope |
|---|---|
| No attendees / blocked solo time | Self |
| 1:1 with your own manager or skip-level | Self |
| 1:1 with a direct report | People |
| Whole team or majority of team present | Team |
| Your team + people from other teams | Org |
| Entirely outside your team (other depts, execs, customers) | Org |
| Hiring interviews | People |

### Driver rules — purpose is the key signal

| Purpose | Driver |
|---|---|
| Building capabilities, learning, developing skills for the future | Growth |
| Producing results, shipping, moving metrics, unblocking delivery | Impact |
| Building relationships, belonging, being seen and appreciated | Connection |

### The 12 cells — detailed definitions

These are the classification engine. Read the relevant cell when a meeting is ambiguous.

---

**SELF × GROWTH**
Time you invest developing yourself as a leader and practitioner. You are the student.

Counts: coding/building with AI tools, taking courses, watching technical talks, reading books/newsletters, receiving coaching or mentorship, experimenting with new methodologies, career planning sessions with your own manager, deliberate self-reflection time.

Does NOT count: news consumption, admin tasks, technical work done primarily for delivery (not learning).

Calendar undercount risk: HIGH — reading and async learning almost never appear on calendars.

---

**SELF × IMPACT**
Time you personally produce something of value — not through your team, but by your own direct contribution.

Counts: deep work blocks producing strategy docs/RFCs/post-mortems, writing performance reviews or promotion cases, building internal tools/dashboards/automations yourself, making key architectural decisions solo, personal firefighting (hands on keyboard), preparing impactful presentations for leadership.

Does NOT count: facilitating meetings where others produce the output, admin busy-work.

Calendar undercount risk: MODERATE — deep work often happens in fragments between meetings.

---

**SELF × CONNECTION**
Building YOUR professional network outside your current company — relationships that benefit your career and perspective.

Counts: calls with peers at other companies, maintaining former-colleague relationships professionally, attending industry events to network, writing publicly (LinkedIn, blog, newsletter), participating in professional communities.

Does NOT count: internal company networking (that's Org×Connection).

Calendar undercount risk: VERY HIGH — external professional networking is almost never calendared.

---

**PEOPLE × GROWTH**
Deliberately developing your direct reports — their careers, skills, and next level. Intentional and forward-looking, not task management.

Counts: 1:1s where you explicitly discuss career goals, growth plan, or next role; writing/preparing promotion cases; giving meaningful developmental feedback (pattern-level, not incident-level); delegating stretch assignments intentionally; helping an engineer prepare a talk, article, or new responsibility; setting up shadowing or team-switching; matching work to driver type; hiring interviews; explicit career conversations.

Does NOT count: 1:1s that are purely task status updates. A 1:1 without a development agenda is not People×Growth regardless of length.

Scoring note for MoM: if their direct reports are other managers, People×Growth includes coaching those managers on their own leadership, not just IC development.

---

**PEOPLE × IMPACT**
Helping your engineers connect with and contribute to real business outcomes — not just shipping code, but shipping things that matter and get noticed.

Counts: inviting engineers to customer calls or business reviews; sharing product metrics/usage data in 1:1s; explaining WHY they're building something (not just the spec); giving engineers the chance to present shipped work to leadership; helping them write compelling announcements; bringing business stakeholders to talk to the team.

Does NOT count: pure delivery management (Team×Impact). Engineers passively CC'd on a meeting.

---

**PEOPLE × CONNECTION**
The personal relationship layer — knowing engineers as human beings, making them feel genuinely seen and psychologically safe.

Counts: asking about family, life events, hobbies and remembering; specific genuine recognition (not "great job" but what exactly); proactively noticing when someone seems off; salary conversations and compensation advocacy; being a safe space for personal or vulnerable topics; casual timely standup-style feedback delivered with respect; celebrating life events; letting engineers announce good news themselves.

Does NOT count: team social events (Team×Connection). Purely performative appreciation.

Calendar undercount risk: HIGH — most happens in the last 5 minutes of a 1:1, in DMs, or informally.

---

**TEAM × GROWTH**
Building the collective capability of the team — closing skill gaps, growing technical maturity, learning together.

Counts: knowledge mapping (who knows what, bus factor risks); organizing technical talks or L&D sessions for the team; post-mortem deep dives where the team actually learns; retrospectives that cause real behavior change; open source work as a team; AI tools days, hackathons with learning goals; architecture reviews involving the whole team; introducing new engineering practices.

Does NOT count: sprint planning or delivery standups (Team×Impact). Team social events (Team×Connection).

---

**TEAM × IMPACT**
The delivery engine — the team consistently executes, ships on time, and produces real value.

Counts: sprint planning and goal-setting (especially "always green" — minimal confident goals); sprint reviews and demos; daily standups focused on blockers and delivery; roadmap planning and prioritization with PM; actively removing blockers; monitoring feature adoption after releases; incident coordination; getting technical debt onto the roadmap with business justification; working with PM to scope down for reliable delivery.

Does NOT count: 1:1s (even delivery-focused ones). Social activities.

---

**TEAM × CONNECTION**
Building the team's bonds, trust, psychological safety, and identity as a unit.

Counts: team meetings with genuine sharing and discussion (not just task updates); team focus days or offsites; social activities (games, lunches, volunteering); personal talks where engineers share something they care about; celebrating shipped work together; playful hackathons; team memory walls, shared humor channels.

Does NOT count: task-update standups. Focus days that are purely work sprints.

---

**ORG × GROWTH**
Your contribution to building the broader organization's capabilities — things that outlast your team.

Counts: leading or significantly contributing to cross-team technical initiatives; hiring panels for roles outside your team; mentoring people who are not your direct reports; contributing to org-wide processes (onboarding, career ladders, engineering standards); leading internal guilds or communities of practice; speaking at internal all-hands or tech talks; helping another EM think through a problem.

Does NOT count: your own team's technical work. Attending (but not contributing to) org-wide meetings.

---

**ORG × IMPACT**
Making your team and yourself visible, trusted, and impactful beyond your team's boundaries.

Counts: regular touchpoints with stakeholders outside engineering (product, CS, support, finance, HR); proactively helping other departments achieve their goals; presenting team results to senior leadership; getting technical work defended in roadmap conversations; cross-functional projects where you are a decision-maker; speaking in business terms (ROI, retention, churn) with leaders; being part of org-level decisions.

Does NOT count: internal team delivery work. Attending stakeholder meetings passively.

---

**ORG × CONNECTION**
Being known and liked across the organization — building goodwill and allies beyond your team.

Counts: the "new person rule" (intentional coffee chat with someone new each week); cross-department informal 1:1s; engaging with announcements from other teams; participating genuinely in company-wide social events; following up on personal things learned about colleagues in other teams; proactive DMs to people you don't know well.

Does NOT count: building your own external professional network (Self×Connection). Stakeholder management with a business agenda (Org×Impact).

Calendar undercount risk: VERY HIGH — almost all Org×Connection happens in Slack or informal conversations.

---

## Step 5: Score Each Cell

**Raw minutes:** total duration of all classified events in that cell (split duration proportionally when an event covers two cells)

**Add Slack signal:** for cells where Slack data revealed meaningful activity not on the calendar, add an estimated 30–90 minutes per week (120–360 minutes per month) per cell, based on how active the pattern appeared. Be conservative.

**Normalized score (0–10):**
- Find the cell with the most total minutes → that becomes 10
- All others: `score = (cell_minutes / max_minutes) × 10`, rounded to nearest 0.5
- Cell with 0 minutes and no Slack signal: score = 0

**Quality adjustment (±1 point):**
- 1:1s that appear to be pure task check-ins (no developmental signal in Slack DMs either): adjust People×Growth down by 1
- Standups that are clearly just status-read-outs: adjust Team×Impact down by 0.5
- Any cell with clear high-quality intentional activity (e.g. Slack shows consistent developmental DMs): adjust up by 1

**Flag cells with undercount risk:** add ⚠️ to cells where calendar likely misses real activity (Self×Growth, Self×Connection, People×Connection, Org×Connection)

---

## Step 6: Output

### Grid table

```
## Your EM Grid — Last 30 Days

|  | Growth | Impact | Connection |
|---|---|---|---|
| **Self** | X/10 ⚠️ | X/10 | X/10 ⚠️ |
| **People** | X/10 | X/10 | X/10 ⚠️ |
| **Team** | X/10 | X/10 | X/10 |
| **Org** | X/10 | X/10 | X/10 ⚠️ |
```

⚠️ = calendar underrepresents this cell; actual score may be higher.

Below the table, add one line: the data it's based on — e.g. "Based on 47 unique meeting patterns (from 183 calendar events) + Slack activity across 12 channels and 8 DM threads."

### Pattern diagnosis

2–3 honest sentences naming what kind of EM this pattern reveals. Examples of what this should sound like:
- "You're in execution mode — Team×Impact dominates and almost everything else is thin. Your team ships, but you're not investing in their development, your own growth, or your organizational presence."
- "You spend most of your time developing your people, which is real and valuable — but Team×Impact is weak, which means delivery probably lives or dies by the team's own discipline, not your active involvement."
- "You're organizationally well-connected but your own team may be feeling it. The bottom two rows of the grid are strong; the top two are thin."

Be direct. This is the highest-value part of the output.

### Top 3 blind spots

For each of the 3 lowest-scoring cells:
- **Cell name**
- **What's missing in practice:** one specific sentence about what's not happening
- **One action this week:** small, specific, immediately doable. Read `references/suggested-actions.md` and pick the most relevant to what you know about this EM from their calendar patterns.

### Accuracy note

If Slack was not available:
> ⚠️ Calendar-only analysis. Cells marked ⚠️ are likely underscored — if you're active in Slack, the real scores there are probably higher. Connecting Slack will significantly improve accuracy, especially for connection-type cells.

If both were available, no caveat needed — just note what was included.

---

## Tone

Direct, specific, brief. No preamble, no filler encouragement. The EM is a professional who wants signal, not comfort. Target: everything fits on one screen after the grid.
