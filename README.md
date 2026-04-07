# Actuarial Forecasting

`actuarial-forecasting` is a Codex skill for turning uncertain real-world questions into explicit probability forecasts and fair-odds views.

It is built for questions like:
- "What is the probability this merger closes by September 30?"
- "Forecast Tesla Q2 deliveries and show the numerical anchors."
- "Price this election market and tell me who is under- or overpriced."
- "Give fair odds for these outcomes without using the market price as evidence."

This repo is not a trading bot, a market data feed, or a black-box forecaster. It is a reusable forecasting workflow: a structured prompt, supporting playbooks, example outputs, and a small arithmetic helper script.

## What This Skill Does

The skill pushes the model toward disciplined forecasting instead of narrative guesswork.

Its core behavior is:
- parse the exact resolution question,
- choose the right forecasting playbook,
- gather minimum evidence,
- separate base rates from recent updates,
- run at least one explicit numerical pass,
- surface 3-6 visible numerical anchors,
- stress-test the forecast with the strongest counter-case,
- produce a final percentage view with an audit artifact.

The design goal is simple: if a forecast matters, the numeric backbone should be visible.

## What This Skill Does Not Do

The skill is intentionally opinionated about a few things.

It does not:
- use prediction markets, betting odds, or crypto forecast screens as evidence,
- treat one poll, one headline, or one analyst note as sufficient,
- normalize overlapping outcomes into a fake 100% total,
- hide all the reasoning behind a polished top-line percentage,
- finalize a current-event forecast without at least one explicit numeric check.

It may inspect a market page for resolution wording, listed outcomes, liquidity, or spread, but only after building the independent forecast.

## Intended Use Cases

Use this skill when the user is asking for:
- explicit odds or probabilities,
- fair value or fair yes/no prices,
- bucket or range probabilities,
- expected values,
- scenario weights,
- stress tests,
- market-pricing sanity checks,
- probability comparisons across multiple outcomes.

The strongest fit is:
- elections and political contests,
- quarterly company metrics,
- merger close timing,
- regulatory approvals,
- deadline-driven yes/no events,
- multi-outcome or threshold prediction markets.

## How The Skill Thinks

The workflow in [`SKILL.md`](./SKILL.md) follows a strict sequence:

1. Parse the exact question.
2. Choose the right playbook.
3. Gather minimum evidence.
4. Build a working table.
5. Run the quantitative pass.
6. Stress-test the counter-case.
7. Write the final answer.
8. Run the audit checklist.

Three design choices matter most:

- Base rates come first.
  Recent news matters, but it should move a prior rather than replace one.

- Arithmetic is mandatory.
  The skill explicitly requires calculations such as growth tables, threshold math, scenario-weighted expected value, coalition arithmetic, or timeline feasibility checks.

- The answer must show its load-bearing numbers.
  The final output includes a `Numerical Anchors` section with 3-6 concrete checks that materially shaped the forecast.

## Output Contract

The default final structure is:

- `Executive Summary`
- `Numerical Anchors`
- `Research Synthesis`
- `Outcome Analysis`
- `Final Probabilities`
- `Key Vulnerabilities`
- `Sources`
- `Audit Artifact`

This makes the skill useful both for direct answers and for downstream review. A reader can see the percentage, the supporting math, the strongest rival case, and the key assumption without reverse-engineering hidden reasoning.

## Repo Layout

- [`SKILL.md`](./SKILL.md)
  The main skill definition: workflow, rules, stop conditions, output format, activation tests, and resource map.

- [`references/elections.md`](./references/elections.md)
  Playbook for elections, runoffs, candidate fields, coalition arithmetic, and incomplete market fields.

- [`references/company-forecasting.md`](./references/company-forecasting.md)
  Playbook for quarterly company metrics, deliveries, revenue, subscribers, runway, and milestone forecasts.

- [`references/market-pricing.md`](./references/market-pricing.md)
  Rules for pricing prediction markets without contaminating the forecast with market prices.

- [`references/examples.md`](./references/examples.md)
  Concrete examples showing the intended structure, level of rigor, and visible numeric discipline.

- [`references/source-log.md`](./references/source-log.md)
  Lightweight source ledger for evidence-heavy forecasts.

