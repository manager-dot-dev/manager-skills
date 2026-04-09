# Skill Analysis
Audit of all 29 skills against *The Complete Guide to Building Skills for Claude*

---

## Summary

| Issue | Severity | Count |
|-------|----------|-------|
| Description doesn't state WHAT Claude will do (only WHEN) | Medium | 27/29 |
| No negative triggers to prevent over-triggering | Medium | 29/29 |
| Skills are knowledge dumps, not workflow guides | Medium | ~20/29 |
| No examples of successful output | Medium | 29/29 |
| `managing-yourself` is too large (3302 words) | Medium | 1/29 |
| Description undersells the skill (not "pushy" enough) | Low | ~15/29 |
| No `references/` subfolder for heavy content | Low | 29/29 |

All skills pass the hard technical requirements (kebab-case names, valid frontmatter, no XML angle brackets, all have version metadata).

---

## Issue 1: Descriptions state WHEN but not WHAT (All skills)

**The guide's formula:** `[What it does] + [When to use it] + [Key capabilities]`

Every skill in this repo opens with "When the user wants to..." — that's the WHEN. But descriptions are missing the WHAT: what will Claude actually *produce* or *do*?

**Current pattern (all 27):**
> "When the user wants to [goal]. Also use when the user says [phrases]."

**Guide's expected pattern:**
> "[What Claude produces]. Use when user wants to [goal] or says [phrases]."

**Examples to fix:**

| Skill | Current start | Should start with |
|-------|--------------|-------------------|
| `1on1s` | "When the user wants to prepare for, run, improve..." | "Provides agendas, frameworks, and scripts for 1:1 meetings. Use when..." |
| `feedback` | "When the user wants to give structured feedback..." | "Delivers structured SBI feedback, scripts for hard conversations, and written review language. Use when..." |
| `hiring` | "When the user wants to define a role..." | "Guides role definition, interview structure, candidate evaluation, and hiring decisions. Use when..." |
| `managing-yourself` | "When the user wants to reflect on their own effectiveness..." | "Diagnoses EM blind spots and provides frameworks for managing up, across, and self. Use when..." |

**Priority fixes:** `feedback`, `hiring`, `1on1s`, `managing-yourself` (most-used skills)

---

## Issue 2: No negative triggers (All skills)

The guide explicitly recommends adding negative triggers when there's a risk of over-triggering. In our set, several skill pairs are at high risk of triggering when the wrong one should load.

**Risky pairs / clusters:**

| Skill | Could mis-trigger when... | Negative trigger to add |
|-------|--------------------------|------------------------|
| `team-health` | User is asking about a specific developer (→ `1on1s`) | "Do NOT use for individual developer situations — use 1on1s" |
| `retaining-developers` | User asks about team morale broadly (→ `team-health`) | "Do NOT use for general team health — use team-health" |
| `managing-yourself` | User is asking about delegation (→ `delegation`) | "Do NOT use for delegating specific tasks — use delegation" |
| `team-composition` | User is mid-hiring process (→ `hiring`) | "Do NOT use for specific candidate evaluation — use hiring" |
| `shadow-work` | User asks about roadmap capacity (→ `roadmap-planning`) | "Do NOT use for roadmap prioritization — use roadmap-planning" |
| `delegation` | User asks about task-level maturity (→ `managing-yourself`) | N/A — actually contained within delegation |

**Recommendation:** Add one sentence to the description of each skill flagged above: `"Do NOT use for [adjacent case] (use [other-skill] instead)."`

---

## Issue 3: Skills are knowledge repositories, not workflow guides (~20 skills)

**What the guide says:** Category 2 skills (Workflow Automation) should guide Claude through a *process* with step-by-step workflow, validation gates, and explicit next steps.

**What our skills do:** Most are structured as *reference libraries* — a series of framework sections that Claude can draw on. Claude must decide on its own how to use the material.

**The gap:** There's no "given this user situation, here's what Claude should do next" logic. A user who asks "help me with my 1:1" gets frameworks, but Claude doesn't know whether to ask clarifying questions, produce an agenda, give scripts, or diagnose the relationship.

**Skills most affected:**

| Skill | Problem | Quick fix |
|-------|---------|-----------|
| `1on1s` | No guidance on what to produce | Add "If user wants to prepare: produce agenda. If user wants to diagnose: ask these questions first..." |
| `feedback` | No decision tree for type of feedback | Add "Step 1: Determine type (positive vs. constructive). Step 2: Apply SBI..." |
| `performance-reviews` | Many sections, no entry point | Add "Start by identifying the review type..." |
| `hiring` | Many sections, no entry point | Add "Start by identifying the stage (defining role vs. interviewing vs. deciding)..." |
| `managing-yourself` | Pure reference dump | Add decision logic: "If user feels stuck: use the 10 traps. If user is under pressure: use BAA..." |

**Skills already doing this well:**
- `em-context` — clear setup workflow
- `feature-flags` — sequential decision logic built in
- `shadow-work` — structured by problem type

---

## Issue 4: No examples of successful output (All skills)

The guide recommends including examples showing what a successful interaction looks like. None of our skills do this.

**What to add to each skill:**

```
## Example
User says: "My 1:1 with Alex keeps turning into status updates and I want to fix it"
Claude should: Diagnose the pattern using the "don't focus on day-to-day work" principle,
provide 3 specific redirect questions, and suggest a different opening structure.
```

This is especially important for skills like `feedback`, `written-communication`, and `1on1s` where the expected output format is not obvious from the content.

