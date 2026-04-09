---
name: team-health
description: When the user wants to assess, improve, or track the health of their engineering team. Also use when the user says "team morale," "team is struggling," "burnout," "engagement," "attrition risk," "team survey," "retro," "psychological safety," "team dynamics," "something feels off," "team culture," or "team is unhappy."
metadata:
  version: 1.0.0
---

# Team Health

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

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

## Related Skills

- `1on1s` — Primary place to detect and address individual health issues
- `feedback` — For addressing specific behavioral concerns on the team
- `roadmap-planning` — Workload and capacity as inputs to team health
- `retaining-developers` — The 5-state retention framework maps directly to team health signals
