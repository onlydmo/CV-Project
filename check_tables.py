import sqlite3

conn = sqlite3.connect('C:\\Users\\HP\\..\\..\\..\\Users\\HP\\.gemini\\antigravity\\scratch\\startupmap-scraper\\startupmap.db')
conn.row_factory = sqlite3.Row

# Get all tables
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:")
for row in cursor.fetchall():
    print(row['name'])
    # print schema
    c = conn.execute(f"PRAGMA table_info({row['name']})")
    print([r['name'] for r in c.fetchall()])

print("\nSample from jobs:")
j = conn.execute("SELECT * FROM jobs LIMIT 1").fetchone()
if j:
    print(dict(j))

conn.close()
