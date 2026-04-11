---
name: team-health
description: Helps engineering managers assess and improve team health across morale, cohesion, delivery culture, and engagement — produces Google's 5 Factors (Project Aristotle), a 4-state team health diagnosis (Falling Behind / Treading Water / Repaying Debt / Innovating), a 5-zone intensity model, the Engagement Stack, the Trust Battery, Teamicide patterns (Peopleware), a blameless postmortem format, and a library of team activities organized by driver. Use when the user says "team morale," "team is struggling," "burnout," "engagement," "attrition risk," "psychological safety," "team dynamics," "something feels off," "team culture," "team is unhappy," "retros aren't working," "team isn't working hard enough," "ideas for team activities," or "how do I run a team offsite." Do NOT use for individual performance concerns (use `managing-high-performers`), team staffing or hiring (use `team-composition`), or individual motivation interventions (use `engineer-motivation`).
metadata:
  version: 2.1.2
---

# Team Health

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

If `.agents/em-context.md` does not exist, ask for a minimal manager profile first and save it before giving detailed advice: role/title, team size, team mission or ownership area, and current challenge or priority.

If a specific person is central to the conversation and `.agents/reports/[name].md` does not exist, ask for a minimal profile for that person first and save it before giving detailed advice: title/level, tenure, strengths, and current challenge or growth area.

If the conversation reveals durable new context later, update `.agents/em-context.md` or `.agents/reports/[name].md` automatically. Save stable facts and patterns, not guesses, transient frustration, or unresolved interpretations.
---

## Response Style

Keep the first answer concise and useful. Do not dump the whole framework unless the user asks for depth.

Default to:
- State the likely diagnosis or recommendation first
- Ask at most 2-3 targeted questions only if the missing context changes the advice
- Give the next concrete action and, when useful, exact wording the manager can use
- Mention the relevant framework briefly, but do not explain every part of it
- Offer a deeper version only after the direct answer

---

## How to Use This Skill
- **Don't know where to start / need a health diagnostic** → The 5 Factors of Effective Teams
- **Team is slow, behind on commitments, or burning out** → Team Health States
- **Team is running at an unsustainable pace** → Managing Team Intensity
- **Someone said "the team isn't working hard enough"** → "The Team Isn't Working Hard Enough"
- **Team seems disengaged or disconnected** → The Engagement Stack
- **Planning a team meeting and need content ideas** → Team Meetings
- **Planning a team offsite or focus day** → Team Focus Days
- **Want a library of activity ideas (Growth / Connection / Impact)** → read [`references/activities.md`](references/activities.md)
- **Retros keep surfacing the same issues** → When Retros Feel Repetitive
- **Team members don't seem to trust each other** → Trust Battery
- **Something broke — need to run a postmortem** → Blameless Postmortems
- **Team is technically strong but cohesion feels fragile** → Jelled Teams and Teamicide
- **Unsure how much to share with the team** → Transparency as a Team Health Signal
- **Want to model flexible work without creating a surveillance culture** → Leave Loudly

---

## Default Response Shape

When helping with team health, diagnose before prescribing activities:

1. **Health read:** morale, safety, dependability, clarity, intensity, trust, or engagement.
2. **Evidence:** what the user observed and what it likely means.
3. **Immediate stabilizer:** what to do this week.
4. **Structural intervention:** meeting, ritual, transparency change, recovery plan, retro change, or activity.
5. **Watch signal:** what to monitor to know if the team is improving.

If the team is in burnout or high-intensity mode, address recovery and priorities before suggesting morale activities.

---

## The 5 Factors of Effective Teams

Google's Project Aristotle studied hundreds of teams to find what actually makes them effective. The top 5 factors, in order of importance:

1. **Psychological safety** — Can team members take risks without feeling insecure or embarrassed?
2. **Dependability** — Can team members count on each other to do high-quality work on time?
3. **Structure & clarity** — Are goals, roles, and execution plans clear?
4. **Meaning** — Is the work personally important to each team member?
5. **Impact** — Does the team believe their work matters?

The order matters. All five are necessary, but psychological safety is foundational — without it, the others don't activate. People don't raise concerns, share ideas, or flag problems when they fear judgment.

A practical way to use this: run a short team exercise where each person scores each factor (1–5). Look at where the scores are lowest. The lowest factor by average score is your most important focus area — not the one that feels most urgent to you.

---

## Your Peer Team Matters Too

When managers are asked "who is your team?", they almost always list their direct reports. Never their peers.

But a manager's peer group is also a team — and the same five factors apply to it. Engineering managers who treat peer relationships as purely transactional (or competitive) create the conditions for silos: no knowledge sharing, slow cross-team coordination, and blame when things go wrong at the boundaries.

