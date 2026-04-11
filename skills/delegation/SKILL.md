---
name: delegation
description: Guides managers out of the bottleneck role — provides the Team Rep pattern, Epic Ownership model, Task-Relevant Maturity framework, kingdom ownership, and three-layer assignment strategy. Use when the user wants to delegate work or says "I'm doing everything," "team isn't taking ownership," "I can't let go," "team rep," "project ownership," "I'm the go-to person," "bus factor," "I work weekends," "how do I delegate," or "engineers don't take initiative." Do NOT use for managing a specific underperformer (use performance-reviews) or deciding what work to prioritize (use roadmap-planning).
metadata:
  version: 2.1.2
---

# Delegation

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
Identify the situation first:

- **You're the bottleneck — doing too much yourself** → The Two Things to Delegate First (start here)
- **Not sure how much involvement to have on a task or with a person** → Task-Relevant Maturity
- **Wondering if you're micro or under-managing** → Micromanagement vs. Under-management
- **Engineers wait to be told rather than acting** → Intent-Based Leadership
- **Want to give engineers deeper ownership beyond individual tasks** → Giving Engineers a Kingdom
- **Assigning work across the team strategically** → Three-Layer Assignment Framework
- **Feeling anxious about letting someone do it differently than you would** → read [`references/extended.md`](references/extended.md) — Delegation Anxiety
- **Going on vacation / someone needs to cover** → read [`references/extended.md`](references/extended.md) — Covering for You While You're Away
- **Deciding which tasks to pick up yourself as EM** → read [`references/extended.md`](references/extended.md) — Being Hands-On: Choose Tasks Intentionally
- **Someone on the team seems entirely self-directed** → read [`references/extended.md`](references/extended.md) — Free Electrons
- **A process keeps breaking despite repeated asks** → read [`references/extended.md`](references/extended.md) — Mechanisms Over Intentions
- **Engineers keep coming to you for answers instead of deciding** → read [`references/extended.md`](references/extended.md) — Pulling Instead of Pushing
- **Feedback about being too controlling or too hands-off** → read [`references/extended.md`](references/extended.md) — 4 Decision-Making Modes

---

## Default Response Shape

When helping with delegation, diagnose the bottleneck before giving tactics:

1. **Delegation target:** what work should move away from the manager.
2. **Maturity read:** how much context, autonomy, and follow-up the person or task needs.
3. **Delegation contract:** owner, decision rights, check-in cadence, and done criteria.
4. **Risk controls:** what the manager should inspect without taking the work back.
5. **Script:** exact wording for assigning the work or resetting ownership.

If the manager is anxious about quality, address the control fear directly and design a review loop rather than advising them to "just let go."

---

## The Two Things to Delegate First

### 1. Day-to-Day Operations: The Team Rep

The most impactful first delegation is the daily operational load — alerts, support requests, production issues.

**How it works:**

- Each day/week, one team member is the "Team Rep" (rotating)
- The Rep is responsible for: monitoring alert channels, helping the support team, debugging new issues, coordinating incident response
- The Rep is NOT responsible for fixing everything — the developer who introduced a bug fixes it. The Rep coordinates and learns.
- The manager is NOT the first call. The Rep is.

**Setup tips:**

- Put it on the calendar as a recurring rotation with a written guidelines doc
- In the first rotations, consultations with you are fine — but never solve it yourself
- Keep yourself in the rotation. Don't exempt yourself from the load you're delegating.

**Benefits:**

- No single point of failure (bus factor)
- Increased ownership and debugging skills across the team
- Developers feel "we're in the same boat"

### 2. New Projects: Epic Ownership

Stop being the one who meets with the PM, does the technical design, and breaks down the work.

**How it works:**

- When a new epic arrives, assign a team member as the owner
- They: meet with the PM, write the technical design, break it into tasks, decide work distribution
- You: stay involved — share thoughts, ask questions, review — but they make the decisions

Each developer leads only one project at a time, so they can be 100% dedicated to it — often producing better designs than you rushing through five simultaneously.

---

## Knowledge Ownership

If you're the go-to person for every system and every question, that's a problem. Divide the team's systems and applications across people with clear, explicit owners. When someone asks you about a system, redirect them to the owner.

---

## Delegation Principles

