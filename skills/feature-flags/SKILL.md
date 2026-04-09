---
name: feature-flags
description: When the user wants to manage feature flag sprawl, establish flag governance, or decide how to structure flags across product and engineering. Also use when the user says "feature flags," "feature toggles," "flag cleanup," "flag debt," "too many flags," or "release toggles."
metadata:
  version: 1.0.0
---

# Feature Flags

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

---

## Why Flag Sprawl Happens

Feature flags accumulate because there is no shared taxonomy. A PM creates an experiment toggle and treats it as permanent. A developer adds a release toggle and forgets to delete it. An ops toggle gets repurposed as a permission system. After a year, nobody knows which flags are safe to remove, and removing any of them feels risky.

The root cause is always the same: flags were created without agreeing on their category, owner, and expected lifetime.

---

## The Four-Category Framework

Not all feature flags are equal. Treating them the same is the root cause of flag sprawl.

### 1. Release Toggles
- **Owner:** the developer
- **Lives in:** config files or code
- **Lifetime:** 1–2 weeks after the feature ships, then deleted
- **Purpose:** decouples deployment from release — ship code to production before it's exposed to users

Release toggles are the most common and the most commonly left to rot. Enforce a hard rule: if a release toggle is still active 2 weeks after the feature launched, it gets deleted in the next sprint.

### 2. Ops Toggles
- **Owner:** the Ops/SRE team
- **Lives in:** a dedicated ops configuration tool (not the codebase)
- **Lifetime:** deleted once confidence in the system is established; rare exceptions become permanent kill-switches
- **Purpose:** circuit breakers, graceful degradation, load shedding

### 3. Experiment Toggles
- **Owner:** the PM
- **Lives in:** an A/B testing or experimentation platform
- **Lifetime:** days to weeks, deleted as soon as enough data is collected
- **Purpose:** controlled rollout and measurement of product changes

Experiment toggles that outlive their experiment are a warning sign — it usually means nobody is watching the results.

### 4. Permission Toggles
- **Owner:** the PM
- **Lives in:** a long-lived configuration store, architecturally designed for permanence
- **Lifetime:** intentionally long-lived — sometimes years
- **Purpose:** entitlements, plan-based features, beta access

The critical design point: permission toggles must be designed as permanent from day one. They cannot be treated as temporary and promoted later — the architecture must support long-lived flags from the start, or the system breaks under them.

---

## The EM's Role in Flag Governance

**Align the team on the taxonomy.** Developers need to know which category to use before they create a flag — this determines where it lives, who owns it, and when it gets deleted. A 15-minute team discussion prevents months of confusion.

**Enforce expiration.** The simplest mechanisms: automated test failures on flags older than a threshold, a hard cap on active flags that forces deletion before creation, or a weekly hygiene slot in the sprint.

**Protect the architecture for permission toggles.** When a PM requests a new entitlement system or beta gate, the conversation needs to include the lifetime. If it's permanent, it needs to be designed for permanence.

**Watch for category drift.** The most common failure: a release toggle that gets repurposed as an ops toggle, or an experiment toggle that quietly becomes a permission system. Flag migrations between categories should be explicit, not accidental.

---

## Related Skills

- `roadmap-planning` — Flag debt is technical debt that belongs in the tech backlog with business justification
- `working-with-pm` — PMs own experiment and permission toggles; this is a shared responsibility conversation
