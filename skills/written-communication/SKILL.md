---
name: written-communication
description: Helps engineering managers write messages, announcements, and stakeholder updates that land well — produces a 3-Step Writing Framework (Prepare / Write Simply / Run a Garbage Collector), the Async Re-Explanation Trap (calling out missed messages), and the Compression/Decompression model for diagnosing why messages are misunderstood. Use when the user says "draft a message," "write an announcement," "communicate this change," "how do I word this," "message for my team," "write an update," or "how do I communicate X." Do NOT use for verbal feedback or difficult conversations (use `feedback` or `difficult-situations`).
metadata:
  version: 2.1.2
---

# Written Communication

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it. If a person is mentioned, check `.agents/reports/[name].md`.



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
- **Need to write or draft a message** → The 3-Step Framework
- **High-stakes announcement or sensitive policy change** → When Stakes Are High
- **Writing for different audiences (engineers vs. stakeholders vs. leadership)** → The 3-Step Framework → Step 1: Prepare
- **Someone is calling out missed messages in Slack ("as I already said…")** → The Async Re-Explanation Trap
- **Message wasn't understood the way you intended** → The Compression/Decompression Model

---

## Default Response Shape

When helping with written communication, draft the actual message:

1. **Intent:** what the message must accomplish.
2. **Audience calibration:** what this audience knows, fears, and needs.
3. **Draft:** concise, direct, and ready to send.
4. **Why it works:** short notes on structure or wording.
5. **Risk check:** what could be misread and how to reduce it.

If the user asks for wording, put the draft before the explanation.

---

## The 3-Step Framework

Writing code for machines is predictable — you know the language, version, and libraries. Writing for people isn't: the same message lands completely differently depending on who reads it. This framework reduces that gap.

### Step 1: Prepare

Before writing a single word, answer three questions:

**Why are you writing?**
What triggered this message? Make sure the reason is in the message if it matters. Also: if you're writing while frustrated, stop. The goal of most messages isn't to win an argument — it's to get a result. Understanding your own intent often causes you to completely rewrite the message.

**What do you want to achieve?**
Be specific. "I want my team to follow the new deployment rule" is a goal. "I want to communicate about deployments" is not. If you can't state the goal, the message won't have one.

**Who is your audience?**
Different groups need different vocabulary and depth:
- *Engineers* — technical detail appropriate, assume domain context
- *Business stakeholders* — explain what matters to them, avoid jargon
- *Support team* — they want all scenarios and edge cases
- *Fellow managers* — share most context, be concise

The more you know about your audience, the more you can anticipate misunderstanding before it happens.

---

### Step 2: Write Simply

Write the way you speak. Simple words carry the same meaning as complex ones, with less cognitive load on the reader. Complex sentences aren't a sign of intelligence — they're a sign that the writing wasn't edited.

Specific rules that help:
- **Use active voice.** "I pushed to production" instead of "The production environment was updated."
- **Put the most important thing first.** Don't bury the headline.
- **Avoid walls of text.** Use paragraph breaks, 3–4 sentences each.
- **Structure for skimming.** If it's long, use headers or bullets.

---

### Step 3: Run a Garbage Collector

Before sending: remove every word that doesn't add information. Shorter messages get read. Longer messages get skimmed, misread, or ignored.

Example:
> "We are changing the current rule for merging our pull requests: you now need at least one approval to merge your changes, instead of two approvals — we trust you, and we want to move our things a bit faster."

After the garbage collector:
> "We are changing the rule for merging pull requests: you need one approval, instead of two — we trust you, and we want to move faster."

Same message. Less friction.

---

## When Stakes Are High

For messages with significant consequences — a policy change, a team restructure, a difficult announcement — ask someone from your target audience to read it before you send. You'll catch misunderstandings before they reach everyone.

Don't aim for perfection. A clear, timely message is better than a perfect delayed one.

---

## The Async Re-Explanation Trap

The most damaging Slack pattern is not bad grammar or long messages — it is calling out when someone missed a prior message: "as I already said," "I clearly wrote above," "I explained this last week."

The recipient feels humiliated. Repeat exposure destroys working relationships. The root cause is a false assumption: that because you wrote something clearly, the other person read and processed it the same way.

A corrective mental model: assume the other person has ten times as many active threads as you do. This reframes their miss as expected, not negligent — and produces two improvements: you write more concise, context-complete messages upfront, and you respond to misses with patience rather than public correction.

If a pattern of missed messages becomes a systemic problem, address it directly and privately, never in-thread.

---

## The Compression/Decompression Model

All communication is lossy. The speaker compresses rich internal experience or technical context into transmittable language. The listener decompresses it through their own lens. The received message is never identical to the sent one.

Two failure modes follow:
- **Over-compression:** too little context; the recipient fills gaps wrong
- **Over-explanation:** past a clarity peak, adding more detail actually reduces understanding by introducing noise

Compression skill means finding the minimum set of words that reliably produces an "aha" moment in the specific listener — not the most complete explanation, but the most efficient one for that audience. This applies to feedback, technical proposals, and stakeholder updates.

Decompression skill means actively working to receive what was actually meant, not what you expected to hear. The more confident you feel you understood, the more likely you are wrong.

A calibration tool: after delivering a message, ask the other person to reflect back what they heard. The gap between your intent and their summary is your compression error. Technical managers are often weakest here — precision in code does not transfer to precision in communication.

---

## Dive Deeper

If the user asks where a framework came from or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md).

---

## Related Skills

- `feedback` — Specific principles for written and verbal feedback delivery
- `managing-yourself` — Communication finesse with senior leadership
- `working-with-pm` — Stakeholder communication is central to the PM–EM relationship
- `influence` — Written communication as a tool for building organizational influence
