---
name: retaining-developers
description: When the user wants to understand why developers quit, reduce attrition, or keep their best engineers engaged. Also use when the user says "developer quit," "attrition," "someone is disengaged," "how do I retain," "engineer is leaving," "motivation," "developer unhappy," or "keeping the team."
metadata:
  version: 1.0.0
---

# Retaining Developers

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it. If a specific person is mentioned, check `.agents/reports/[name].md`.

---

When a developer quits, it's almost always because they feel one of these 5 things. Use the inverse to diagnose and act.

| What they feel | What they need |
|----------------|---------------|
| Unappreciated | To feel valued |
| Lonely | To feel connected |
| Bored | To feel challenged |
| Stuck | To feel like they're growing |
| Apathetic | To feel passionate about the work |

---

## 1. Unappreciated → Valued

**Initial salary is critical.** The first salary you offer sets an anchor that's hard to correct later. Underpaying at hire means you'll always be playing catch-up — raises feel like corrections, not rewards, and the gap in perceived appreciation accumulates. When negotiating offers, fight for fair compensation from the start. It's far harder to fix this after the fact.

**Raise salary before they ask.** When a developer has to ask for a raise, the damage is already done — it signals that you weren't paying attention or weren't advocating for them. If you give the raise, they won't thank you; they'll feel like they got what they deserved. If you don't, they'll leave. **Be proactive.** Also: don't deny raises because the engineer earns more than you. That's not a competition.

**Don't steal the thunder.** When something good happens — a promotion, a milestone, a successful launch — let the engineer announce it. Good news should come from them. Reserve your channel for bad news. If you announce their achievements for them, you take the moment; if they announce it themselves, you amplify it.

**Just tell them.** Many managers recognize good work internally and assume the engineer knows. They often don't. Say it directly in a 1:1: *"I wanted to tell you — the way you handled X was exactly what I needed. That made a real difference."* It takes five seconds. It costs nothing. It often lands harder than a formal recognition program.

**Recognition:** Give them the stage — let them write the Slack announcement for features they shipped, tag them publicly, push for your people to get company recognition. Route praise through its source: if a VP is excited, ask them to tell the team directly. What feels trivial to you may make someone's year.

## 2. Lonely → Connected

You can't force people to connect, but you can create opportunities: team meetings, focus days outside the office, activities during working hours (not forced evening dinners). The goal is shared memories and personal conversation.

Be honest in interviews about what your team culture actually looks like. If your team is mostly married with kids and nobody hangs out after work, say so. Don't let someone join expecting something that isn't there.

## 3. Bored → Challenged

The best way: **delegate interesting tasks**. Writing technical designs, mentoring a new engineer, leading a cross-team effort — things you currently own but don't have to.

Also just ask: "Do you feel challenged? What's missing from your work today?" Often we assume we know what developers want instead of having the conversation.

## 4. Stuck → Growing

Even challenged developers can feel stuck if they can't see a path forward. Career planning is your job.

Work through it together:
- What are the requirements for the next level?
- How far are they from it — and why? Be 100% honest.
- What tasks do they need to take on to get there?

If they want a management path and there's no open slot: make them your second-in-command, let them experience the work. Help them prepare. Never promise a timeline.

## 5. Apathetic → Passionate

When developers don't care about the product or customers — only the technical puzzles — engagement is fragile. Connect the team to the business: share customer success stories, bring in senior leaders to talk with the team, involve developers in customer conversations when possible.

---

## Stock Options and Equity Conversations

Equity is one of the most misunderstood parts of compensation — and one of the most common sources of silent resentment or missed retention opportunities. As EM, you're often the one who has (or can get) the context to have this conversation well.

### At Hire

When a developer joins and receives an options grant, three numbers matter and most people don't explain them clearly:

- **Exercise price (strike price):** What they'll pay per share to own it. Set at fair market value on grant date.
- **Current price (FMV):** What the company is currently worth per share.
- **The 10X scenario:** What is this worth if the company grows 10X? Put a number on it. "These options could be worth ~$Xk at a 10X outcome" makes equity concrete rather than abstract.

Most people sign offer letters without understanding any of this. Be the person who explains it.

### At Tenure

Additional grants are a common and underused retention tool. After a year or two of strong performance, a developer's original grant is largely vested — the "golden handcuffs" loosen. A refresh grant re-anchors the retention value and signals that you're investing in them long-term.

If your company has a refresh grant program, use it proactively. Don't wait for a developer to ask or start interviewing.

### At Departure

When someone leaves, there are three common scenarios and each needs a different conversation:

1. **Staying at a startup, going to a bigger company:** They're likely leaving unvested equity on the table. Help them understand what they're walking away from. Not to guilt them — just so they have full information.

2. **Leaving before a liquidity event:** Most options expire 90 days after departure. If they have in-the-money options, they may need to decide whether to exercise and pay for them. This can be expensive. Make sure they know the clock is running.

3. **Leaving after a long tenure:** If they've been there long enough that most options are vested, the financial picture is cleaner — but still worth reviewing together.

These conversations aren't about keeping people against their will. They're about treating people with respect by making sure they understand their own financial situation.

---

## Zero-Budget Recognition

Some of the most memorable recognition moments cost nothing. These are specific ideas that have worked:

**Creative onboarding.** When a new developer joins, send a personal newsletter introducing them to the team — something beyond "please welcome X, they come from Y." Include their background, what they care about, an interesting fact. Or build a simple landing page about them. It signals that they matter as a person, not just a resource.

**The physical promotion ceremony.** When a developer is promoted, don't just post it in Slack. Order a physical placard with their new title. Present it in person (or ship it). The object makes the moment real. Slack announcements are forgotten in hours; objects last.

**The birthday widget.** Add team birthdays to your engineering dashboard or status page. When someone's birthday appears on the Grafana screen the team stares at all day — and someone points it out — it creates a moment. Small, but noticed.

**Surprise senior leader catch-up.** Arrange a 30-minute casual conversation between a high-performing developer and a VP or senior leader they wouldn't normally interact with. Not a presentation — just a conversation. The message it sends: you're seen at the highest levels. This one scales zero dollars and creates loyalty that salary increases can't buy.

**Personalized books.** When you see a developer struggling with a problem — leadership, communication, a technical challenge — send them a relevant book with a personal note. It says: "I pay enough attention to know what you're working on."

None of these require a budget. All of them require paying attention.

---

## 5 Warning Signs of a Disengaging Engineer

By the time someone resigns, you've usually missed the signals by weeks or months. Watch for:

1. They stop speaking up in architecture meetings
2. They stop pushing for better practices
3. Documentation efforts disappear
4. Tech debt tickets keep getting deprioritized without comment
5. Standup updates get shorter and more mechanical

Each of these individually might mean nothing. Together, they often mean someone has already accepted another offer in their head — they're just waiting for the paperwork.

---

## Final Caveat

Not everything is in your hands. People get offers you can't match, want to change domains, start companies, or relocate. When the time comes, part on good terms. Don't take it personally.

---

## Related Skills

- `engineer-motivation` — The 3 Drivers framework: proactively understanding and acting on what motivates each person
- `delegation` — Delegating challenging work (#3) is a retention lever
- `1on1s` — The place to diagnose which of the 5 states someone is in
- `team-health` — Broader team signals often map to these 5 states
