from datetime import datetime

from aggregator import Signal, calculate_aggregate
from db import init_db, insert
from fetch import fetch_headlines
from price import get_price
from sentiment import classify
from verdict import find_verdict

TICKER = "SPCX"

init_db()

headlines = fetch_headlines(TICKER)
sentiments = classify(headlines)
price = get_price(TICKER)
timestamp = datetime.now().isoformat()

insert(timestamp, TICKER, price, headlines, sentiments)


signal = calculate_aggregate(sentiments)
verdict = find_verdict(signal)
print(signal)
print(verdict)
