import sqlite3

conn = sqlite3.connect('data/civicpulse.db')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print('Tables:', cur.fetchall())
cur.execute("PRAGMA table_info(complaints)")
print('Complaints schema:', cur.fetchall())
cur.execute('SELECT COUNT(*) FROM complaints')
print('Current count:', cur.fetchone()[0])
cur.execute('SELECT * FROM complaints LIMIT 2')
rows = cur.fetchall()
for r in rows:
    print(r)
conn.close()
