---
name: retaining-developers
description: Helps engineering managers prevent and respond to engineer attrition by diagnosing retention risk, choosing the right intervention, and preparing retention conversations. Use when the user says "developer quit," "attrition," "someone is disengaged," "how do I retain," "engineer is leaving," "developer unhappy," "keeping the team," "someone seems checked out," "engineer received another offer," "retention risk," or "my best engineer may leave." Produces a five-state diagnostic, action plan, conversation script, compensation/equity guidance, zero-budget recognition ideas, and warning signs. Do NOT use when the issue is day-to-day motivation only; use engineer-motivation.
metadata:
  version: 2.1.2
---

# Retaining Developers

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it. If a specific person is mentioned, check `.agents/reports/[name].md`.



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
- **Engineer seems disengaged or at risk** -> diagnose with The 5 States
- **Compensation or raise conversation** -> start with Unappreciated -> Valued
- **Equity or options conversation at hire, refresh, or departure** -> use Stock Options and Equity Conversations
- **Want to recognize someone but have no budget** -> use Zero-Budget Recognition
- **Worried someone might be leaving but has not said anything** -> use 5 Warning Signs of a Disengaging Engineer
- **Engineer already has another offer** -> use When Someone Has Another Offer

---

## Default Response Shape

When the user asks for help with retention, produce a practical manager response:

1. **Risk read:** low / medium / high, with evidence from the prompt.
2. **Likely state:** unappreciated, lonely, bored, stuck, apathetic, or mixed.
3. **What to verify in the next 1:1:** 3-5 questions that are direct but not interrogating.
4. **Action plan:** what to do this week, this month, and structurally.
5. **Conversation script:** concrete wording the manager can use.
6. **What not to do:** common overreactions that will make the situation worse.

If someone has already resigned or has another offer, do not pretend normal retention tactics are enough. Shift to: understand the reason, decide if there is a credible counter, treat them respectfully, and protect the relationship.

---

## Retention Risk Diagnostic

Use this before choosing an intervention:

- **Signal strength:** Is this one weak signal, a pattern over weeks, or a direct statement that they may leave?
- **State:** Which of the five states best explains the behavior?
- **Specificity:** Can the manager name the exact moment, project, decision, or pattern that caused the shift?
- **Agency:** Is there something the manager can actually change, or is this outside the manager's control?
- **Time horizon:** Is the risk immediate, emerging, or long-term?
- **Trust level:** Will the engineer believe the manager is acting because they care, or only because they are afraid of losing them?

The last question matters. Retention attempts that appear only after someone disengages can feel transactional. Acknowledge that directly when needed.

---

## The 5 States

When a developer quits, it is often because they feel one of these five things. Use the inverse to diagnose and act.

| What they feel | What they need |
|----------------|---------------|
| Unappreciated | To feel valued |
| Lonely | To feel connected |
| Bored | To feel challenged |
| Stuck | To feel like they are growing |
| Apathetic | To feel passionate about the work |

---

## 1. Unappreciated -> Valued

**Initial salary is critical.** The first salary you offer sets an anchor that is hard to correct later. Underpaying at hire means you will always be playing catch-up. Raises feel like corrections, not rewards, and the gap in perceived appreciation accumulates.

**Raise salary before they ask.** When a developer has to ask for a raise, the damage is already done. It signals that you were not paying attention or were not advocating for them. Be proactive. Also: do not deny raises because the engineer earns more than you. That is not a competition.

**Do not steal the thunder.** When something good happens, like a promotion, milestone, or successful launch, let the engineer announce it. Good news should come from them. If you announce their achievements for them, you take the moment; if they announce it themselves, you amplify it.

**Just tell them.** Many managers recognize good work internally and assume the engineer knows. They often do not. Say it directly in a 1:1: "I wanted to tell you: the way you handled X was exactly what I needed. That made a real difference."

**Recognition:** Give them the stage. Let them write the Slack announcement for features they shipped, tag them publicly, and push for your people to get company recognition. Route praise through its source: if a VP is excited, ask them to tell the team directly.

---

## 2. Lonely -> Connected

You cannot force people to connect, but you can create opportunities: team meetings, focus days outside the office, activities during working hours, and shared work that creates real memories.

Be honest in interviews about what your team culture actually looks like. If your team is mostly married with kids and nobody hangs out after work, say so. Do not let someone join expecting something that is not there.

---

## 3. Bored -> Challenged

The best lever is to delegate interesting tasks: writing technical designs, mentoring a new engineer, leading a cross-team effort, or owning a project area you currently hold.

Ask directly: "Do you feel challenged? What's missing from your work today?" Managers often assume they know what developers want instead of having the conversation.

---

## 4. Stuck -> Growing

Even challenged developers can feel stuck if they cannot see a path forward. Career planning is your job.

Work through it together:

- What are the requirements for the next level?
- How far are they from it, and why? Be fully honest.
- What tasks do they need to take on to get there?
- What evidence will promotion decision-makers need to see?

