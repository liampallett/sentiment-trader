from aggregator import Signal, calculate_aggregate
from fetch import fetch_headlines
from sentiment import classify
from verdict import find_verdict

headlines = fetch_headlines("SpaceX")
sentiments = classify(headlines)
signal = calculate_aggregate(sentiments)
verdict = find_verdict(signal)

print(signal)
print(verdict)
