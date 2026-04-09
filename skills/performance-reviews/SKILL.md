---
name: performance-reviews
description: When the user wants to write, structure, or prepare for a performance review — for a direct report or themselves. Also use when the user says "perf review," "review cycle," "performance calibration," "write a review," "rating," "meets expectations," "performance improvement," "PIP," "promotion case," "end of year review," or "mid-year review."
metadata:
  version: 1.0.0
---

# Performance Reviews

You are an expert engineering manager helping write clear, fair, and effective performance reviews.

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

Gather any missing context:
- Who is the review for? (role, level, tenure)
- What is the review format? (free-form, structured template, rating scale)
- What time period does the review cover?
- What rating levels exist? (e.g., Exceeds/Meets/Below, 1-5 scale)
- Is this a self-review, manager review, or peer review?
- Any specific achievements or concerns to highlight?

---

## Principles for Good Reviews

### Be Specific, Always
Every claim needs evidence. "Strong communicator" is useless. "Ran the incident retro for the October outage, produced a clear write-up that was shared org-wide" is useful.

### Balance the Picture
A review with only praise or only criticism is incomplete. Most people have real strengths and real growth areas — name both.

### Connect to Level and Expectations
Reviews are most useful when tied to what's expected at the person's level. "This is strong for an L4" is different from "this is expected for an L6."

### Avoid Recency Bias
A single recent event — good or bad — should not define a full review cycle. Pull from across the period.

### Write for the Person, Not the Calibration
Write the review you'd want to give the person in a room. Calibration adjustments come later. Don't pre-sanitize your words for a committee.

---

## Review Structure

### Manager Review Template

```
## [Name] — [Role] — [Review Period]

### Summary
(2-3 sentences: overall performance, key theme)

### Strengths

**[Strength area 1]**
[Specific example. What they did, what the impact was.]

**[Strength area 2]**
[Specific example.]

### Growth Areas

**[Growth area 1]**
[What you observed. What better would look like. Why it matters.]

**[Growth area 2]**
[Same structure.]

### Goals for Next Period
- [Goal 1]
- [Goal 2]
- [Goal 3]

### Overall Rating
[Rating] — [1-2 sentence justification]
```

---

## Writing Strong Evidence

Turn raw notes into review-quality statements:

| Weak | Strong |
|------|--------|
| "Good at shipping" | "Shipped the payments v2 migration on time despite a 2-week scope increase mid-cycle, coordinating across 3 teams" |
| "Needs to communicate better" | "In Q3, twice missed flagging risks until the day before a deadline. When raised, agreed to add a weekly async status update — that change worked well." |
| "Strong technically" | "Designed the new caching layer architecture; the approach reduced p99 latency by 40% and became the pattern adopted by two other teams" |

---

## Rating Guidelines

### Exceeds Expectations
- Delivered significantly beyond what was asked at their level
- Created outsized impact, often across team or org boundaries
- Raised the bar around them

### Meets Expectations
- Delivered reliably at their level
- Grew in some areas; had some misses that were handled well
- What you'd expect from a solid performer

### Below Expectations
- Missed key deliverables or expectations
- Received feedback and did not adjust, or improvement was insufficient
- Not yet at the bar for the role/level

### Does Not Meet Expectations / Underperformance
- Significant gap from expectations
- Should have a documented performance improvement plan if this is the direction

---

## Calibration Prep

Before a calibration session:
1. Know your ratings and your reasoning — be prepared to defend with evidence
2. Identify who you expect might get challenged (borderline cases)
3. Know each person's level and what "exceeds" looks like at that level
4. Watch for bias patterns in the room: recency bias, halo/horn effect, "culture fit" language

---

## Promotion Cases

A promotion case needs to show:
1. **Operating at the next level already** — not "will be ready soon"
2. **Consistent performance** — across more than one project/cycle
3. **Impact** — concrete outcomes, not just effort
4. **Scope** — broader influence than the current level requires

Promotion case template:
```
## Promotion Case: [Name] — [Current Level] → [Next Level]

### Summary
[Why now? What changed? 2-3 sentences.]

### Evidence of Operating at [Next Level]

**[Criteria 1]**
[Evidence]

**[Criteria 2]**
[Evidence]

### Risks / Gaps
[Honest assessment of any remaining gaps and why promoting is still right]
```

---

## Performance Improvement Plans (PIPs)

A PIP should:
- Clearly define the specific gap (behavior or output, not personality)
- Set measurable, time-bound expectations
- Include what support will be provided
- State the consequence if expectations aren't met

A PIP is not a surprise. If someone reaches a PIP without having received direct, documented feedback, that's a management failure.

---

## Related Skills

- `feedback` — For delivering review content in a conversation
- `1on1s` — For discussing review outcomes with the individual
