---
name: ai-adoption
description: When the user wants to introduce AI coding tools to their engineering team, roll out AI tools org-wide, measure AI adoption, or deal with engineer skepticism about AI. Also use when the user says "AI tools," "Copilot," "Cursor," "Claude Code," "AI adoption," "roll out AI," "engineers skeptical of AI," or "measure AI impact."
metadata:
  version: 1.0.0
---

# AI Adoption

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

---

## The 5-Level Framework

Most teams mess up AI adoption by buying every tool, running vanity metrics (token usage! AI usage up 40%!), or forcing adoption to claim credit. The teams that succeed follow a staged pattern.

---

## Level 1: Code Editors

**Choose tools to evaluate.** The market has Cursor, Claude Code, GitHub Copilot, Windsurf, and others. Pick 2 and run a real evaluation. A reasonable starting pair: Claude Code and Cursor.

**Pick an alpha team.** 3–5 engineers who are:
- Naturally curious about new tools
- Influential with their peers
- From different teams and seniority levels

Expect 4–5 hours per week per person for the first month. This is real time investment — plan for it.

**Set up rules files.** AI tools don't know your team's style by default. Create 10–15 specific rules instead of vague guidelines.

Bad: `"Write clean code"`
Good: `"Always use TypeScript interfaces for component props. Name them with 'Props' suffix (e.g., ButtonProps)"`

Bad: `"Follow security best practices"`
Good: `"Never hardcode API keys. Use environment variables with VITE_ prefix for client-side"`

**Set up MCP servers.** The Model Context Protocol lets AI tools pull in relevant context — your Postgres database schema, internal APIs, Jira, GitHub, Sentry. Almost every major tool has an MCP server. Configure them so AI has the context it needs to generate useful output.

**Roll out org-wide.** After alpha team selects a tool, creates rules, and sets up MCPs — roll it out. Plan 2–4 weeks of alpha testing before going org-wide.

**Run ongoing internal training.** Your alpha team has the deepest knowledge. Make them internal trainers. Focus training on context engineering — the art of communicating with AI to get what you want. Keep sessions practical, not theoretical.

---

## Level 2: Background Agents

Background agents (Devin, Cursor Background Agent, Codex, etc.) make commits directly to your repos with minimal human intervention. A growing number of teams use them for low-judgment tasks: documentation updates, boilerplate generation, test scaffolding.

Configure agents the same way as code editors: rules files + relevant MCP connections. They need the same context to be useful.

---

## Level 3: AI Code Reviews

Once agents start committing code, code reviews become the new bottleneck. AI code reviewers can handle the obvious issues — style violations, common bugs, security patterns — freeing engineers to focus on architecture and design decisions.

Two notes:
- Don't use the same tool to write and review code. Different tools catch different things.
- Set up reviewer rules the same way as coding rules. The reviewer doesn't know your team's standards unless you tell it.

---

## Level 4: Measurement

Track adoption quality, not just usage. "AI usage went up 40%" is meaningless without context.

**Adoption metrics:**
- Daily active users by team
- Background agent adoption rate
- Token burn rate vs. actual output

**Productivity metrics (should improve):**
- Time to first commit for new features
- Code review cycle time
- Deployment frequency

**Warning sign:** if code review time increases significantly, engineers may be dumping unreviewed AI code on reviewers. Address it.

**Quality metrics (should stay flat or improve):**
- PR revert rate
- Time spent on bug fixes vs. new features
- Code turnover rate: percentage of code rewritten within 90 days

**ROI:** `(Time saved × hourly rate) / Tool costs`

Start simple: pick 3 metrics total — one adoption, one productivity, one quality. Review monthly.

---

## Level 5: Ongoing Innovation

Create a process for evaluating new tools: who is responsible, how often, how they measure success. The AI tooling landscape changes fast — you need a repeatable process, not ad-hoc evaluation every time something new appears.

Extend to other teams. Evaluate AI tools for presentations (Gamma), internal apps and PoCs (Lovable), and other functions. The engineering team's experience makes you a natural resource for broader AI adoption in the organization.

---

## How Vibe Coding Changes Your Role

As AI dramatically accelerates developer output, 5 things shift for the EM:

**1. The bottleneck moves.** When dev speed doubles or triples, engineering is no longer the constraint. Product discovery, design, QA, and deployment become the new bottlenecks. Your job: invest in making those faster too. More time spent on clear specs before coding, better QA tooling, faster deploy pipelines.

**2. Bigger scope per team.** A small team can now own more surface area. You'll be expected to manage more systems with the same headcount. The challenge: ongoing maintenance costs scale up too (see `roadmap-planning`).

**3. More outages and bugs.** Faster output without proportionally more testing = more production problems. Your team needs guardrails: automated tests, staged rollouts, better monitoring. Speed without guardrails creates a quality debt that compounds.

**4. Engineers making product decisions.** When shipping is fast, the bottleneck shifts to "what do we build?" Product validation becomes the rate-limiting step. Engineers will increasingly be pulled into defining requirements. Help your team build product instincts — customer conversations, usage metrics, outcome thinking.

**5. Less focus time.** AI tools require constant context-switching to review, prompt, and redirect. The developer isn't in deep work — they're in a review loop. Protect blocks of uninterrupted time even with AI tools (see `deep-work`).

---

## Why Engineers Resist

Engineer skepticism about AI tools is usually one of three things:
1. They've seen low-quality AI output and don't trust it
2. They feel the tool is being imposed on them without input
3. They fear the tool is a precursor to headcount reduction

The alpha team approach addresses #1 and #2 directly — engineers evaluate and choose the tool themselves. For #3: be honest about what AI adoption means for the team's expectations. Don't let rumors fill the vacuum.

---

## Related Skills

- `deep-work` — AI tools change the nature of developer focus — good rules files reduce context-switching
- `team-health` — Skepticism about AI tools is often a team health signal worth addressing in 1:1s
- `roadmap-planning` — AI tooling investment is a tech initiative that needs business justification and tracking

