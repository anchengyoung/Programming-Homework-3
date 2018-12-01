import sqlite3
conn = sqlite3.connect("northwind.sqlite")
cur = conn.cursor()
query = "SELECT name FROM sqlite_master WHERE type = 'table';"
cur.execute(query)
print(cur.fetchall())
