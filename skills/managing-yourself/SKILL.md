---
name: managing-yourself
description: Helps EMs assess their own effectiveness, avoid common traps, navigate bad days, and handle recurring tensions in their own mindset and behavior. Use when the user says "I feel stuck," "am I doing this right," "personal development," "EM effectiveness," "blind spots," "bad days," "sanity check on my behavior," "the same problem keeps coming back," "made a mistake with someone," or "my team isn't motivated." Do NOT use when the issue is about the user's relationship with their own manager (use managing-up) or giving specific feedback to someone (use feedback).
metadata:
  version: 2.1.2
---

# Managing Yourself

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

If `.agents/em-context.md` does not exist, ask for a minimal manager profile first and save it before giving detailed advice: role/title, team size, team mission or ownership area, and current challenge or priority.

If a specific person is central to the conversation and `.agents/reports/[name].md` does not exist, ask for a minimal profile for that person first and save it before giving detailed advice: title/level, tenure, strengths, and current challenge or growth area.

If the conversation reveals durable new context later, update `.agents/em-context.md` or `.agents/reports/[name].md` automatically. Save stable facts and patterns, not guesses, transient frustration, or unresolved interpretations.
---

## Response Style

Keep the first answer concise and useful. Do not dump the whole framework unless the user asks for depth.

Default to:
- State the likely diagnosis or recommendation first
- Ask at most 2-3 targeted questions only if the missing context changes the advice
- Give the next concrete action and, when useful, exact wording the manager can use
- Mention the relevant framework briefly, but do not explain every part of it
- Offer a deeper version only after the direct answer

---

## How to Use This Skill
Identify the situation first:

- **Feeling stuck or wondering if you're doing the EM job right** → The 10 Ways EMs Get Stuck (start here)
- **Things keep going wrong and you feel like the victim** → The Drama Triangle
- **Having lots of bad management days** → Why Managers Have More Bad Days
- **Team seems unmotivated or output is low** → Clear the Path
- **Made a mistake with someone and need to recover** → Repair
- **The same problem keeps coming back no matter how you solve it** → Problems vs. Polarities
- **Your strength as an EM is becoming a failure mode** → read [`references/extended.md`](references/extended.md) — The Dichotomies
- **Feeling disconnected from the big picture / product** → read [`references/extended.md`](references/extended.md) — Balcony Awareness
- **Facing unexpected criticism, VP grilling, or a major outage** → read [`references/extended.md`](references/extended.md) — Staying Calm: The BAA Framework
- **Auditing how your time is split across growth / connection / impact** → read [`references/extended.md`](references/extended.md) — The EM Grid
- **Maintaining coding skills or staying hands-on** → read [`references/extended.md`](references/extended.md) — The Maker/Manager Mode
- **Getting feedback on management decisions before acting** → read [`references/extended.md`](references/extended.md) — Code-Reviewing Your Own Decisions
- **Writing your own performance review** → read [`references/extended.md`](references/extended.md) — Your Manager Delta
- **Diagnosing low engagement or bad team culture** → read [`references/extended.md`](references/extended.md) — The Inversion Model
- **Auditing your own time allocation** → read [`references/extended.md`](references/extended.md) — The LNO Framework
- **Something went wrong and you're figuring out what you missed** → read [`references/extended.md`](references/extended.md) — Extreme Ownership
- **Team is scared or anxious during a hard period** → read [`references/extended.md`](references/extended.md) — The Leader Absorbs Fear
- **Anything about your manager, managing up, or senior leadership** → use `managing-up` skill

---

## Default Response Shape

When helping an EM self-diagnose, be concrete and non-therapeutic:

1. **Pattern:** which trap, polarity, bad-day cause, or repair need is showing up.
2. **Cost:** how it affects the team, manager, peers, or the EM's own judgment.
3. **Reframe:** the more useful interpretation of the situation.
4. **Next action:** one behavior to try this week.
5. **Reflection question:** what to observe afterward.

If the EM sounds overwhelmed, reduce the advice to one next move rather than listing every framework.

---

## The 10 Ways EMs Get Stuck

Most experienced EMs are guilty of at least 5 of these.

