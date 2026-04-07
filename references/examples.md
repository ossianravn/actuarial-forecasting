# Examples

Use these examples to imitate structure, level of rigor, and numerical discipline.  
Do not reuse the illustrative facts or numbers. Replace them with current sourced values for the live question.

The recurring pattern to copy is:
- state the forecast date and resolution window,
- separate base rates from recent developments,
- show 3-6 visible numerical anchors,
- handle incomplete fields explicitly,
- include the strongest counter-case,
- normalize only when the outcomes are mutually exclusive and exhaustive.

---

## Example 1: Local election market with an incomplete field

**Input**

Price this mayoral election market and tell me who is under- or overpriced.  
Listed outcomes: Candidate A, Candidate B, Candidate C, Candidate D.

**Output**

### Executive Summary
As of 2026-04-07, I would price the race as Candidate A 44%, Candidate B 31%, Candidate C 9%, Candidate D 6%, and Other / unlisted field 10%. Candidate A is the favorite, but Candidate B is the only clearly live challenger. The listed market looks too incomplete and too thin to trust as evidence.

### Numerical Anchors
- The continuity bloc won 53% in the previous cycle; applying a 5-8 point open-seat discount gives a starting prior in the mid-40s for Candidate A.
- The best recent poll was A 35, B 29, C 12, D 6, undecided 18; that supports A as the first-round leader but not a first-round winner.
- A recent endorsement that consolidates a centrist list is worth roughly 2-3 points to A, which helps but does not end the race.
- Candidate filing is not final, so `Other / unlisted field` stays elevated at 10% rather than being compressed into named candidates.
- The listed market sums to 142% on trivial volume, which signals a broken or incomplete screen rather than usable information.

### Research Synthesis

#### Base Rates & Structural Constraints
This is an open-seat succession race after two wins by the incumbent-aligned bloc, so continuity starts ahead but weaker than with a sitting incumbent. The runoff rule matters because a fragmented opposition can keep the favorite in first place without producing a first-round victory.

#### Recent Developments
Recent coalition movement helps Candidate A modestly. Candidate B remains the main anti-continuity alternative, but Candidates C and D still prevent a full consolidation of the rival vote. Because the live field may not be final, uncertainty is still wider than the headline poll numbers suggest.

### Outcome Analysis
- **Candidate A:** strongest machine, best base-rate position, modest coalition tailwind; vulnerable if anti-incumbent voters consolidate.
- **Candidate B:** only clearly live challenger; path depends on becoming the undisputed alternative before the runoff.
- **Candidate C:** plausible spoiler, weak direct win path unless the top two stumble.
- **Candidate D:** lower-probability spoiler, little evidence of a runoff path.
- **Other / unlisted field:** still meaningful because the field is not fully settled.

### Final Probabilities
- Candidate A 44%
- Candidate B 31%
- Candidate C 9%
- Candidate D 6%
- Other / unlisted field 10%

### Key Vulnerabilities
The biggest swing factor is whether anti-continuity voters consolidate early behind Candidate B. A second key variable is whether the final certified field is broader than the listed market.

### Sources
Use official election authority materials, local-language reporting, polling with methodology, and candidate filing or endorsement sources.

### Audit Artifact
- Forecast date: 2026-04-07
- Resolution window: election day / runoff as applicable
- MECE check: yes
- Probability sum check: 100%
- Market-price contamination check: passed
- Biggest assumption: the opposition remains fragmented long enough for Candidate A to enter the runoff as the leader

---

## Example 2: Company quarter forecast with threshold pricing

**Input**

Forecast Acme Mobility Q2 deliveries and estimate the probability that deliveries exceed 480k.

**Output**

### Executive Summary
My central estimate for Acme Mobility Q2 deliveries is 456k. I would put the chance of exceeding 480k at 27%. The base case is a normal seasonal lift from Q1 into Q2, but the upside case needs both strong end-of-quarter execution and a meaningful inventory draw.

### Numerical Anchors
- The last four Q1→Q2 delivery changes were +10%, +14%, +16%, and +13%; the median is +13.5%, and applying that to the current Q1 level of 402k gives 456k.
- The simple mean of those four lifts is +13.25%, which points to roughly the same central estimate and suggests there is no major outlier distorting the baseline.
- To exceed 480k from a 402k Q1 base, deliveries must rise 19.4% sequentially, which is above 3 of the last 4 comparable years.
- Installed capacity and recent inventory trends imply a plausible operating ceiling around 475k-485k unless the company draws inventory much harder than usual.
- Scenario weights of Bear 25%, Base 50%, Bull 20%, Stretch 5% produce an expected value near 456k.

### Research Synthesis

#### Base Rates & Structural Constraints
The clean starting point is seasonal history: compare the current Q1 base with the last several Q1→Q2 transitions, then cross-check against current production capacity, inventory, and logistics constraints. Historical seasonality supports a lift into Q2, but not every comparable year supports a breakout quarter above 480k.

