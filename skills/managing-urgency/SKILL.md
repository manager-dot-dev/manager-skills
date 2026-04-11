---
name: managing-urgency
description: Helps engineering managers respond to high-urgency requests and use deadlines effectively — produces a five-question framework for evaluating unreasonable deadlines, guidance on scope/staffing/intensity decisions under pressure, Parkinson's Law applied to engineering, and five common deadline mistakes to avoid. Use when the user says "urgent deadline," "everything is on fire," "we need to ship fast," "fake deadline," "unreasonable timeline," "crisis mode," "working weekends," "Parkinson's Law," or "leadership is pushing for faster delivery."
metadata:
  version: 2.1.2
---

# Managing Urgency

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
- **Just received an unreasonable deadline — need to decide how to respond** → When You're Handed an Unreasonable Deadline (start here)
- **Want to use deadlines proactively to drive focus** → Using Deadlines as a Tool
- **Deadline is set — want to avoid common pitfalls in execution** → 5 Mistakes to Avoid

---

## Default Response Shape

When helping with urgency, make tradeoffs explicit:

1. **Deadline type:** real, fake, useful constraint, or panic.
2. **Five-question check:** goal, scope, quality, staffing, and intensity.
3. **Options:** reduce scope, add capacity, accept risk, move date, or stop other work.
4. **Recommendation:** the least-bad path and why.
5. **Stakeholder script:** how to communicate the tradeoff without sounding defensive.

Never answer urgent requests with only "push back." Give a concrete tradeoff menu.

---

## When You're Handed an Unreasonable Deadline

Before committing the team, work through five questions:

**1. Is the deadline actually necessary?**

Speed has a cost: technical debt, poor decisions, and burnout. Each engineering team has an optimal sustainable pace — pushing significantly beyond it reaches the first milestone faster but degrades everything that follows.

Pressure-test the deadline. Who set it and on what basis? Does it reflect an external constraint (contract, launch, regulatory date) or an internal wish? Does everyone involved understand the quality trade-offs? If the deadline is genuinely necessary, communicate exactly why — teams will go further when they know what they're fighting for.

**2. Who should work on it?**

More people is not always faster. Above a small number, coordination costs overtake the benefit of additional capacity — especially on tightly coupled work. Identify the minimum effective team size. It's often acceptable to split the team for a short sprint, keeping critical ongoing work alive elsewhere, rather than pulling everyone into one crisis.

**3. How hard should you ask people to work?**

People have lives. The bar for asking for extra effort should be high — and when you ask, you need to mean it. Guidelines that tend to hold:
- Weekend work: only when the company's success genuinely depends on it, and compensate with time off after
- People differ in capacity and willingness — don't assume uniformity
- If your business has predictable crunch periods (launches, seasonal peaks), set those expectations during onboarding, not mid-crisis

When you do ask for extraordinary effort, bring in a senior leader to acknowledge it directly — it answers questions and signals that the effort is seen.

**4. Are you on the right path?**

Normal delivery tolerates course corrections over time. Urgent delivery doesn't — a small wrong turn compounds fast. Your most critical job during a crunch is ensuring the team is working on the right thing in the right way.

Run short feedback loops. Involve PM and design immediately. Ask daily: what can be cut? What can be simplified? What already exists that we can reuse? Early in the sprint, even temporary micromanagement on key decisions is justified — every early choice locks in or unlocks downstream time.

**5. What does the return to normal look like?**

After a successful crunch, leadership may assume the team can always work that way. It cannot. Sustained crisis mode drives attrition and degrades quality. Your job after the crunch is to be explicit: "We delivered this under exceptional circumstances — this isn't the baseline." Set that expectation before the next deadline appears.

---

## Using Deadlines as a Tool

Parkinson's Law: **work expands to fill the time available.** Projects without deadlines take longer than they need to and accumulate scope. This isn't a flaw in people — it's a structural property of open-ended time.

The practical implication: a challenging deadline in a healthy environment drives focus and creativity. The same deadline in a toxic environment drives shortcuts and fear. The tool is neutral — the environment determines the outcome.

A simple test: send a survey with no deadline vs. the same survey due tomorrow. Response rate and speed differ dramatically. Apply this principle broadly — to internal reviews, design sign-offs, decision cycles.

The critical distinction between a *challenging* deadline and an *impossible* one: a challenging deadline requires prioritization and focus. An impossible deadline requires cutting corners on things that matter, burning people out, or both. Your judgment on which category a deadline falls into is one of the most consequential calls you make as EM.

---

## 5 Mistakes to Avoid

**1. Not telling the team what happens after the deadline.**
Teams will work harder when they understand the consequence of hitting or missing the date. If the deadline is internal, say so — and explain what it enables. "Nothing external happens, but shipping this unlocks Q3 roadmap approval" is a real reason worth knowing.

**2. Not involving the team in scoping.**
Deadlines work best when the team has had input on what's feasible. You don't need consensus — you need to have asked. An engineer who thinks "if anyone had asked me, I could have told them this wouldn't work" is disengaged before the sprint begins.

**3. Pushing too hard to hit it.**
The point of a deadline is focus, not suffering. When unexpected obstacles appear — external blockers, underestimated complexity, a dependency that slips — a deadline should flex before it breaks the team. Missing a self-imposed deadline occasionally is better than working weekends to defend a date that no longer makes sense.

**4. Not pushing hard enough.**
The opposite failure. Some managers avoid asking for more effort to protect goodwill — sometimes doing the extra work themselves rather than asking. That's not protection; it's avoidance. Finding the right level of push is the job.

**5. Being rigid when the scope or date needs to change.**
External requests to adjust scope or timeline are not failures. They're new information. The right response is to communicate the trade-offs clearly and make a joint decision — not to defend the original plan as a matter of pride.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md).

---

## Related Skills

- `delegation` — Chronic urgency is often a symptom of delegation failures upstream
- `working-with-pm` — Most fake or misaligned urgency originates in the PM–EM relationship
- `roadmap-planning` — Unreasonable deadlines are usually a planning and scoping problem at the source
