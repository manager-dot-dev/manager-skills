---
name: performance-reviews
description: Helps diagnose underperformance, structure a performance case, decide whether to put someone on a PIP or let them go, and think through your own manager review. Use when the user says "perf review," "review cycle," "performance calibration," "write a review," "rating," "meets expectations," "performance improvement," "PIP," "promotion case," "end of year review," "mid-year review," "underperformer," "struggling employee," or "should I let them go." Do NOT use for delivering day-to-day feedback (use feedback) or for evaluating a new hire candidate (use hiring).
metadata:
  version: 2.1.2
---

# Performance Reviews

## Before Starting

Check for EM context first:
1. Read `.agents/em-context.md` if it exists (for review cycle format, rating scale, etc.)
2. If a person is mentioned, look for `.agents/reports/[name].md` — it will have their role, level, goals, current projects, and feedback history
3. Use that context — only ask for information not already covered

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

- **Someone on the team isn't performing — not sure what's wrong** → Diagnosing Underperformance: Work Left to Right (start here)
- **You've diagnosed the problem — now need to address the behavior** → 4-Stage Process for Addressing Persistent Behavior Problems
- **Wondering if you've been tolerating underperformance too long** → Recognizing Underperformance Early
- **Seriously considering letting someone go** → Making the Hard Call + When to Act
- **Writing or structuring your own manager review** → The Meta Performance Review Question

---

## Default Response Shape

When helping with performance, separate diagnosis from action:

1. **Performance read:** behavior, impact, pattern, and severity.
2. **Root-cause hypothesis:** resources, training, desire, fit, or ability.
3. **Evidence needed:** examples, expectations, prior feedback, and business impact.
4. **Manager action:** feedback, support plan, PIP, promotion case, or separation path.
5. **Wording:** review language or conversation script.

Do not let empathy turn into vagueness. Be humane and specific at the same time.

---

## Recognizing Underperformance Early

The most common trap: confusing improvement with potential. An engineer who goes from bad to mediocre is improving — but they may still be below the bar.

**The key question isn't "are they getting better?" It's "are they at the level I need?"**

Ray Dalio: *"If someone who has been getting grades of 30s and 40s raised their scores to 50s for a few months, it would be accurate to say they are getting better — but they would still be woefully inadequate."*

### Why managers tolerate underperformers too long

1. **Emotional connection** — you've invested in this person, you like them, you don't want to hurt them
2. **Sunk cost fallacy** — you've spent months training them and don't want to start over

Both are real. Both lead to lying to yourself and settling for mediocrity.

### How to stay objective

- **Set concrete expectations before problems start** — 30/60/90 day goals, on-call readiness, project lead criteria. Without a clear bar, "improving" will always feel like enough.
- **Use the "would I hire today?" question** — Not "am I better with or without them?" (always anchors on sunk cost). Instead: "Knowing what I know now, would I hire this person?" If no, that's your answer.
- **Set a checkpoint in advance** — 30 days, 60 days, end of cycle. A forced decision point prevents indefinite deferral.

### Staying humble

You will be wrong sometimes. A struggling engineer can turn into a standout with time, the right environment, or a role that fits them better. Frameworks are guides, not verdicts.

---

## Making the Hard Call: Letting Someone Go

Deep inside, you usually know. When you start to genuinely consider firing someone, it's probably already overdue.

**The relief test:** Imagine the employee tells you they're quitting. Do you feel relieved — or upset? If relieved, that's your answer.

(The Netflix "keeper test" — would you fight to keep them? — is the stricter version. The relief test is more realistic for most teams.)

### Why it's always hard

Usually it's one of three situations: you hired someone not suitable for the role; you didn't provide clear expectations or enough support; or the role changed and they no longer fit it. In all three cases, you share responsibility for the situation. That's why it should be hard — and why good managers struggle.

Don't confuse "they have potential" with "I can't make a hard decision." They're different things.

### The price of waiting

