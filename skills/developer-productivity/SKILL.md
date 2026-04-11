---
name: developer-productivity
description: Helps engineering managers measure and improve team delivery — produces a history of why common metrics fail, the DORA four-key-metrics framework (deployment frequency, lead time, change failure rate, MTTR), DevEx's three dimensions (feedback loops, cognitive load, flow state), a translation layer from engineering metrics to business outcomes, and a list of measurement anti-patterns to avoid. Use when the user says "how do I measure productivity," "DORA metrics," "velocity," "cycle time," "developer experience," "DevEx," "how do I show our team is performing well," "metrics for engineering," "team is slow," "engineering performance," or "connect engineering to business." Do NOT use for managing an underperforming individual — use performance-reviews instead.
metadata:
  version: 2.1.2
---

# Developer Productivity

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
- **Don't know where to start with engineering metrics** → DORA: The Four Key Metrics (start here)
- **Team feels slow but you can't point to data / engineers say they're blocked** → DevEx: Three Dimensions
- **Leadership asking how the team is performing** → Tying Engineering Metrics to Business Outcomes
- **Being asked to rank or score individual developers** → The Problem With Productivity Metrics + What Not to Do
- **Wondering whether surveys and qualitative data count** → Qualitative Metrics Are Not Soft

---

## Default Response Shape

When helping with productivity, keep the focus on systems, not individual scoring:

1. **Problem framing:** what the user is trying to learn or prove.
2. **Metric set:** 2-5 team-level signals, mixing delivery, quality, and developer experience.
3. **Interpretation:** what each metric can and cannot tell you.
4. **Action loop:** how the team will use the data to remove friction.
5. **Anti-pattern warning:** what not to measure or communicate.

If leadership wants a single productivity number, explain the risk and offer a small dashboard of complementary signals instead.

---

## The Problem With Productivity Metrics

Measuring developer productivity is one of the hardest problems in engineering management. The history of attempts illustrates why: every metric that gets adopted gets gamed or misinterpreted.

- **SLOC** (lines of code) — incentivizes verbose code, penalizes refactoring
- **Velocity** (story points per sprint) — measures effort estimates, not output; easily inflated
- **Cycle time** — better, but captures only one dimension of delivery

The underlying issue: software development is a knowledge work discipline. Unlike factory output, it can't be measured by counting things without losing what actually matters.

**The wrong use of metrics:** measuring individuals. Any metric applied to individual developers creates perverse incentives — people optimize for the metric at the expense of the actual work. Don't rank engineers by PR count, commit frequency, or story points.

**The right use of metrics:** identifying system-level friction. Good metrics answer "where is the team slowing down, and why?" — not "who is performing well?"

---

## DORA: The Four Key Metrics

The most evidence-backed framework for measuring engineering delivery health. Based on research across thousands of organizations, high performers consistently score well on all four:

| Metric | What it measures | High performer benchmark |
|---|---|---|
| **Deployment frequency** | How often you deploy to production | Multiple times per day |
| **Lead time for changes** | Commit to production | Less than 1 hour |
| **Change failure rate** | % of deployments causing incidents | 0–15% |
| **Mean time to recovery (MTTR)** | How quickly you recover from incidents | Less than 1 hour |

These metrics correlate strongly with business outcomes (revenue, customer satisfaction, reliability). They measure the delivery system, not individuals.

**How to use them as EM:**
- Baseline your current state. Don't compare to benchmarks yet — just establish your own baseline.
- Pick the one metric where your team is furthest from high performance. Fix that first.
- Don't optimize all four simultaneously — that's how you get gaming instead of improvement.

---

## DevEx: Three Dimensions of Developer Experience

The DevEx framework (from DX research) focuses on the developer's lived experience rather than system outputs. It organizes friction into three categories:

**Feedback loops** — When a developer makes a change, how fast do they know if it worked? This includes CI/CD speed, test run time, code review turnaround, and stakeholder feedback speed. Slow feedback loops break concentration and delay learning.

**Cognitive load** — How much do developers have to keep in their heads to do their work? Complex processes, unclear ownership, undocumented systems, and context switching all increase cognitive load. High cognitive load slows work and increases errors.

**Flow state** — Can developers get into deep, uninterrupted focus? Flow state requires: blocks of uninterrupted time, fast tooling, clear goals, and low anxiety. Even good feedback loops and low cognitive load won't produce flow if the environment is fragmented.

**How to use it:** Run a short team exercise — ask engineers to score each dimension (1–5). The lowest-scoring dimension is your most important focus area. The answers often surface specific, actionable problems (e.g., "our CI takes 45 minutes" or "I never know who owns this service").

---

## Qualitative Metrics Are Not Soft

A common misconception: quantitative metrics are objective and reliable; surveys and qualitative data are fuzzy and unreliable.

This is wrong. Some of the most important productivity signals can only come from humans:

- How often do you feel blocked waiting for someone else?
- How confident are you that your work won't break something unexpectedly?
- How clear is it to you what "good" looks like for your current project?

**DORA itself uses surveys** for several of its four key metrics — including deployment frequency for organizations that can't measure it automatically. Google's research found that self-reported data is highly reliable when questions are specific and objective.

The practical rule: **use quantitative metrics to identify where** there's a problem; use qualitative data to understand **why**. Neither alone gives the full picture.

---

## Tying Engineering Metrics to Business Outcomes

When leadership asks "how is the engineering team doing?", the answer that lands is the one connected to what they care about.

Common business metrics that engineering directly impacts:

| Business metric | Engineering connection |
|---|---|
| **GRR / NRR** (customer retention) | Reliability, quality, user experience |
| **CAC** (cost to acquire customers) | Feature velocity — shipping faster reduces sales cycle |
| **Time to market** | Lead time for changes, deployment frequency |
| **Support cost** | Change failure rate, MTTR |

A practical translation example: "Our change failure rate dropped from 22% to 8% this quarter. That means fewer incidents, less time in firefighting mode, and fewer support escalations — which directly reduces support cost and improves retention."

**The EM's job** is to build this translation layer. Engineering metrics don't automatically tell the business story — you have to connect the dots explicitly and repeatedly.

---

## What Not to Do

- **Don't use metrics to evaluate individual developers.** This destroys trust and optimizes for the metric at the expense of real work.
- **Don't report raw velocity.** It measures estimated effort, not output. Leadership will compare across sprints and ask why it dropped, forcing the team to inflate estimates.
- **Don't pick a framework and implement all of it at once.** Start with one or two metrics, establish a baseline, and use them to have conversations — not to produce dashboards nobody reads.
- **Don't treat metrics as a substitute for judgment.** A team with perfect DORA scores can still be building the wrong thing. Metrics measure delivery health, not direction.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md) for the full list of source articles (with links) and books.

---

## Related Skills

- `team-health` — Productivity friction and DevEx signals often surface in team health conversations
- `roadmap-planning` — Delivery metrics inform capacity planning and deadline discussions
- `meetings` — Flow state is the DevEx dimension most directly affected by meeting culture
