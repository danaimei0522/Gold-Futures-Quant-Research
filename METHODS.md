# Research methods

This independently written specification describes the owner's research design. It is not a translation or reproduction of a platform template, and is not an executable substitute for the private strategy.

## Recorded settings

| Setting | Value |
|---|---:|
| Market | Gold futures, AU / SHF |
| RSI window | 10 sessions |
| Long RSI threshold | 60.0 |
| Short RSI threshold | 15.7143 |
| ATR window | 10 sessions |
| Chandelier lookback | 10 sessions |
| ATR multiple | 2.0 |
| Trend average window | 30 sessions |
| Contract multiplier used in research | 1000.0 |
| Maximum notional divided by equity | 1.0 |
| Warmup target | 40 trading sessions |

No parameter search history is available. The asymmetric thresholds must not be described as optimized or independently validated. Contract specifications need confirmation for any future execution study.

## Information set and indicators

Use completed observations for the selected individual futures contract strictly before the decision date. Do not substitute an adjusted continuous series without identifying that methodological change. Forty warmup sessions are a target, not a guarantee that each newly selected contract has adequate history. The recorded design requires at least 32 prior observations before evaluating signals.

For each close-to-close change, define the gain as its positive part and the loss as the positive part of its negative. RSI uses the ratio of the 10-observation arithmetic mean gain to arithmetic mean loss: RSI = 100 - 100 / (1 + mean gain / mean loss). It does not use Wilder smoothing. Zero loss or both means equal to zero require an explicit numerical convention in a future implementation; this methods release does not silently choose one.

True range is the largest of high minus low, absolute high minus preceding close, and absolute low minus preceding close. ATR is its 10-observation arithmetic mean. The trend filter is the 30-observation arithmetic mean close. Compute the highest high and lowest low over the preceding 10 completed observations.

## Entry hypothesis

The reference decision price is the current session open, subject to the timing caveat below. Enter long when the latest historical RSI crosses from at or below 60.0 to above 60.0 and that reference price exceeds the historical trend average. Enter short when RSI crosses from at or above 15.7143 to below 15.7143 and the reference price is below the average. Equality alone does not trigger entry.

The design considers trailing exits before new entries and may request closure of an opposing position before a new entry. It does not establish that closure is filled before the subsequent request is matched.

## Trailing exit hypothesis

For a long holding, the candidate line is the historical 10-session highest high minus twice ATR. Preserve the greater of the preceding line and the candidate. A reference price strictly below the line triggers a close request.

For a short holding, the candidate line is the historical 10-session lowest low plus twice ATR. Preserve the smaller of the preceding line and the candidate. A reference price strictly above the line triggers a close request.

Trailing state is reset for a new position or a contract switch. These are decision rules, not guaranteed fill prices or evidence of intraday stop execution. A trailing exit can realize a loss.

## Sizing and contract switches

The sizing hypothesis is the nonnegative integer floor of equity times 1.0 divided by reference price times 1000.0. The private design substitutes configured initial capital when reported equity is falsy. This fallback is a recorded behavior, not a recommendation to ignore depleted equity. Notional sizing is not a margin, liquidity, or loss limit.

Use a dated dominant-contract route. When the selected contract changes, the design requests closure of the previous holding and clears trailing state before considering the new contract. Historical dominance must have been observable before the decision; a retrospectively constructed route is insufficient evidence of causality.

## Open execution and validation questions

Observing the current open and then submitting an order does not prove eligibility for that same open. Actual callback timing, earliest fill, slippage, commissions, partial fills, rejection, asynchronous account updates and rollover sequencing remain unresolved. The private design's local position-state updates are not independently reconciled with actual fills.

A future evaluation must separately establish date/calendar consistency, missing-data behavior, contract history completeness, point-in-time routing, costs, margin constraints, parameter selection history, and an untouched evaluation sample. No such validation was performed in this release.
