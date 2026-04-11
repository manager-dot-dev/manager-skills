---
name: team-composition
description: Helps engineering managers diagnose team skill gaps and make better hiring and assignment decisions — produces the Dungeon Party archetype model (Warrior, Tank, Healer, Wizard, Rogue), the Barrels and Ammunition framework for understanding throughput limits, the Commandos/Infantry/Police phase model, and a minimum team size guideline. Use when the user says "team balance," "what roles do I need," "who should I hire next," "team is missing something," "skill gaps," "team is slow despite headcount," "this person thrived before but struggles now," or "what type of engineer should I hire."
metadata:
  version: 2.1.2
---

# Team Composition

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
- **Diagnosing what the team is missing / who to hire next** → The Dungeon Party Model
- **Team is slow despite having enough headcount** → Barrels and Ammunition
- **Senior engineer who thrived before is struggling now (or vice versa)** → Commandos, Infantry, and Police
- **Team is dangerously small or built around one person** → Minimum Team Size

---

## Default Response Shape

When helping with team composition, diagnose capability before recommending headcount:

1. **Team need:** execution, reliability, glue, architecture, exploration, or phase-fit.
2. **Current imbalance:** which archetype or capability is missing or overloaded.
3. **Evidence:** symptoms in delivery, incidents, planning, collaboration, or morale.
4. **Intervention:** hire, grow, reassign, pair, split ownership, or change expectations.
5. **Risk:** what happens if the team adds the wrong kind of person.

Do not default to "hire a senior." Explain what capability is missing.

---

## The Dungeon Party Model

Every role-playing game requires a balanced party. A team of all warriors dies to magic. A team of all healers can't kill anything. The same logic applies to engineering teams.

The five archetypes:

### The Warrior
Senior problem-solver. Owns the hard bugs, the production fires, the gnarly migrations. Decisive and effective under pressure. The person you call when something is genuinely broken.

**Team need it fills:** execution on difficult, high-stakes work.

### The Tank
Reliable executor, typically earlier in career, works closely with a Warrior. Not expected to lead — expected to deliver consistently on well-defined work and absorb some of the Warrior's load.

**Team need it fills:** sustained output on standard work without burning senior bandwidth.

### The Healer
Empathy-driven, business-oriented, the team's social glue. Often the bridge between engineering and product/design. Great at facilitating difficult conversations, unblocking cross-team friction, and keeping team morale intact during hard periods.

**Team need it fills:** relationships, communication, and organizational navigation.

### The Wizard
Senior or staff engineer who handles system design, architecture documents, and systemic thinking. Sees consequences several steps ahead. Slower to produce output but prevents expensive mistakes.

**Team need it fills:** architectural quality and long-range technical direction.

### The Rogue
Versatile full-stack utility player. Context-switches across areas, ships exploratory work, covers gaps. The person who can pick up anything and make progress.

**Team need it fills:** flexibility and coverage in unpredictable situations.

---

## Using the Model

**Audit your current roster.** For each engineer, identify their primary archetype. Then look for gaps: which archetype is missing or overloaded?

**Common gaps:**
- No Tank → Warriors burn out on routine work
- No Healer → Team is technically strong but organizationally brittle; cross-functional friction accumulates
- No Wizard → Architecture decisions get made ad hoc; technical debt compounds

**Watch for EM archetype bias.** EMs tend to over-hire in their own archetype. Former Warriors hire Warriors and ignore Healers. Former Healers hire for culture fit and end up short on execution. The model counteracts this by making the gap explicit.

**Use it for hiring decisions.** When a headcount opens, map the current team first. The next hire should fill the most critical gap — not replicate the most common archetype.

---

## Caveats

This is a diagnostic model, not a box to lock people into. Most senior engineers span multiple archetypes. The point is not to label people but to identify what the team is currently missing and what to optimize for next.

---

## Barrels and Ammunition

Keith Rabois's insight: adding headcount doesn't linearly increase velocity, because most hires are **ammunition** — skilled people who need direction. What limits your team's throughput is the number of **barrels**.

A barrel is someone who can take an idea from conception all the way to shipping and bring people along in the process. They don't need direction — they create it. Adding a barrel doubles your effective output. Adding ammunition without barrels just creates more coordination overhead.

**Barrels are rare and culturally specific.** Someone who is a barrel at one company may not be at another — the skill is partly about navigating a specific organization. When you find one, treat them accordingly: give them equity, visibility, and significant scope. Replacing a barrel is nearly impossible.

**Practical application:** when a team is slow despite headcount, the diagnosis is often "not enough barrels." Before requesting more engineers, ask: how many of the people we already have can end-to-end own something? If the answer is one or two, more ammunition won't fix it.

---

## Commandos, Infantry, and Police

Robert X. Cringely's model of how companies evolve requires different types of people at different stages:

**Commandos** — the first wave. Operate at startup speed. Work hard, fast, and cheap. Their job is to establish a beachhead: build the prototype, prove the idea, move before anyone knows they're there. They're not precious about quality — they're precious about speed.

**Infantry** — the second wave. Scale what the commandos started. They work systematically, build properly, and ship the first real product. Where commandos made 20 decisions a day, infantry makes them stick.

**Police** — the third wave. Companies that succeed eventually need compliance, process, and stability. Police ensure repeatable quality but are poor at innovation or speed.

**The management trap:** most people strongly prefer one of the three modes and are poorly suited for the others. A commando in a police phase is a troublemaker. A police officer in a commando phase is a bottleneck. Mismatches explain a large fraction of "why is this person struggling?" situations.

**Two practical uses:**
1. When hiring, identify which phase your team/product is in. Hire commandos to build new things; hire infantry to scale them. Police skills are rarely a shortage in engineering.
2. When a senior engineer who thrived in a startup phase struggles in your scaled organization (or vice versa), phase mismatch is often the explanation — not a sudden decline in skill.

---

## Minimum Team Size

From *An Elegant Puzzle* (Will Larson): never let a team drop below roughly 4 people — and never create a team around a single person.

A team of 1 or 2 is structurally fragile: one person's vacation, illness, or departure can halt everything. It also means no real code review, no knowledge redundancy, and no ability to handle an incident while also doing normal work.

The failure mode to avoid: creating small "teams" as organizational fictions — one engineer "owns" a product area and is technically a team. This engineer carries all the risk and gets none of the support structure a real team provides. When something goes wrong or when they leave, there's no team to absorb it.

**Minimum viable team (Larson's guidance):** ~4 engineers. This gives enough coverage for on-call, code review, technical design, and vacation without creating a single point of failure.

**When you're below this:** either grow the team to minimum viability, merge it into a larger adjacent team, or be explicit that it's a temporary solo/pair arrangement with a transition plan — not a permanent structure.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md).

---

## Related Skills

- `hiring` — Use the model to define what you're looking for before writing the job description
- `delegation` — Kingdom assignments often follow archetype: give systems ownership to Warriors and Wizards, cross-team coordination to Healers
- `managing-high-performers` — Wizards in particular need visible, high-complexity work to stay engaged
- `engineer-motivation` — Phase mismatch (Commando in a Police phase) often looks like a motivation problem
