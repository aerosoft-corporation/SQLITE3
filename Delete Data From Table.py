import sqlite3

conn = sqlite3.connect("Database.db")

cr = conn.cursor()

cr.execute(""" CREATE TABLE IF NOT EXISTS customer(
    firstname text,
    lastname text,
    email text
) """)

n = int(input("Enter ID Number : "))

cr.execute(
    "DELETE FROM customer WHERE oid = " + str(n)
)

add = cr.execute(
    "SELECT *, oid FROM customer"
)

for i, j, k, l in add:
    print(
        f"FirstName: {i}, LastName: {j}, Email: {k}, ID: {l}"
    )




# Here we will commit our database
conn.commit()

# Here we will close our database
conn.close()