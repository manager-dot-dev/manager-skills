---
name: roadmap-planning
description: Helps engineering managers plan roadmaps, prioritize work, and communicate priorities effectively — produces the 20% tech debt framework (and its 5 traps), a phased release pressure-test, a maintenance cost model, the Always Green delivery method, sprint anti-patterns, hidden costs of custom features, a critical deadline playbook, the Iron Law of Projects with reference-class forecasting, a "no technical projects" framing, and feature factory warning signs. Use when the user says "roadmap," "quarterly planning," "OKRs," "prioritization," "what should we work on," "planning cycle," "backlog grooming," "stakeholder alignment," "capacity planning," "technical debt," "we're always late," or "leadership doesn't understand engineering work."
metadata:
  version: 2.1.2
---

# Roadmap Planning

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
- **Negotiating tech debt time with stakeholders** → Tech Debt and the "20% Rule"
- **Feature is being broken into phases — pressure-test whether it's right** → Phased Releases
- **Need to show the ongoing cost of building new things** → Maintenance Costs as a Third Dimension
- **Team keeps missing sprint goals / perception of the team is "slow"** → The Always Green Method
- **Sprint rituals are creating more friction than value** → Sprint Anti-Patterns
- **PM keeps adding one-off custom features** → Hidden Costs of Custom Features
- **Hard deadline is at risk — what to do** → When the Team Can't Make a Critical Deadline
- **Project estimates keep being wrong** → The Iron Law of Projects
- **Technical work keeps getting deprioritized** → There Are No Technical Projects
- **Team is shipping but nothing seems to have impact** → Feature Factory Warning Signs
- **Running a company-wide cleanup event** → read [`references/extended.md`](references/extended.md) — The Cleanathon

---

## Default Response Shape

When helping with roadmap planning, make tradeoffs visible:

1. **Planning problem:** tech debt, phases, deadlines, capacity, maintenance, feature factory, or stakeholder alignment.
2. **Decision frame:** what options are actually on the table.
3. **Business translation:** why the engineering work matters in product or company terms.
4. **Recommendation:** what to do now and what to defer.
5. **Stakeholder message:** concise wording for PMs, leadership, or the team.

If the issue is "technical work keeps losing," translate it into risk, cost, speed, reliability, or customer impact before arguing for it.

---

## Tech Debt and the "20% Rule"

Dedicating 20% of capacity to purely engineering work is a widely recommended practice — and it genuinely helps. But most teams implement it poorly and fall into predictable traps.

### The 5 Traps

**1. Separate backlogs for product and tech**

When product work and tech work live in separate backlogs, Product stops interfering in tech decisions and Engineering stops engaging with product priorities. It sounds like peace — it's actually a slow failure.

Product and technology are not separate things. Bug fixes, library updates, automation improvements, security patches — almost all of these have business value (reliability, security, speed of delivery).

The fix: every item on the technical list should have a clearly defined business value. Once it does, **move it to the product backlog** — where it gets prioritized alongside everything else. Reserve the separate tech track only for critical work too hard to explain to non-technical stakeholders.

**2. The company doesn't understand the value of your work**

If the business doesn't care about or understand your technical initiatives, those initiatives will always be the first thing deprioritized when "urgent" things appear. And you'll have a much harder time negotiating for hiring, training, or additional time.

The fix: make technical work visible. Hold monthly reviews where engineering teams present the progress of technical initiatives not tied to specific product teams. Show why the work matters in business terms — not just "we migrated to Swift" but "this reduces compilation time, improves developer experience, and helps with hiring because fewer engineers want to touch Objective-C."

**3. Diluted focus**

Getting 20% doesn't solve everything. If you assign a separate tech initiative to every single person on the team, each going in a different direction — you'll make no real progress anywhere.

The fix: focus your 20% on a coherent set of initiatives that contribute to a longer-term engineering strategy. Know your goals, know which initiatives contribute to them, and resist the temptation to address every technical itch simultaneously.

**4. "We'll fix it later"**

Once a team has 20% protected time, it becomes tempting to push things faster, assuming tech debt will get cleaned up later. It almost never does — the next sprint always has something more urgent.

20% time is to make things better, not just less bad. Even when building an MVP, it must be functional, usable, and reliable. Writing tests "after we push to customers" is a classic — those tasks almost never get done because you're either fixing production issues or jumping into the next initiative.

**5. Ineffectiveness on large initiatives**

20% is one day a week, 1.5 hours a day, or ~4–5 days a month. For genuinely large initiatives — breaking down a monolith, re-platforming — this means a year of context-switching to make 2–3 months of progress. It doesn't work.

The fix: large strategic initiatives shouldn't live in the 20% — they should become product priorities with business justification, full organizational support, and tracked progress. Save the 20% for genuine maintenance and smaller tactical improvements.

---

## Phased Releases: When They Help and When They Don't

Releasing a feature in phases sounds careful and de-risked. Often it just delays learning and creates drag.

Five questions to pressure-test a phased roadmap:

1. **Are you phasing because users asked for it, or because the team wants to build more?** Phase 2 is often a wish list, not a user need.
2. **Will Phase 1 actually be used without Phase 2?** If Phase 1 alone isn't valuable, you're just shipping a stub. Users don't care about your internal phases.
3. **What are you learning in Phase 1 that should inform Phase 2?** If you can't name it, Phase 2 is already fully designed — which means you're not actually using Phase 1 as a learning milestone.
4. **What's the cost of stopping after Phase 1?** Phases create internal expectations. Once you ship Phase 1, Phase 2 starts to feel like a commitment rather than a choice.
5. **Is there a simpler version that delivers the full value?** The best version of "Phase 1 + Phase 2" is often just a better-scoped Phase 1.

**The Honda story.** When Honda entered the US motorcycle market, they planned to lead with their large bikes — the serious motorcycles. Those broke down. Their small, cheap motorcycles (which they were riding around themselves) caught attention instead. They pivoted fast and built a market they hadn't planned for.

The lesson: the plan you start with is a hypothesis. Great product teams are willing to stop a feature mid-build if the signal says to. They treat stopping as a sign of good product culture, not failure.

**Communicate this to your team.** Engineers often feel demoralized when a feature is stopped. Your job is to frame it differently: "We shipped, we learned, we're redirecting based on real data. That's how this is supposed to work." The alternative — continuing to build something that's clearly not working — is the actual failure.

---

## Maintenance Costs as a Third Dimension

Roadmap discussions usually get trapped on two axes: *what* to build and *how long* it will take. This misses the ongoing cost of everything you commit to.

Every feature you ship adds permanent weight. Maintaining it, supporting it, keeping it fast and secure — even with zero technical debt — takes ongoing team capacity. The more unrelated the systems, the harder this becomes.

How to add maintenance cost to the conversation:
1. Map the current ongoing costs of each system you own (bug fixes, outages, urgent customer requests, security patches)
2. Estimate as a percentage of team capacity (e.g., "~10% of our time per system")
3. Show the estimated increase in ongoing cost if you take on the proposed new work
4. Let the other side make the decision with that information visible

The numbers won't be accurate. That's not the point. The goal is to make the maintenance cost dimension visible in the conversation — not to be precise, but to change what gets considered.

When you start tracking these things and bringing in real stories, it becomes much easier to push back on scope without it feeling like obstruction.

---

## The Always Green Method

Delivery speed is 95% about perception. A team that consistently delivers on-time small goals is perceived as fast. A team that swings for ambitious goals and misses looks slow — even if they shipped more.

The core insight: **you can always deliver on time if you choose the right goals.**

**The Hill Concept (from Shape Up)**

