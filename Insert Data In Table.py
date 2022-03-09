import sqlite3

conn = sqlite3.connect("Database.db")

cr = conn.cursor()

cr.execute(""" CREATE TABLE IF NOT EXISTS customer(
    firstname text,
    lastname text,
    email text
) """)

cr.execute(
    "INSERT INTO customer VALUES (:fname, :lname, :email)",
    {
        "fname" : "",
        "lname" : "",
        "email" : ""
    }
)




# Here we will commit our database
conn.commit()

# Here we will close our database
conn.close()