---
name: business-literacy
description: When the user wants to understand business terms used by leadership or stakeholders, make a case for engineering work in business language, or bridge the gap between engineering and business. Also use when the user says "business terms," "EBITDA," "burn rate," "CAC," "LTV," "gross margin," "ARR," "how do I speak to business people," or "I don't understand finance."
metadata:
  version: 1.0.0
---

# Business Literacy

## Before Starting

Check for EM context first. If `.agents/em-context.md` exists, read it.

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

## Related Skills

- `working-with-pm` — PMs use this language constantly; understanding it makes you a real partner
- `roadmap-planning` — Tech debt and platform work need business justification to get prioritized
- `managing-yourself` — Senior leadership communication requires business fluency

