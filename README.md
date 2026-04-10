# Engineering Management Skills

An OPINIONATED library of Agent Skills for engineering managers, tech leads, and directors.

LLMs were trained on the whole internet, and they suck at advice related to management.

For this repo, I gathered info from the best articles I've read in the last 10 years, engineering management and leadership books, and my own articles and posts based on my own experience. For books, I've used only my notes from the books. I didn't upload the full books to LLMs.

You may strongly disagree with an answer. That's good, and that's the point. Generic shit advice is not helpful. If you disagree, follow your own opinion.

My goal is to provide you with some useful perspective, like if you had talked to a fellow EM and shared your dilemma.

The opinions are mine, and not a universal truth or a how-to guide.

See the [Resources](#resources) section for the full list of articles and books that inspired this repo, including resources that did not end up being used directly in a skill. The skills are heavily based on articles from my blog and newsletter, [newsletter.manager.dev](https://newsletter.manager.dev/).

## What This Repository Is

These skills help AI agents give sharper management support for 1:1s, feedback, hiring, performance, roadmap tradeoffs, team health, delegation, stakeholder communication, and related engineering leadership work.

The repository follows the [Agent Skills specification](https://agentskills.io/specification.md). Each skill lives in `skills/<skill-name>/SKILL.md` and may include focused supporting material under `references/`.

## How The Skills Work

`em-context` is the foundation skill. It stores team, org, manager, and direct-report context. Other skills instruct the agent to read that context first when it exists, so advice can be grounded in the user's actual team.

Each management skill is designed to:

- Trigger from realistic manager prompts, not only exact skill names
- Ask only for missing context that materially changes the advice
- Give concise, direct, manager-ready guidance by default
- Provide scripts, next steps, tradeoffs, and risks where useful
- Preserve a clear point of view instead of flattening everything into generic advice
- Link to source material in `references/sources.md`

## Skills By Management Area

The `skills/` directory stays flat so skills are easy to install and publish. This grouping is only here to make the library easier to browse.

### Foundation

| Skill | Purpose |
|---|---|
| [em-context](skills/em-context/) | Stores team/org context and direct-report profiles used by the other skills |

### Managing People

Individual humans: growth, feedback, motivation, performance, retention, hiring, and direct manager/report conversations.

| Skill | Purpose |
|---|---|
| [1on1s](skills/1on1s/) | Prepare, run, improve, and follow up on 1:1s |
| [career-development](skills/career-development/) | Support career growth, promotion readiness, and career conversations |
| [engineer-motivation](skills/engineer-motivation/) | Diagnose what drives engineers and match work to motivation |
| [feedback](skills/feedback/) | Give specific positive or corrective feedback and ask for feedback upward |
| [hiring](skills/hiring/) | Define roles, structure interviews, calibrate hiring, and evaluate new hires |
| [managing-high-performers](skills/managing-high-performers/) | Manage top engineers, brilliant jerks, boredom, ambition, and burnout risk |
| [performance-reviews](skills/performance-reviews/) | Diagnose underperformance, write reviews, and decide on PIPs or exits |
| [retaining-developers](skills/retaining-developers/) | Diagnose attrition risk and prepare retention conversations |

### Building The Team

The team as a system: ownership, trust, rituals, staffing shape, knowledge flow, and sensitive team-level situations.

| Skill | Purpose |
|---|---|
| [delegation](skills/delegation/) | Move managers out of the bottleneck role and build ownership |
| [difficult-situations](skills/difficult-situations/) | Handle high-stakes management edge cases and sensitive situations |
| [knowledge-sharing](skills/knowledge-sharing/) | Break knowledge silos and improve documentation/onboarding flow |
| [meetings](skills/meetings/) | Decide whether to meet, run better meetings, and protect engineering focus time |
| [team-composition](skills/team-composition/) | Diagnose team capability gaps and hiring/assignment needs |
| [team-health](skills/team-health/) | Assess and improve morale, trust, intensity, engagement, and team culture |

### Delivery And Execution

Getting work through the system: prioritization, deadlines, productivity, hidden work, delivery tradeoffs, and capacity.

| Skill | Purpose |
|---|---|
| [developer-productivity](skills/developer-productivity/) | Measure team productivity without harmful individual scoring |
| [managing-urgency](skills/managing-urgency/) | Handle deadlines, fake urgency, crisis pressure, and tradeoff conversations |
| [roadmap-planning](skills/roadmap-planning/) | Plan roadmaps, prioritize tech work, and communicate tradeoffs |
| [shadow-work](skills/shadow-work/) | Identify hidden capacity drains like support, glue work, and shadow backlogs |

### Product, Business, And Stakeholders

Operating outside the team boundary: PM partnership, business framing, stakeholder trust, upward communication, architecture collaboration, and written alignment.

| Skill | Purpose |
|---|---|
| [business-literacy](skills/business-literacy/) | Translate engineering work into business and finance language |
| [influence](skills/influence/) | Persuade stakeholders and get buy-in without direct authority |
| [managing-up](skills/managing-up/) | Build a reliable relationship with your manager and communicate upward |
| [working-with-architects](skills/working-with-architects/) | Work effectively with architects, staff engineers, and principal engineers |
| [working-with-pm](skills/working-with-pm/) | Build a stronger PM-EM partnership and improve product orientation |
| [written-communication](skills/written-communication/) | Draft clear Slack messages, announcements, and stakeholder updates |

### Managing Yourself

Your own operating system as a manager: role transitions, personal traps, bad-day patterns, and recurring leadership tensions.

| Skill | Purpose |
|---|---|
| [management-transitions](skills/management-transitions/) | Navigate new-manager, inherited-team, peer-to-manager, and acquisition transitions |
| [managing-yourself](skills/managing-yourself/) | Diagnose personal EM traps, bad-day patterns, and recurring leadership tensions |

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

## Resources

The skills are heavily based on articles from [newsletter.manager.dev](https://newsletter.manager.dev/), plus the articles and books below. This list includes sources that inspired the repo even when they did not end up directly referenced in a specific skill.

### Articles

| # | Title | URL |
|---|---|---|
| 1 | 10 Interview Techniques From the World's Best Interviewers | https://www.readtheprofile.com/p/the-profile-10-interview-techniques |
| 2 | 1:1 as a manager of managers | https://randsinrepose.com/archives/the-update-the-vent-and-the-disaster/ |
| 3 | 12 signs you are working in a feature factory | https://cutle.fish/blog/12-signs-youre-working-in-a-feature-factory |
| 4 | 5 Engineering Manager Archetypes | https://www.patkua.com/blog/5-engineering-manager-archetypes/ |
| 5 | A company is not a family - it's a team | https://world.hey.com/dhh/you-re-not-guaranteed-a-spot-on-the-team-95080248 |
| 6 | Advice for new directors | https://www.rubick.com/advice-for-new-directors/ |
| 7 | Agile is Dead! The Endless Debate! | https://dpereira.substack.com/p/agile-is-dead-true-or-false |
| 8 | All Projects Are Business Projects | https://staysaasy.com/management/2023/10/08/all-projects-are-business-projects.html |
| 9 | Ambition gravity | https://www.developing.dev/p/ambition-gravity |
| 10 | Answer to 'no estimations' | https://lucasfcosta.com/2023/07/15/people-who-cant-estimate.html |
| 11 | Article - Reliable teams | https://staysaasy.com/management/2022/09/17/Reliable-Teams.html |
| 12 | Best interview questions by Lenny | https://www.lennysnewsletter.com/p/the-best-interview-questions |
| 13 | Bottlenecks and the theory of constraints | https://www.theengineeringmanager.com/growth/theory-of-constraints/ |
| 14 | Brian Chesky on how to hire | https://www.lennysnewsletter.com/p/brian-chesky-on-hiring |
| 15 | Brook's Law - adding more people can make software later | https://newsletter.eng-leadership.com/p/brooks-law |
| 16 | Commandos, Infantry, and Police | https://cdixon.org/2010/02/18/the-three-phases-of-business-growth |
| 17 | CTO vs VPE / VP R&D | https://www.gitprime.com/the-cto-vs-vp-engineering-debate/ |
| 18 | Data Dog downtime incident | https://www.datadoghq.com/blog/2023-03-08-postmortem/ |
| 19 | Dealing with feature factory | https://www.svpg.com/dealing-with-feature-teams/ |
| 20 | Developer Experience management | https://newsletter.pragmaticengineer.com/p/developer-experience |
| 21 | Developer productivity - Advocating for qualitative metrics | https://newsletter.pragmaticengineer.com/p/developer-productivity |
| 22 | Developer progression | https://www.progression.fyi/ |
| 23 | DevEx - measuring developer productivity | https://queue.acm.org/detail.cfm?id=3595878 |
| 24 | Disagree and commit just doesn't work | https://newsletter.weskao.com/p/disagree-and-commit |
| 25 | DMO Framework - Developer Motivation Explained | https://www.developing.dev/p/dmo-framework |
| 26 | DX Core 4 - Developer Productivity Metrics | https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/ |
| 27 | Elite vs Average performers | https://www.developing.dev/p/elite-vs-average-performers |
| 28 | Embracing negativity and the Abilene paradox | https://www.rubick.com/embracing-negativity/ |
| 29 | Engineering excellence | https://newsletter.pragmaticengineer.com/p/engineering-excellence |
| 30 | Engineering Metrics Explained | https://newsletter.pragmaticengineer.com/p/engineering-metrics |
| 31 | Fail fast, fail cheap, fail forward | https://www.svpg.com/fail-fast/ |
| 32 | Feature Flags - Engineering practices | https://martinfowler.com/articles/feature-toggles.html |
| 33 | Fixing broken teams - don't blame the previous leader | https://mgmt.beehiiv.com/p/fix-your-broken-team-8-turnaround-tips-for-sustained-success |
| 34 | Gamifying feedback | https://www.bitsandbrushes.news/p/how-to-boost-remote-speed-feedback |
| 35 | Getting an Engineering Executive Job | https://newsletter.pragmaticengineer.com/p/getting-an-engineering-executive |
| 36 | Good Managers Clear Paths | https://leadership.garden/ |
| 37 | Good product teams | https://www.youtube.com/watch?v=Y4PdUItyXUk |
| 38 | Google - The five keys to a successful team | https://rework.withgoogle.com/blog/five-keys-to-a-successful-google-team/ |
| 39 | Handling layoffs | https://kellanem.com/notes/layoff-foundations |
| 40 | Hands-On | https://open.substack.com/pub/chaitimewithchaitali/p/hands-on |
| 41 | Have Concerns And Commit | https://blog.staysaasy.com/p/have-concerns-and-commit |
| 42 | Hiring - culture contribution instead of culture fit | https://kevanlee.substack.com/p/513-how-what-vs-do-is |
| 43 | Hiring A Players | https://mgmt.beehiiv.com/p/the-talent-factory-how-to-identify-and-develop-a-players-for-your-team |
| 44 | Hiring for Additivity | https://medium.com/@aaronlerch/hiring-for-additivity-548d58016cc7 |
| 45 | How Can You Help Your Team Avoid Layoffs | https://mgmt.beehiiv.com/p/how-can-you-help-your-team-avoid-layoffs |
| 46 | How Engineering Management is Changing in 2024 | https://refactoring.fm/p/how-engineering-management-is-changing |
| 47 | How I stay motivated as an engineering manager | https://open.substack.com/pub/becomingaleader/p/how-i-stay-motivated-as-an-engineering |
| 48 | How To Build The Leadership Habits That Lead To Great Teams | https://mgmt.beehiiv.com/p/how-to-build-the-leadership-habits-that-lead-to-great-teams |
| 49 | How much appreciation do you show your team | https://open.substack.com/pub/thecaringtechie/p/how-much-appreciation-do-you-show |
| 50 | How to Become More Likable | https://open.substack.com/pub/theprofile/p/how-to-become-more-likable-charismatic |
| 51 | How to Become a Master Negotiator | https://open.substack.com/pub/theprofile/p/negotiation-techniques |
| 52 | How to Design an Org for Founder Mode | https://open.substack.com/pub/danhock/p/designing-an-org-for-founder-mode |
| 53 | How to Self-Manage Even if You Have a Manager | https://open.substack.com/pub/thecaringtechie/p/how-to-self-manage-even-if-you-have |
| 54 | How to Ship Fast | https://wraptext.equals.com/how-to-ship-fast/ |
| 55 | How big companies do project management | https://blog.pragmaticengineer.com/project-management-at-big-tech/ |
| 56 | How to create a culture of dogfooding | https://nickey.substack.com/p/how-to-create-a-culture-of-dogfooding |
| 57 | How to get more headcount | https://lethain.com/how-to-get-more-headcount/ |
| 58 | How to on-board yourself when you join a new team | https://open.substack.com/pub/weskao/p/how-to-on-board-yourself |
| 59 | How to operate (barrels and ammunition) | https://www.youtube.com/watch?v=6fQHLK1aIBs |
| 60 | How to prioritize features | https://www.ycombinator.com/library/8p-how-to-prioritize-features |
| 61 | How to properly estimate a project | https://hybridhacker.email/p/demystifying-project-estimation |
| 62 | How to run better meetings | https://open.substack.com/pub/torstenwalbaum/p/how-to-run-better-meetings |
| 63 | Ice breaker questions | https://dariarudnik.com/tpost/spnhl05sk1-breaking-the-virtual-ice-100-questions-f |
| 64 | In a Job Interview, Acknowledge Your Weaknesses | https://adamgrant.substack.com/p/in-a-job-interview-this-is-how-to |
| 65 | Judge Your Coworkers | https://open.substack.com/pub/staysaasy/p/judge-your-coworkers |
| 66 | Kebab vs Cake organization | https://blog.alexewerlof.com/p/kebab-vs-cake |
| 67 | Layers of context | https://lethain.com/layers-of-context/ |
| 68 | Lessons from Netflix CTO | https://www.lennysnewsletter.com/p/how-netflix-builds-a-culture-of-excellence |
| 69 | Maker's Schedule, Manager's Schedule | https://www.paulgraham.com/makersschedule.html |
| 70 | Management Time: Who's Got the Monkey | https://hbr.org/1999/11/management-time-whos-got-the-monkey |
| 71 | Manager / Leader / Mentor | https://enginuity.substack.com/ |
| 72 | Managing Expectations | https://markasmithjr.substack.com/p/practical-to-powerful-great-expectations |
| 73 | Managing High Performers | https://blog.staysaasy.com/p/managing-high-performers |
| 74 | Managing Up | https://review.firstround.com/a-tactical-guide-to-managing-up-30-tips-from-the-smartest-people-we-know |
| 75 | Managing Urgency | https://oded.substack.com/p/note-to-future-self-beware-of-fake |
| 76 | Managing up - shit rolls downhill | https://www.leahtharin.com/p/the-skill-that-gets-you-fired-or |
| 77 | Managing up: 11 ways to get better feedback | https://newsletter.weskao.com/p/get-better-feedback |
| 78 | Micromanagement balance | https://shamun.dev/posts/micromanagement |
| 79 | Mistakes you shouldn't let your reports make | https://bjorg.bjornroche.com/management/mistakes-should-not-let-make/ |
| 80 | On Estimates - Shay Yallin Blog | https://www.shaiyallin.com/post/someestimates |
| 81 | On multi dimensional tradeoffs | https://lethain.com/multi-dimensional-tradeoffs/ |
| 82 | Onboarding for technical leadership roles | https://substack.com/app-link/post?publication_id=1002265&post_id=142445063 |
| 83 | One on One Meeting Format Ideas | https://marcgg.com/ |
| 84 | Organizing a Hackathon | https://newsletter.pragmaticengineer.com/p/hackathons |
| 85 | Performance management the rising tide | https://theengineeringmanager.substack.com/p/performance-management-the-rising |
| 86 | Performance of engineering teams | https://blog.malt.engineering/should-we-measure-the-performance-of-an-engineering-team-e461ccff1cd4 |
| 87 | Polarity Management | https://www.chaitime.chaitalinarla.com/p/equilibrium |
| 88 | Practices to reduce meetings | https://medium.com/illumination/back-to-back-meetings-create-an-illusion-of-productivity-why-the-best-leaders-keep-an-empty-adbb02abdc0f |
| 89 | Prioritization vs Filtering | https://betterprogramming.pub/you-will-always-have-more-problems-than-engineers-aafff94a4623 |
| 90 | Reframing technical debt | https://www.engineeringleadership.xyz/p/reframing-technical-debt |
| 91 | Retention techniques - Elena Verna | https://www.elenaverna.com/p/how-to-improve-your-voluntary-churn |
| 92 | Stop with the compliment sandwich | https://adamgrant.substack.com/p/stop-serving-the-compliment-sandwich |
| 93 | Team building - dream team workshop by Miro | https://miro.com/miroverse/dream-team-workshop/ |
| 94 | Ten Types of Software Engineering Waste | https://www.practicalengineering.management/p/ten-types-of-software-engineering |
| 95 | The 5 Questions to Unlock Poor Performers | https://mgmt.beehiiv.com/ |
| 96 | The 6 Mistakes You're Going to Make as a New Manager | https://terriblesoftware.org/2024/12/04/the-6-mistakes-youre-going-to-make-as-a-new-manager/ |
| 97 | The Management Skill Nobody Talks About - repair | https://terriblesoftware.org/2025/08/22/the-management-skill-nobody-talks-about/ |
| 98 | The Tarzan Method for career development | https://open.substack.com/pub/theengineeringmanager/p/the-tarzan-method |
| 99 | The lifecycles of engineering teams | https://betterprogramming.pub/10-ideas-from-the-best-book-on-engineering-management-c3caa706f77c |
| 100 | The origin of blameless post mortems | https://www.etsy.com/codeascraft/blameless-postmortems |
| 101 | The unspoken skill of finesse | https://open.substack.com/pub/weskao/p/the-unspoken-skill-of-finesse |
| 102 | Tying Engineering Metrics to Business Metrics | https://icchasethi.medium.com/tying-engineering-metrics-to-business-metrics-f4df7651e026 |
| 103 | What is good retention | https://www.lennysnewsletter.com/p/what-is-good-retention-issue-29 |
| 104 | What makes a good manager at Google | https://addyo.substack.com/p/effective-engineering-managers |
| 105 | Why Engineers Hate Their Managers | https://terriblesoftware.org/2025/06/24/why-engineers-hate-their-managers-and-what-to-do-about-it/ |
| 106 | Your manager wants you to manage him | https://mgmt.beehiiv.com/p/your-managers-dirty-little-secret-they-want-you-to-manage-them |

### Books

| # | Title | Author |
|---|---|---|
| 1 | The Everything Store | Brad Stone |
| 2 | Amp It Up: Leading for Hypergrowth | Frank Slootman |
| 3 | An Elegant Puzzle: Systems of Engineering Management | Will Larson |
| 4 | High Output Management | Andrew Grove |
| 5 | Atomic Habits | James Clear |
| 6 | Become an Effective Software Engineering Manager | James Stanier |
| 7 | Crossing the Chasm | Geoffrey Moore |
| 8 | Deep Work | Cal Newport |
| 9 | Empowered: Ordinary People, Extraordinary Products | Marty Cagan |
| 10 | Extreme Ownership | Jocko Willink & Leif Babin |
| 11 | From Worst to First | Gordon Bethune |
| 12 | Hit Refresh | Satya Nadella |
| 13 | How Big Things Get Done | Bent Flyvbjerg & Dan Gardner |
| 14 | Influence: The Psychology of Persuasion | Robert Cialdini |
| 15 | Intercom on Jobs to be Done | Intercom |
| 16 | It Doesn't Have to Be Crazy at Work | Jason Fried & David Heinemeier Hansson |
| 17 | Competing Against Luck | Clayton M. Christensen, Karen Dillon, Taddy Hall & David S. Duncan |
| 18 | Leading Snowflakes | Oren Ellenbogen |
| 19 | Mistakes Were Made (But Not by Me) | Carol Tavris & Elliot Aronson |
| 20 | Never Split the Difference | Chris Voss |
| 21 | No Rules Rules | Reed Hastings |
| 22 | Hackers & Painters | Paul Graham |
| 23 | Peopleware: Productive Projects and Teams | Tom DeMarco & Tim Lister |
| 24 | Radical Candor | Kim Scott |
| 25 | Setting the Table | Danny Meyer |
| 26 | The Five Dysfunctions of a Team | Patrick Lencioni |
| 27 | The Almanack of Naval Ravikant | Eric Jorgenson |
| 28 | The Art of Leadership: Small Things, Done Well | Michael Lopp |
| 29 | The Diary of a CEO: The 33 Laws of Business and Life | Steven Bartlett |
| 30 | The Dichotomy of Leadership | Jocko Willink & Leif Babin |
| 31 | The Goal | Eliyahu M. Goldratt |
| 32 | The Hard Thing About Hard Things | Ben Horowitz |
| 33 | The Making of a Manager | Julie Zhuo |
| 34 | The Mom Test | Rob Fitzpatrick |
| 35 | The Mythical Man-Month | Frederick P. Brooks Jr. |
| 36 | The Nvidia Way: Jensen Huang and the Making of a Tech Giant | Tae Kim |
| 37 | Turn the Ship Around! | L. David Marquet |
| 38 | Work Rules! | Laszlo Bock |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or improve skills.

Each `SKILL.md` should:

- Use valid YAML frontmatter
- Keep `name` equal to the directory name
- Keep `description` under 1024 characters
- Stay under 500 lines
- Read `em-context` before giving personalized advice
- Prefer concise, direct, manager-ready output
