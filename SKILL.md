---
name: actuarial-forecasting
description: "research and produce explicit probability forecasts and fair-odds views for current events, elections, policy outcomes, company metrics, mergers, regulatory approvals, and other uncertain questions. use when the user asks for odds, fair value, probability distributions, scenario weights, stress tests, or pricing for a prediction market or other yes/no or multi-outcome event. especially use for deadline-driven questions, election markets, quarterly company forecasts, and requests to compare market price versus fair probability without using market prices as evidence."
---

# Actuarial Forecasting

Use this skill to turn uncertain questions into explicit probabilities anchored in base rates, current evidence, structural constraints, and visible numerical checks.

## Default mode
- Use **rigorous mode** by default for any current, numeric, or market-related forecast.
- Use **concise mode** only when the user explicitly asks for a brief answer.
- In rigorous mode, do not stop at a qualitative narrative. Run at least one explicit numerical check and show the most important numerical anchors in the final answer.

## Non-negotiables
- Do not use prediction markets, betting odds, or crypto forecasting platforms as evidence or anchors.
- Do use the market page when relevant only to inspect resolution wording, listed outcomes, liquidity, spread, and whether the field is incomplete.
- Do anchor the forecast to a stated forecast date or data cutoff.
- Do separate **base-rate evidence** from **recent-update evidence**.
- Do include the strongest competing hypothesis before finalizing.
- Do regress toward the base rate when evidence is thin, contradictory, or incomplete.
- Do use exact arithmetic for sums, normalization, expected values, growth rates, and threshold checks. Prefer `scripts/forecast_math.py` or a calculator over mental math.
- Do avoid finalizing until the stop conditions near the end of this file are met.

## Workflow overview
Follow this sequence in order.

1. Parse the exact question.
2. Choose the playbook.
3. Gather minimum evidence.
4. Build the working table.
5. Run the quantitative pass.
6. Stress-test with the best counter-case.
7. Write the final answer using the output template.
8. Run the audit checklist.

## 1) Parse the exact question
Write a 1-2 line intent statement covering:
- event or variable being forecast,
- resolution date or forecast window,
- geography or institution,
- outcome set,
- whether the outcomes are mutually exclusive and exhaustive,
- any user constraints such as no web, no polls, no market references, or required sources.

If the question is ambiguous, make the narrowest reasonable assumption and state it.

## 2) Choose the playbook
Choose one primary playbook before searching.

- **Election or political contest:** read `references/elections.md`.
- **Quarterly company metric, guidance, deliveries, revenue, subscribers, defaults, runway, or operational milestone:** read `references/company-forecasting.md`.
- **Prediction-market pricing, fair-value comparison, or market screen sanity check:** read `references/market-pricing.md`.
- **Other current-event forecast:** stay in this file and adapt the generic workflow.

If the question spans multiple playbooks, use the most specific one first, then borrow only the needed pieces from the others.

## 3) Gather minimum evidence
Do not finalize until all relevant minimum evidence is gathered or explicitly unavailable.

### Minimum evidence for all forecasts
Collect at least:
- one historical or structural base-rate anchor,
- one official or primary current anchor,
- one recent development from the last 1-14 days when the topic is current,
- one disconfirming or rival-specific source,
- one explicit resolution source or resolution rule.

### Source order
Prefer sources in this order:
1. official data, filings, court documents, statutes, regulators, election authorities, company releases,
2. peer-reviewed or well-documented research,
3. high-quality journalism with named sourcing,
4. expert synthesis that cites evidence.

If direct data is sparse, search for proxy metrics or structural constraints rather than filling the gap with narrative.

## 4) Build the working table
Before drafting the final answer, build a compact working table for yourself. Do not dump the whole table unless the user asks for the full methodology.

Use these columns:
- outcome,
- baseline prior or proxy prior,
- positive adjustments,
- negative adjustments,
- current provisional probability,
- strongest counter-case,
- load-bearing sources,
- confidence note.

This table is the control surface for the forecast. If the final answer is thin, return here first.

## 5) Run the quantitative pass
Always perform at least one of these numerical passes when the question is quantitative or current.

### Required numerical checks
Choose the checks that fit the question:
- growth-rate table,
- mean / median / trimmed-mean comparison,
- scenario-weighted expected value,
- threshold math,
- capacity / inventory / runway math,
- vote-share or coalition arithmetic,
- timeline feasibility check,
- normalization to exactly 100% for mutually exclusive outcomes.

### Arithmetic discipline
- Use small moves for soft evidence.
- Use bigger moves only for hard legal, financial, numerical, or procedural changes.
- Normalize only after the provisional percentages make sense.
- Round late.
- If rounding breaks the total, fix the largest bucket by the residual.

### Visible output requirement
Show a short **Numerical Anchors** block in the final answer with 3-6 bullets. Each bullet should present one concrete calculation or numeric comparison that materially shaped the forecast. Do not expose raw scratchwork or long hidden reasoning.

