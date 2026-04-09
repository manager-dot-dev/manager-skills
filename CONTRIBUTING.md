# Contributing

Thanks for your interest in contributing to Engineering Management Skills!

## Requesting a Skill

Open a [skill request issue](../../issues/new) with the topic you'd like covered.

## Adding a New Skill

### 1. Create the skill directory

```bash
mkdir -p skills/your-skill-name
```

### 2. Create SKILL.md with frontmatter

```yaml
---
name: your-skill-name
description: When the user wants to... Include trigger phrases and keywords.
metadata:
  version: 1.0.0
---

# Your Skill Name

Instructions for the agent go here...
```

### 3. Naming conventions

- **Directory name**: lowercase, hyphens only (e.g., `performance-reviews`)
- **Name field**: must match directory name exactly
- **Description**: 1-1024 characters, include trigger phrases

### 4. Skill structure

```
skills/your-skill-name/
├── SKILL.md           # Required - main instructions
└── references/        # Optional - frameworks, templates, additional docs
    └── guide.md
```

### 5. Writing effective skills

- Reference `em-context` at the top so the agent has team context
- Keep `SKILL.md` under 500 lines
- Include step-by-step instructions
- Add example inputs/outputs where helpful
- List related skills at the bottom

### 6. Open a PR

Submit your PR with a short description of what the skill does and why it's useful.
