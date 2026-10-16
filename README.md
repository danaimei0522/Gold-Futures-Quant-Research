# Gold Futures Quant Research

A methods and pseudocode portfolio studying RSI threshold entries, a moving-average trend filter, and ATR Chandelier exits for gold futures (AU / SHF). This release contains independently written research explanations and platform-neutral pseudocode. It contains no executable trading strategy or platform adapter.

## Historical report, not independently validated performance

The project owner reports the following post-fix historical backtest figures from PandaAI QUBE:

| Metric | Platform-reported value |
|---|---:|
| Total return | 89.89% |
| Annualized return | 20.92% |
| Sharpe ratio | 1.13 |
| Maximum drawdown | 19.60% |
| Reported trade count | 78 |

**Independent out-of-sample validation has not been completed. Actual order matching and fill timing remain uncertain.** These figures were not recomputed for this release. The full run configuration, metric definitions, source-to-run association, and complete ledger have not been independently reconciled. The reported count does not establish 78 completed round trips. Historical performance does not establish future or executable returns.

The owner identifies this as the post-fix report; preparing this methods release makes no further strategy changes. The PDF and all empirical series remain private and are not distributed.

## Research scope

The research asks how RSI crossings combined with trend filtering and a ratcheting volatility-based exit define a gold-futures trading hypothesis, and what evidence is needed to evaluate it causally. Methods describe the recorded design without tuning its parameters. They do not establish robustness or optimality.

- [Methods and parameter definitions](METHODS.md)
- [Platform-neutral pseudocode](STRATEGY_PSEUDOCODE.md)
- [Data and timestamp requirements](DATA_REQUIREMENTS.md)
- [Reproduction limits and static checks](REPRODUCING.md)
- [Provenance and publication boundary](CODE_PROVENANCE.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)
- [Release audit](CODE_ONLY_RELEASE_AUDIT.md)

## Package check

```bash
python3 scripts/verify_release.py
```

The standard-library verifier checks package inventory, hashes, Python syntax, local document links, and limited sensitive-content patterns. It does not obtain data, execute a strategy, connect to a platform, or validate backtest results. No historical runtime environment or strategy dependency lockfile is claimed.

This code-only portfolio distributes explanatory text, pseudocode and a package verifier only. The original platform strategy, platform templates, SDK implementations, PDFs, screenshots, market data, trade logs and private account information are excluded. No project reuse license has been selected.
