---
name: working-with-architects
description: When the user wants to work effectively with Software Architects, Staff Engineers, or Principal Engineers. Also use when the user says "architect," "staff engineer," "principal engineer," "getting help from architects," "technical design review," or "working with senior technical people."
metadata:
  version: 1.0.0
---

# Working With Architects

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

---

*Applies to any cross-team Senior+ engineers — Architects, Staff Engineers, Principal Engineers. The title varies by organization.*

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

## Related Skills

- `delegation` — Working with architects is one of the highest-leverage forms of external collaboration
- `influence` — Arguing your case for architect time uses the same skills as broader stakeholder influence
