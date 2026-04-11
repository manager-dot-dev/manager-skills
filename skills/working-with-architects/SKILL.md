---
name: working-with-architects
description: Helps engineering managers work effectively with Software Architects, Staff Engineers, and Principal Engineers — covers the EM's side of the relationship (responsiveness, proactive consultation, giving credit), how to advocate for architect time, pre-consultation preparation, and the two architecture team models (Centralized vs. Decentralized). Use when the user says "architect," "staff engineer," "principal engineer," "technical design review," "working with senior technical people," "getting architecture help," or "how do I get more architect time." Do NOT use for managing staff/principal engineers who report directly to you (use `managing-high-performers` or `delegation`).
metadata:
  version: 2.1.2
---

# Working With Architects

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
- **Unclear what the EM's responsibilities are in the architect relationship** → Do Your Side Well
- **Need to make the case for architect time on a project** → Their Side of the Deal — Don't Hesitate to Push
- **About to kick off a complex project with architect involvement** → Before You Consult Them
- **Unclear who makes decisions — your team vs. the architecture function** → Two Architecture Team Models

---

*Applies to any cross-team Senior+ engineers — Architects, Staff Engineers, Principal Engineers. The title varies by organization.*

---

## Default Response Shape

When helping with architects or senior technical partners, clarify ownership:

1. **Situation:** advice, review, decision, blocked project, or architect-time request.
2. **EM responsibility:** what the manager must own before asking for help.
3. **Architect ask:** specific input, decision, review, or escalation needed.
4. **Preparation:** context, constraints, options, and decision deadline.
5. **Relationship move:** credit, follow-through, or expectation reset.

Do not frame the architect as the owner of the EM's project unless they explicitly own delivery.

---

## Do Your Side Well

### Don't drag their requests

When Architects need something from you — security updates, a shared-service refactor, a new testing methodology — do it fast. These things are almost never truly urgent, which makes it tempting to take your time. Don't.

A big side benefit: being the first team to implement such initiatives gets you more help and guidance from the architects. They'll invest more in teams that move quickly on shared work.

### Proactively consult them

For complex technical dilemmas, ask for their opinion before you decide — even on things smaller than what typically requires their involvement. When they're kept in the loop early, there's a much higher chance they can help in later stages.

### Give credit

Long projects are easy to finish while forgetting the early help that made them possible. By the end, we often don't remember the significant guidance we got from architects in the initial phases.

When presenting a feature: mention their help, thank them personally. If they did exceptional work — let their manager know.

---

## Their Side of the Deal

### You own it — don't forget that

In complex projects, architects may write initial infrastructure or examples to show the way. Once that initial phase is done, **the ownership is 100% yours**. Their role is to help you do it in the best way — not to share responsibility when things go wrong.

Resist the temptation to offload incidents or mistakes onto work they contributed to. It's your project.

### Don't hesitate to push for their time

Architect time is never automatically allocated to your team. Those who advocate clearly are the ones who get help.

When asking for their involvement:
- Define the scope of help you need
- Explain why you need it and what benefit it provides to the organization (time-sensitive project, new technology useful to other teams, sensitive area of the codebase where mistakes are costly)
- **Argue your case**

More senior team leaders get more resources because they present their cases better. Practice makes perfect.

### Don't offload trivial things

Once you know exactly what to do and how to do it, you don't need them anymore. Let them move to the next important project. Abusing the privilege damages the relationship and wastes time that should go to harder problems.

---

## Before You Consult Them

Collect context first. The first things any architect will ask when starting architecture work:
- What do you know about the problem?
- Why does the business need it solved?
- When does it need to be solved?

Come prepared with these three answers.

---

## Two Architecture Team Models

**Centralized:** Architects make all architecture decisions. You're the Subject Matter Expert — they consult you to understand the problem space, then design the solution. Requires tight, ongoing communication between you and the architect.

**Decentralized:** Architects help *you* design solutions for your team. They define principles and a Tech Radar. As long as you follow the guidelines, decision-making is yours. Communication is lighter, but you need to drive things forward and reach out proactively.

In either model: **engage early**. Engaging too late is the biggest mistake. If too much work has already been done, changing direction may require significant rework or be impossible.

---

## Dive Deeper

If the user asks where a framework came from or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md).

---

## Related Skills

- `delegation` — Working with architects is one of the highest-leverage forms of external collaboration
- `influence` — Arguing your case for architect time uses the same skills as broader stakeholder influence
- `managing-high-performers` — If the architect reports to you, that's a different relationship with different dynamics
