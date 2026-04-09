# Engineering Management Skills for AI Agents

A collection of AI agent skills for engineering managers. Built for EMs, tech leads, and directors who want AI coding agents to help with 1:1s, performance reviews, hiring, team health, roadmap planning, and more. Works with Claude Code, Cursor, Windsurf, and any agent that supports the [Agent Skills spec](https://agentskills.io).

**Contributions welcome!** Found a way to improve a skill or have a new one to add? [Open a PR](#contributing).

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, your agent can recognize when you're working on an engineering management task and apply the right frameworks and best practices.

## How Skills Work Together

Skills reference each other and build on shared context. The `em-context` skill is the foundation — every other skill reads it first to understand your team, org structure, and management style.

```
                         ┌─────────────────────────────┐
                         │         em-context          │
                         │  (read by all skills first) │
                         └──────────────┬──────────────┘
                                        │
    ┌───────────────┬───────────────────┼───────────────────┬───────────────┐
    ▼               ▼                   ▼                   ▼               ▼
┌──────────┐  ┌──────────┐       ┌──────────┐        ┌──────────┐  ┌──────────────┐
│  People  │  │  Growth  │       │ Planning │        │  Hiring  │  │   Culture &  │
│          │  │          │       │          │        │          │  │    Health    │
├──────────┤  ├──────────┤       ├──────────┤        ├──────────┤  ├──────────────┤
│  1on1s   │  │  perf-   │       │ roadmap- │        │interview │  │ team-health  │
│ feedback │  │  reviews │       │ planning │        │ hiring   │  │              │
└──────────┘  └──────────┘       └──────────┘        └──────────┘  └──────────────┘
```

## Available Skills

<!-- SKILLS:START -->
| Skill | Description |
|-------|-------------|
| [em-context](skills/em-context/) | Foundation skill. Set your team context, org structure, and management style so all other skills work with your specific situation. |
| [1on1s](skills/1on1s/) | When the user wants to prepare for, run, or follow up on 1:1 meetings with direct reports. |
| [feedback](skills/feedback/) | When the user wants to give structured feedback — positive or constructive — to an individual or in a review. |
| [performance-reviews](skills/performance-reviews/) | When the user wants to write, structure, or prepare for a performance review cycle. |
| [hiring](skills/hiring/) | When the user wants to define a role, write a job description, structure an interview loop, or make a hiring decision. |
| [roadmap-planning](skills/roadmap-planning/) | When the user wants to plan a team roadmap, prioritize projects, or communicate priorities to stakeholders. |
| [team-health](skills/team-health/) | When the user wants to assess, improve, or track the health of their engineering team. |
<!-- SKILLS:END -->

## Installation

### Claude Code

```bash
claude mcp add-plugin https://raw.githubusercontent.com/YOUR_USERNAME/engineeringmanagementskills/main/.claude-plugin/marketplace.json
```

Or copy the skills you want into `.agents/skills/` in your project.

### Any Agent (Agent Skills spec)

```bash
mkdir -p .agents/skills
cp -r skills/1on1s .agents/skills/
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or improve skills.

**Skill ideas welcome!** [Open a skill request](../../issues/new) if you have a topic that's missing.
