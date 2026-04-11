---
name: working-with-pm
description: Helps engineering managers build a functional PM–EM partnership and become more product-oriented — produces a 3-pattern PM–EM dynamic model (PM-Led / Engineering-Led / Fake Balanced), a true partnership definition, the "It's Important to Me" card for navigating disagreements, tips for getting engineers closer to customers and usage data (launch vs. landing, session recordings, customer conversations), and an explicit responsibilities exercise. Use when the user says "PM relationship," "PM drives me crazy," "product manager," "roadmap disagreement," "PM overrides me," "PM–EM partnership," "I want to be more product-oriented," or "how do I get engineers closer to customers." Do NOT use for general roadmap prioritization (use `roadmap-planning`) or when urgency is being manufactured by a PM (use `managing-urgency`).
metadata:
  version: 2.1.2
---

# Working With Your PM

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
- **Diagnosing the current PM–EM dynamic** → The 3 Relationship Patterns
- **Trying to build a real partnership** → What a True Partnership Looks Like + 3 Tips to Get There
- **Navigating a specific disagreement with your PM** → The "It's Important to Me" Card
- **PM doesn't understand or respect technical work** → Tip 1: Help Your PM Become Tech-Oriented
- **Getting engineers closer to customers and product outcomes** → Building a Product Lens on Your Team
- **Confusion about who owns what between EM and PM** → Tips from Experienced PMs

---

## Default Response Shape

When helping with a PM-EM relationship, identify the operating pattern first:

1. **Pattern read:** PM-led, engineering-led, fake balanced, or true partnership.
2. **Specific friction:** roadmap, estimates, quality, customer context, ownership, or trust.
3. **EM move:** product lens, technical translation, boundary, escalation, or responsibility exercise.
4. **Conversation script:** wording that protects the relationship while naming the issue.
5. **Shared mechanism:** recurring sync, decision log, customer exposure, or responsibility split.

If the PM is creating urgency, connect to `managing-urgency`; if the issue is roadmap tradeoff, connect to `roadmap-planning`.

---

## The 3 Relationship Patterns

### PM-Led Team

The PM talks to customers alone, sets the roadmap alone, and tells you how long things should take. You're executing orders.

The real problems surface after a while:
- People burn out
- Nobody on the team knows **why** they're building things — so they can't anticipate, and prepare for the wrong scenarios
- The codebase degrades — no tests, shallow code reviews, quick and dirty solutions

You might think you can just insist on more time and higher standards. People who've been in this situation know the reality: when the PM is the final decision maker, it's very hard to resist.

### Engineering-Led Team

You set the priorities, scope, and estimates. You make unilateral calls on refactoring. High-level designs and estimates are never challenged.

This results in disappointed stakeholders and customers — which misses the entire point of engineering. If your PM is not up to the task, sometimes you have to take a deep breath and do the PM work yourself.

### "Fake Balanced" Team

Each side has its own territory — tech debt time is untouched, product roadmap is untouched. On the surface this looks fine.

In the long run, it fails. A much better model: **a single roadmap that both of you agree on**, where every technical initiative has a product-related justification.

---

## What a True Partnership Looks Like

A true partnership is reached when both sides want to make the right decision for the long-term success of the **company** — not just their team, not just customers, not just other stakeholders.

The best restaurant in the world was run by both the chef and the restaurateur together, making decisions for the good of the whole. An engineering team works the same way.

---

## 3 Tips to Get There

### 1. Help Your PM Become Tech-Oriented

If your PM doesn't have a technical background, it's on you to bring them up to speed. Explain the benefits of technical work using real examples, not technical jargon.

Instead of: *"We need to create the backend in a new service instead of our Java monolith, there was a decision to start breaking it down to microservices."*

Go for: *"We prefer to create the logic in a new service our team will own, instead of the shared code. This will allow us to move much faster on future requirements, without being bogged down by other teams."*