### 1. Ignoring Destructive Behaviors
What you permit, you promote. The longer you ignore a behavior, the harder it is to address. The developer won't magically change on their own. Now is always the best time to have the conversation, no matter how much time has passed.

### 2. Trying to Please Everyone
The instinct to be liked leads to encouraging bad ideas, agreeing to unreasonable deadlines, and avoiding hard conversations. You'll have to learn to disappoint people and stand your ground.

### 3. Fighting Too Hard for Your Principles
Not every hill is worth fighting on. Ask yourself "why is this so important to me?" before going to war over something. Some principles are load-bearing; many aren't. (Example: fighting hard over standup attendance at the cost of team morale.)

### 4. Not Building Relationships Outside Your Team
Most EMs focus on two relationships: their manager and the PM. That's not enough. Your team's impact depends on other teams and customers — and that requires a supportive network. Have 1:1s with key people, and do what you can to help them.

### 5. Defining Your Role Too Narrowly
Every EM has a strength — technical, people, process — and the trap is falling into only doing that. Effective managers fill gaps. Constantly assess what's weakest on the team and invest there.

### 6. Forgetting Your Manager Is Human
It's easy to get frustrated when your manager puts you in bad situations or commits your team without asking. They almost certainly did it with the best of intentions. Give them room to make mistakes.

### 7. Neglecting Personal Development
You become so focused on the day-to-day that you forget to spend time on your own growth — leading to stagnation and burnout. Protect time for it.

### 8. Only Managing Down
Fighting for your team's ideas even when they don't connect to business goals. Even if you win a 3-month refactor nobody asked for, it'll cost you credibility in the long run.

### 9. Only Managing Up
Following your manager's agenda blindly and saying "management wants this" too many times. Say it too many times, and there will be no team left.

### 10. Never Managing Up
Your team's success and recognition depend on your relationship with your management chain. Excellent work goes unnoticed when it's never shared upward. Be the "Minister of Foreign Affairs" for your team.

