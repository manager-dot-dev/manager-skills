---
name: code-reviews
description: When the user wants to improve their team's code review culture, deal with slow or ineffective reviews, assign reviewers, or set code review guidelines. Also use when the user says "code review," "PR review," "review culture," "pull request," "CR," "reviewers," "code review taking too long," or "nobody reviews my PRs."
metadata:
  version: 1.0.0
---

# Code Reviews

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

---

## The 4 Reviewer Types

Every team has these archetypes. Knowing who you're working with helps you manage reviews effectively.

### 1. The Perfectionist

Reviews every line, comments on everything, blocks PRs on style issues. High standards, but can slow the team down and demoralize authors — especially juniors.

**How to work with them:**
- Set limits on what's blocking vs. non-blocking
- When you see them arguing on a PR for the 3rd comment in a row, call it — "let's take this to a conversation"
- If feedback is about something out of scope (design, architecture), open a ticket for later rather than blocking the current PR

### 2. The Guru

Deep technical knowledge. Reviews uncover real issues, teach younger engineers, and raise overall quality. Often the most valuable reviewer for critical or complex work.

**How to work with them:**
- Involve them early in the design phase, not just at PR time — they catch more when they've seen the approach before implementation
- Use them as a learning resource: pair less experienced engineers with Guru reviewers deliberately
- Best reviewer for: junior engineers' PRs, complex domain changes, new architectural patterns

### 3. The Skimmer

Reviews fast, approves fast, misses things. Useful for low-risk or time-sensitive changes, but dangerous for critical paths.

**How to work with them:**
- Highlight specific areas in the PR description where you want their focused attention
- Don't use a Skimmer as the only reviewer for anything critical
- Best reviewer for: urgent hotfixes, low-risk changes, PRs where you mainly need a second pair of eyes

### 4. The Ignorer

Doesn't review unless you chase them. PRs sit open for days. Often not malicious — just overloaded or conflict-averse.

**How to work with them:**
- Be proactive: assign them explicitly, don't just tag
- If chasing hasn't worked, be assertive: "I need your review by EOD — can we set a time to walk through it?"
- For repeat patterns: set a meeting to walk through the PR together rather than waiting for async review

---

## The EM's Role in Code Review Culture

**Set clear guidelines.** Without guidelines, every reviewer invents their own standard. This creates inconsistency and conflict. Adopt or adapt existing standards (Google's Engineering Practices documentation is a solid reference).

**One concrete rule that matters: time.** Google's guideline: code reviews should be completed within one business day. If a reviewer can't do it in time, they should say so immediately so it can be reassigned. PRs sitting open is one of the most common and avoidable engineering bottlenecks.

**Don't let CRs sit.** As EM, watch for PRs that have been open too long with no movement. This is your signal to intervene — either unblock the author, reassign the reviewer, or escalate the decision.

**Match reviewer to task.** Not all PRs are equal, and not all reviewers are equal:
- Junior engineer's PR → assign a Guru (for learning)
- Urgent fix → assign a Skimmer (for speed), or a Guru if it's critical path
- New architecture → involve a Guru in the design phase, before a line of code is written
- Contentious PR (known disagreement) → assign someone who will engage, not avoid

---

## What the Data Says About Review Frequency and Speed

From research across 400+ engineering teams:

- **Skipping reviews entirely** produces ~1.9x more output but ~2.4x more bugs — roughly 25% more bugs per unit of work. Speed gains are real but not free.
- **The biggest quality gains** come between 0 and 0.5 reviews per PR. Diminishing returns set in after that. Not every PR needs a review.
- **High-quality reviews** correlate with 61% fewer bugs at the cost of 38% slower output. If you do reviews, make them thorough — shallow reviews have neither the speed benefit nor the quality benefit.
- **Turnaround speed is critical.** Teams merging PRs within 3 hours are 2.1x more productive than those taking 8+ hours. 10% of PRs wait 24+ hours — this kills both morale and flow.
- **Review quality is reciprocal.** Engineers who give low-effort reviews tend to receive them. The culture you model cascades.

Practical target: selective reviews on meaningful changes, high quality when done, resolved within 3 hours.

---

## The Refactor Authorization Framework

Developers chronically overestimate the need to rewrite code they didn't write. Joel Spolsky's observation explains why: it's harder to read code than to write it, meaning unfamiliarity is routinely misdiagnosed as technical debt.

Before authorizing a significant refactor, require two things:

1. **Is substantial new feature work planned in this area soon?** If not, the refactor may never pay off — the additional development velocity benefit never arrives.
2. **Has the developer spent meaningful time understanding the existing code?** It is common for 6–8 week rewrites to begin without a single day studying what is being replaced.

Old code that has survived years of production has accumulated implicit bug fixes and edge case handling that won't be obvious in a rewrite and will take years to rediscover.

Your role as EM: fight for refactor time when the business case is genuine, and push back when it isn't. Both are necessary.

---

## Related Skills

- `delegation` — Assigning the right reviewer is a form of delegation
- `team-health` — Review culture problems are often symptoms of broader team friction
- `working-with-architects` — Architects/Staff engineers are your Gurus; pull them in early

