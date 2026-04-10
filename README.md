# Engineering Management Skills

A production-ready library of Agent Skills for engineering managers, tech leads, and directors.

These skills help AI agents give sharper management support for 1:1s, feedback, hiring, performance, roadmap tradeoffs, team health, delegation, stakeholder communication, and related engineering leadership work.

The repository follows the [Agent Skills specification](https://agentskills.io/specification.md). Each skill lives in `skills/<skill-name>/SKILL.md` and may include focused supporting material under `references/`.

## How The Skills Work

`em-context` is the foundation skill. It stores team, org, manager, and direct-report context. Other skills instruct the agent to read that context first when it exists, so advice can be grounded in the user's actual team.

Each management skill is designed to:

- Trigger from realistic manager prompts, not only exact skill names
- Ask only for missing context that materially changes the advice
- Give concise, direct, actionable guidance by default
- Provide scripts, next steps, tradeoffs, and risks where useful
- Link to source material in `references/sources.md`

## Available Skills

| Skill | Purpose |
|---|---|
| [em-context](skills/em-context/) | Stores team/org context and direct-report profiles used by the other skills |
| [1on1s](skills/1on1s/) | Prepare, run, improve, and follow up on 1:1s |
| [business-literacy](skills/business-literacy/) | Translate engineering work into business and finance language |
| [career-development](skills/career-development/) | Support career growth, promotion readiness, and career conversations |
| [delegation](skills/delegation/) | Move managers out of the bottleneck role and build ownership |
| [developer-productivity](skills/developer-productivity/) | Measure team productivity without harmful individual scoring |
| [difficult-situations](skills/difficult-situations/) | Handle high-stakes management edge cases and sensitive situations |
| [engineer-motivation](skills/engineer-motivation/) | Diagnose what drives engineers and match work to motivation |
| [feedback](skills/feedback/) | Give specific positive or corrective feedback and ask for feedback upward |
| [hiring](skills/hiring/) | Define roles, structure interviews, calibrate hiring, and evaluate new hires |
| [influence](skills/influence/) | Persuade stakeholders and get buy-in without direct authority |
| [knowledge-sharing](skills/knowledge-sharing/) | Break knowledge silos and improve documentation/onboarding flow |
| [management-transitions](skills/management-transitions/) | Navigate new-manager, inherited-team, peer-to-manager, and acquisition transitions |
| [managing-high-performers](skills/managing-high-performers/) | Manage top engineers, brilliant jerks, boredom, ambition, and burnout risk |
| [managing-up](skills/managing-up/) | Build a reliable relationship with your manager and communicate upward |
| [managing-urgency](skills/managing-urgency/) | Handle deadlines, fake urgency, crisis pressure, and tradeoff conversations |
| [managing-yourself](skills/managing-yourself/) | Diagnose personal EM traps, bad-day patterns, and recurring leadership tensions |
| [meetings](skills/meetings/) | Decide whether to meet, run better meetings, and protect engineering focus time |
| [performance-reviews](skills/performance-reviews/) | Diagnose underperformance, write reviews, and decide on PIPs or exits |
| [retaining-developers](skills/retaining-developers/) | Diagnose attrition risk and prepare retention conversations |
| [roadmap-planning](skills/roadmap-planning/) | Plan roadmaps, prioritize tech work, and communicate tradeoffs |
| [shadow-work](skills/shadow-work/) | Identify hidden capacity drains like support, glue work, and shadow backlogs |
| [team-composition](skills/team-composition/) | Diagnose team capability gaps and hiring/assignment needs |
| [team-health](skills/team-health/) | Assess and improve morale, trust, intensity, engagement, and team culture |
| [working-with-architects](skills/working-with-architects/) | Work effectively with architects, staff engineers, and principal engineers |
| [working-with-pm](skills/working-with-pm/) | Build a stronger PM-EM partnership and improve product orientation |
| [written-communication](skills/written-communication/) | Draft clear Slack messages, announcements, and stakeholder updates |

## Installation

Copy the skills you want into `.agents/skills/` in your project:

```bash
mkdir -p .agents/skills
cp -r skills/em-context .agents/skills/
cp -r skills/1on1s .agents/skills/
```

For the full library:

```bash
mkdir -p .agents/skills
cp -r skills/* .agents/skills/
```

Then create or update `.agents/em-context.md` with your team context so the other skills can tailor their advice.

## Repository Structure

```text
skills/
  skill-name/
    SKILL.md
    references/
      sources.md
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or improve skills.

Each `SKILL.md` should:

- Use valid YAML frontmatter
- Keep `name` equal to the directory name
- Keep `description` under 1024 characters
- Stay under 500 lines
- Read `em-context` before giving personalized advice
- Prefer concise, direct, manager-ready output
