from enum import Enum

from aggregator import Signal

MAX_NEUTRAL_PCT = 50
MIN_POS_NEG_PCT = 30
SCORE_THRESHOLD = 0.1


class Verdict(Enum):
    WATCH = "watch"
    HOLD = "hold"
    AVOID = "avoid"


def find_verdict(signal: Signal) -> Verdict:
    if signal.pct_neutral > MAX_NEUTRAL_PCT:
        return Verdict.HOLD
    if min(signal.pct_positive, signal.pct_negative) > MIN_POS_NEG_PCT:
        return Verdict.HOLD
    if signal.score > SCORE_THRESHOLD:
        return Verdict.WATCH
    if signal.score < -SCORE_THRESHOLD:
        return Verdict.AVOID
    return Verdict.HOLD