The same trust, conflict, accountability, and commitment that you invest in building with your reports — invest it with your peer EMs too.

---

## Team Health States

From *An Elegant Puzzle* (Will Larson): teams exist in one of four states at any given time, each requiring a different response from the EM.

| State | What it looks like | What to do |
|---|---|---|
| **Falling behind** | Backlog grows every sprint; team feels overwhelmed; commitments slip | Add capacity. This is the only state where hiring directly helps. In the short term: reduce the scope of what you're committing to and communicate that to stakeholders honestly. |
| **Treading water** | Team is shipping, but only product work — no tech debt addressed, no improvements | Reduce WIP. Focus the team on fewer things. Create space by finishing existing work before starting new work. |
| **Repaying debt** | Team is actively working down tech debt; velocity feels slower | Protect the work. Shield the team from new product demands until the debt is paid. This state is temporary and necessary — don't let urgency interrupt it. |
| **Innovating** | Low tech debt, stable delivery, team has headspace to experiment | Preserve it carefully. This state is fragile. Only add work that's compatible with the team's current way of working. The wrong new hire or the wrong project can push you back to Treading water fast. |

The most common mistake: treating all states the same. Pushing a "Falling behind" team to also repay debt doesn't work. Trying to innovate while treading water doesn't work. Diagnose the current state first, then apply the right response.

---

## Team Meetings

Most engineering managers underinvest in team meetings — either skipping them entirely (too busy, afraid of wasting time) or running them without an agenda. The common excuse: "I'll create one when I have something good to say." The result: 3 meetings a year.

Team meetings create shared context, shared memory, and connection that 1:1s can't replace.

### 7 Ideas for Meeting Content

1. **Review the next project**: How it fits the roadmap, why it was chosen, what you're trying to achieve. Not a substitute for a technical kickoff — this is for context and alignment.

2. **Post-mortem of a recent incident**: Go over what happened and brainstorm as a team on how to prevent the next one.

3. **A developer shares a project they worked on**: Improves their presentation skills; the rest of the team learns something new.

4. **Interesting projects from elsewhere in the company**: New PoCs with clients, technical work other teams are doing.

5. **Business updates**: You know things your team typically doesn't. Share sales updates, usage metrics, plans for the next funding round.

6. **Bring a guest**:
   - A sales representative — before starting a major project, have them share context on the customer and how the project was won
   - The designer — how they work, what matters to them, what guides their decisions
   - The VP Product — their agenda, how they see the roadmap, the next 6 months
   - Your own manager — especially during periods of uncertainty
   - Other team leaders, architects, support, customer success, or any cross-functional role

7. **Fun**: Lunch together, a short game. For remote teams, something like Drawize.

### Cadence

There's no universal answer. Weekly 30 minutes is probably too much to sustain with quality. A reasonable starting point: **30 minutes, twice a month** — then adjust based on how it's going.

The most important thing: start, then don't cancel. Create the recurring meeting before you talk yourself out of it.

---

## Team Focus Days

The difference between great and average teams often shows up in three places:
1. How the team communicates — not just what they communicate, but how
2. How they handle conflict — whether they address it or let it fester
3. How connected they feel to each other as people, not just coworkers

Team Focus Days are a structured way to work on all three. The concept: take the team out of the office for a full day, twice a year, with a mix of work and connection.

### The Format

- **Outside the office.** A different environment changes the dynamic. Renting a meeting room somewhere else, going to a co-working space, or finding an off-site venue all work. The point is: not your usual setting.
- **Every 6 months.** Frequent enough to be meaningful, infrequent enough that it stays special.
- **Include the PM.** This is not an engineering-only day. If you have a PM partner, they should be there. Shared context and alignment happen best in person.
- **Mix work and connection.** Not all day in a meeting room, not all day at an activity. Both matter.

### 10 Ideas for Focus Day Content

1. **Roadmap review:** Walk through where you're going and why. What's coming in the next 6 months and what trade-offs were made.
2. **Technical debt audit:** What's slowing the team down? Let engineers name it openly.
3. **Retrospective:** What worked in the last 6 months? What didn't?
4. **"I wish we did more of X":** Each person names one thing. No judgment. Then prioritize.
5. **Cross-team dynamics:** Any friction with other teams? Surfaces better in person.
6. **Process review:** Standups, code review, deployments — what's working, what's overhead?
7. **Career conversations in pairs:** Structured time for engineers to share where they're headed.
8. **Hackathon or prototype time:** Build something experimental. No pressure to ship.
9. **Teach each other:** Each person does a 10-minute share on something they know that others don't.
10. **Shared meal or activity:** End with something social. Not mandatory fun — something chosen together.

