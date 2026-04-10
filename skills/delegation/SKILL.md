---
name: delegation
description: When the user wants to delegate work, reduce bottlenecks, give their team more ownership, or stop being the single point of failure. Also use when the user says "I'm doing everything," "team isn't taking ownership," "I can't let go," "team rep," "project ownership," "I'm the go-to person," "bus factor," "I work weekends," or "how do I delegate."
metadata:
  version: 1.0.0
---

# Delegation

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

---

## The Two Things to Delegate First

### 1. Day-to-Day Operations: The Team Rep

The most impactful first delegation is the daily operational load — alerts, support requests, production issues.

**How it works:**
- Each day, one team member is the "Team Rep" (rotating)
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

## Signs You're Not Delegating Enough

- You work through weekends to "help" the team meet deadlines
- You handle production incidents yourself so the team "isn't disturbed"
- You lead every new project personally
- Developers come to you as the source of knowledge for every question

---

---

## Covering for You While You're Away

When you go on vacation, who runs the team? Three options, in increasing order of long-term value:

- **Your manager** — convenient, easy, keeps developers focused on work. Has the side benefit of giving your manager direct exposure to your team.
- **The PM** — builds their understanding of the team's work and challenges. Strengthens the PM-team relationship.
- **A team member** — hardest to implement, most valuable. Even if no one on your team is currently interested in a management path, covering for you gives them genuine experience: designing tasks, guiding teammates, managing production issues, working directly with the PM, communicating with broader audiences.

Don't assume someone won't want the responsibility — sometimes all they need is the opportunity. If they try it and discover it's not for them, that's also useful information.

---

## Being Hands-On: Choose Tasks Intentionally

When you take a task as an EM, three patterns that look like contribution but aren't:

- **Taking only small or undesirable tasks** — avoids real risk, stays in the margins
- **Sticking to what you know** — comfort over learning
- **Taking too many tasks** — spreading thin, blocking others, reverting to IC mode

Before picking up a task, ask: what's the actual goal behind me doing this? Is it to work closely with a new team member? To help in a difficult period? To learn a system you don't know well? To reduce friction somewhere?

Tasks you take as EM should serve a purpose beyond helping the team ship. If the only reason is "I like this kind of work," that's a comfort trap.

---

## How Much Involvement Is Right: Task-Relevant Maturity

Most managers stop at "juniors need more oversight, seniors less." That's still too blunt.

Andy Grove's concept from *High Output Management*: **Task-Relevant Maturity (TRM)** — not the person's general seniority, but their maturity for *this specific task*. A senior engineer doing something for the first time has low TRM for that task. A junior doing their fifth microservice has high TRM.

- **Low TRM** → structured involvement: tell them what to do, check in regularly, be available
- **High TRM** → step back: set the goal, let them work, trust the outcome

Getting this wrong in either direction is a failure:
- Too hands-on with high TRM → micromanagement, demotivation
- Too hands-off with low TRM → the customer (internal or external) pays for the mistake

When a task feels high-stakes, ask yourself: is this person's TRM actually high for *this* task — or just in general?

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

## Delegation Anxiety

Nobody tells you about the pit-in-the-stomach feeling when someone does your task differently.

They accept a solution you'd have pushed back on. They make a quick fix where you'd have dug deeper. They write code that works but not the way you'd write it. These are emotional triggers — not performance issues.

Delegation doesn't mean perfect. It means finding the balance between maintaining standards, preserving your own sanity, accepting different approaches, and growing your team. Your job is not to create mini-versions of yourself.

When you feel the anxiety: ask whether the outcome was acceptable, not whether it was done your way. If the outcome was acceptable, that's delegation working correctly.

---

## Free Electrons

From *Peopleware*: some engineers are self-motivated super-achievers who naturally choose their own orbits. They define their own problems, drive their own directions, and produce disproportionate value precisely because they're self-directed.

The worst thing you can do with a free electron is decide what they should be working on. The best response: let them define their own job.

Not every engineer is a free electron. The skill is identifying the few who have the right mix of perspective, maturity, and drive — and then getting out of their way rather than managing them into mediocrity.

---

## Related Skills

- `managing-yourself` — Over-involvement is trap #5 in the 10 ways EMs get stuck
