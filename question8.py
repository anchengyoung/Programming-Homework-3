import sqlite3

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def GetCustomer():
    conn = sqlite3.connect("northwind.sqlite")
    cur = conn.cursor()
    query = "SELECT ContactName FROM Customer;"
    cur.execute(query)
    return [r[0] for r in cur.fetchall()]

names_to_check = []

for name in GetCustomer():
    if not is_ascii(name):
        print(name)
        names_to_check.append(name)
