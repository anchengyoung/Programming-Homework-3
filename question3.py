import sqlite3
conn = sqlite3.connect("northwind.sqlite")
cur = conn.cursor()
exchange_rate = 0.87
query = "SELECT ProductName, UnitPrice, UnitPrice *" + str(exchange_rate) + " AS EuroPrice FROM Product LIMIT 10;"
cur.execute(query)
print(cur.fetchall())
