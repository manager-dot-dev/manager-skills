---
name: hiring
description: Helps structure the interview process, calibrate the hiring bar, counter interview bias, and decide between promoting internally vs. hiring externally. Also covers evaluating a new hire's fit during their first 90 days. Use when the user says "interview," "hire," "job description," "JD," "interview loop," "debrief," "hiring bar," "offer," "reject," "sourcing," "recruiter," "headcount," "should I hire a junior," "promote from within," or "new hire isn't working out." Do NOT use for ongoing performance management of an established team member (use performance-reviews).
metadata:
  version: 2.1.2
---

# Hiring

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

- **Structuring the interview or deciding on a work sample** → See the Work Before You Hire
- **Calibrating seniority level / case for hiring juniors** → Why You Should Hire Juniors
- **Worried about cultural bias affecting the evaluation** → The Beer Test Bias
- **Deciding between internal promotion and external hire for a management role** → Internal vs. External
- **New hire isn't meeting expectations — wondering if you should act** → Setting Up New Hires for Objective Evaluation

---

## Default Response Shape

When helping with hiring, turn the advice into a hiring artifact:

1. **Hiring goal:** what problem this role or hire must solve.
2. **Bar / evidence:** what evidence should prove the candidate can do it.
3. **Process:** interview loop, work sample, debrief, or 30/60/90 plan.
4. **Bias check:** where the decision may be distorted by similarity, urgency, or sunk cost.
5. **Decision language:** concise recommendation: hire, reject, calibrate, or gather more evidence.

For new-hire concerns, shift from candidate evaluation to objective 30/60/90 success criteria.

---

## Setting Up New Hires for Objective Evaluation

The most common new manager mistake is tolerating underperformers because they're improving. The fix starts on day one.

**Define success in advance.** Before the person starts, write down concrete expectations:
- How long before they can complete a task in repo X without help?
- What type and size of tasks do you expect at 30 / 60 / 90 days?
- When should they be contributing to on-call? To technical design?
- For senior hires: what inputs and initiative do you expect from them?

Without this, you'll drift toward forgiveness. A small improvement will feel like success because you have no anchoring standard.

**Use the "would I hire today?" checkpoint.** At 30 days (and again at 60 and 90), ask yourself one question: "Knowing what I know now, would I hire this person?"
- If yes: tell them. It builds real commitment.
- If no: act. Every day you wait, you're doing more damage to the team — and to them.
- If "I need more time": be honest with yourself. You usually know by 30 days. 3 months is almost always enough.

**Don't ask "am I better with or without them?"** That question anchors on sunk cost — the training time, the relationship, the hassle of re-hiring. Ask the forward-looking question instead.

---

## Why You Should Hire Juniors

Most companies have an excuse not to hire juniors — too small to mentor, growing too fast, infrastructure too complex. Most of it is bullshit.

Ambition, character, and brains have little to do with experience. Some developers become seniors in under 3 years. There are diminishing returns on experience: you can tell the difference between 1 year and 5 years; between 10 and 15, probably not.

### 5 reasons to hire a great junior for the next open position

1. **Bigger candidate pool.** When you need "full-stack with 5+ years Python and 3+ years React," you'll have fewer options and may end up compromising. Broader criteria means access to absolute top talent.

2. **Fresh energy.** Juniors want to learn and have a drive to prove themselves. Their motivation is contagious. Seniors on the team enjoy working with smart, motivated people — and get opportunities to mentor, which they might miss on an all-senior team.

3. **Not restricted by what they know.** They won't try to reuse the same technologies or patterns from previous companies. They approach problems without baggage.

4. **More flexible.** More open to new technologies and less picky about tasks. Doesn't mean assigning them only annoying bugs — but it gives you more flexibility.

5. **Easier to develop.** Great juniors want feedback and seek to improve. They want to know what you think about their work.

### The internship advantage

Juniors often come through student or intern positions. This means you can judge their skill **before** offering a full-time role — a privilege you never have with senior hires.

### The river, not the lake

Think of your team as a river instead of a lake. A lake stagnates — it cultivates mediocrity and complacency. A river is always running and changing, with great energy. A river depends on the flow of people: new blood, new leaders, elders ready for a new challenge. If you never hire juniors, your team stagnates.

