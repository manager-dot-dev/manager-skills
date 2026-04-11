---
name: managing-high-performers
description: Guides engineering managers through the specific challenges of managing top engineers — produces a four-quadrant ability/confidence diagnostic, the Rock Star vs. Superstar distinction, common mistakes to avoid, a stagnation diagnostic (Diminishing XP), and a Pusher vs. Puller framework for managing burnout and team friction. Use when the user says "rockstar engineer," "superstar," "high performer," "brilliant jerk," "wants promotion," "hardest to manage," "overconfident," "my best developer is burning out," "engineer is frustrated," or "my best developer is pushing me." Do NOT use for standard underperformance (use performance-reviews) or general motivation questions (use engineer-motivation).
metadata:
  version: 2.1.2
---

# Managing High Performers

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it. If the person is named, check `.agents/reports/[name].md`.



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
- **Not sure what kind of challenge you're dealing with** → The 4 Quadrants (start here)
- **High performer who wants to keep climbing vs. one who's settled** → Rock Stars and Superstars
- **Promotion conversation or setting goals for a high performer** → What to Do
- **High performer is damaging team dynamics or being a jerk** → The Brilliant Jerk Problem
- **Senior engineer seems productive but quietly stagnating** → The Diminishing XP Diagnostic
- **High performer is burning people out or burning themselves out** → Pushers and Pullers

---

## Default Response Shape

When helping with a high performer, avoid treating excellence as a generic good:

1. **Type of high performer:** rock star, superstar, pusher, puller, brilliant jerk, bored expert, or burnout risk.
2. **Core tension:** autonomy vs. oversight, growth vs. stability, impact vs. team cost.
3. **Manager move:** goals, visibility, feedback, constraints, scope, or recovery.
4. **Conversation script:** direct wording that respects their competence.
5. **Team impact:** how to protect the rest of the team while keeping the person engaged.

If the issue is harmful behavior, do not excuse it because the person is talented.

---

## The 4 Quadrants

Not every "difficult" engineer is a rockstar problem. Diagnose first:

| | Low Confidence | High Confidence |
|---|---|---|
| **High Ability** | Needs a mentor to grow — this is where you come in | Your (positive) headache |
| **Low Ability** | Often the wrong role/fit — be honest with expectations | Almost impossible to work with — give honest feedback; if no improvement, cut it |

The true rockstar challenge is **High Ability + High Confidence**:
- They expect you to always challenge them with bigger and bigger projects
- They have tons of ideas they want implemented
- The question of promotion always hangs in the air — if the org doesn't grow, they'll leave

---

## Rock Stars and Superstars

From *Radical Candor* (Kim Scott): not every high performer wants the same thing. The mistake is assuming they do.

**Superstars** are on a steep growth trajectory — they want challenge, advancement, and new scope constantly. They're building toward something bigger. Managing them well means clearing the path, delegating high-visibility work, and being honest about what promotion requires.

**Rock Stars** are excellent performers in stable mode — the "rock" of the team. They're not stagnating; they're doing great work at a level they've chosen. They may have interests outside work, have reached a career equilibrium they're satisfied with, or simply not want the cost of constant upward movement. They are not under-performing. They are essential.

**The management mistake:** treating Rock Stars as Superstars who failed to advance. Asking them repeatedly "where do you see yourself in two years?" signals that their current contribution isn't enough. It creates pressure they didn't ask for and resentment they shouldn't have to manage.

**What Rock Stars need:** recognition for the stability and expertise they provide. Meaningful work. Not being pushed toward a path they haven't chosen.

**What Superstars need:** visible, difficult assignments. Regular feedback on what's between them and the next level. An honest answer to "what do I need to do to get there?"

A team that has both — and treats each well — is more resilient than one that only prizes the Superstar trajectory.

---

## How NOT to Manage a Rockstar

**Overpromise.** The worst thing you can do. Painting a picture of a promotion that doesn't happen — even if your manager overrules you at the last moment — destroys trust permanently. If it's not 100% up to you, **don't promise**.

