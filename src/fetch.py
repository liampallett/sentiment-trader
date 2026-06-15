import feedparser


def _build_url(stock: str) -> str:
    return f"https://news.google.com/rss/search?q={stock}"


def fetch_headlines(stock: str) -> list[str]:
    try:
        feed = feedparser.parse(_build_url(stock))
        return [str(entry.title) for entry in feed.entries]
    except Exception as e:
        print(f"Error fetching headlines: {e}")
        return []
