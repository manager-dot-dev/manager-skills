---
name: engineer-motivation
description: Helps engineering managers understand and act on what drives each engineer — produces a three-driver framework (Growth, Connection, Impact), techniques for identifying someone's primary driver, driver-aligned delegation patterns, and a team composition diagnostic. Use when the user says "this person isn't motivated," "nobody picks up tasks," "I keep reminding people," "what drives my engineers," "how do I motivate my team," "what should I delegate to this person," "engineer seems disengaged," or "what growth activity should I give this person." Do NOT use when someone is actively leaving or at risk of quitting (use retaining-developers) or when the engineer is a high performer with specific management challenges (use managing-high-performers).
metadata:
  version: 2.1.2
---

# Engineer Motivation

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it. If a person is mentioned, check `.agents/reports/[name].md` — it may contain their motivation profile.



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
- **Don't know what drives someone / need to figure out their driver** → How to Identify Someone's Driver
- **Know their driver, want to delegate something that sticks** → Driver-Aligned Delegation
- **Looking for specific activity ideas for a specific engineer** → read [`references/activities.md`](references/activities.md)
- **Thinking about hiring or team composition** → Team Composition
- **Your own driver is bleeding into how you manage everyone** → The 3 Drivers (the common EM mistake)

---

## Default Response Shape

When diagnosing motivation, avoid generic "motivate them" advice:

1. **Likely driver:** Growth, Connection, Impact, or mixed, with evidence.
2. **Signals to verify:** what to ask or observe before acting.
3. **Matching intervention:** delegation, activity, visibility, customer context, or relationship-building.
4. **Mismatch risk:** what would demotivate this person if the manager assumes wrong.
5. **Next 1:1 script:** a short way to test the hypothesis with the engineer.

If the person may be actively leaving, switch to `retaining-developers` rather than treating it as ordinary motivation.

---

## The 3 Drivers

The most powerful frame for understanding what motivates a software engineer:

**Growth** — This person wants to be challenged, grow their skills, and advance their career. They hate boring or repetitive work. They're energized by new technical problems, learning opportunities, and a clear promotion path.

**Connection** — This person gets their energy from relationships. They can stay in the same company for years primarily because of the people. Isolation drains them. They're energized by collaboration, team events, mentoring, and building relationships across the org.

**Impact** — This person cares about what the company does and whether it matters. They want to see features actually used, be close to customers, and understand how their work moves business metrics. They'll do unglamorous work without complaint if it clearly helps the business.

All people have a little of all three, but most have one primary driver and possibly a secondary.

**The common EM mistake:** defaulting to your own driver when supporting your team. Growth-focused EMs fight for promotions and challenging work for everyone. Impact-focused EMs connect everyone to metrics. Connection-focused EMs organize events for everyone. Good EMs manage across all three — including drivers that don't come naturally to them.

---

## How to Identify Someone's Driver

Watch how they respond to different things:
- Do they light up when you talk about a promotion path or a new technical challenge? → **Growth**
- Do they mention teammates by name, care about team dynamics, and thrive in collaborative settings? → **Connection**
- Do they ask about customers, usage, and business outcomes? Do they take on unglamorous work without complaint? → **Impact**

When unsure, ask: *"Which would you prefer — a project that pushes your technical skills in a new direction, one where you'd work closely with a lot of people across the org, or one that directly solves a major pain point for customers?"*

---

## Driver-Aligned Delegation

This is the biggest unlock for freeing your time as EM.

When you delegate something that doesn't align with someone's driver, it doesn't stick. They procrastinate, you nag, they finish it reluctantly, and you follow up again next week. When delegation aligns — it sparks.

**"Every task you don't like can be a growth opportunity for someone else."**

Examples:
- Sending a Growth-driven engineer to represent the team in technical architecture reviews they care about — they come alive; you get a free hour.
- Assigning a Connection-driven engineer to mentor a new hire or organize team events — they love it; you stop feeling guilty about it.
- Inviting an Impact-driven engineer to customer calls or giving them access to usage metrics — they become passionate about work that felt like overhead to others.

This is particularly powerful for tech debt: frame it as the business problem it solves, and assign it to an Impact-driven engineer who wants to see the metrics improve.

---

## Activity Ideas by Driver

A few vivid examples per driver — for the full list of specific individual-scope activities, read [`references/activities.md`](references/activities.md).

**Growth:** Give them a technical kingdom (full ownership of a system, including PM relationship and tech debt prioritization). Assign them to lead a long-term tech initiative that *they* identified as painful. Help them write a real technical article — not AI-generated, but a deep dive into something they actually solved.

**Connection:** Assign them to onboard a new engineer (you keep the 1:1s, they handle everything else). Have them lead a retrospective — connection-driven engineers usually know what frustrated teammates better than you do.

**Impact:** Invite them to a customer call or business meeting — ask privately in a 1:1 so there's no pressure. Share deeper business context in 1:1s: metrics, the sales pipeline, the real stakes behind what the team is building.

---

## Team Composition

Every team needs all three driver types to be effective long-term.

A team entirely of Growth drivers is technically sharp but often disconnected and may not care whether features get used. A team of all Impact drivers ships things but can drift technically. A team of all Connection drivers builds great culture but may lack urgency.

When thinking about hiring, check which driver type is underrepresented. If everyone eats lunch at their desk alone — it's worth bringing in someone more outgoing. If nobody asks about business outcomes — look for an Impact-driven engineer.

The drivers coexist fine. In practice, mixing them creates teams where someone naturally picks up the work that feels like a chore to others.

---

## Dive Deeper

If the user asks where a framework came from or wants more context — read [`references/sources.md`](references/sources.md). For a full list of individual-scope activity ideas organized by driver, read [`references/activities.md`](references/activities.md).

---

## Related Skills

- `delegation` — Driver-aligned delegation is the primary mechanism for acting on this
- `retaining-developers` — The 5 reasons engineers quit often map to an unmet primary driver
- `managing-high-performers` — High performers have driver needs too, but with additional complexity
- `1on1s` — The place to surface and update your understanding of someone's driver
- `hiring` — Use driver balance to assess what your team is missing
