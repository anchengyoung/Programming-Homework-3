import sqlite3
conn = sqlite3.connect("northwind.sqlite")
cur = conn.cursor()
exchange_rate = 0.87
query = "CREATE TABLE ConvertPrice AS SELECT ProductName, UnitPrice, UnitPrice * " + str(exchange_rate) + " AS EuroPrice FROM Product;"
cur.execute(query)
print(cur.fetchall())
