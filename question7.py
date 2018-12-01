import sqlite3

def GetProduct(product_name):
    conn = sqlite3.connect("northwind.sqlite")
    cur = conn.cursor()
    query = "SELECT UnitPrice FROM Product WHERE ProductName = '%s';" %product_name
    cur.execute(query)
    return cur.fetchall()[0][0]

def CheckPrice(price):
    if price < 10:
        return "Cheap!"
    else:
        return ""

print(CheckPrice(GetProduct('Teatime Chocolate Biscuits')))
