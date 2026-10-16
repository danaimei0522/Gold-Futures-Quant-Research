# Data requirements

No data are supplied. Any future implementation needs lawfully obtained individual-contract daily open, high, low and close observations; contract identifiers and specifications; a trading-session calendar; dated contract-selection information; account equity and holdings; and timestamped order and fill events.

For each input, record source, version, timezone, night-session attribution, observation timestamp, publication/availability timestamp, revision policy and missing-value conventions. Contract selection must be available before the relevant decision. Prior-session prices alone do not establish that the route was known in advance.

Support at least 40 trading sessions of intended warmup and assess history separately for each routed contract. The design's evaluation minimum is 32 prior rows. Dates must use one consistent calendar and ordering convention. Do not substitute continuous adjusted prices for individual contracts without disclosing the change.

A future result reconciliation also needs complete equity and trade series, run dates, initial cash, fees, slippage, margin settings, fill eligibility rules and metric definitions. These are not present here. No synthetic replacement ledger or fabricated configuration is provided.

Software access and platform use do not establish permission to redistribute market data or derived outputs. Obtain applicable permissions separately. Only the owner-authorized five aggregate historical figures in README are included; reports, raw data, logs and identifiers are excluded.