- **The employee suffers** — coming every day to a job where you're not doing well is exhausting
- **You suffer** — trying to help someone thrive when you know deep down they won't is draining
- **The team suffers** — working alongside underperformers is demotivating; when you finally act, the team almost always understands

I haven't yet encountered a manager who regretted a firing. Only ones who regretted waiting.

### Before you act: do this first

To know you did everything right before letting someone go:

1. **Give feedback immediately** — as soon as they step off track. Don't wait for it to accumulate.
2. **Be specific** — give concrete examples of what went wrong and what better looks like
3. **Have them repeat it back** — until what they say matches what you mean. People often think they understand expectations but don't.
4. **Write it down** — a clear list of what needs to change, measurable, visible to both of you
5. **Be patient** — changing behavior takes real work. It's often worth it.

Note: 50% of people on performance improvement plans become repeat offenders. Smart employees know how to rise to the occasion temporarily. Watch for the pattern.

---

## When to Act: The Fire Quickly Heuristic

A rough but useful signal: *if you've thought seriously about firing someone even once, you should probably act sooner rather than later.*

With genuinely strong employees, the thought doesn't arise. The fact that it arose at all is diagnostic.

This doesn't mean fire impulsively. It means: if you've crossed the threshold of "should I let this person go?" without acting on it, examine why you're waiting. The most common reason is discomfort — not evidence that the situation will resolve itself.

---

## The Meta Performance Review Question

The most useful question for evaluating a manager's performance: *"What would have been different if this person hadn't been here?"*

This targets manager delta — not what the team shipped, but what the manager caused to happen that wouldn't have happened otherwise. Apply it to yourself: what is your contribution to outcomes that your team couldn't have produced without you?

Common contributions that count:
- A hard conversation that shifted someone's trajectory
- Hiring decisions that raised the bar
- Removing a blocker nobody else could remove
- Growing someone who was stuck

---

## 4-Stage Process for Addressing Persistent Behavior Problems

For an engineer who repeatedly shows a problematic pattern (constant complaining, missing commitments, interpersonal friction):

**Stage 1 — Listen and understand.** Do everything you can to understand what's behind the behavior. There is almost always some legitimate grievance underneath. Don't skip this — going straight to "stop doing X" ignores the signal.

**Stage 2 — Address the root cause.** Identify the 1–2 biggest underlying issues and address them in partnership with the person. This requires actually solving something, not just acknowledging it.

**Stage 3 — Discuss the behavior itself.** Once you've addressed the root cause, have an explicit conversation about how the behavior needs to change: what's acceptable, what isn't, and what the expectations are going forward.

**Stage 4 — Let them go.** If the behavior persists after stages 1–3, it's a choice, not a circumstance. Act.

The failure mode is skipping stages. Managers who haven't done stages 1–2 don't have standing to hold stage 3 conversations with credibility.

---

## Diagnosing Underperformance: Work Left to Right

Before deciding "up or out," work through this spectrum in order. As you move right, ownership shifts from you to the employee:

1. **Resources** — do they have what they need? Access, software, tooling, support. If not, that's 100% your problem. Fix it before drawing any conclusions about them.
2. **Training** — do they have enough knowledge to do the job? This is shared responsibility: you ensure they have access to training; they own using it. Avoid the bottomless training trap — aim for sufficient, not exhaustive.
3. **Desire** — do they actually want to do this work? The hardest conversation, with real personal stakes for them. If you've been clear about expectations from day one, and they still don't want to meet them, that's theirs to own. You can be their fan or their coach — you can't want it for them.
4. **Fit** — are they in the right role for their strengths? Someone can be talented and still be wrong for this specific job.
5. **Ability** — do they have the raw capability to reach the required level?

Most underperformance diagnoses jump straight to #3 or #5 without addressing #1 and #2. This is a mistake: it skips the manager's responsibility, burns trust, and produces a weak performance case.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic — read [`references/sources.md`](references/sources.md) for the full list of source articles (with links) and books.

---

## Related Skills

- `feedback` — Immediate, specific feedback is the prerequisite for any of this
- `hiring` — Setting concrete expectations starts at hire time
