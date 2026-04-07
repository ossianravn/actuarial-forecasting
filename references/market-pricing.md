# Market Pricing Playbook

Use this playbook when the user asks whether a prediction market, yes/no contract, bucket market, or multi-outcome screen is mispriced.

## Build the forecast before looking at price
1. Parse the resolution wording and official resolution source.
2. Build your own forecast using base rates and current evidence.
3. Inspect the market only after your forecast exists.

## What the market may be used for
Use the market page only to inspect:
- resolution wording,
- listed outcomes,
- whether the field is complete,
- liquidity or volume,
- spread,
- whether listed probabilities sum implausibly above or below 100%.

Do not use the market price as an anchor for the probability forecast.

## If the market is incomplete
- Add `other / unlisted field`.
- Say that the market screen is incomplete.
- Be more conservative about precision.

## If the user wants a trading view
After building your own forecast, you may provide:
- fair yes price,
- fair no price,
- which listed outcomes look underpriced or overpriced,
- whether the market is too thin to trust.

## Useful calculations
- sum of listed probabilities,
- expected value from bucket probabilities,
- fair-price comparison between your forecast and the screen,
- liquidity note if volume is trivial.
