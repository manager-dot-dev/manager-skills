---
name: working-with-pm
description: When the user wants to improve their relationship with their Product Manager, fix an imbalanced PM–EM dynamic, or become more product-oriented. Also use when the user says "PM drives me crazy," "PM relationship," "product manager," "roadmap disagreement," "PM overrides me," "PM–EM partnership," or "engineering-led vs product-led."
metadata:
  version: 1.0.0
---

# Working With Your PM

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

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

**Involve engineers in customer conversations.** Not just PMs talking to customers and reporting back. Engineers who hear customers explain their problems in their own words make different decisions than engineers handed a requirements doc. Even one customer conversation per quarter changes how engineers think.

**After shipping — engage with usage data.** What got used? What didn't? This is where engineers start developing product instincts. Share the data in retrospectives, not just the bugs and velocity.

**Articulate tech debt in business terms.** When engineers can say "this API costs us $40k/year and causes our top 3 customer complaints" rather than "this code is messy," they become credible voices in roadmap conversations — not just implementers pushing back on scope.

---

## Related Skills

- `managing-urgency` — Most fake urgency originates from PM–EM misalignment
- `roadmap-planning` — A true partnership produces a single shared roadmap
