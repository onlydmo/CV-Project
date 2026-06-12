import sqlite3

conn = sqlite3.connect('C:\\Users\\HP\\..\\..\\..\\Users\\HP\\.gemini\\antigravity\\scratch\\startupmap-scraper\\startupmap.db')
conn.row_factory = sqlite3.Row

# Get schema of startups table
print("--- Startups columns ---")
cursor = conn.execute("PRAGMA table_info(startups)")
for row in cursor.fetchall():
    print(dict(row))

print("\n--- A sample row from startups ---")
sample = conn.execute("SELECT * FROM startups LIMIT 1").fetchone()
if sample:
    print(dict(sample))

conn.close()
