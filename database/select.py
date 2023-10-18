import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

# for row in cursor.execute("SELECT * FROM User"):
cursor.execute("SELECT * FROM User")
# print(next(cursor))
# print(next(cursor))
# print(cursor.fetchall())
# print(next(cursor))
    # print(row)

print(cursor.fetchone())
print(cursor.fetchone())