---

## Issue 5: `managing-yourself` is too large

**Current size:** 3302 words (the guide recommends under 5000, but also under 500 lines for the body)

**Sections that could move to `references/`:**
- The full 10-trap list with explanations (could be a `references/ten-traps.md`)
- The BAA framework scenarios (could be `references/baa-scenarios.md`)
- The Dichotomies table (short enough to keep)

**Impact:** Large skill body slows response and may cause Claude to skim rather than read carefully.

---

## Issue 6: Descriptions are not "pushy" enough (~15 skills)

**The guide says:** "Claude has a tendency to 'undertrigger' — to not use skills when they'd be useful. To combat this, make skill descriptions a little bit pushy."

**Example of pushy vs. neutral:**

Neutral (current):
> "When the user wants to delegate work, reduce bottlenecks, give their team more ownership..."

Pushy (guide style):
> "Provides the Team Rep pattern, kingdom ownership framework, and 3-layer assignment model for delegation. Use whenever the user mentions bottlenecks, ownership, being too busy, or anything where the manager is doing work the team could own — even if they don't say 'delegation' explicitly."

**Most undertriggered skills (phrases too narrow):**

| Skill | Missing trigger context |
|-------|------------------------|
| `shadow-work` | Wouldn't trigger on "why do we keep missing sprint goals" or "team seems busy but nothing ships" — needs broader capacity-miss language |
| `team-composition` | Wouldn't trigger on "something feels off with the team dynamic" without clear skill-gap language |
| `em-internal-tools` | Very niche trigger phrases — "build something" could easily miss this |
| `feature-flags` | Wouldn't trigger on "our codebase is getting cluttered" or "PM keeps asking for permanent flags" |
| `getting-feedback` | Wouldn't trigger on "I don't know how my team really sees me" |

---

## Per-Skill Scorecard

| Skill | Words | WHAT stated | Negative triggers | Workflow guide | Examples | Priority |
|-------|-------|------------|-------------------|---------------|----------|----------|
| 1on1s | 588 | ✗ | ✗ | ✗ | ✗ | High |
| ai-adoption | 1396 | ✗ | ✗ | ~partial | ✗ | Medium |
| business-literacy | 765 | ✗ | ✗ | ✗ | ✓ partial | Low |
| code-reviews | 980 | ✗ | ✗ | ✗ | ✗ | Medium |
| deep-work | 521 | ✗ | ✗ | ✗ | ✗ | Low |
| delegation | 1001 | ✗ | ✗ | ~partial | ✗ | High |
| em-context | 572 | ✓ | ✗ | ✓ | ✗ | Low |
| em-internal-tools | 509 | ✗ | ✗ | ~partial | ✗ | Medium |
| feature-flags | 611 | ✗ | ✗ | ~partial | ✗ | Low |
| feedback | 417 | ✗ | ✗ | ✗ | ✗ | High |
| getting-feedback | 492 | ✗ | ✗ | ✗ | ✗ | Medium |
| hiring | 1073 | ✗ | ✗ | ✗ | ✗ | High |
| influence | 661 | ✗ | ✗ | ✗ | ✗ | Medium |
| knowledge-sharing | 993 | ✗ | ✗ | ✗ | ✗ | Low |
| management-transitions | 1085 | ✗ | ✗ | ~partial | ✗ | Medium |
| manager-readme | 525 | ✗ | ✗ | ~partial | ✗ | Low |
| managing-high-performers | 841 | ✗ | ✗ | ✗ | ✗ | Medium |
| managing-urgency | 860 | ✗ | ✗ | ~partial | ✗ | Medium |
| **managing-yourself** | **3302** | ✗ | ✗ | ✗ | ✗ | **High** |
| performance-reviews | 778 | ✗ | ✗ | ✗ | ✗ | High |
| retaining-developers | 1257 | ✗ | ✗ | ✗ | ✗ | Medium |
| roadmap-planning | 1544 | ✗ | ✗ | ✗ | ✗ | Medium |
| shadow-work | 600 | ✗ | ✗ | ✓ | ✗ | Low |
| team-composition | 545 | ✗ | ✗ | ~partial | ✗ | Low |
| team-health | 1300 | ✗ | ✗ | ✗ | ✗ | Medium |
| working-with-architects | 668 | ✗ | ✗ | ✗ | ✗ | Low |
| working-with-pm | 994 | ✗ | ✗ | ✗ | ✗ | Medium |
| written-communication | 917 | ✗ | ✗ | ✓ | ✓ partial | Low |

**Legend:** ✓ = good, ~partial = somewhat, ✗ = missing

---

## Recommended Action Order

### Phase 1 — High impact, low effort: Fix descriptions (all skills)
Add WHAT to each description. Change "When the user wants to X" → "Does X. Use when the user wants to X." Takes ~5 min per skill.

### Phase 2 — High priority skills: Add workflow entry points
For `1on1s`, `feedback`, `hiring`, `performance-reviews`, `managing-yourself`: add a brief decision section at the top of the body that routes Claude to the right section based on the user's situation.

### Phase 3 — Size: Split `managing-yourself`
Move the 10-trap section and BAA scenarios to `references/`. Keep the body focused on the core frameworks.

### Phase 4 — Triggering: Add negative triggers
Add one "Do NOT use for..." line to the 5-6 skills at highest risk of over-triggering.

### Phase 5 — Use skill-creator description optimizer
Run the description optimization loop (from skill-creator) on the 5 most-used skills to maximize correct triggering.
