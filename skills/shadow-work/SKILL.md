---
name: shadow-work
description: Helps engineering managers identify, quantify, and reduce hidden capacity drains that make teams miss commitments even when everyone is busy. Use this skill whenever the user mentions invisible work, untracked work, support requests consuming the team, glue work, shadow backlog, sprint spillover, capacity planning being wrong, teams always underestimating, senior engineers burning out, or "we are busy but nothing ships." Produces a diagnostic, evidence plan, and concrete interventions.
metadata:
  version: 2.1.2
---

# Shadow Work

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
- **Team misses commitments but everyone seems busy** -> diagnose all three shadow-work types and identify the dominant capacity drain
- **Ad-hoc incidents and support requests eat capacity** -> start with Type 1: Invisible Production Support
- **Senior engineers burn out doing unglamorous coordination** -> start with Type 2: Glue Work
- **Off-the-record requests quietly consume sprints** -> start with Type 3: The Shadow Backlog
- **Remote team has weak visibility into what people actually absorb** -> include The Remote Amplification Problem

---

## Default Response Shape

When the user asks for help, do not only explain the concept. Produce a practical diagnosis:

1. **Likely shadow-work type** - name the type(s), with confidence and evidence from the user's prompt.
2. **What to measure for 2-6 weeks** - lightweight signals, not a heavy process rollout.
3. **Immediate containment** - what to do this week so the team stops bleeding capacity.
4. **Structural fix** - what to change in planning, ownership, rotation, recognition, or PM/EM workflow.
5. **Stakeholder message** - a concise script the EM can use with PMs, leadership, or the team.

If the user's facts are thin, ask for the minimum missing data: where the work comes from, who absorbs it, how often it happens, and whether it is currently tracked anywhere.

---

## What Shadow Work Is

Shadow work is untracked work that consumes real capacity but does not appear in the plan. It makes teams consistently miss commitments without anyone understanding why. It falls into three types, and each type requires a different response.

The key management move is not "work harder" or "estimate better." The first move is to make the work legible enough that the team can make tradeoffs honestly.

---

## Diagnostic Questions

Use these questions before prescribing fixes:

- **Source:** Where does the unplanned work come from: production, other teams, PM requests, managers, engineers, customers, or the codebase itself?
- **Absorber:** Who usually handles it? Is it evenly distributed, or does it concentrate on one or two senior people?
- **Visibility:** Does it appear in tickets, sprint boards, incident logs, review docs, or performance reviews?
- **Pattern:** Is it recurring, seasonal, project-specific, or random?
- **Cost:** Does it mostly cost calendar time, focus time, emotional energy, roadmap capacity, or promotion credit?
- **Tradeoff:** What planned work silently loses when this work appears?

---

## Type 1: Invisible Production Support

Ad-hoc incident triage, alert investigation, support-team requests, manual fixes, and customer escalations that never enter the ticket system.

Without tracking, patterns go unnoticed. The same 15-minute manual fix can burn hundreds of hours annually while the root cause stays unfixed. The team appears to have capacity but consistently underdelivers, and has no data to show why.

**What to do:**
- Create a lightweight category for unplanned support work, even if it is only a tag in the ticketing system
- Track for 4-6 weeks, then run a frequency analysis: top recurring issues, top request sources, top absorbers
- Rotate hot-fix responsibility instead of letting one person become the permanent human circuit breaker
- Convert repeated manual fixes into roadmap items with a visible cost-of-delay argument

---

## Type 2: Glue Work

Code reviews, mentoring, onboarding, documentation, coordination, cross-team translation, and "can you just help them unblock?" work that lands disproportionately on senior engineers.

Glue work creates two problems when unmanaged: the engineers doing it burn out without recognition, and the engineers not doing it get promoted without learning the work that keeps the organization functioning.

**What to do:**
- Name glue work explicitly in performance conversations and promotion packets
- Distribute the skills downward through pairing, live review sessions, office hours, and rotating ownership
- Protect senior engineers' maker time when they are acting as multipliers
- Track whether glue work is becoming a default identity for one person rather than a shared team capability

---

## Type 3: The Shadow Backlog

Work outside the official roadmap: PMs making off-the-record fix requests, engineers taking longer routes they know are right, unplanned integrations negotiated directly with other teams, and "small asks" that never look small in aggregate.

This can quietly consume a large share of real capacity while breaking trust between business and engineering. Leadership sees a team that commits and misses, without seeing where the capacity went.

**What to do:**
- In planning, ask: "What are we likely to get asked to do that we have not scoped?"
- Budget explicit shadow capacity when the environment is noisy; start with 10-20% if you lack data
- Redirect off-the-record PM requests into the official backlog without shaming the requester
- Periodically present shadow backlog data to stakeholders as evidence for roadmap tradeoffs

---

## The Remote Amplification Problem

For remote teams, shadow work is doubly invisible: your manager cannot casually observe it either. This means you have no natural evidence when advocating for a team member's raise or promotion, and weak visibility when capacity is being consumed.

Building lightweight tracking habits is therefore management infrastructure, not overhead. It protects the team's ability to get credit for real work and gives the EM evidence for capacity conversations.

---

## Stakeholder Scripts

Use direct, non-accusatory language. The goal is to expose the tradeoff, not blame the source of the work.

**With a PM:**
"I want to make these requests visible because they are real work. If we keep handling them outside the backlog, we will keep missing the planned roadmap and neither of us will have good data. Let's add them to the board and decide what they displace."

**With leadership:**
"The team is not missing commitments because the estimates are careless. We are absorbing unplanned work that is not represented in the plan. I am going to track it for the next few weeks and come back with the recurring sources, cost, and options."

**With a senior engineer doing too much glue work:**
"I see how much coordination and review work you are absorbing. Some of it is valuable, but I do not want it to become invisible or trap you away from growth work. Let's decide what should be recognized, rotated, or stopped."

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill, read [`references/sources.md`](references/sources.md).

---

## Related Skills

- `roadmap-planning` - Shadow work should be explicitly budgeted in capacity planning, not ignored
- `working-with-pm` - Off-the-record requests are a PM-EM relationship problem, not just a capacity problem
- `retaining-developers` - Senior engineers absorbing invisible glue work without recognition are in the "unappreciated" retention state
- `knowledge-sharing` - Glue work often overlaps with documentation and onboarding failures
