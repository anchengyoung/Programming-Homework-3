import sqlite3
conn = sqlite3.connect("northwind.sqlite")
cur = conn.cursor()
query = "SELECT ProductName FROM Product WHERE ProductName LIKE '%chocolate%'"
cur.execute(query)
results = (cur.fetchall()[0][0])
print(results.lower().replace('chocolate','CHOCOLATE'))
