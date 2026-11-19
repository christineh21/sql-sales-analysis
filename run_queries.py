import sqlite3

conn = sqlite3.connect("sales.db")

with open("queries.sql", encoding="utf-8") as f:
    sql = f.read()

# strip comments, split into statements
lines = [line for line in sql.splitlines() if not line.strip().startswith("--")]
statements = [s.strip() for s in "\n".join(lines).split(";") if s.strip()]

for i, statement in enumerate(statements, start=1):
    print(f"\n{'=' * 60}")
    print(f"Query {i}")
    print("=" * 60)

    cursor = conn.execute(statement)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    print(" | ".join(columns))
    print("-" * 60)
    for row in rows:
        print(" | ".join(str(value) for value in row))

conn.close()