- **Never delegate 100% of an area.** Stay in the rotation. Do the work yourself occasionally.
- **You can share at least 50% of your current work.** The exceptions are fewer than you think.
- **Never solve it for them.** When they're struggling, coach — don't rescue.
- **Match the task to the person's driver.** When you delegate something that doesn't align with what motivates someone, they procrastinate and you end up nagging. When it aligns — they take ownership without being asked. A Connection-driven engineer will thrive as the team's interview coordinator; an Impact-driven one will take on the CS sprint you've been avoiding; a Growth-driven one will light up when you hand them an architectural decision. "Every task you don't like can be a growth opportunity for someone else." (See `engineer-motivation` for how to identify each person's driver.)

---

## Intent-Based Leadership

From _Turn the Ship Around_ (Marquet): instead of asking permission or waiting for direction, team members state their intent and proceed unless stopped.

The pattern: _"I intend to deploy the release at 2pm — let me know if you see a reason not to."_ Instead of: _"Should I deploy the release?"_

Why it works: asking permission transfers ownership to the person being asked. Stating intent keeps ownership with the person acting, while still maintaining oversight. Over time, it trains the entire team to think like owners rather than executors.

**How to implement it:**

- Model it yourself with your own manager: "I intend to finalize this hire — flag me if you have concerns" (this is also how you earn delegation upward)
- When a report comes to you asking "should I do X?" — ask them what they intend to do and have them tell you. Then respond to their intent rather than making the decision for them
- Reserve overrides for cases where you have information they don't. If you're overriding purely because you'd do it differently, ask whether that's worth the cost to their ownership

The goal: a team that moves without being told, rather than a team that waits to be told.

---

## Micromanagement vs. Under-management

From _The Dichotomy of Leadership_ (Willink): the failure modes on both ends of the delegation spectrum are equally real, and the symptoms are distinct.

**Signs you're micromanaging:**

- You approve every decision before it moves forward
- Team members stop bringing you problems because they expect you to solve them
- You review and rewrite work that was "good enough"
- No one acts when you're not available
- Your calendar is full of unnecessary check-ins

**Signs you're under-managing:**

- Tasks go off-track and you're the last to know
- Team members make significant decisions without relevant context you had
- Quality degrades or standards slip without you noticing
- Work done by different people on the team is inconsistent in ways that matter
- You find out about problems after they've become crises

Neither extreme is safe. The default assumption in engineering culture is that under-management is better than micromanagement — which leads many EMs to stay too hands-off and catch problems too late.

The right position moves depending on the person and the task (see Task-Relevant Maturity). But the diagnostic above gives you early signals before you've drifted too far in either direction.

---

## How Much Involvement Is Right: Task-Relevant Maturity

Most managers stop at "juniors need more oversight, seniors less." That's still too blunt.

Andy Grove's concept from _High Output Management_: **Task-Relevant Maturity (TRM)** — not the person's general seniority, but their maturity for _this specific task_. A senior engineer doing something for the first time has low TRM for that task. A junior doing their fifth microservice has high TRM.

- **Low TRM** → structured involvement: tell them what to do, check in regularly, be available
- **High TRM** → step back: set the goal, let them work, trust the outcome

Getting this wrong in either direction is a failure:

- Too hands-on with high TRM → micromanagement, demotivation
- Too hands-off with low TRM → the customer (internal or external) pays for the mistake

When a task feels high-stakes, ask yourself: is this person's TRM actually high for _this_ task — or just in general?

---

## Giving Engineers a Kingdom

Beyond task delegation, each engineer should own a defined area — a kingdom with real decision-making authority, not just execution responsibility.

Four ownership types that work:

1. **An application or system** — the owner drives the roadmap relationship with PM, monitors usage, and is the incident point-of-contact
2. **A microservice** — health monitoring, technical debt prioritization, contributing guidelines
3. **A third-party integration** — leads the vendor relationship, monitors release notes, tracks integration health
4. **An internal tool** — the internal expert and champion, responsible for adoption and updates

The key distinction from task delegation: kingdom owners hold decision-making authority over their area. They prioritize, not just execute.

Aim for one to two kingdoms per engineer; spreading too many thin defeats the purpose. Start by identifying the areas that consume the most of your own time and transfer those first.

The framing matters: "ownership area" can feel like a burden of chores. "Kingdom" implies authority and pride — both affect whether engineers embrace or resist the responsibility.

---

## The Three-Layer Assignment Framework

Work assignment operates across three layers that must be balanced simultaneously:

- **Efficiency** — assign the most capable person for what's needed right now
- **Advancement** — assign for growth and career trajectory, often at a speed cost
- **Durability** — assign to prevent single-points-of-failure, even when neither efficiency nor growth is optimized

The knowledge map exercise makes the third layer concrete: plot engineers against skill/system areas to visualize coverage gaps and identify dangerous single-owner areas.

When moving engineers into new domains to serve advancement or durability, apply Task-Relevant Maturity (see above) — a Staff engineer new to a domain needs closer guidance than their title implies.

Two traps to watch: **inertia** (comfortable assignments calcify even when business needs change) and **activation energy** (the transition cost is real and must be planned for, not wished away). Revisit assignments deliberately every quarter rather than letting the last good decision run indefinitely.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic — read [`references/sources.md`](references/sources.md) for the full list of source articles (with links) and books.

---

## Related Skills

- `managing-yourself` — Over-involvement is trap #5 in the 10 ways EMs get stuck
- `engineer-motivation` — Identifies each engineer's driver for motivation-aligned delegation
