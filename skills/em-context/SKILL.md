---
name: em-context
description: Foundation skill for engineering managers. Use when setting up context about your team, org structure, management philosophy, and current priorities. All other EM skills read this first. Trigger phrases: "set my team context," "update my EM context," "here's my team setup," "my team is," "my org is."
metadata:
  version: 1.0.0
---

# EM Context

This is the foundation skill. Its purpose is to capture your team and org context so every other skill can work with your specific situation rather than generic advice.

## How to Use

Create a file at `.agents/em-context.md` in your project with your team context. All other EM skills will read this file first.

If the file doesn't exist, ask the user for the relevant context before proceeding.

## Context Template

When helping a user set up their EM context, populate the following:

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

## Instructions for Other Skills

When another skill says "check em-context first," this means:
1. Look for `.agents/em-context.md`
2. If it exists, read it and use that context
3. If it doesn't exist, ask the user for the relevant pieces before proceeding
4. Never ask for information already in the context file