## 6) Stress-test with the best counter-case
Write the strongest grounded case against the current favorite.

At minimum answer:
- What is the best argument against the leading outcome?
- What hard fact would most damage the current forecast?
- Which assumption is doing the most work?

If the counter-case is strong, widen the distribution or move probability toward the rival.

## 7) Special rules for outcome structure
### If the outcomes are mutually exclusive and exhaustive
- Make the final probabilities sum to exactly 100%.
- Include an `other / unlisted field` bucket if the listed outcomes are not complete.

### If the outcomes overlap
- Score them as marginal probabilities.
- Say explicitly that they do not sum to 100%.
- Do not normalize overlapping outcomes into fake exclusivity.

### If the field is incomplete
- Increase uncertainty.
- Use a larger residual bucket before filing deadlines, final candidate certification, or official publication of the field.
- Explain why the residual exists.

## 8) Write the final answer
Use this default structure unless the user requests another format.

### Executive Summary
Give the bottom line in 2-4 sentences.

### Numerical Anchors
Show 3-6 bullets with the most important calculations or numeric cross-checks.

### Research Synthesis
Use two subsections:
- **Base Rates & Structural Constraints**
- **Recent Developments**

### Outcome Analysis
For each important outcome, include:
- base-rate anchor,
- catalysts,
- barriers,
- strongest counterargument.

### Final Probabilities
List the final percentages clearly.

### Key Vulnerabilities
List the variables most likely to move the forecast soon.

### Sources
List the key primary and secondary sources.

### Audit Artifact
Include:
- forecast date or data cutoff,
- resolution date or window,
- mece check: yes/no,
- probability sum check,
- market-price contamination check: passed/failed,
- biggest assumption.

## Audit checklist
Run these checks before finalizing.

1. **Question fit:** match the exact resolution wording and time window.
2. **Coverage:** include at least one historical anchor and one current anchor.
3. **Freshness:** tie the important recent updates to the forecast date and last 1-14 days.
4. **Disconfirmation:** include the best rival case or strongest reason you may be wrong.
5. **Math:** verify the percentages, expected values, or threshold math exactly.
6. **Field completeness:** add `other / unlisted field` when the live field is incomplete.
7. **Market hygiene:** do not let market prices influence the forecast before the forecast is built.
8. **Confidence discipline:** widen uncertainty when evidence is sparse or the field is still moving.

## Stop conditions
Do not finalize until all of the following are true:
- the question and resolution are explicit,
- the playbook has been selected,
- the minimum evidence is gathered or its absence is stated,
- the working table exists,
- at least one explicit numerical pass was completed,
- the strongest counter-case was considered,
- the final output includes numerical anchors,
- the audit checklist passes.

## Common failure modes
- giving a polished narrative without doing explicit arithmetic,
- using a single fresh headline as a substitute for a base rate,
- relying on one poll or one analyst note without structural context,
- treating a thin or incomplete market as if it reveals fair odds,
- omitting `other / unlisted field` when the live field is incomplete,
- skipping local-language or official local sources for local elections,
- hiding all numeric justification instead of surfacing the key calculations,
- normalizing low-confidence guesses into false precision.

## Mini patterns
### If asked to price a prediction market
1. Build the forecast without the market price.
2. Inspect the market only after the forecast exists.
3. Check liquidity, spread, resolution wording, and whether listed outcomes are incomplete.
4. Compare your fair probabilities to the market only at the end.

### If asked for a company quarter forecast
1. Build a comparable-period table.
2. Calculate sequential and year-over-year changes.
3. Identify outlier quarters and explain whether to trim them.
4. Run at least one scenario or threshold check.

### If asked for a local election forecast
1. Verify the official election date and runoff rule.
2. Confirm whether the field is final.
3. Search in the local language and use official local sources.
4. Compute a residual bucket if the field is still incomplete.

For concrete input/output patterns and the expected level of numerical rigor, read `references/examples.md`.

## Activation tests
### Should trigger
- "price this mayoral election market and tell me who is under- or overpriced."
- "estimate the probability that this merger closes by september 30."
- "forecast tesla q2 deliveries and show the key numerical anchors."
- "give fair odds for candidate a, candidate b, and other."
- "stress-test my view that the bill passes this session."
- "estimate the chance this regulator approves the deal this quarter."

### Should not trigger
- "summarize this article."
- "explain bayes' theorem in plain english."
- "show me the betting odds."
- "generate random percentages for fun."

## Resource map
- `SKILL.md`: default workflow, output structure, audit checklist, and stop conditions.
- `references/elections.md`: election and political-contest playbook.
- `references/company-forecasting.md`: company quarter and operational-metric playbook.
- `references/market-pricing.md`: fair-value and prediction-market playbook.
- `references/examples.md`: concrete example forecasts showing structure and numerical rigor.
- `references/source-log.md`: lightweight evidence ledger template.
- `scripts/forecast_math.py`: exact arithmetic helpers for normalization, expected value, and growth-rate summaries.
