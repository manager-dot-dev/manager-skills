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

From the articles directly:

- **Never delegate 100% of an area.** Stay in the rotation. Do the work yourself occasionally.
- **You can share at least 50% of your current work.** The exceptions are fewer than you think.
- **Never solve it for them.** When they're struggling, coach — don't rescue.

---

## Signs You're Not Delegating Enough

- You work through weekends to "help" the team meet deadlines
- You handle production incidents yourself so the team "isn't disturbed"
- You lead every new project personally
- Developers come to you as the source of knowledge for every question

---

## Related Skills

- `managing-yourself` — Over-involvement is trap #5 in the 10 ways EMs get stuck
