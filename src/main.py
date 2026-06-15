from aggregator import Signal, calculate_aggregate
from fetch import fetch_headlines
from sentiment import classify

headlines = fetch_headlines("SpaceX")
sentiments = classify(headlines)
aggregate = calculate_aggregate(sentiments)
print(aggregate)
