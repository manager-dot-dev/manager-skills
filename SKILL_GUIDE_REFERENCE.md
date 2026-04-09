# Skill Guide Reference
Extracted from *The Complete Guide to Building Skills for Claude*

Use this file to audit each skill in the repo against official best practices.

---

## Structure Requirements

### File & folder rules
- Folder name: `kebab-case` (no spaces, no capitals, no underscores)
- Main file: exactly `SKILL.md` (case-sensitive — no `skill.md`, `SKILL.MD`, etc.)
- No `README.md` inside the skill folder
- Optional subdirectories: `scripts/`, `references/`, `assets/`

### SKILL.md size
- Keep under **5,000 words** to avoid large-context performance issues
- Move detailed documentation to `references/` and link to it

---

## YAML Frontmatter

### Required fields
```yaml
---
name: skill-name-in-kebab-case
description: What it does and when to use it. Include specific trigger phrases.
---
```

### Optional fields
```yaml
license: MIT
allowed-tools: "Bash(python:*) WebFetch"
metadata:
  author: Name
  version: 1.0.0
  category: productivity
  tags: [tag1, tag2]
```

### Rules
- `name`: kebab-case only, no spaces, no capitals — must match folder name
- `description`: under 1024 characters, no XML angle brackets (`<` `>`)
- Forbidden in frontmatter: XML tags, skills named with "claude" or "anthropic" prefix

---

## The Description Field — Most Important

The description is how Claude decides whether to load the skill. It's the **first level of progressive disclosure** — loaded into every system prompt.

### Required elements
A good description must contain **BOTH**:
1. **What the skill does** (the output/purpose)
2. **When to use it** (trigger conditions — specific phrases users would say)

### Good examples
```
Analyzes Figma design files and generates developer handoff documentation.
Use when user uploads .fig files, asks for "design specs", "component
documentation", or "design-to-code handoff".
```
```
Manages Linear project workflows including sprint planning, task creation,
and status tracking. Use when user mentions "sprint", "Linear tasks",
"project planning", or asks to "create tickets".
```

### Bad examples
- Too vague: `"Helps with projects."` — won't trigger reliably
- Missing triggers: `"Creates sophisticated multi-page documentation systems."` — Claude doesn't know when to load it
- Too technical, no user phrases: `"Implements the Project entity model with hierarchical relationships."`

### Debugging trigger issues
Ask Claude: *"When would you use the [skill name] skill?"* — Claude will quote the description back. Adjust based on what's missing.

---

## Writing Instructions (SKILL.md body)

### Best practices
- **Be specific and actionable** — tell Claude exactly what to do, not what to think about
- **Put critical instructions at the top** — don't bury key rules in the middle
- **Use structured formatting** — bullet points, numbered lists, headers
- **Include examples** — show what a successful interaction looks like
- **Include error handling** — common failure modes and what to do about them
- **Use progressive disclosure** — keep SKILL.md focused on core instructions; move detailed docs to `references/` and link

### Anti-patterns
- Vague instructions: `"Validate the data before proceeding."` → Bad
- Specific instructions: `"Run validate.py --input {filename}. If validation fails, check for: missing required fields, invalid date formats (use YYYY-MM-DD)"` → Good
- Instructions too verbose → Claude may not follow them; split into references/

### Forcing compliance on critical steps
For critical validations, use explicit language:
```
CRITICAL: Before calling create_project, verify:
- Project name is non-empty
- At least one team member assigned
```
Or use scripts for deterministic validation — code is more reliable than language instructions.

---

## The 3-Level Progressive Disclosure System

| Level | What it is | When loaded |
|-------|-----------|-------------|
| 1 — YAML frontmatter | Name + description | Always (every system prompt) |
| 2 — SKILL.md body | Full instructions | When Claude thinks skill is relevant |
| 3 — Linked files in `references/` | Detailed documentation | Only when Claude navigates to them |

**Implication for our skills:** The description must be strong enough to trigger the skill on its own. The body should stay focused. Heavy reference material belongs in `references/`.

---

## Triggering Issues

### Under-triggering (skill doesn't load when it should)
**Cause:** Description too vague or missing trigger phrases
**Fix:** Add specific phrases users would naturally say; add technical terms; be more concrete about what the skill handles

### Over-triggering (skill loads for unrelated queries)
**Cause:** Description too broad
**Fix:** Add negative triggers ("Do NOT use for..."), narrow scope, clarify what the skill is NOT for

---

## Common Structural Patterns

### Pattern 1: Sequential workflow
- Explicit step ordering
- Dependencies between steps
- Validation at each stage
- Rollback instructions for failures

### Pattern 2: Domain-specific intelligence
- Domain expertise embedded directly in logic
- Compliance/checks before action
- Comprehensive documentation of decisions

### Pattern 3: Iterative refinement
- Explicit quality criteria
- Iterative improvement loops
- Know when to stop iterating

---

## Pre-Analysis Checklist

For each skill in this repo, check:

**Frontmatter**
- [ ] `name` is kebab-case, matches folder name
- [ ] `description` includes WHAT the skill does
- [ ] `description` includes WHEN to use it (trigger phrases)
- [ ] `description` is under 1024 characters
- [ ] No XML angle brackets anywhere
- [ ] `metadata.version` is present

**Instructions**
- [ ] Critical instructions are near the top
- [ ] Instructions are specific and actionable (not vague)
- [ ] Examples are included (or at least described)
- [ ] Related skills are listed for composability
- [ ] "Before Starting" context-loading is present (em-context pattern)

**Triggering**
- [ ] Would Claude know when to use this from the description alone?
- [ ] Does the description include phrases users would naturally say?
- [ ] Is there any risk of over-triggering with other skills?

**Size / structure**
- [ ] SKILL.md is under 5,000 words
- [ ] Heavy reference material is in body (acceptable) or could move to `references/`

---

## Key Insight for Our Skill Set

Our skills are **Category 2: Workflow Automation** — multi-step processes with consistent methodology. The guide notes these benefit from:
- Step-by-step workflow with validation gates
- Templates for common structures
- Built-in review and improvement suggestions
- Iterative refinement loops

This means our skills should **guide Claude through a process**, not just dump knowledge. Skills that are pure reference material (a list of frameworks) should be restructured to include workflow guidance.
