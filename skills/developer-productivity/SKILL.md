---
name: developer-productivity
description: When the user wants to measure, discuss, or improve their team's productivity, choose engineering metrics, or explain engineering performance to leadership. Also use when the user says "how do I measure productivity," "DORA metrics," "velocity," "cycle time," "developer experience," "DevEx," "how do I show our team is performing well," or "metrics for engineering."
metadata:
  version: 1.0.0
---

# Developer Productivity

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

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

## Related Skills

- `team-health` — Productivity friction and DevEx signals often surface in team health conversations
- `roadmap-planning` — Delivery metrics inform capacity planning and deadline discussions
- `deep-work` — Flow state is the DevEx dimension most directly affected by meeting culture