**Ignore advice.** You'll get good ideas constantly. If you say you'll do something, do it. If you decide not to — explain why. Don't just endlessly implement everything to please them, either — you'll lose credibility with the rest of the team.

**Micromanage.** They want freedom. Trust them to come to you when they need you.

---

## What to Do

**Set clear goals.** Ambitious people love goals. If they're aiming for promotion: sit together and define exactly what they need to do to make it happen. Verify with your superiors that achieving those targets will almost guarantee it (and still — don't promise).

**Delegate the hardest and most visible tasks.** This is the best way to lay groundwork for their promotion. When everyone in the organization gets a chance to work with them — including your peers and your manager — they'll support the promotion when you suggest it.

**Give unfiltered feedback.** Giving tough feedback to someone who gives everything can feel like picking on them. Don't. Superstars are always looking for good feedback. Even if they disagree, they'll appreciate it.

**Help them focus.** High performers can be in many places at once, wanting to make things better everywhere. Listen to why they're focusing on what they are. Find alternative solutions. Align on what's truly important.

---

## Protecting Them from Burnout

A rockstar may get frustrated when working on a very ambiguous problem that requires cross-team alignment. The complexity and stakeholder involvement slows them down, and they may overwork to compensate.

Options:
- Provide a secondary project for a sense of accomplishment
- Pair them with an engineer who is comfortable with ambiguity
- If frustration is high and they want to move on, find a different project

---

## The Brilliant Jerk Problem

Rockstars can become brilliant jerks if not managed. They may grow impatient with "slower" team members, dismiss questions they consider trivial.

In most cases, they have good intentions and are simply oblivious. Bringing it up directly usually fixes it. If the problem is genuinely unfixable, you may have to let them go — a brilliant jerk who damages team trust and morale is not worth it.

---

## The Diminishing XP Diagnostic

Engineers who stay in the same role for years can quietly stagnate even when they appear productive — doing familiar work returns negligible growth while the requirements for promotion keep increasing.

The RPG analogy is useful: the same task that was a stretch challenge at mid-level becomes rote at senior level. Rote work produces disengagement that precedes departure by months or years, often before either the engineer or manager notices.

**How to use this:** Periodically map each senior engineer's primary skills against what they have actually worked on in the last two quarters. If every assignment falls within their existing comfort zone, they are grinding low-XP monsters.

The fix isn't a job switch — most organizations have internal opportunities, but those require active EM intervention to surface and assign. Ask directly: "What skills do you want to level up in the next six months that you haven't had the chance to?" Then design at least one assignment per cycle that sits in their zone of proximal development — hard enough to generate real growth, not so far beyond current capability that it produces failure.

---

## Pushers and Pullers

High performers fall into two distinct patterns — and each needs a different response:

**Pushers** always want more: more responsibility, more recognition, more impact. They drive themselves hard and can handle almost anything. The problem: they burn the people around them. They create friction by moving faster than the team can follow, and can make colleagues feel inadequate or pressured.

What to do: tell them directly that their success depends on the people around them succeeding too. Help them see that not everyone operates at their pace — and that bringing people along is a leadership skill, not a compromise.

**Pullers** don't ask — but they'll take everything you give them. They do great work, are reliable, and exercise good judgment. Then one day they explode: burned out, resentful, or quietly checked out.

What to do: set expectations proactively. Actively offload things from their plate before they ask. Check in on their energy, not just their output.

Identifying which type you're dealing with changes what kind of support to provide.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context — read [`references/sources.md`](references/sources.md).

---

## Related Skills

- `retaining-developers` — Rockstars are primarily in the "Bored" and "Stuck" states
- `engineer-motivation` — Use the 3 Drivers to find what kind of high-visibility work actually motivates them
- `delegation` — Delegating high-visibility work is both retention and development
- `performance-reviews` — Setting clear promotion criteria is how you manage expectations
