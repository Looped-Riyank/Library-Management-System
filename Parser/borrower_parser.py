import mysql.connector
import csv

# Define your MySQL database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "Library",
}

# Create a connection to the MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Open and read the CSV file
with open('borrowers.csv', 'r', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)
    
    for row in csvreader:
        card_id, ssn, first_name, last_name, email, address, city, state, phone = row
        
        # Define the SQL query to insert data into the BORROWERS table
        insert_query = "INSERT INTO BORROWERS (CARD_ID, SSN, FIRST_NAME, LAST_NAME, EMAIL, ADDRESS, CITY, STATE, PHONE) " \
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        
        # Execute the SQL query to insert the data
        cursor.execute(insert_query, (card_id, ssn, first_name, last_name, email, address, city, state, phone))

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Data inserted successfully.")
