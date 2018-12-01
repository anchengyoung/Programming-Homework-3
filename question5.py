import sqlite3
conn = sqlite3.connect("northwind.sqlite")
cur = conn.cursor()
query = "SELECT Country, COUNT(*) FROM Customer GROUP BY Country;"
cur.execute(query)
print(cur.fetchall())
