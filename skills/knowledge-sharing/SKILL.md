---
name: knowledge-sharing
description: When the user wants to break down knowledge silos, improve documentation culture, improve onboarding, or build better cross-team collaboration. Also use when the user says "knowledge silos," "reinventing the wheel," "nobody reads docs," "onboarding is bad," "teams don't talk," "documentation culture," or "cross-team friction."
metadata:
  version: 1.0.0
---

# Knowledge Sharing

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

---

## Why Silos Form

In many organizations, 45% of developers report that knowledge silos negatively impact their productivity multiple times a week. They spend time building something that another team already built. They can't find information that exists somewhere. They don't know who to ask.

There are 4 root causes — and each has a different fix.

---

## 1. No Horizontal Information Flow

Traditional hierarchies move information up and down, not sideways. Knowledge stays locked within teams.

**The fix: Engineering Guilds** (also called Chapters) — cross-team groups organized around a domain (frontend guild, ML guild, platform guild, etc.).

What makes guilds work vs. fail: guilds fail when they're informal gatherings with no allocated time and no real output. Engineers vent, agree "something should be done," then return to their team backlogs. To work, guilds need three things:
1. **Strategic alignment** — guild projects must tie to company goals, not just engineering preferences
2. **Official recognition** — leadership acknowledges the guild and gives members time to participate
3. **Member freedom** — engineers choose what to work on based on their interests and career goals

A lighter version if guilds aren't feasible: dedicated Slack channels by tech domain. Encourage questions, cross-team problem-solving, and sharing solutions there.

---

## 2. Ineffective Knowledge Sharing

Without a documentation culture, knowledge lives in people's heads, in Slack threads, in undiscoverable emails. When those people leave or are unavailable, the knowledge disappears.

**The fix: Minimum Viable Documentation + ADRs**

Documentation fails for two reasons:
- It becomes obsolete quickly and nobody reads it anyway
- Writing it is tedious, so nobody does it consistently

The principle: **don't document everything — document what people actually need to do their jobs**. Focus on:
- The reasoning behind critical decisions (why, not just what)
- Fundamental architectural principles and protocols
- Agreed-upon patterns and approved third-party packages

**Architecture Decision Records (ADRs)** are the best practical implementation. Stored directly in the codebase, with a shared template, they capture: the decision, the context, the alternatives considered, and who to contact. Developers always know where to look and why things are the way they are.

Standardized templates are the key to documentation actually getting written — engineers don't have to think about format, just fill in the blanks.

---

## 3. Poor Onboarding

Onboarding is when new hires form their first knowledge map of the organization. When that's chaotic, knowledge silos form from day one.

**The fix: Structured onboarding buddies**

A buddy guides new joiners through:
- **Pair programming** — the fastest way to learn codebase, workflows, and unspoken context (historically taken decisions, tech debt, testing practices)
- **Product and architecture overviews** — what the team builds, why it matters, how the system fits together
- **Domain deep dives** — tools and processes specific to the team

Equally important: introductions *outside* the team. Have new hires attend other teams' product overviews. Introduce them to people across the company. This creates the cross-team relationships that make knowledge flow naturally later.

---

## 4. "Us vs. Them" Thinking

When teams are isolated or compete for resources, knowledge becomes a source of power. Sharing it feels risky — it exposes weaknesses or reduces competitive advantage.

**The fix: Radical transparency and shared problem framing**

When teams understand each other's constraints and trade-offs, "us vs. them" shifts to "us together vs. the problem." Two structural approaches that work:

**Architecture Review Sessions** — open design decisions to the whole organization. Anyone can attend to learn or to influence. This guarantees visibility and creates a shared sense of ownership over technical direction.

**Meetups and lightning talks** — formal or informal, these give teams opportunities to share expertise and build personal connections. Presenters improve their communication skills; attendees gain broader context.

The critical addition: **incentivize knowledge sharing in your career framework**. Embed it in how performance is evaluated. Reward people who unblock others and contribute to cross-team collaboration — not just people who ship their own work.

---

## The 3 Paths for Cross-Team Requests

When your team gets a request from another team — a feature, an integration, access to a system — there are three ways it gets handled in practice:

1. **No attention:** The request is noted, deprioritized, and never addressed.
2. **Delayed attention:** The team acknowledges it but puts it in the backlog. "We'll get to it next quarter."
3. **Prioritize:** The team commits real time to it.

The counterintuitive finding: **delayed attention is often worse than no attention**.

When you say "we'll get to it next quarter," the requesting team builds around the assumption that the request will be fulfilled. They design their system expecting that integration. They commit to their stakeholders. When "next quarter" arrives and nothing happens, the cost is much higher than if you had said "no" at the start and let them find another path.

**What to do with cross-team requests:**
- Decide quickly. Even "not this quarter, not next quarter" is more useful than "we'll see."
- If the answer is delayed: be specific about timeline and set a real calendar reminder to follow up.
- If the answer is no: say so clearly, and help them understand why. They can make better decisions with that information.

The cost of a delayed "no" compounds. The sooner you're honest about capacity, the less damage accumulates.

---

## Related Skills

- `team-health` — Team Focus Days are a structural support for cross-team connection
- `working-with-architects` — Architects are often central to Architecture Review Sessions
- `management-transitions` — New Boss transitions benefit most from immediate knowledge-sharing investment