#### Recent Developments
Recent reports suggest stable demand but uneven regional mix. That supports a normal seasonal rebound rather than a blowout. The upside case improves if there is evidence of stronger end-quarter incentive pull-forward or cleaner export logistics than in the prior quarter.

### Outcome Analysis
- **Below 440k:** requires either weaker demand conversion or logistics slippage.
- **440k-460k:** the most natural base case using historical seasonality.
- **460k-480k:** credible upside if execution is smooth.
- **Above 480k:** possible, but it needs a stronger-than-normal seasonal lift and little room for operational friction.

### Final Distribution
- Below 440k: 14%
- 440k-460k: 39%
- 460k-480k: 20%
- Above 480k: 27%

### Key Vulnerabilities
The forecast moves most if current-quarter inventory is materially higher or lower than assumed, or if a new production constraint appears late in the quarter.

### Sources
Use company filings, investor relations releases, regulator or registration data where relevant, and reputable current-quarter tracking sources.

### Audit Artifact
- Forecast date: 2026-04-07
- Resolution window: Q2 delivery release
- MECE check: yes
- Probability sum check: 100%
- Market-price contamination check: passed
- Biggest assumption: Q2 follows roughly normal seasonal lift rather than an outlier upside or downside pattern

---

## Example 3: Merger close-by-date probability

**Input**

Estimate the probability that DealCo acquires TargetCo by September 30 and give fair yes/no levels.

**Output**

### Executive Summary
I would price closing by September 30 at 41% Yes and 59% No. My base case is that the deal is more likely than not to close eventually, but less likely than not to close by this specific date because the remaining procedural path is tight.

### Numerical Anchors
- In a comparable set of complex cross-border deals with antitrust review, roughly 35-45% closed by the original target date; that is the base-rate band.
- There are 78 days left until the resolution date, while the shortest plausible remaining path across antitrust, shareholder, and foreign-investment steps is about 95 days.
- Financing is committed and the board recommendation remains in place, which supports eventual close probability but does less for the close-by-date question.
- If the key regulator moves from standard review to an extended review phase, the by-date probability drops sharply and the No side becomes dominant.

### Research Synthesis

#### Base Rates & Structural Constraints
This is primarily a timeline-feasibility question, not a pure eventual-merits question. The right base rate is not “how often do signed deals close,” but “how often do deals with this structure and this remaining process close by this deadline.”

#### Recent Developments
Recent procedural progress has been constructive but not decisive. No major party has broken from the deal, but the remaining approvals still leave little slack in the calendar.

### Outcome Analysis
- **Yes by September 30:** needs a clean path with no review extension and no procedural delays.
- **No by September 30:** becomes the base case if any key step slips, even if the deal remains alive after the date.

### Final Probabilities
- Yes by September 30: 41%
- No by September 30: 59%

### Trading View
- Fair Yes: 41c
- Fair No: 59c
- The position is only attractive if the live market is materially away from these levels after accounting for fees and liquidity.

### Key Vulnerabilities
The most important swing variable is whether the lead regulator stays on the fast path or moves to a deeper review.

### Sources
Use merger agreement language, company filings, regulator notices, shareholder materials, and comparable-case timelines.

### Audit Artifact
- Forecast date: 2026-04-07
- Resolution window: by 2026-09-30
- MECE check: yes
- Probability sum check: 100%
- Market-price contamination check: passed
- Biggest assumption: no major review extension occurs

---

## Example 4: Overlapping outcomes must not be normalized

**Input**

Give the odds that the bill passes committee this month and the odds that it passes the full chamber this session.

**Output**

### Executive Summary
I estimate a 64% chance the bill passes committee this month and a 37% chance it passes the full chamber this session. These are marginal probabilities and do **not** sum to 100% because the outcomes overlap.

### Numerical Anchors
- Historically, about two-thirds of bills at this stage clear committee, which supports a starting point in the low-to-mid 60s.
- Only a subset of bills that clear committee reach a floor vote in the same session, which keeps the full-chamber probability materially lower.
- The current calendar has only a limited number of floor days left, which is the main reason the second probability stays below the first.

### Final Probabilities
- Passes committee this month: 64%
- Passes full chamber this session: 37%

### Audit Artifact
- Forecast date: 2026-04-07
- Resolution window: this month / this session
- MECE check: no, overlapping outcomes
- Probability sum check: not applicable
- Market-price contamination check: passed
- Biggest assumption: leadership continues to prioritize the bill after committee

---

## Style rules the examples are teaching

- Do not jump from headlines straight to a polished percentage.
- Surface a few concrete calculations in a visible `Numerical Anchors` section.
- Keep base rates and recent developments separate.
- Add `Other / unlisted field` when the field is incomplete.
- Treat timeline questions as timeline questions.
- Do not normalize overlapping outcomes into fake exclusivity.
- Use the market only after the independent forecast exists.
