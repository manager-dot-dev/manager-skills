---
name: em-context
description: Foundation skill for engineering managers. Use when setting up context about your team, org structure, management philosophy, and current priorities. All other EM skills read this first. Also use when creating or updating a direct report profile. Trigger phrases: "set my team context," "update my EM context," "here's my team setup," "my team is," "my org is," "add a report," "update report profile," "create a profile for."
metadata:
  version: 1.2.0
---

# EM Context

This is the foundation skill. Its purpose is to capture your team, org, and individual direct report context so every other skill can work with your specific situation rather than generic advice.

This skill is not meant to be the main thing you invoke every day. It is the shared memory layer for the other EM skills.

## File Structure

```
.agents/
├── em-context.md          # Your team and org context
└── reports/
    ├── alice.md           # One file per direct report
    ├── bob.md
    └── carol.md
```

## How to Use

**Team context:** Create `.agents/em-context.md` with your team and org context. All EM skills read this first.

**Direct report profiles:** Create `.agents/reports/[firstname].md` for each direct report. Skills like `1on1s`, `feedback`, and `performance-reviews` will look for this file when you mention a person by name.

If files don't exist, ask the user for the relevant context before proceeding.

When other skills learn durable new context, they should update these files automatically. Treat them as living memory, not static setup files.

---

## Auto-Update Rules

All EM skills should use `em-context` as shared memory:

1. Read `.agents/em-context.md` first if it exists
2. If a specific person is involved, also read `.agents/reports/[name].md`
3. If the conversation reveals durable new context, update the relevant file automatically
4. Prefer additive updates over rewrites
5. Do not overwrite existing context unless the user clearly corrected it

Only save information that is likely to remain useful across future conversations.

Good candidates for auto-save:

- team size, charter, org changes, stakeholder changes
- management preferences and communication norms
- a report's level, goals, working style, motivations, and recurring growth areas
- durable project ownership or recurring responsibilities
- feedback history and stable risk signals worth remembering

Do not save:

- one-off frustration or venting phrased as fact
- speculative diagnoses that have not been validated
- transient emotions that will age badly
- details that are too vague to help later

When in doubt, ask: "Will this still be useful and fair three months from now?"

---

## Team Context Template

```markdown
# EM Context

## About Me
- Role: (e.g., Engineering Manager, Senior EM, Director of Engineering)
- Years as EM:
- Company/team size:
- Industry:

## My Team
- Team size:
- Team mission/charter:
- Key areas of ownership:
- Current tech stack (brief):
- Team tenure mix: (e.g., mostly senior, mixed, mostly junior)
- Remote/hybrid/in-person:

## Org Structure
- Who I report to:
- Peer teams:
- Key stakeholders:
- How engineering relates to product/design:

## Current Priorities
- Top 3 team goals this quarter:
- Known challenges or risks:
- Recent wins:

## My Management Style
- How I like to run 1:1s:
- Feedback style (direct, coaching-oriented, etc.):
- Decision-making approach:
- Anything I'm actively working on as a manager:

## Norms and Preferences
- How we communicate (Slack, email, etc.):
- Meeting cadences:
- Performance review cycle:
- Anything unusual about this team/org I should know:
```

---

## Direct Report Profile Template

Create one file per person at `.agents/reports/[firstname].md`:

```markdown
# [Name]

## Role & Background
- Title:
- Level: (e.g., L4, Senior, Staff)
- Tenure on team:
- Background / how they joined:

## Strengths
- [What they're genuinely good at — specific, not generic]

## Growth Areas
- [What they're actively working on or should be]

## Working Style
- How they prefer to receive feedback:
- Communication style:
- What motivates them:
- What drains them:
- How they handle ambiguity:

## Goals
- Short-term (this quarter):
- Long-term (career):

## Current Projects
- [Project name]: [their role and status]

## 1:1 Notes
- Cadence:
- What works well in our 1:1s:
- Recurring themes or topics:

## Feedback History
- [Date]: [Brief note on feedback given — topic, not full transcript]

## Flags / Things to Watch
- [Anything to be aware of — risk of attrition, stress, interpersonal friction, etc.]
```

---

## Instructions for Other Skills

When another skill says "check em-context first," this means:
1. Read `.agents/em-context.md` if it exists
2. If the task involves a specific person, also look for `.agents/reports/[name].md`
3. If the conversation reveals durable new context, update the relevant file automatically
4. If files don't exist, ask the user for the relevant pieces before proceeding
5. Never ask for information already in the context files
6. Never store guesses, temporary frustration, or unresolved interpretations as facts
