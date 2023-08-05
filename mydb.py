import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass123",
    autocommit=True
)



# Create a cursor object to execute SQL statements
cursor = cnx.cursor()

# Create a new database
database_name = "amirdevtest"
cursor.execute(f"CREATE DATABASE {database_name}")

# Close the cursor and connection
cursor.close()
cnx.close()
