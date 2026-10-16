# Platform-neutral strategy pseudocode

This is newly written conceptual notation, not Python, not copied platform code, and not an executable backtest. It describes decision intentions; order acknowledgements and fill accounting are deliberately unspecified because the original matching semantics remain unresolved. See [METHODS.md](METHODS.md) for formulas and exact settings.

```text
RESEARCH SETTINGS
    RSI window: 10; upward threshold: 60.0; downward threshold: 15.7143
    ATR window: 10; trailing window: 10; ATR distance: 2.0
    trend window: 30; warmup target: 40; minimum prior rows: 32
    research contract multiplier: 1000.0; notional/equity ceiling: 1.0

AT A DECISION SESSION
    identify the session's selected contract and the preceding selected contract
    if the selection changes:
        record an intention to close holdings in the preceding contract
        clear the trailing threshold state

    assemble completed observations of the selected contract before this session
    obtain the session-open reference, without assuming a fill at that reference
    if history or required numerical inputs are unavailable:
        produce no further decision for this evaluation

    calculate historical RSI, ATR, trend average and trailing high/low
    observe the reported long and short holdings

    if a long holding is reported:
        raise or initialize its trailing threshold using highest high minus 2 ATR
        if reference is strictly below the threshold:
            record a long-close intention and clear its threshold

    if a short holding is reported:
        lower or initialize its trailing threshold using lowest low plus 2 ATR
        if reference is strictly above the threshold:
            record a short-close intention and clear its threshold

    upward crossing means previous RSI <= 60.0 and latest RSI > 60.0
    downward crossing means previous RSI >= 15.7143 and latest RSI < 15.7143

    if upward crossing and reference exceeds the trend average:
        if the local decision state is not already long:
            request an opposing-position close when applicable
            calculate whole-contract target from the recorded sizing rule
            record a long-open intention if the target is positive
            clear the long trailing threshold
    otherwise, if downward crossing and reference is below the trend average:
        if the local decision state is not already short:
            request an opposing-position close when applicable
            calculate whole-contract target from the recorded sizing rule
            record a short-open intention if the target is positive
            clear the short trailing threshold
```

The local decision state can differ from confirmed holdings. Close and open intentions must not be treated as completed transactions. The notation does not define a fill simulator, resolve missing route entries, choose indicator edge-case conventions, or certify equivalence to the private platform execution. It cannot reproduce the historical metrics on its own.
