---
name: business-literacy
description: Explains business financial terms and frameworks for engineering managers — produces term definitions (ARR, COGS, CAC, LTV, gross margin, burn rate, EBITDA, AARRR), translation formulas for making engineering work visible in business language, and a three-layer framework for building business credibility. Use when the user says "business terms," "EBITDA," "burn rate," "CAC," "LTV," "gross margin," "ARR," "how do I speak to business people," "I don't understand finance," "make the case for engineering work," "connect engineering to business outcomes," "talk to the P&L owner," or "business impact." Do NOT use when the user wants to connect engineering metrics (DORA, velocity) to business metrics — use developer-productivity instead.
metadata:
  version: 2.1.2
---

# Business Literacy

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
- **Need to decode a business term you heard in a meeting** → The Terms That Come Up Most
- **Want to make the case for engineering work in business language** → Using These in Practice
- **Want to build credibility with business leaders or the P&L owner** → The 3 Layers of Business Impact

---

## Default Response Shape

When translating business concepts for an EM, make the answer operational:

1. **Plain-English definition:** explain the term without finance theater.
2. **Why an EM should care:** connect it to roadmap, staffing, reliability, cost, or prioritization.
3. **Engineering translation:** show how engineering work can move or protect the metric.
4. **Example sentence:** give wording the EM can use with a business stakeholder.
5. **Caveat:** note where the metric can mislead or be gamed.

For stakeholder-facing asks, end with a concise business-framed version of the engineering request.

---

## Why This Matters

Engineers can succeed without understanding business language. Engineering managers cannot. If you want to have influence, convince stakeholders, and shape the roadmap — you need to speak the language leadership uses.

Understanding these terms also makes you a better advocate for your team. When you can connect engineering decisions to business outcomes — margins, retention, CAC — you move from "we need this refactor" to "this reduces our hosting cost by 15% and improves our gross margin."

---

## The Terms That Come Up Most

### Money In

**ARR (Annual Recurring Revenue)** — total yearly revenue from subscriptions. The core metric for SaaS companies. When leadership says "we're at $5M ARR," this is it.

**MoM (Month-over-Month)** — growth rate from one month to the next. A 10% MoM growth rate is exceptional.

**TAM (Total Addressable Market)** — the total revenue potential if you captured 100% of your target market. Used to justify investment size.

### Costs

**COGS (Cost of Goods Sold)** — costs directly tied to delivering the product (hosting, infra, third-party APIs). For SaaS, engineering teams directly influence COGS.

**Gross Margin** — `(Revenue - COGS) / Revenue`. For SaaS, 70–80% is healthy. Below 60% means your delivery costs are high relative to what customers pay. **This is where engineering decisions show up in financials.** Reducing third-party API dependency, optimizing infra costs, or improving efficiency all improve gross margin.

**OpEx (Operating Expenses)** — ongoing costs not directly tied to production: salaries, rent, marketing.

**CapEx (Capital Expenditure)** — large investments with long-term value. Building a new data center is CapEx; monthly AWS bill is OpEx.

**Burn Rate** — how much cash the company spends per month. High burn + low revenue = limited runway.

**Net Margin** — what's left after ALL costs. Most startups have negative net margin for years.

**EBITDA** — Earnings Before Interest, Taxes, Depreciation, Amortization. A profitability measure that strips out financing. Matters more at late-stage.

### Customers

**CAC (Customer Acquisition Cost)** — average cost to acquire a customer. If you spend $100k on marketing and get 100 customers, CAC = $1,000.

**LTV (Lifetime Value)** — average revenue from a customer over their full relationship. LTV should be 3–5x CAC for a healthy business. If not, growth is expensive.

**Churn** — percentage of customers lost per period. The silent killer. 5% monthly churn = ~46% of customers gone per year.

**Retention** — the inverse of churn. Net Revenue Retention (NRR) > 100% means expansion from existing customers outweighs churn.

**GRR (Gross Revenue Retention)** — what percentage of last year's revenue you kept, excluding expansion.

**NPS (Net Promoter Score)** — "How likely are you to recommend us?" Scores 9–10 = promoters, 7–8 = passives, 0–6 = detractors.

### Business Health

**Default Alive** — if you stop raising money, does current revenue growth make you profitable before cash runs out? If not, you're "default dead."

**Moat** — what makes you hard to copy. Deep tech, network effects, proprietary data, brand. Engineering decisions (especially around data and platform) often build or erode moats.

**AARRR (Pirate Metrics)** — Acquisition, Activation, Retention, Referral, Revenue. A framework for diagnosing where growth is leaking. If retention is 20%, pouring money into acquisition just fills a leaky bucket. Fix the leak first.

---

## Using These in Practice

When proposing technical work, translate it:
- Not: "we need to migrate off this legacy API" → Yes: "this API costs us $40k/year and is our top cause of outages; removing it improves gross margin and reduces customer churn"
- Not: "we should invest in platform" → Yes: "right now each new feature takes 2 weeks to wire up; a platform investment gets that to 2 days, directly improving our CAC by reducing time-to-value"

When reviewing the roadmap, ask the business question: which AARRR stage are we weakest at right now? Invest there first.

---

## The 3 Layers of Business Impact

EMs who drive real business impact typically work across three layers, in increasing order of difficulty:

**Layer 1 — Product:** Do you and your team understand how your features are used? Have a dashboard showing feature usage that everyone can see. Know the product's AARRR metrics. A feature that ships but nobody adopts has zero impact.

**Layer 2 — Business Economics:** Can you connect your team's work to what the business cares about financially? Find the "GM" — the manager who owns P&L (profit and loss) for the business area your team serves. Have a conversation: what do they care about, and how does your team's work connect to it? Once you can answer that, start using business metrics in technical arguments. "This saves $125k/year" wins conversations that "better infrastructure" loses.

**Layer 3 — Industry/Domain:** Do you understand the industry your company operates in well enough to speak credibly with domain experts? Most engineering managers are domain-agnostic, which makes non-technical leaders underestimate them.

Three levels of domain knowledge:
- **Level 1 (Passive):** Know the terminology. Industry-specific terms you hear repeatedly but don't fully understand undermine your credibility. Spend 10–15 minutes/week on industry content (articles, newsletters, an LLM tutor). Ask it to explain the domain as an instructor would.
- **Level 2 (Sharing):** Share what you learn. Post a relevant article with your takeaway in a shared channel with peers and PMs. People who see you engaging with the domain start treating you as a peer.
- **Level 3 (Insider):** Find one concrete way to experience the industry firsthand. Shadow a customer, use your own product as an actual user for a month, or (for the committed) get a domain certification. The gap between knowing the domain and experiencing it is the difference between being taken seriously and being tolerated.

---

## Dive Deeper

If the user asks where a framework came from, wants to read the original article, or wants more context on any topic in this skill — read [`references/sources.md`](references/sources.md) for the full list of source articles (with links) and books.

---

## Related Skills

- `working-with-pm` — PMs use this language constantly; understanding it makes you a real partner
- `roadmap-planning` — Tech debt and platform work need business justification to get prioritized
- `developer-productivity` — For connecting engineering metrics (DORA, velocity) to business outcomes
- `influence` — Business fluency directly enables the 3rd level of positioning (being trusted)
