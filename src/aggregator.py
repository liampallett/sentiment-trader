from collections import Counter
from dataclasses import dataclass

DIRECTION = {"positive": 1, "negative": -1, "neutral": 0}


@dataclass
class Signal:
    score: float
    pct_positive: float
    pct_neutral: float
    pct_negative: float


def calculate_aggregate(sentiments: list[dict]) -> Signal:
    if not sentiments:
        return Signal(
            score=0.0,
            pct_positive=0.0,
            pct_neutral=0.0,
            pct_negative=0.0,
        )

    total = sum(DIRECTION[e["label"]] * e["score"] for e in sentiments)
    labels = Counter(e["label"] for e in sentiments)
    n = len(sentiments)

    return Signal(
        score=total / n,
        pct_positive=labels["positive"] / n * 100,
        pct_neutral=labels["neutral"] / n * 100,
        pct_negative=labels["negative"] / n * 100,
    )