### Pay based on skills, not tenure

The point of hiring juniors is not to have rotating cheap labor. Paying juniors less initially makes sense — you're investing time and energy training them. But once great juniors prove themselves (often within a year), pay them based on their skills, not their years of experience. Otherwise they'll go get mid/senior roles at other companies, and rightly so.

### When you do need a senior

Sometimes you need a specific level of expertise: building an iOS app for the first time, solving performance problems at scale, navigating a genuinely complex domain. For those cases, hire a senior. For most teams working on a standard SaaS product, the junior/senior ratio can be quite high.

---

## The Beer Test Bias

"Would I want to grab a beer with this person?" — or some version of it — is one of the most common informal filters in hiring. It feels like culture fit. What it actually does: filter for people who are similar to the interviewer. Over time, this creates less diverse teams and reinforces existing blind spots.

The bias runs both ways. You may be undervaluing someone who is genuinely excellent but communicates differently, comes from a different background, or isn't immediately likeable in a 30-minute conversation.

**The comparative advantage argument.** The goal isn't to hire someone you'd be friends with — it's to hire someone whose strengths complement the team's weaknesses. A team full of people similar to the existing team is weaker than a team with diverse thinking styles, experiences, and perspectives.

**5 steps to counter it:**

1. **Examine your own biases explicitly.** Before the debrief, ask yourself: "Am I rating this person down for a substantive reason, or because they're different from me?"
2. **Focus on strengths, not absence of weaknesses.** What does this person do well that nobody else on the team does? That's the question that changes decisions.
3. **Plan interview conversations in advance.** Don't improvise. Improvised conversations drift toward comfort — topics you know, styles you recognize.
4. **Ask for feedback on your process.** Have a colleague outside the hiring loop review your debrief notes. What patterns do they see?
5. **Adapt your approach to the candidate.** A senior engineer from a startup communicates differently than one from a large tech company. Neither is better. Your process should surface both.

This isn't about lowering the bar. It's about making sure the bar measures what you think it measures.

---

## Internal vs. External: The Case for Promoting from Within

The default instinct when a management role opens is to look outside. An external hire brings experience, fresh perspective, no baggage. It feels like the safe, professional choice.

The reality:

An internal promotion is harder in the short term — the person has no management experience, someone else on the team may feel passed over, your VP may need to provide more support, and they'll have to navigate managing their former peers.

But the long-term case is strong:
- They can still contribute technically during the transition
- They have genuine insight into what needs to improve
- They know the codebase, the people, and the customers
- They are more likely to be loyal to the company that invested in them

If no one on your team wants to try management, that's worth examining. It may mean the path isn't visible, or that management looks unattractive from where they sit.

Your job is to help your people grow outside their comfort zone — including toward management, if there's interest. When a manager slot opens, ask yourself who on the team is ready to try before looking outside. Often the right answer is someone who just needs the opportunity.

---

## See the Work Before You Hire

From *Peopleware* (DeMarco & Lister): you wouldn't hire a juggler without watching them juggle.

Before you trust someone with production code, see them do something close to what they'll actually do. A one-hour coding exercise isn't perfect, but it's dramatically more predictive than a conversation about how they'd approach a hypothetical problem.

**What to look for in a work sample that a conversation misses:**
- How they handle ambiguity (do they ask clarifying questions or make assumptions?)
- Whether their code is readable, not just functional
- How they respond to feedback on their work (do they get defensive, or engage?)
- What they prioritize when they can't do everything

**For senior candidates:** consider having them review code rather than (or in addition to) writing it. Code review reveals judgment in a way that new code doesn't — it shows whether they can identify real issues, give useful feedback, and communicate technically.

**For internship-to-hire pipelines:** this is the strongest hiring signal you have. You've seen them work for months before you make the offer. Use that data.

The discomfort many EMs feel about structured technical assessments ("it feels like a test") is real — but the alternative is making a $200k+ decision based on a good conversation. The juggler analogy is a useful reframe: the assessment isn't a judgment of the person; it's a standard you'd apply to anyone in that role.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic — read [`references/sources.md`](references/sources.md) for the full list of source articles (with links) and books.

---

## Related Skills

- `em-context` — For team and role context
- `performance-reviews` — For evaluating performance over time
