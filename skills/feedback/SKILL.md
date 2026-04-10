---
name: feedback
description: Structures and scripts feedback conversations — positive, constructive, or behavioral — for a specific person or situation. Produces SBI-framed feedback statements, opening lines for hard conversations, scripts for real situations, and ways to handle resistance. Use when the user wants to give someone feedback, says "how do I tell someone," "this person is struggling," "address a behavior," "hard conversation," "someone is underperforming," "praise this person," "write feedback for," "I need to say something," or "difficult conversation." Do NOT use for formal annual or performance reviews (use performance-reviews) or sensitive HR situations that go beyond feedback (use difficult-situations).
metadata:
  version: 2.0.0
---

# Feedback

## Before Starting

Check for EM context first:
1. Read `.agents/em-context.md` if it exists
2. If a person is mentioned, look for `.agents/reports/[name].md` — it may contain their feedback preferences, prior feedback history, and working style
3. Use that context — only ask for information not already covered

---

## How to Use This Skill

Identify what the user needs before diving into frameworks:

- **Giving positive feedback** → Go to Precision: No Weasel Words — it applies equally to praise
- **Constructive feedback — know the issue but not how to open** → Opening a Critical Feedback Conversation, then Instead of the Compliment Sandwich
- **Expecting resistance or pushback** → Behavior Change Stages first
- **Something happened recently and the user wants to address it now** → In-the-Moment Feedback (don't save it for the 1:1)
- **Building feedback culture across the whole team** → Speed Feedback
- **Writing feedback for a review or document** → Precision section first; then ask for the specific events to document
- **Building a lightweight weekly accountability loop with reports** → read [`references/extended.md`](references/extended.md) — Weekly Called Shots

**If the user hasn't given you a specific event yet, ask for it.** Vague feedback inputs always produce vague feedback outputs.

---

## Precision: No Weasel Words

The most common feedback mistake is vagueness. "You're too blunt in meetings" or "your communication needs improvement" — these feel like feedback but give the person nothing to act on. They're also easy to dismiss: "I don't think I'm blunt."

Specific feedback is factual and indisputable.

**Weak:** "You're too blunt in meetings."
**Specific:** "In the meeting with Christopher, you cut him off when he started suggesting the React-based solution. We missed an opportunity to check more approaches. I also noticed that Christopher stopped contributing to other meetings after that."

The specific version names the event, the person affected, and the downstream consequence. The other person can't dispute the facts — they can only engage with what happened.

Apply this same standard to positive feedback. "You did a great job" is forgettable. "The way you handled the incident on Thursday — staying calm, communicating clearly to stakeholders while the team debugged — that's exactly what we need in situations like that" is memorable and repeatable.

**Before giving feedback, do the homework.** Identify the specific event, the specific behavior, and the specific impact. Vague feedback isn't kind — it's just unprepared.

---

## Public Praise Isn't Universal

"Praise in public, criticize in private" is standard management advice. The first half isn't always true.

Some engineers genuinely don't want to be called out in front of the team. They prefer private acknowledgment. Surprising them with public praise — a Slack shoutout, a nomination for a recognition program — can create awkwardness instead of motivation.

Ask before you assume. A simple "How do you prefer to be recognized when you do great work?" in a 1:1 is enough.

---

## Translating Social Cues

Not everyone can read a room. If you're good at this, part of your job is translating for those who aren't.

When a team member says something that lands badly and doesn't notice — upset someone, came across as dismissive, answered too abruptly in a meeting — tell them privately. Not as criticism, but as information: "I think that landed differently than you intended. Here's what I noticed." They often don't know. Telling them is the most useful thing you can do.

---

## Behavior Change Stages

When addressing a performance or behavior problem, people typically move through three stages before accepting feedback:

1. **Ignore** — they don't acknowledge the problem exists
2. **Deny** — they actively push back ("That's not true" / "You're wrong")
3. **Blame others** — they redirect responsibility elsewhere

In a single 1:1, you can often move someone through all three stages. The right response at each stage is different:
- At **Ignore/Deny**: bring specific facts. Don't argue — present evidence calmly.
- At **Blame**: don't let them escape into it. Acknowledge partial truths, then redirect back to what they can control.

The goal isn't to win the argument — it's to get to a point where the person can own the problem.

---

## Instead of the Compliment Sandwich

Starting with a compliment and ending with one — sandwiching criticism in between — backfires in two ways: the opening compliment feels insincere (they're braced for the hit), and the closing compliment can bury the critique due to recency effects.

Four steps that work better (from Adam Grant, based on research):

1. **Explain why you're giving the feedback.** Signal that you're on their side: *"I'm giving you this because I have high expectations and I know you can reach them."* It's harder to reject a hard truth from someone who believes in you.
2. **Take yourself off a pedestal.** Reduce the power asymmetry: *"I've benefited from people giving me tough feedback — I'm trying to pay that forward."* It makes the feedback less threatening.
3. **Give the criticism directly.** No burying. Say the specific thing, the specific event, the specific impact.
4. **Invite them to respond.** Ask what they think. Let them engage, not just receive.

---

## Opening a Critical Feedback Conversation

From *The Making of a Manager* (Zhuo): the moments right before a difficult feedback conversation feel uncomfortable — for both people. That discomfort is a good sign. It means the conversation is real.

Comfortable feedback conversations often aren't achieving anything. If neither person feels any friction, the feedback is probably not specific enough, not honest enough, or not about anything that actually matters.

**What to say at the start:**

The opening doesn't need to be elaborate. What it needs to signal is: you're saying this because you care about the person, not because you're judging them.

*"I want to share something that's hard for me to say, and I'm saying it because I think it matters for where you're going."*

Or simply naming what's happening: *"I have some direct feedback for you. It might feel uncomfortable, and I want you to know it's coming from a place of caring about your success here."*

**Then say the thing.** Don't circle around it. The opening sets the tone; the feedback itself has to be clear, specific, and direct. Softening after a strong opener defeats the purpose.

**Silence is data.** If someone goes quiet after critical feedback, don't rush to fill the space. Let them process. The silence often means they're actually taking it in — which is exactly what you wanted.

---

## In-the-Moment Feedback

Waiting for the next 1:1 to give feedback costs most of its effectiveness. The closer feedback is to the event, the more likely the person can connect it to what they actually did.

**Standup feedback** — feedback given in the flow of work, at or near the moment it's relevant. Not a big formal conversation; a direct, brief comment. Example: a developer repeatedly delays code reviews for teammates. Raising this in the standup (or right after, in the hallway) is far more effective than bringing it up three days later in a 1:1 where the person may barely remember the specific instance.

**The volume button.** In-the-moment feedback doesn't need to be loud or intense. Think of it as tuning down the tone and volume — not the substance. Keep the content clear and direct; deliver it calmly and without drama. Brief, respectful, and close to the event beats formal, thorough, and a week later.

**Why timing matters.** Humans (like any animal) struggle to connect feedback to action when the gap is too long. Waiting days doesn't just reduce effectiveness — it trains the team to expect feedback only in formal settings, which reduces psychological safety in day-to-day work. Google's research on team effectiveness identified psychological safety as the #1 factor — and the team leader is the primary influence on it.

---

## Speed Feedback: Building a Feedback Habit on the Team

Teams that only give feedback in formal reviews are too slow. Speed feedback is a structured activity for building a team-wide feedback habit.

**How it works:** Team members pair up in a private space. Each person gets a fixed amount of time to give feedback to the other, then they switch. Pairs rotate until everyone has spoken with everyone else.

**The goal isn't depth — it's normalization.** Early rounds focus on appreciation and celebrating contributions. As the team gets comfortable, they naturally start including improvement suggestions. The activity makes feedback part of the team's rhythm rather than a once-a-year event.

Works best with 5–8 people. Can be run remotely with breakout rooms and a shared board. Does not replace regular 1:1 feedback — it supplements it.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md) for the full list of source articles (with links), books, and course material.

---

## Related Skills

- `1on1s` — Delivering feedback in a 1:1 context
- `performance-reviews` — Formal written feedback at review time