### 2. Become a Product-Oriented EM

You don't have the privilege to not care about the business.

- When your CEO talks in an all-hands meeting — listen
- If you're in a public company — study the investor calls
- Try to join customer conversations; visit customers when possible

When you understand the business and feel close to customers and other departments, it becomes much harder to bury your head in technical excellence alone. It also lets you sympathize with your PM, understand the reasons behind their decisions, and challenge them more credibly.

### 3. Use the "It's Important to Me" Card

You'll never agree on everything. Neither of you can abuse the card by pulling it too many times. But it means: whoever genuinely cares more about an issue can have their way.

The willingness of one person to relinquish their own position helps build trust between you. Over time, it creates a relationship where both sides know they can fight hard for the things that truly matter.

---

## Tips from Experienced PMs

- **Create a bubble**: No matter how dysfunctional your company, you and your PM (and designer) have a chance to create your own bubble of excellence. Your PM has some autonomy in their role, and a great relationship between the two of you can overcome many obstacles.
- **Have empathy**: You don't know how much pressure the PM is under. For you, it's "we need two more weeks." For the PM, it's dealing with the angry crowds.
- **Talk about responsibilities explicitly**: Write down all possible responsibilities and each side says where on the EM↔PM graph it falls. You'll be surprised by the differences of opinion.

---

## Building a Product Lens on Your Team

One of the most effective ways to become a true PM–EM partner: get your engineers closer to customers and usage data before and after they build.

**Before building — ask simple questions every time:**
- Who is this for?
- What problem are they trying to solve?
- How will we know if this works?

These aren't PM questions. These are questions every engineer should be able to answer about what they're building. If they can't, the spec isn't done yet.

**Launch vs. Landing.** A feature is not finished when code is in production — it's finished when users actually use it. Launching (writing the code, deploying, announcing) is the fun part. Landing (adoption, actual impact) is boring and non-technical, but it's the part that matters. When you release, schedule a check-in with the engineer who built it 1–2 weeks out to look at the data. This one habit changes how engineers think about their work.

**Understand how users actually behave.** Most PMs have access to session recording tools (FullStory, Hotjar, Posthog). Nothing stops engineers from watching them too. Start with a 30-minute "movie time" monthly — watch recordings related to features your team owns. The gap between what you think users do and what they actually do is always surprising.

**Get engineers into customer conversations.** Three practical ways that don't require reorganizing anything:
- **Piggyback on existing calls.** Ask to silently join a customer discovery call run by PM, sales, or CS. Promise not to interrupt. Even one call per quarter changes how an engineer thinks about the work.
- **Follow up on support tickets.** Find a user who recently had an issue your team fixed. Reach out: *"I'm the engineer who fixed this — I'd love 15 minutes to make sure it's resolved and understand your workflow better."* Customers are more receptive than you expect.
- **Partner with CS to find a power user.** Ask CS to connect you with an engaged customer. *"I'm an engineer on the team that built X — I'd love 15 minutes to learn how we can make it better for you."*

Three questions that work in any customer conversation:
- *"How do you currently solve X?"* (context)
- *"Can you show me how you'd use this new flow?"* (usability)
- *"What's the most frustrating part of your current workflow?"* (pain validation)

**After shipping — engage with usage data.** What got used? What didn't? Share this in retrospectives, not just bugs and velocity.

**Articulate tech debt in business terms.** When engineers can say "this API costs us $40k/year and causes our top 3 customer complaints" rather than "this code is messy," they become credible voices in roadmap conversations — not just implementers pushing back on scope.

---

## Dive Deeper

If the user asks where a framework came from or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md).

---

## Related Skills

- `roadmap-planning` — A true partnership produces a single shared roadmap
- `managing-urgency` — Most manufactured urgency originates from PM–EM misalignment
- `written-communication` — How to frame technical work in terms a PM and stakeholders understand
- `influence` — Making the case for engineering priorities in cross-functional settings
