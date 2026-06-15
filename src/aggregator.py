from dataclasses import dataclass


@dataclass
class Signal:
    score: float
    pct_positive: float
    pct_neutral: float
    pct_negative: float


def calculate_aggregate(headlines: list[dict]) -> Signal:
    if not headlines:
        return Signal(
            score=0.0,
            pct_positive=0.0,
            pct_neutral=0.0,
            pct_negative=0.0,
        )

    total = 0
    num_entries = len(headlines)
    num_pos = 0
    num_neg = 0
    num_neutral = 0

    for entry in headlines:
        match entry["label"]:
            case "positive":
                direction = 1
                num_pos += 1
            case "negative":
                direction = -1
                num_neg += 1
            case _:
                direction = 0
                num_neutral += 1
        weight = float(entry["score"])
        weighted_direction = direction * weight

        total += weighted_direction

    average = total / num_entries
    pct_pos = num_pos / num_entries * 100
    pct_neg = num_neg / num_entries * 100
    pct_neutral = num_neutral / num_entries * 100

    return Signal(
        score=average,
        pct_positive=pct_pos,
        pct_neutral=pct_neutral,
        pct_negative=pct_neg,
    )
