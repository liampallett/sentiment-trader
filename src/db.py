import sqlite3


def init_db():
    conn = sqlite3.connect("data/runs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
        id        INTEGER PRIMARY KEY,
        timestamp TEXT,      -- ISO 8601, e.g. "2026-06-15T21:30:00"
        ticker    TEXT,
        price     REAL
    );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS headlines (
        id      INTEGER PRIMARY KEY,
        run_id  INTEGER,     -- links back to runs.id
        text    TEXT,
        label   TEXT,
        score   REAL,
        FOREIGN KEY (run_id) REFERENCES runs (id)
    );
    """)
    conn.commit()
    conn.close()


def insert(timestamp, ticker, price, headlines, classified):
    conn = sqlite3.connect("data/runs.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO runs (timestamp, ticker, price) VALUES (?, ?, ?)",
        (timestamp, ticker, price),
    )
    run_id = cursor.lastrowid
    rows = [
        (run_id, text, result["label"], result["score"])
        for text, result in zip(headlines, classified)
    ]
    cursor.executemany(
        "INSERT INTO headlines (run_id, text, label, score) VALUES (?, ?, ?, ?)",
        rows,
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