- [`scripts/forecast_math.py`](./scripts/forecast_math.py)
  Small arithmetic helper for normalization, expected value, and growth summaries.

- [`agents/openai.yaml`](./agents/openai.yaml)
  Minimal display metadata for the skill.

## The Three Specialized Playbooks

### Elections

The election playbook emphasizes:
- official election date,
- runoff rules,
- incumbent vs open-seat dynamics,
- previous official results,
- whether the field is final,
- local-language and local-institution sourcing,
- explicit residual treatment for `other / unlisted field`.

This is important because many election errors come from pretending the listed field is complete or ignoring runoff mechanics.

### Company Forecasting

The company playbook emphasizes:
- exact metric definition,
- at least four comparable periods when available,
- sequential and year-over-year framing,
- official current-period anchors,
- structural constraints like capacity, inventory, backlog, or runway,
- scenario-weighted and threshold-based reasoning.

This keeps the skill focused on operational math rather than narrative sentiment.

### Market Pricing

The market-pricing playbook is a hygiene layer.

Its main rule is:
- build the forecast first,
- inspect the market second.

The market can be used to inspect:
- resolution wording,
- completeness of listed outcomes,
- liquidity,
- spread,
- whether the displayed probabilities sum implausibly.

It cannot be used as the probability anchor.

## Examples And Style

The repo includes worked examples in [`references/examples.md`](./references/examples.md). They are there to teach style, not facts.

The recurring pattern is:
- state the forecast date and resolution window,
- separate base rates from recent developments,
- show visible numerical anchors,
- handle incomplete fields explicitly,
- include the strongest counter-case,
- normalize only when outcomes are mutually exclusive and exhaustive.

This is the fastest way to understand what "good" output looks like.

## Arithmetic Helper

The helper script in [`scripts/forecast_math.py`](./scripts/forecast_math.py) covers three common tasks:

### Normalize provisional percentages

```bash
python scripts/forecast_math.py normalize 45 32 8 7 2 6
```

### Compute expected value from weighted buckets

```bash
python scripts/forecast_math.py ev --probs 5,18,36,28,10,3 --midpoints 337.5,362.5,387.5,412.5,437.5,462.5
```

### Summarize historical growth rates

```bash
python scripts/forecast_math.py growth --pairs 184800:201250 310048:254695 422875:466140 386810:443956 --apply 358023
```

The script is intentionally small. Its role is to reduce avoidable arithmetic errors, not to replace the forecasting workflow.

## Quality Bar

The skill has explicit stop conditions. It should not finalize until:
- the resolution question is clear,
- the correct playbook is chosen,
- minimum evidence is gathered or its absence is stated,
- a working table exists,
- at least one quantitative pass is complete,
- the strongest counter-case is considered,
- the final answer includes numerical anchors,
- the audit checklist passes.

That matters because the most common failure mode in forecasting is premature closure dressed up as confidence.

## Typical Failure Modes This Repo Tries To Prevent

- polished narrative without arithmetic,
- current headline substituted for a base rate,
- one poll used as the whole election,
- incomplete market field treated as complete,
- overlapping outcomes normalized to 100%,
- prediction market prices used as hidden anchors,
- false precision when the evidence is sparse or the field is still moving.

## How To Use This Repo

### In Codex

Install the skill in your Codex skills directory and invoke it when the user wants probabilities, fair value, or explicit odds.

The installed local skill path on this machine is:

`C:\Users\Ossian\.codex\skills\actuarial-forecasting\SKILL.md`

### From GitHub

If the skill is not installed locally, the repo itself is the reference:

- repo: [https://github.com/ossianravn/actuarial-forecasting](https://github.com/ossianravn/actuarial-forecasting)
- skill file: [https://github.com/ossianravn/actuarial-forecasting/blob/main/SKILL.md](https://github.com/ossianravn/actuarial-forecasting/blob/main/SKILL.md)

The main thing you need is [`SKILL.md`](./SKILL.md), but the supporting references materially improve output quality.

## Who This Is For

This repo is for people who want forecasts that are:
- explicit,
- numerically anchored,
- source-disciplined,
- audit-friendly,
- useful for market comparison without being contaminated by market prices.

If you want quick narrative commentary, this repo is overkill.

If you want a reproducible forecasting habit, this is exactly what it is for.
