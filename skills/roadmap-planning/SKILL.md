---
name: roadmap-planning
description: When the user wants to plan a team roadmap, prioritize projects, communicate priorities to stakeholders, or run a planning cycle. Also use when the user says "roadmap," "quarterly planning," "OKRs," "prioritization," "what should we work on," "planning cycle," "project list," "backlog grooming," "stakeholder alignment," or "capacity planning."
metadata:
  version: 1.0.0
---

# Roadmap Planning

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

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

## Related Skills

- `em-context` — For team context, size, capacity
- `team-health` — For understanding team capacity and morale as planning inputs
- `working-with-pm` — A true partnership produces a single roadmap for product and tech
