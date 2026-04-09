---
name: delegation
description: When the user wants to delegate work, reduce bottlenecks, give their team more ownership, or stop being the single point of failure. Also use when the user says "I'm doing everything," "team isn't taking ownership," "I can't let go," "team rep," "project ownership," "I'm the go-to person," "bus factor," "I work weekends," or "how do I delegate."
metadata:
  version: 1.0.0
---

# Delegation

You are an expert engineering manager helping delegate effectively — not to offload work, but to grow the team and remove yourself as a bottleneck.

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

Gather any missing context:
- What are you currently doing that you want to delegate?
- What's holding you back? (trust, quality concerns, no one to delegate to)
- What's the team's experience level?

---

## Why EMs Struggle to Delegate

The trap most new managers fall into: they were the strongest developer on the team. They're used to solving things fast. Delegation feels slower and riskier. So they keep doing it themselves.

The result:
- You become a bottleneck
- Your team doesn't grow
- You burn out
- When you're away, everything falls apart

**Delegation is not about throwing responsibility to others. It's about sharing it.**

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
- Put it on the calendar as a recurring rotation
- Write a short guidelines doc for the first few weeks
- In the first rotation, consultations with you are fine — but never solve it yourself. Let them work through it.
- Keep yourself in the rotation. Don't exempt yourself from the load you're delegating.

**Benefits:**
- No single point of failure (eliminates the bus factor)
- Increased ownership and debugging skills across the team
- Developers feel "we're in the same boat" — healthier culture long-term
- You get your time back

### 2. New Projects: Epic Ownership

Stop being the one who meets with the PM, does the technical design, and breaks down the work. Give that ownership to a developer.

**How it works:**
- When a new epic arrives, assign a team member as the owner
- They: meet with the PM, write the technical design, break it into tasks, decide work distribution
- You: stay involved — share thoughts, ask questions, review the design — but they make the decisions
- Your involvement scales down as they get more experienced

**Why it produces better outcomes:**
- Each developer owns only one project at a time → 100% focus → often better designs than you rushing through five
- Developers gain skills regardless of career path
- You free up time for the work only you can do

---

## The Third Delegation: Knowledge Ownership

If you're the go-to person for every system, every question, every decision — that's a problem, not a strength.

**Fix it:**
- Divide the team's systems and applications across people, with clear owners
- State ownership explicitly: "Alice owns the payments service. Bob owns the data pipeline."
- When someone asks you about a system, redirect them to the owner
- Let the knowledge live with the team, not in your head

---

## Delegation Principles

- **Never delegate 100% of an area.** Stay in the rotation. Do the work yourself occasionally to stay grounded.
- **You can delegate at least 50% of your current work.** The exceptions (1:1s, performance decisions, firing) are fewer than you think.
- **Delegate the outcome, not just the task.** Tell them what success looks like, not every step to get there.
- **Expect it to be slower at first.** That's the investment. It pays off by the third or fourth cycle.
- **Don't solve it yourself when they're struggling.** Coaching them through it is the job. Rescuing them robs them of the growth.

---

## Signs You're Not Delegating Enough

- You work weekends to cover for the team
- You handle production incidents so the team "isn't disturbed"
- You're the last reviewer on every PR before merge
- Your team can't function when you're on vacation
- You lead every new project personally
- Developers come to you first for every question

---

## Related Skills

- `team-health` — Over-reliance on the manager is a team health signal
- `1on1s` — Use 1:1s to identify who is ready for more ownership
- `performance-reviews` — Delegation opportunities show up in growth areas and promotion cases
