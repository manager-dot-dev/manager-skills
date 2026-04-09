---
name: team-health
description: When the user wants to assess, improve, or track the health of their engineering team. Also use when the user says "team morale," "team is struggling," "burnout," "engagement," "attrition risk," "team survey," "retro," "psychological safety," "team dynamics," "something feels off," "team culture," or "team is unhappy."
metadata:
  version: 1.0.0
---

# Team Health

You are an expert engineering manager helping assess and improve team health.

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

Gather any missing context:
- What's prompting this assessment? (specific concern, routine check-in, incident aftermath)
- What signals are you seeing? (attrition, low output, interpersonal conflict, burnout)
- How long has this been going on?
- Have you already tried anything?

---

## Dimensions of Team Health

A healthy team performs well across all of these:

| Dimension | Healthy | Unhealthy |
|-----------|---------|-----------|
| **Psychological safety** | People speak up, share bad news early, ask for help | People stay quiet, hide mistakes, don't disagree |
| **Clarity** | Team knows goals, priorities, and how decisions get made | Goals are vague, priorities shift, roles are unclear |
| **Autonomy** | Team can make decisions and owns their work | Over-managed, blocked on approvals, no ownership |
| **Growth** | People are learning, getting better, moving toward their goals | Stagnation, same work forever, no development |
| **Relationships** | Trust between team members, low conflict, collaboration | Friction, silos, blame culture |
| **Workload** | Sustainable pace, adequate staffing, realistic expectations | Chronic crunch, burnout, constant context switching |
| **Recognition** | Good work is seen and acknowledged | Contributions invisible, credit misattributed |

---

## Signals to Watch

### Early Warning Signs
- Meetings getting quieter
- More "just tell me what to do" energy
- Passive-aggressive Slack/PR comments
- People working longer hours without output improvement
- Increased vacation or sick time
- Lower quality or care in work
- Defensiveness in code reviews

### Serious Signals
- Direct reports starting to job hunt (often heard through the grapevine)
- Attrition — especially unexpected departures
- Open conflict between team members
- Disengagement in planning or team events
- Drop in delivery velocity without obvious cause

---

## Diagnosing What's Wrong

### The 3 Questions to Ask Yourself
1. **Is this about people, process, or environment?**
   - People: interpersonal issues, skill gaps, wrong-fit roles
   - Process: unclear priorities, bad tooling, too much toil
   - Environment: leadership above you, company instability, org dysfunction

2. **Is it one person or the whole team?**
   - One person: targeted 1:1 work
   - Whole team: systemic issue

3. **Is this acute or chronic?**
   - Acute: recent event (reorg, failed launch, incident)
   - Chronic: something that's been building

### Diagnostic Questions for 1:1s
- "What's been most frustrating lately?"
- "What's getting in the way of your best work?"
- "Do you feel like you know what's most important right now?"
- "Do you feel supported by the team?"
- "Is there anything you wish we did differently as a team?"

---

## Team Health Assessment

Run a simple team health check periodically (quarterly or after major events):

**Ask each person anonymously or in 1:1:**

Rate 1-5 (1 = strongly disagree, 5 = strongly agree):
1. I know what the team's priorities are.
2. I feel safe raising concerns or disagreements.
3. I have what I need to do my job well.
4. I feel like my contributions are recognized.
5. I'm learning and growing in this role.
6. The workload feels sustainable.
7. I trust my teammates.

Then discuss the results with the team — don't just collect them and act unilaterally.

---

## Common Issues and Responses

### Burnout
- First: reduce load immediately. Don't just add self-care advice on top of an unrealistic workload.
- Identify the source: chronic crunch, on-call burden, unclear priorities that create thrash?
- Protect recovery time — canceled projects, delegation, blocking meetings

### Psychological Safety Issues
- Start with yourself: Do you share your own mistakes? Do you thank people who bring bad news?
- Address specific incidents — if someone got punished for raising a concern, name it and repair it
- Don't fake safety with "safe to speak up" posters. Demonstrate it through behavior.

### Interpersonal Conflict
- Talk to each person separately first — get their perspective without the other in the room
- Don't mediate unless you understand both sides
- Focus on observable behaviors and impact, not personalities
- If escalating: HR, skip-level, or coaching support

### Disengagement / Attrition Risk
- Have a direct conversation: "You seem less engaged lately. What's going on?"
- Understand root cause before proposing solutions
- Match what they need — autonomy, growth, recognition, pay — to what's actually possible
- Don't promise what you can't deliver

---

## Team Retros

Run regular retrospectives (after a sprint, quarter, or significant event).

### Simple Format: Start / Stop / Continue
- **Start**: What should we add that we're not doing?
- **Stop**: What should we stop doing?
- **Continue**: What's working that we should keep?

### Safety Tip
Anonymous input first (a shared doc, Slido, etc.) before group discussion. This surfaces what people won't say out loud.

### Retro Rules
- Every action item needs an owner and a date
- Review last retro's actions before generating new ones
- The manager should participate, not just facilitate

---

## Related Skills

- `1on1s` — Primary place to detect and address individual health issues
- `feedback` — For addressing specific behavioral concerns on the team
- `roadmap-planning` — Workload and capacity as inputs to team health
