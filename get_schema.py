import sqlite3

conn = sqlite3.connect(r'C:\Users\HP\.gemini\antigravity\scratch\startupmap-scraper\startupmap.db')
conn.row_factory = sqlite3.Row

print("=== STARTUPS TABLE ===")
r_startups = conn.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='startups'").fetchone()
if r_startups:
    print(r_startups[0])

print("\n=== JOBS TABLE ===")
r_jobs = conn.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='jobs'").fetchone()
if r_jobs:
    print(r_jobs[0])

conn.close()
