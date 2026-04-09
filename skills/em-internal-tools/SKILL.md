---
name: em-internal-tools
description: When the user wants to build internal tools for their team, use AI to solve team pain points, or stay technically active without taking sprint tasks. Also use when the user says "build something for the team," "internal tool," "automate this," "vibe coding for the team," or "what can I build in a few hours."
metadata:
  version: 1.0.0
---

# EM Internal Tools

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

---

## Why This Matters Now

AI coding tools have eliminated the "I don't have time" excuse for building internal tools. Two to three hours between meetings is now enough to ship a working tool. EMs who use this window solve real team pain points without waiting for a PM to prioritize them — and stay technically connected in the process.

---

## The 10 Highest-Value Tool Categories

1. **Demo data preparator** — copies specific production subsets into QA environments, eliminating the "I can't reproduce this without production data" blocker
2. **Hackathon organizer** — submission tracking, voting, scheduling, and announcement automation
3. **Kudos board** — Slack-integrated recognition system that makes appreciation visible and searchable
4. **On-call rotation scheduler** — fair rotation generator that respects time zones, PTO, and seniority
5. **Support agent** — reads incoming support tickets, matches to known issues, suggests responses or auto-routes to the right team
6. **Custom retrospective tool** — structured input collection with automatic action-item tracking and follow-up reminders
7. **Release notes generator** — pulls merged PRs from GitHub/GitLab since the last release and drafts formatted release notes
8. **Random coffee matcher** — pairs engineers across teams or functions weekly for cross-functional relationship building
9. **Meeting talk-time monitor** — records and surfaces who dominates and who goes quiet in recurring meetings
10. **Team games** — small competitive tools for sprint goals, bug counts, or code review velocity (use carefully — gamification has risks)

---

## Choosing the Right Tool to Build With

| Situation | Use |
|-----------|-----|
| Needs access to internal systems (prod DB, API keys, Jira) | Cursor or Claude Code — full control over integration |
| Standalone internal app with UI | Base44, Lovable, or v0 — faster to ship, no infrastructure management |
| Orchestrates multiple systems (Slack + Calendar + Jira) | n8n or Zapier — visual workflow builder, no custom code needed |

---

## The Triple Payoff

Building internal tools as an EM delivers three returns simultaneously:
1. **Solves real team pain** without competing for roadmap space
2. **Maintains technical fluency** — you stay current with the tools and languages your team uses
3. **Signals to engineers** that their manager still builds — which matters more than most EMs realize

---

## Related Skills

- `managing-yourself` — Building internal tools is one of the three valid categories for Maker/Manager time
- `ai-adoption` — Vibe coding for internal tools is a low-risk way to experiment with AI coding tools personally
- `deep-work` — Tools that reduce friction (notification routing, async defaults) directly protect team focus time
