# Roadmap Planning — Extended Reference

## The Cleanathon: Making Tech Cleanup Happen

One effective format for tackling accumulated dead code, stale infrastructure, and technical clutter: a company-wide competition day.

**The basic format:** every team competes to delete and clean up as much as possible in a single working day. With proper scoring, teams can include non-engineering departments (finance, QA, product) — anyone with files, automations, or processes to clean up.

**What makes it work:**
- **Scoring system** — critical for energy and engagement. Without scores, it's just a boring cleanup day. With scores, teams work until the last minute. Cap points per action (e.g., 1000 points max per deletion, regardless of size) to prevent gaming.
- **Stability safeguards** — require 2 approvals from people familiar with the code, keep PRs open until tested together post-event, run end-to-end tests before merging
- **Celebrate the effort** — team names, logos, printed rosters, lunch together. The social element matters.

**The second-order effect to manage:** in the weeks before the event, teams stop deleting things and save them for points. Remind the team that continuous cleanup is the goal — the event is a catalyst, not a substitute.

**Post-event: use the momentum.** Establish guidelines that prevent the same mess from accumulating: auto-delete merged branches, add dead code analyzers, create tickets to delete feature flags when they're created.

**Source:** [Organizing the Best Cleanathon](https://newsletter.manager.dev/p/organizing-the-best-cleanathon-your) — manager.dev