If they want a management path and there is no open slot, make them your second-in-command where appropriate and let them experience parts of the work. Help them prepare. Never promise a timeline you do not control.

---

## 5. Apathetic -> Passionate

When developers do not care about the product or customers, and only care about technical puzzles, engagement is fragile. Connect the team to the business: share customer success stories, bring in senior leaders to talk with the team, and involve developers in customer conversations when possible.

Do not fake passion. Find a real customer, business, craft, or ownership connection that the engineer can actually care about.

---

## Stock Options and Equity Conversations

Equity is one of the most misunderstood parts of compensation and one of the most common sources of silent resentment or missed retention opportunities. As EM, you are often the one who has, or can get, the context to have this conversation well.

### At Hire

When a developer joins and receives an options grant, three numbers matter and most people do not explain them clearly:

- **Exercise price (strike price):** What they will pay per share to own it. Set at fair market value on grant date.
- **Current price (FMV):** What the company is currently worth per share.
- **The 10X scenario:** What this could be worth if the company grows 10X.

Most people sign offer letters without understanding any of this. Be the person who explains it.

### At Tenure

Additional grants are a common and underused retention tool. After a year or two of strong performance, a developer's original grant is largely vested and the "golden handcuffs" loosen. A refresh grant re-anchors the retention value and signals that you are investing in them long-term.

If your company has a refresh grant program, use it proactively. Do not wait for a developer to ask or start interviewing.

### At Departure

When someone leaves, there are three common scenarios and each needs a different conversation:

1. **Staying at a startup, going to a bigger company:** They may be leaving unvested equity on the table. Help them understand what they are walking away from.
2. **Leaving before a liquidity event:** Most options expire 90 days after departure. If they have in-the-money options, they may need to decide whether to exercise and pay for them.
3. **Leaving after a long tenure:** If most options are vested, the financial picture is cleaner, but still worth reviewing together.

These conversations are not about keeping people against their will. They are about treating people with respect by making sure they understand their own financial situation.

---

## Zero-Budget Recognition

Some of the most memorable recognition moments cost nothing. These are specific ideas that have worked:

**Creative onboarding.** When a new developer joins, send a personal newsletter introducing them to the team. Include their background, what they care about, and an interesting fact. It signals that they matter as a person, not just a resource.

**The physical promotion ceremony.** When a developer is promoted, do not just post it in Slack. Order a physical placard with their new title. Present it in person or ship it. The object makes the moment real.

**The birthday widget.** Add team birthdays to your engineering dashboard or status page. When someone's birthday appears on the Grafana screen the team stares at all day, it creates a small but noticed moment.

**Surprise senior leader catch-up.** Arrange a 30-minute casual conversation between a high-performing developer and a VP or senior leader they would not normally interact with. Not a presentation, just a conversation. The message it sends: you are seen at the highest levels.

**Personalized books.** When you see a developer struggling with a problem, send them a relevant book with a personal note. It says: "I pay enough attention to know what you are working on."

---

## 5 Warning Signs of a Disengaging Engineer

By the time someone resigns, you have usually missed signals by weeks or months. Watch for:

1. They stop speaking up in architecture meetings
2. They stop pushing for better practices
3. Documentation efforts disappear
4. Tech debt tickets keep getting deprioritized without comment
5. Standup updates get shorter and more mechanical

Each signal individually might mean nothing. Together, they often mean someone has already accepted another offer in their head and is waiting for the paperwork.

---

## When Someone Has Another Offer

Slow down. Do not immediately ask, "What will it take to keep you?" That can make the relationship feel purely transactional.

Use this order:

1. **Understand:** "What made you start looking?" and "What does this new role give you that you feel you are missing here?"
2. **Check credibility:** Can you actually change the root cause, or only offer a temporary patch?
3. **Decide on a counter:** Counter only if the fix is real, fast, and fair to the rest of the team.
4. **Protect the relationship:** If they leave, make the exit respectful. Alumni relationships matter.

If the root cause is boredom, stuckness, or compensation, a counter may work only if you can act concretely. If the root cause is trust, apathy, or a long pattern of neglect, a counter often just delays the resignation.

---

## What Not to Do

- Do not offer generic praise when the person needs specific recognition, compensation action, or growth.
- Do not create fake growth opportunities with no real scope or decision authority.
- Do not guilt someone for leaving. It teaches the rest of the team that honesty is unsafe.
- Do not promise promotion timelines you do not control.
- Do not wait for annual review cycles if the retention risk is active now.

---

## Final Caveat

Not everything is in your hands. People get offers you cannot match, want to change domains, start companies, or relocate. When the time comes, part on good terms. Do not take it personally.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context, read [`references/sources.md`](references/sources.md).

---

## Related Skills

- `engineer-motivation` - The 3 Drivers framework helps understand what motivates each person before they disengage
- `managing-high-performers` - High performers have specific retention risks: bored, stuck, burnout
- `delegation` - Delegating challenging work is a retention lever
- `1on1s` - The place to diagnose which of the five states someone is in
- `team-health` - Broader team signals often map to these five states
