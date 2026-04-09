---
name: written-communication
description: When the user wants to write a message, email, or announcement to their team or stakeholders and wants it to land well. Also use when the user says "how do I write this," "draft a message," "write an announcement," "communicate this change," "message for my team," "how to word this," or "write an update."
metadata:
  version: 1.0.0
---

# Written Communication

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it. If a person is mentioned, check `.agents/reports/[name].md`.

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

## Related Skills

- `managing-yourself` — Finesse in how you communicate with senior leadership
- `feedback` — Specific principles for written and verbal feedback
- `working-with-pm` — Stakeholder communication is a core part of the PM-EM relationship

