# AGENTS.md

Guidelines for AI agents working in this repository.

## Repository Overview

This repository contains **Agent Skills** for engineering managers, following the [Agent Skills specification](https://agentskills.io/specification.md). Skills install to `.agents/skills/` (the cross-agent standard).

- **Name**: Engineering Management Skills
- **License**: MIT

## Repository Structure

```
engineeringmanagementskills/
├── skills/                # Agent Skills
│   └── skill-name/
│       ├── SKILL.md       # Required skill file
│       └── references/    # Optional supporting docs
├── CONTRIBUTING.md
├── AGENTS.md
├── LICENSE
└── README.md
```

## Skill File Requirements

Every `SKILL.md` must have valid YAML frontmatter:

```yaml
---
name: skill-name
description: When to use this skill. Include trigger phrases.
metadata:
  version: 1.0.0
---
```

Rules:
- `name` must match directory name exactly
- `name` is 1-64 chars, lowercase alphanumeric + hyphens only
- `description` is 1-1024 characters
- Keep `SKILL.md` under 500 lines; move reference material to `references/`

## Foundation Skill

`em-context` is the foundation. All other skills should instruct the agent to read `.agents/em-context.md` (or `.agents/skills/em-context/SKILL.md`) before proceeding, so they have team and org context.
