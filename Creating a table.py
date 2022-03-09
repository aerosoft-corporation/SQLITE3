# So now here we will create a table in our database
# And see how our database is works
import sqlite3

# Here we are connected to our database
conn = sqlite3.connect("Database.db")

# Here we will create a cursor
cr = conn.cursor()

# Here we will creates our database tables
cr.execute(""" CREATE TABLE customer(
    firstname text,
    lastname text,
    email text
) """)

# Total datatypes in sqlite3 is 5
# 1. NULL - If exist then not null
# 2. INTEGER - 0 TO 9
# 3. REAL - Between number
# 4. TEXT - A to Z
# 5. BLOB - Images, File, Audio, Video etc



# Here we will commit our database
conn.commit()

# Here we will close our database
conn.close()