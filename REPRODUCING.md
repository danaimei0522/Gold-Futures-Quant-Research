# Reproduction boundaries

## What can be checked

From this directory, run:

```bash
python3 scripts/verify_release.py
```

This uses Python's standard library to inspect package inventory, hashes, verifier syntax, relative Markdown links and limited sensitive-content patterns. No strategy is imported, no data are downloaded and no orders or backtests are run. The check does not establish copyright clearance or absence of every possible secret.

## What cannot be reproduced

This release contains no executable strategy, platform adapter, data, engine or tested historical environment. Pseudocode is explanatory and cannot recreate the reported results. No dependency lockfile or historical Python version is asserted.

A separate implementation study would first need to specify indicator edge cases, missing-route and missing-bar behavior, equity fallback, fill-aware state transitions, cost/margin rules and roll accounting; obtain time-stamped licensed inputs; document an actual execution engine; reconcile a complete run ledger; and establish independent sample separation. Choices that differ from the private implementation must be disclosed rather than represented as exact reproduction.

Historical matching timing and close/reopen sequencing remain unresolved. Independent out-of-sample validation has not been completed. Preparing this release neither repairs nor reruns the private strategy.