(Traps #8–10 are explored further in the `managing-up` skill.)

---

## The Drama Triangle — and How to Exit It

When things go wrong, it's easy to fall into one of three roles:

- **Victim** — feels powerless, believes things are happening *to* them. Focuses on who/what to blame.
- **Villain** — what the victim points at as the cause of all problems.
- **Hero** — provides temporary relief (a manager who "handles it," or mindless scrolling that lets you forget).

Three EM examples of falling in:
1. PM publicly overpromises without consulting you → you're the Victim, PM is the Villain, you want your manager to be the Hero
2. CEO tells your manager your team isn't working hard enough → you're the Victim, CEO is the Villain, your spouse validating your frustration is the Hero
3. Underperforming developer who hasn't improved → you're the Victim, previous manager is the Villain, complaining to a peer at lunch is the Hero

In all three cases, the root cause never gets fixed.

**How to exit:**

1. **Recognize you're in a victim mindset.** Notice not just who the villain is, but also who you're turning to as a hero to relieve the frustration.

2. **Try very hard to see their side.** When the PM overpromised: instead of sending the angry Slack message, call them. Ask what made them do it. Often the "villain" is under enormous pressure you weren't aware of.

3. **Focus on the outcome you want, not the problem.** The more you focus on the problem, the bigger it becomes. Ask: what outcome do I actually want here? Then work toward it.

The healthier model: **Creator, Challenger, Coach**. A Creator focuses on what they *do* want, not what they don't want. Creators still face and solve problems — but in the course of creating outcomes, not in the course of stewing in frustration.

---

## Why Managers Have More Bad Days

One thing nobody warns you about: management has a different emotional profile than individual contribution.

As a developer, bad days are bounded. You write code, you fix bugs, you ship things. Even hard days end with something tangible. If things get really bad, you put on headphones and disappear into the work.

As a manager, that escape doesn't exist. Your mood and your work are the same thing. Three reasons managers have more bad days than they expect:

1. **Guilt.** You can't be everywhere. Someone needs more of you than you can give today. This guilt is constant and low-level. It doesn't go away — you learn to work with it.

2. **More interactions means more variance.** As a manager, your day is mostly other people. More interactions means more opportunities for misunderstanding, conflict, a conversation that didn't land, feedback that was received badly.

3. **No coding escape.** When coding was your job, you could always retreat to a hard technical problem and feel competent. Management doesn't have that. The work is ambiguous, slow, and relational.

**What to do when you're having a bad management day:**

Two real options — pick one, don't half-do both:
- **Take the sick day.** If you're depleted and not able to show up well — don't. The team is better off without a depleted manager than with one going through the motions.
- **Go all-in.** If you can't take the day off, fully commit to being present. The worst outcome is showing up half-present — checked out, distracted, irritable.

**3 red flags that something is wrong (not just a bad day):**
1. You find yourself avoiding a specific person or conversation for more than a week.
2. You feel resentful toward your team or your manager — not frustrated, but genuinely resentful.
3. You've stopped being curious about the work and are just executing.

**5 root causes when bad days become a pattern:**
1. A hard relationship you're not addressing (see #1 of the 10 traps above)
2. You don't feel you have enough autonomy — someone is micromanaging you
3. The work doesn't connect to something you care about
4. You're not growing — doing the same problems in a loop
5. You're carrying too much alone and not delegating

None of these fix themselves. Name the one that fits and address it directly.

---

## Clear the Path

The most common management mistake when a team is struggling: assuming they need more motivation.

Most engineers don't wake up wanting to do mediocre work. When output is low, the question isn't "how do I motivate them?" — it's "what's in their way?"

**The obstacle audit:** Ask everyone: *"What prevents you from doing the best work of your career here?"* Classify each obstacle (process, technical, resource, clarity). Fix the top three immediately.

Common obstacles that go unnoticed by managers:
- Contradictory directives from different stakeholders
- Technical debt that turns simple tasks into nightmares
- Approval processes that add days to tasks that take hours
- Incomplete requirements that force constant rework

When you remove a real obstacle, throughput improves without any "motivation" effort. The manager's job is closer to bulldozer than cheerleader.

---

## Repair

You will make management mistakes. You'll give feedback that crushes confidence. You'll commit the team to something without consulting them. You'll lose your temper. You'll drop a promise.

The question isn't whether these happen — it's what you do after.

The managers who lose their best people aren't necessarily the ones who made the most mistakes. They're the ones who never acknowledged them. Who doubled down when wrong. Who let ego prevent them from saying: *"I put you in an impossible position. I should have consulted you first. Here's how I'll do it differently."*

That kind of acknowledgment — specific, honest, without over-apologizing — builds more trust than never making the mistake would have. It signals that you're safe to work with.

**How to repair well:**
1. Name what happened specifically. Don't generalize.
2. Take responsibility. Don't explain it away.
3. Say what you'll do differently. Keep it concrete.
4. Then drop it. Extended guilt-tripping helps no one.

---

## Problems vs. Polarities

Some management challenges keep coming back no matter how well you solve them. That's often because they're not problems — they're **polarities**.

A problem can be solved once and stays solved. A polarity is a tension between two interdependent opposites that must be managed continuously. Neither pole is the "right answer."

Examples: Speed vs. Quality. Autonomy vs. Alignment. Short-term delivery vs. Long-term architecture health. Individual focus time vs. Team collaboration.

The mistake: treating a polarity like a problem. You "solve" quality by clearing the bug backlog — and a year later the backlog is back. You "solved" the wrong thing. The real work is managing the ongoing tension between speed and quality.

**How to manage a polarity:**
- Name both poles. Resist the temptation to pick one as "correct."
- Identify the upsides and downsides of each pole.
- Recognize when you're over-indexed on one side — that's when the pressure to swing to the other builds.
- Build mechanisms that let you consciously shift between poles rather than lurching between them.

When you catch yourself wondering why a recurring problem keeps coming back, ask: is this actually a polarity I'm trying to solve?

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic — read [`references/sources.md`](references/sources.md) for the full list of source articles (with links) and books.

---

## Related Skills

- `managing-up` — Managing your relationship with your manager, communicating up, handling disagreements with leadership
- `delegation` — The bottleneck trap maps directly to #5 and the dichotomies
- `feedback` — Ignoring destructive behaviors (#1) is a feedback failure
- `feedback` — Getting honest feedback from your team; blind spots are central to the 10 ways EMs get stuck
- `influence` — Managing up and across requires the persuasion skills in `influence`
