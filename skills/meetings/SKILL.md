---
name: meetings
description: Covers the full meeting lifecycle for engineering managers — produces guidance on whether to schedule a meeting, how to run it well, how to protect team focus time, how to kill recurring waste, and how to evaluate a past meeting from a transcript or description. Use when the user says "too many meetings," "meetings are a waste of time," "how do I run this meeting," "meeting agenda," "meeting culture," "nobody comes prepared," "meetings go nowhere," "how do I decline meetings," "distractions," "focus time," "engineers can't focus," "context switching," "protect engineering time," "review this meeting," or "transcript."
metadata:
  version: 1.1.0
---

# Meetings

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
- **Wondering if something should be a meeting** → Is This a Meeting?
- **Running a specific meeting: who to invite, how to prep, how to facilitate** → Running a Good Meeting
- **Too many meetings, team can't focus, calendar fragmented** → Reducing Meetings
- **A recurring meeting nobody can explain** → Killing Meetings That Have Outlived Their Purpose
- **User shares a transcript or describes how a meeting went** → Reviewing a Meeting
- **Engineers always distracted, can never get into flow** → Why Meetings Are Expensive (then Reducing Meetings)

---

## Default Response Shape

When helping with meetings, produce a decision and operating plan:

1. **Meeting decision:** keep, kill, shorten, async, split, or redesign.
2. **Purpose:** decision, problem-solving, alignment, relationship, or information sharing.
3. **Agenda / async alternative:** concrete structure or written replacement.
4. **Participants:** who must attend and who can be informed afterward.
5. **Follow-up mechanism:** owner, decisions, notes, and review date.

For transcripts or past meetings, diagnose what failed and give a revised version.

---

## Why Meetings Are Expensive

Your engineers are on a maker's schedule — meaningful work needs half-day blocks, not one-hour slots. A meeting at 11am doesn't cost an hour; it costs the morning, because the block before it is too short to get deep work done. When you schedule a meeting, it's routine for you and expensive for them.

Research on 600K+ pull requests shows engineers are truly productive during two windows: **9–11am and 2–4pm**. Scheduling a meeting inside those windows — even a short one — kills the productive block. Put meetings at 8:30, 11:30, 1:00, or 4:00+. The difference is not marginal.

---

## Is This a Meeting?

Before scheduling, identify what type of meeting this is:

- **Problem-solving** — the group needs to work through a problem together
- **Decision-making** — a decision needs to be made and requires the right people present
- **Getting buy-in** — you've already decided; you need alignment and commitment
- **Information sharing** — you're communicating something

Information sharing almost never needs a meeting. Record a Loom, send a doc, post in Slack. Reserve synchronous time for things that require real back-and-forth.

**Does the decision-maker need to be there?** If they can't attend, reschedule. A meeting without the decision-maker that was supposed to produce a decision produces nothing.

**More than 7 people in a decision meeting is almost always too many.** Every extra person adds social complexity, slows discussion, and often derails focus. People who need to be "in the loop" can get a summary.

---

## Running a Good Meeting

**Prepare.**
Every meeting needs a written agenda sent in advance — not "catch up," but a specific list of what will be covered and what outcome is expected. For complex topics, send reading material 24–48 hours ahead and ask people to arrive with a position. Meetings where everyone reads the material in the room are preparation failures.

**Run it.**
Start on time — always. Assign a facilitator and a note-taker. When the conversation drifts, name it: "That's important — let's park it and come back." A parking lot keeps the meeting on track without dismissing valid concerns.

Drive to decisions, not discussions. A meeting that ends with "we should think more about this" has failed. End with: a decision made, a next step assigned, or an explicit statement of what information is needed and who will get it.

If you reach the goal in 20 of 60 minutes, end it.

**Follow through.**
Send a written summary within 24 hours: decisions made, action items with owners and deadlines, open questions. Even if the meeting felt obvious, people remember it differently. The written record is the truth.

---

## Reducing Meetings

**Your calendar is the model for your team's calendar.** If you're in back-to-back meetings all day, you're signaling that's normal.

- **Protect proactive time.** Aim for at least 30% of your work week in uninterrupted blocks. When it drops below 20%, you're in reactive mode.
- **Batch meetings.** Cluster them into fixed windows — mornings, or specific days — to preserve deep work blocks.
- **Shorten by default.** Use 25 and 50 minutes instead of 30 and 60. The shorter slot forces efficiency; meetings expand to fill their scheduled time.
- **Delegate attendance.** Some meetings don't need you personally — a report can go and brief you afterward.
- **You're allowed to decline.** If you're not a decision-maker and not a required input-provider, decline and ask to be looped in via summary.

---

## Killing Meetings That Have Outlived Their Purpose

Every team has recurring meetings nobody can explain. A standup that adds no value. A sync that's been on the calendar for two years.

Ask regularly: **"Why are we still doing this?"** If the answer is "because we always have" — that's inertia, not a reason. Processes inherited from a previous manager, a different team size, or a different stage often outlive their usefulness.

A simple habit: once a quarter, list your team's regular rituals and ask for each: what problem does this solve? If nobody can answer, try removing it for one month. Most people will feel relieved.

---

## Reviewing a Meeting

When the user shares a transcript or describes how a meeting went, evaluate it across five dimensions:

**1. Purpose** — Was the goal clear before the meeting started? Was it achieved? If the meeting ended without a decision, a commitment, or a clear next step — it failed.

**2. Attendance** — Were the right people there? Was the decision-maker present? Were there people in the room who only needed a summary?

**3. Preparation** — Was there an agenda? Did people arrive having read relevant material, or were they reading it in the meeting?

**4. Facilitation** — Did the conversation stay on track? Were tangents named and parked? Did one person dominate? Did quieter people get airtime?

**5. Follow-through** — Were decisions recorded? Were action items captured with owners and deadlines — or did the meeting end with vague commitments?

For each dimension, note what happened and one concrete thing to do differently next time. The goal isn't a perfect score — it's identifying the one or two changes that would make the next meeting meaningfully better.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md) for the full list of source articles (with links) and books.

---

## Related Skills

- `managing-urgency` — Urgency culture is a common driver of unnecessary meetings and chronic interruptions
- `delegation` — EMs who don't delegate become a common source of interruptions themselves
- `team-health` — Meeting cadence and quality show up in team health and engagement
- `1on1s` — 1:1s are a specific meeting type with their own format