Every project has two phases: climbing the hill (discovering unknowns, figuring out what to actually build) and going down (executing on what's now clear). You can't fully understand what a project requires through planning alone — you have to climb far enough to see everything.

Before committing to a goal, start the work a sprint early. Spend a few days actually doing it — uncovering the hard parts, the dependencies, the unknowns. Once you've reached the top of the hill, you can commit with high confidence. Scope surprises become rare.

**How to set a sprint goal that you always finish:**

1. **Pick a minimal goal.** One clear, user-facing outcome. Nothing fancy. It should fill at most half the team's capacity — so you're confident it's done by midweek.
2. **Break it into parallel work.** Pieces that people can work on without blocking each other. No dependencies on other teams.
3. **Announce it publicly.** Post in a shared channel: *"If all else fails, this is what we deliver."* Take full ownership.
4. **Watch it daily.** Be on top of it. Unblock immediately. Pull people from "non-goal" tasks if needed.
5. **Finish it.** If you have 3 goals, you need 3 checkmarks. Two out of three is not a success — it just resets the expectation that your team doesn't finish.

The rest of the sprint doesn't stop — bugs, tech debt, planning, supporting other teams. The minimal goal is just the non-negotiable floor.

**On ambitious goals:** teams with consistent 100% delivery rates do more over time than teams chasing ambitious goals and missing. An always-succeeding team is more effective, more trusted, and more willing to over-deliver as a bonus. The alternative — ambitious goals, consistent misses — just burns everyone out.

---

## Sprint Anti-Patterns

Sprints, when followed rigidly, create their own problems. Signs that sprint process is working against the team:

- Taking a smaller bug at sprint end because 2 days aren't enough for the real work
- Pushing to finish sprint goals that no longer make sense
- "Making progress on X" counted as a sprint goal
- Velocity tracked as a success metric while features are consistently late
- Tech debt moved to "next sprint" for 6 months running

**What to do when you can't change the process:**

- Always leave breathing room. Fight the argument "let's take it in the sprint, worst case we move it" with "let's not take it, best case we add it if we have time."
- Don't force meaningless sprint goals. No goal is better than a fake one.
- When someone finishes their tasks, let them work on what they want.
- Fight for "quality sprints" — 2–3 week periods for fixing things, at least once a year.
- Question practices that don't serve your team. Daily standups adding no value? Make them optional.

---

## Hidden Costs of Custom Features

When a PM or customer asks for a one-off "special" feature, the visible cost is the development time. Three costs that almost never make it into the estimate:

1. **Future maintenance tax** — every custom feature needs to be fixed, adjusted to product changes, and kept working. This cost compounds indefinitely.
2. **Complexity tax** — every new feature makes the overall product more complex, which increases the cost of every subsequent feature.
3. **Opportunity cost** — that developer-month could have gone toward higher-impact work.

Practical responses:
- Price "customer specials" significantly higher than standard features to make the true cost visible
- Track what percentage of team capacity goes toward specials. Agree on a ceiling with PM/leadership
- Measure actual feature usage. Features nobody uses are maintenance cost with zero return

---

## When the Team Can't Make a Critical Deadline

When a hard deadline is at risk, the options most managers reach for first are the ones that work least well.

**What almost never works:**
- **Adding people** — adding developers to a late project adds communication overhead and slows things down initially (Brook's Law). The one exception: adding a senior developer as a shadow/pair to an existing developer can help if done early enough.
- **Reducing quality** — "we'll write tests after" always costs more than the time saved. It either causes post-launch fires or results in a growing unpayable quality debt.

**What sometimes works:**
- **Adding work time** — genuinely warranted in a true crisis, but sets a precedent. Use sparingly.

**What works best:**
- **Reducing scope** — identify what can be cut while still delivering core value. "What's the minimum we can ship that still solves the problem?" is the most important question to ask before a deadline crunch, not during.

---

## The Iron Law of Projects

From *How Big Things Get Done* (Flyvbjerg): across thousands of large projects studied, only 8.5% came in on time and on budget. This is not a project management failure — it's a structural property of how humans plan.

**Why estimates are almost always wrong:**
- Planners anchor on best-case scenarios and uniqueness ("this project is special")
- Unknown unknowns don't show up in any estimate
- Complexity grows non-linearly but estimates grow linearly
- Optimism bias: teams systematically underestimate duration and cost

**Reference-class forecasting — the fix:**

Instead of estimating from scratch ("how long will this take?"), ask: *"What happened on similar projects?"*

Find a set of comparable completed projects — similar scope, similar team, similar domain. Look at how long they actually took and how much they actually cost. Anchor your estimate there, then adjust for specific differences.

This sounds obvious. Almost no one does it. The instinct is to treat every project as unique and estimate bottom-up. The data says: the outside view (comparable projects) is almost always more accurate than the inside view (detailed bottom-up estimation).

**Think Slow, Act Fast:**

The most expensive thing in project delivery is changing course mid-execution. Flyvbjerg's principle: invest heavily in planning before committing, then execute quickly once committed.

The pattern that kills projects: starting fast before the design is settled, then encountering fundamental issues mid-way and either pivoting expensively or shipping something that doesn't work.

Practically: before green-lighting a large initiative, ask whether the design is actually resolved. "We'll figure it out as we go" is not a design. The hill concept (see "The Always Green Method") is a micro-version of the same idea: climb far enough to see the full scope before you commit.

---

## There Are No Technical Projects

Hot take worth internalizing: **all projects are business projects.** If an engineering team is doing something that can't be justified in business terms, they're doing it wrong.

This doesn't mean abandoning technical work. It means every technical initiative — refactors, dependency upgrades, infrastructure changes, architecture improvements — should be framed in terms of the business value it delivers.

| Looks like | Is actually |
|---|---|
| Refactoring | Reducing the time it takes to ship features by N weeks |
| Updating dependencies | Reducing security risk and support costs |
| Adding tests | Reducing the frequency and cost of production incidents |
| Improving architecture | Enabling the team to build X, which they currently can't |

The business case doesn't have to be exact — it has to be honest and visible. When technical work has no business framing, it's the first thing cut in planning. When it does, it competes on equal footing.

There's a second principle: **some things just need to happen.** You can't build software without tests, security, or operational support. Explain why these are necessary, but don't let "but this is really a business decision" become a reason to continuously deprioritize work that keeps the system running.

---

## Feature Factory Warning Signs

Signs your team is being run as a feature factory — shipping output with no measurement of outcomes:

- No measurement of feature impact after shipping
- Teams reshuffled between projects constantly (Team Tetris)
- Success theater around "shipping" with no discussion of whether it worked
- Features are never removed, even when they don't get used
- Teams can't connect their work to key business or customer metrics
- Retrospectives focus on process, never on whether product decisions were right

The risk is that a feature factory *feels* productive — lots of shipping, lots of demos — while actually delivering little business value. As EM, your job is to push for outcome measurement even when the delivery machine doesn't want to slow down.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md). For running a company-wide cleanup event, read [`references/extended.md`](references/extended.md).

---

## Related Skills

- `shadow-work` — Shadow backlog and untracked work are a major source of capacity planning failures
- `team-health` — Team capacity and morale as planning inputs
- `working-with-pm` — A true partnership produces a single roadmap for product and tech
- `managing-urgency` — When deadline pressure overrides the plan
