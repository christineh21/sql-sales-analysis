import csv
import sqlite3

conn = sqlite3.connect("sales.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS sales")
cur.execute("""
    CREATE TABLE sales (
        order_id   INTEGER PRIMARY KEY,
        order_date TEXT,
        customer   TEXT,
        category   TEXT,
        product    TEXT,
        quantity   INTEGER,
        price      REAL
    )
""")

with open("sales.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute(
            "INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                int(row["order_id"]),
                row["order_date"],
                row["customer"],
                row["category"],
                row["product"],
                int(row["quantity"]),
                float(row["price"]),
            ),
        )

conn.commit()
count = cur.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
conn.close()

print(f"Loaded {count} rows into sales.db")
