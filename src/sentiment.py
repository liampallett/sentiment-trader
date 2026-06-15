from transformers import pipeline

CLASSIFIER = pipeline("sentiment-analysis", model="ProsusAI/finbert")


def classify(headlines: list[str]) -> list[dict]:
    if not headlines:
        return []
    return CLASSIFIER(headlines)
