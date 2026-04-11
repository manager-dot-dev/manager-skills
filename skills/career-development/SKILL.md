---
name: career-development
description: Helps engineering managers support direct report growth — produces a stage-by-stage model of engineering impact (Circles of Influence), a framework for non-linear career planning (Tarzan Method), diagnostic signals for stalled growth, conversation scripts for career talks, and a promotion readiness vs. timing distinction. Use when the user says "career growth," "promotion," "career path," "this person wants to grow," "career conversation," "what's next for this person," "career ladder," "IC vs manager track," "how do I help my report advance," "help someone grow," or "engineer wants a promotion." Do NOT use for formal written performance reviews or underperformance — use performance-reviews instead.
metadata:
  version: 2.1.2
---

# Career Development

## Before Starting

Check for EM context first:
1. Read `.agents/em-context.md` if it exists
2. If a person is mentioned, look for `.agents/reports/[name].md` — it may contain their level, goals, and growth history
3. Use that context — only ask for information not already covered

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
- **Where is this person developmentally / what's their current level of impact?** → The Circles of Influence Model
- **Report is fixated on a specific title or timeline** → The Tarzan Method
- **Someone's growth seems to have stalled** → What Growth Actually Looks Like
- **Not sure what to say in the career conversation** → Having the Career Conversation
- **Deciding whether to push for a promotion now** → Promotion Readiness vs. Promotion Timing

---

## Default Response Shape

When helping with career development, produce a manager-ready plan:

1. **Current growth read:** where the person appears to be operating now.
2. **Next growth edge:** what kind of impact they need to demonstrate next.
3. **Conversation questions:** what to ask in the next career 1:1.
4. **Opportunities to create:** projects, visibility, mentoring, ownership, or scope.
5. **Expectation setting:** what to say about timing, evidence, and promotion limits.

Do not promise promotion. Separate "ready to grow" from "the organization has a slot and evidence."

---

## The Circles of Influence Model

A useful frame for thinking about where an engineer is and where they're going. Impact expands in concentric circles:

**Personal** — Masters their own craft. Delivers reliable results. Writes good code, handles on-call, completes tasks well. This is the foundation.

**Team** — Makes the team better. Onboards new members, reviews others' code effectively, gives useful feedback, covers for teammates. Their absence would be felt on the team.

**Group** — Shapes cross-team work. Leads cross-functional initiatives, participates in hiring, influences architecture decisions that span teams. Their impact reaches beyond their immediate team.

**Company** — Drives org-wide outcomes. Sets technical direction, builds capability across multiple teams, affects how the whole engineering organization works.

**How to use this in career conversations:**
- Figure out which circle the engineer is currently operating in consistently.
- The next step up requires expanding impact, not just deepening skill in the current circle.
- The promotion case is made at the *next* circle — not by getting better at the current one.

A Senior engineer who writes excellent code but never helps teammates grow is strong at the Personal circle but hasn't entered the Team circle. That's the gap to address, not more technical depth.

---

## The Tarzan Method

Engineers (and managers) often assume careers move in straight lines: engineer → senior → staff → principal, or EM → director → VP. This leads to fixating on the fastest route up a single ladder.

The reality: senior roles require both capability AND company need. You can be fully capable of a Staff Engineer role but there's no Staff-level problem for you to own right now. The role has to exist and need filling at the moment you're ready for it.

The Tarzan model: **swing to the next vine, not to the destination.** Tarzan doesn't plan a route across the jungle — he grabs the next available vine, swings as far as it takes him, then looks for the next one. Careers work the same way.

Practical implications for career conversations with reports:
- Help them identify the *next* swing, not a 5-year plan.
- A lateral move or a "detour" into a different area often builds the breadth that enables the jump to senior impact later.
- Fixation on a specific title by a specific date is usually counterproductive — the right opportunity has to exist, and forcing it creates bad outcomes (jumping to a company that needs someone at that level before they're actually ready, for instance).

---

## What Growth Actually Looks Like

Growth isn't a continuous line — it comes in bursts separated by consolidation periods. Signs an engineer is growing:

- They're working on problems slightly beyond their current comfort zone
- They're making decisions they previously would have escalated
- They're teaching others things they've learned
- Their scope of ownership is expanding

Signs growth has stalled (and what to do):
- Same problems, same tools, no stretch — find them something harder
- Expanding technically but not building relationships or influence — give them cross-team work
- Making the same mistakes repeatedly — this is a feedback gap, not a growth gap; address the feedback first

---

## Having the Career Conversation

Career development conversations are uncomfortable for a lot of managers because they feel high-stakes. Some principles:

**Ask before advising.** "What does growth look like for you in the next year?" beats "here's what I think you should work on." You'll often get a much clearer picture of what they actually want, which may differ significantly from what you assumed.

**Separate "what they want" from "what the company needs."** Be honest when these aren't aligned. If someone wants to move into a Staff role but the team doesn't have Staff-level problems, say so — and help them think through what that means (a different team, a different company, a different timeframe).

**Be specific about the gap.** "You need to show more leadership" is useless. "The gap I see is that you're not yet driving alignment with the PM and design on your projects — you're still waiting for requirements rather than shaping them" is something they can act on.

**Document it.** After a career conversation, write down what was discussed and share it with the report. Memory is unreliable. A written note creates shared accountability.

---

## Promotion Readiness vs. Promotion Timing

Two separate questions that managers often conflate:

**Is this person ready for promotion?** — Are they consistently operating at the next level? Do they have a track record of impact at that level, not just occasional moments?

**Is now the right time to push the case?** — Is there headcount/budget for a promotion? Is the calibration cycle coming up? Do you have enough documented evidence? Is the person visible enough to the people who will weigh in?

Both have to be true. Pushing someone for promotion before they're ready damages your credibility and can actually set them back. Waiting too long after they're ready damages trust and risks losing them.

The rule: start building the promotion case *while* the person is still being developed — document impact, get visibility, prepare specific examples. Don't scramble at calibration time.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md) for the full list of source articles (with links) and books.

---

## Related Skills

- `1on1s` — The primary venue for ongoing career conversations
- `performance-reviews` — Promotion cases are made at review time; the groundwork is laid here
- `managing-high-performers` — High performers need growth challenges to stay engaged
- `management-transitions` — Counseling engineers on whether management is the right path
