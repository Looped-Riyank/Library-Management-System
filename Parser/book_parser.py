import mysql.connector

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

# Process and insert data
fileObj = open('books.csv', 'r', encoding="utf-8")
text_file = list(fileObj)
author_id = 0
author_list = []

for line in text_file[1:]:
    line = line.strip()
    column_list = line.split('\t')
    ISBN13 = column_list[1]
    Title = column_list[2]
    authors = column_list[3]

    # Insert book information
    insert_book_query = "INSERT INTO Books (ISBN13, Title) VALUES (%s, %s);"
    cursor.execute(insert_book_query, (ISBN13, Title))

    authors = authors.replace(";",",").split(',')
    
    for author in authors:
        author = author.strip()  # Remove leading/trailing spaces

        # Check if the author name is not empty
        if author:
            if author not in author_list:
                # Insert author information
                author_id += 1
                insert_author_query = "INSERT INTO Authors (Author_id, Name) VALUES (%s, %s);"
                cursor.execute(insert_author_query, (author_id, author))
                author_list.append(author)
            
            # Insert the relationship between book and author
            insert_relationship_query = "INSERT INTO Book_authors (Author_id, ISBN13) VALUES (%s, %s);"
            cursor.execute(insert_relationship_query, (author_id, ISBN13))
        else:
            # Handle the case where the author's name is empty or null
            print("Author name is empty or null. Skipping insertion.")
    # ...

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
