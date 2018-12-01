import sqlite3
conn = sqlite3.connect("northwind.sqlite")
cur = conn.cursor()

def GetCustomer(name):
    query = "SELECT ContactName, Address, Country FROM Customer WHERE ContactName = '%s';" %name
    cur.execute(query)
    return cur.fetchall()[0]

def GetCountry(name):
    query = "SELECT Country FROM Customer WHERE ContactName = '%s';" %name
    cur.execute(query)
    return cur.fetchall()[0]

def SameCountry(country):
    query = "SELECT ContactName FROM Customer WHERE Country = '%s';" %country
    cur.execute(query)
    return [r[0] for r in cur.fetchall()]

input = 'Maria Anders'

print(
"""Dear %s,

Our records indicate that you currently live at %s, which is
in %s. Our records indicate that the following customers are
also from your country:
""" %GetCustomer(input))

for name in SameCountry(GetCountry(input)):
    if name != input:
        print(name)

print("""
Sincerely,
A company that handles your data carelessly""")
