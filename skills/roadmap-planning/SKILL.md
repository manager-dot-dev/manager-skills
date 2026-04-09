---
name: roadmap-planning
description: When the user wants to plan a team roadmap, prioritize projects, communicate priorities to stakeholders, or run a planning cycle. Also use when the user says "roadmap," "quarterly planning," "OKRs," "prioritization," "what should we work on," "planning cycle," "project list," "backlog grooming," "stakeholder alignment," or "capacity planning."
metadata:
  version: 1.0.0
---

# Roadmap Planning

You are an expert engineering manager helping build clear, defensible, and executable roadmaps.

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

Gather any missing context:
- What time horizon? (quarterly, H1, annual)
- What's the team's capacity? (headcount, known absences, tech debt load)
- What are the top company/org goals this period?
- What's the current list of potential work items?
- Who are the key stakeholders and what do they care about?

---

## Principles

### Strategy First, Then Projects
A roadmap is a communication tool for a strategy. If you can't explain why this set of projects over others, the roadmap will fall apart in the first stakeholder conversation.

### Say No Out Loud
A roadmap that tries to do everything is not a roadmap. Every "yes" is a "no" to something else. Name what you're not doing and why.

### Separate Outcomes from Outputs
Bad: "Ship feature X." Good: "Improve checkout conversion by 10%." Projects should serve outcomes, not the other way around.

### Build in Slack
A team running at 100% capacity can't handle incidents, tech debt, or unexpected priorities. Plan for 70-80% utilization.

### Stakeholders Are Inputs, Not Approvers
Gather input broadly. Make the decision clearly. Communicate with confidence.

---

## Planning Process

### Step 1: Inputs Gathering
Collect:
- Company / org strategy and goals
- Product priorities and commitments
- Tech debt and reliability needs
- Team requests and growth opportunities
- Carry-over from last cycle

### Step 2: Capacity Estimation
```
Available weeks: [X weeks in quarter]
Minus: holidays, onboarding, meetings overhead (~20%)
Minus: on-call / incidents / support (~10-15%)
Minus: planned PTO
= Available engineering weeks: [N]

At [average velocity], that supports roughly [X] medium-sized projects.
```

### Step 3: Prioritization

Use a simple framework. Recommended: **Impact × Confidence ÷ Effort**

| Project | Impact (1-5) | Confidence (1-5) | Effort (1-5) | Score |
|---------|-------------|-----------------|-------------|-------|
| Project A | 5 | 4 | 2 | 10 |
| Project B | 3 | 3 | 4 | 2.25 |

Qualitative overlays:
- Is this a commitment we've already made?
- Is there a hard deadline or external dependency?
- Does this unblock another team?
- Is there a strategic reason to deprioritize high-scoring work?

### Step 4: Draft Roadmap
Group work into themes. Name the goal each theme serves.

### Step 5: Stakeholder Review
Present the draft. Gather input. Make final decisions. Communicate clearly.

---

## Roadmap Document Template

```markdown
# [Team Name] Roadmap — [Quarter/Period]

## Team Goals
1. [Goal 1 — outcome-oriented]
2. [Goal 2]
3. [Goal 3]

## Theme 1: [Name]
*Why: [How this connects to goals]*

| Project | Owner | Size | Status |
|---------|-------|------|--------|
| [Project A] | | M | Planned |
| [Project B] | | S | Planned |

## Theme 2: [Name]
*Why: [Justification]*

...

## What We're NOT Doing (and Why)
- [Item]: [Reason — deferred, deprioritized, out of scope]
- [Item]: [Reason]

## Risks and Dependencies
- [Risk or dependency and mitigation]

## Capacity Summary
Total team capacity: [N] eng-weeks
Allocated: [X] eng-weeks ([Y]%)
Buffer: [Z]%
```

---

## Communicating the Roadmap

### To Your Team
- Explain the *why* behind priorities, not just the *what*
- Invite questions on trade-offs — don't just present
- Make clear what's locked vs. still flexible

### To Stakeholders
- Lead with outcomes, not projects
- Name what you said no to and why — this builds credibility
- Be clear on what you need from them (decisions, input, sign-off)

### To Leadership
- Connect to company goals explicitly
- Name the risks and what would change the plan
- Don't present false certainty — distinguish committed from planned

---

## Common Pitfalls

- **Roadmap as wish list** — Every item gets added, nothing is real
- **No themes** — A list of projects is not a strategy
- **Over-commitment** — Plan at 100% capacity, then miss everything
- **Set and forget** — Roadmaps should be reviewed monthly and updated quarterly
- **Stakeholder-driven thrash** — Changing priorities every time someone complains

---

## Related Skills

- `em-context` — For team context, size, capacity
- `team-health` — For understanding team capacity and morale as planning inputs
