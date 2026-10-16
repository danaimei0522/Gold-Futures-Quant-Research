# Methods-only release audit

## Approved boundary

The owner authorized a public methods and pseudocode portfolio. The payload contains independently drafted explanations, platform-neutral pseudocode, a standard-library verifier, ignore rules and a hash manifest. The original strategy file and all PDFs, datasets, screenshots, logs and private information are excluded.

## Static verification

The verifier enforces an exact 12-file inventory, payload SHA-256 hashes, no symlinks outside Git metadata, syntax parsing of the verifier, relative document links and limited sensitive-content patterns. It permits no other executable source. The unsigned manifest excludes itself from hashing; it provides integrity checks, not provenance certification.

Checks do not validate backtest metrics, execution semantics, legal rights to withheld code, or all possible secret formats. The historical figures are owner-authorized platform-reported values, not independently recomputed performance. No backtest, strategy execution, platform connection or data download is part of package verification.

## Remaining research limitations

Independent out-of-sample validation has not been completed. Actual matching and fill timing, close/reopen order sequencing, original run configuration, metric definitions, parameter selection history and complete ledger reconciliation remain unresolved. The methods and pseudocode do not resolve them.

## Source publication boundary

The withheld original strategy's complete authorship/template ancestry and applicable platform terms are not verified. This release does not distribute that source or claim permission to do so. Original local files remain outside this publication directory. No project reuse license has been selected.

## Publication procedure

Run the verifier, stage only the allowlisted files, inspect the staged inventory and diff, commit on main, then publish to the owner-authorized public repository. Git metadata is excluded from payload integrity scanning. Use a GitHub noreply commit identity and do not copy local credential files. Publication completion is reported separately with its remote commit reference rather than assumed by this document.