---

## Transparency as a Team Health Signal

What you share (and don't share) with your team shapes their trust in you and in the company.

**Don't be a shit umbrella.** Managers who shield their teams from every difficult reality think they're protecting people. What they're actually doing is creating a team that's perpetually surprised by bad news and has no way to prepare or respond. Some information is genuinely confidential. But most "bad news" should be shared.

**The disappointment frontier.** Share information that your team will eventually learn anyway — about roadmap changes, reorgs, financial pressures, strategy shifts. If they find out from someone else, or after the fact, you've damaged your credibility. Better to share early, even if the news is uncertain.

**Share the financial situation.** Developers who understand how the business is doing make better decisions — they understand urgency, scope, and trade-offs. You don't need to show spreadsheets. But "we had a strong quarter and we have runway to invest" vs. "it's been a tough few months and we need to be efficient" changes how people think about their work.

Think of it like a ship: everyone on a ship knows if it's sinking. The crew doesn't need a board meeting to understand the situation. Give your team enough context to be crew, not passengers.

**Share the roadmap draft.** Before priorities are finalized, share what's being considered and why. People can handle a draft. What they can't handle is being handed a finished plan they had no visibility into.

---

## Managing Team Intensity

Not every week should feel the same. Teams that run at full sprint indefinitely burn out. Teams that coast lose edge. The skill is knowing what zone you're in — and choosing it consciously.

A simple 5-zone model, borrowed from endurance training:

| Zone | Feel | When to use |
|------|------|-------------|
| 1 — Very light | Calm, sustainable, low pressure | Recovery after intense periods; onboarding new members |
| 2 — Light | Steady output, no crunch | Default healthy pace for most of the year |
| 3 — Moderate | Focused, some urgency | Normal sprint periods, regular delivery cycles |
| 4 — Hard | High energy, tight deadlines | Product launches, critical milestones |
| 5 — Maximum | All-in, not sustainable | True crises only — production outages, make-or-break moments |

**The mistake most EMs make:** defaulting to Zone 4 as the steady state. Zone 4 feels productive. It looks like commitment. But it has a ceiling — teams can't sustain it, and the recovery cost is high.

**How to use this:**
- Name the zone explicitly. "This sprint we're at Zone 4 because of the launch." The team tolerates intensity better when it has a name and an end date.
- After Zone 4 or 5 periods, plan Zone 2 recovery. Don't immediately load the next hard sprint.
- If your team is always in Zone 3–4 without recovery, that's a workload problem, not a motivation problem.

---

## "The Team Isn't Working Hard Enough"

If someone tells you your team isn't working hard enough, don't dismiss it and don't accept it uncritically. There are three distinct root causes — and each requires a different response:

1. **Lack of "hustle"** — an external person sees no visible effort signals. People seem relaxed, unhurried, and don't look busy. This is often a perception gap, not a performance gap — especially in remote environments.

2. **Lack of visible output** — poor communication, unreasonable expectations, or poor prioritization. The team is working but progress isn't visible to stakeholders. This is a communication/transparency problem.

3. **Lack of passion** — the team seems unmotivated or detached. This is a morale and engagement problem.

In all three cases: don't dismiss the feedback. Find ways to bridge the gap between what you see and what the feedback-giver sees. Often, making the work more visible (more frequent updates, clearer progress communication) is enough.

---

## Leave Loudly — and Don't Ask for Permission

When a developer tells you they'll continue working from home, don't say "ok" — that implies they need to explain themselves or seek approval.

Instead, say something like: *"I trust you to manage your own time — no need to mention it when you continue from home."*

Then model it yourself. When you leave early, don't add "I'll continue working after the kids go to sleep." Just leave. Announce it without the justification. This signals that you trust people to manage their own time without surveillance — which is what psychological safety around flexible work actually looks like.

---

## When Retros Feel Repetitive

If retros keep surfacing the same issues without resolution, try:

- **Different questions.** The 4Ls format (Liked, Learned, Lacked, Longed for) changes what people surface.
- **Different tools.** Online retro tools (EasyRetro, Parabol, etc.) can re-engage people who've gone through the motions too many times.
- **A meta-retro.** Summarize the last 6 months of retros. What themes keep appearing? Why haven't they been resolved?
- **"Reveal at end" format.** Everyone writes items without seeing others'. Reveal all at once. Reduces anchoring.

The deeper issue behind retro déjà vu is usually that the output doesn't lead to action. Before changing the format, check whether anything from previous retros was ever actually addressed.

---

## The Engagement Stack

Individual engagement requires four layers to be aligned — each depends on the one below:

1. **The individual** — is this person fundamentally energized at work?
2. **The role** — does the work use their strengths and grow them?
3. **The team** — do they feel connected and respected by their peers?
4. **The company** — do they believe in the direction and feel proud of where they work?

When someone is disengaged, find out which layer broke first. Fixing company communication won't help someone who's in the wrong role. Fixing the role won't help someone who has a bad team dynamic.

---

## Engineers' Emotional State as a Performance Signal

Tense before standup. Exhausted after every sprint. Frustrated about decisions they had no input into. These are not personal problems — they're team health signals.

Nobody performs at their best when their body is in a stress state. Ask *"How did you feel this week?"* in 1:1s — not as a therapy question, but as a diagnostic one. Give space for a real answer.

If someone's nervous system is consistently in threat mode at work, that's an environment problem as much as a performance problem.

---

## Jelled Teams and Teamicide

From *Peopleware* (DeMarco & Lister): a jelled team is one that has coalesced into a cohesive unit — members trust each other, move in sync, and collectively outperform what you'd predict from individual skill levels. Jelled teams are genuinely rare and disproportionately valuable.

**What jelling requires:**
- Enough time working together to build shared context and trust
- A challenge worth caring about — not just assigned work, but a goal the team has ownership over
- Freedom from bureaucratic friction that breaks flow and signals management distrust

**Teamicide — the patterns that destroy cohesion:**

| Factor | What it looks like |
|---|---|
| Defensive management | Micromanagement, second-guessing decisions, checking in constantly — signals you don't trust the team |
| Separated workspace | Open offices that make deep work impossible; remote setups without shared async norms |
| Fragmented work | Team members constantly switching between unrelated projects; no one gets to finish anything |
| Quality reduction for schedule | Forcing shortcuts that engineers know are wrong — kills pride of craft |
| Phony deadlines | Artificial urgency; "this is critical" for every sprint — engineers learn urgency means nothing |
| Clique control | Managers who treat a subset of the team as the inner circle and the rest as implementers |

You can do many things right and still destroy a jelled team with one of these. The most common is defensive management disguised as staying involved.

---

## Trust Battery

From *It Doesn't Have to Be Crazy at Work* (Basecamp/Fried): every relationship between two people has an implicit trust battery, starting at around 50%.

The battery charges when someone does what they say they'll do — responds when they said they would, ships what they committed to, handles a situation the way they promised. It discharges when they don't.

Trust isn't primarily built by being warm, friendly, or enthusiastic. It's built by delivery. The engineer who quietly ships what they committed to, every sprint, has a fuller battery with their colleagues than the one who makes everyone feel great but misses constantly.

**Practical use:**
- When someone on the team is struggling socially — colleagues seem cold or disengaged — look at their delivery record before concluding it's a personality issue. A discharged battery often looks like a relationship problem.
- When a new hire seems isolated, they haven't had time to charge the battery yet. Giving them small, visible wins early charges it faster than any onboarding activity.
- As a manager, your own battery with the team is the foundation of everything. They watch whether you deliver on what you said, whether you fight for the things you promised to fight for.

---

## Blameless Postmortems

When something breaks — a production incident, a failed deployment, a major bug — the traditional response is to find the person responsible and correct them. Etsy's approach (which became the industry standard) is different: assume that people acted with the best information and tools they had at the time. The goal is not to find who caused the problem, but to understand how the system allowed it to happen.

**Why blame-first postmortems backfire:**
- People self-censor. They hide what happened or minimize their role.
- You lose the detailed picture of what actually occurred.
- You fix the person instead of the system — and the next person makes the same mistake.

**What a blameless postmortem looks like:**
1. Construct a timeline of events without attributing blame. What happened, in sequence, not "who did what wrong."
2. Ask: what did people know at the time of each decision? They almost certainly made the best decision available with the information they had.
3. Ask: what would have had to be different for this not to happen? Usually the answer involves tooling, processes, missing alerts, or insufficient context — not individual negligence.
4. Capture action items that change the system, not just people's behavior.

**The EM's role:** model the tone. If you're leading the postmortem and you're looking for a villain, the team will protect themselves. If you're genuinely curious about what the system allowed, they'll tell you the truth.

Blameless doesn't mean consequence-free. Repeated individual negligence or deliberate violations are different situations. But they're the exception, not the default explanation.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md). For a library of team activity ideas organized by driver (Growth / Connection / Impact), read [`references/activities.md`](references/activities.md).

---

## Related Skills

- `1on1s` — Primary place to detect and address individual health issues
- `feedback` — For addressing specific behavioral concerns on the team
- `engineer-motivation` — Individual-level motivation and engagement interventions
- `roadmap-planning` — Workload and capacity as inputs to team health
- `retaining-developers` — The 5-state retention framework maps directly to team health signals
