# Technical Dependiencies

Flask==3.0.0
Flask_Cors==4.0.0
mysql_connector_repackaged==0.3.1
pandas==2.1.3

python3
MySQL
pip3

# THE COMMANDS GIVEN BELOW ARE TESTED FOR MACOS 14 Sonoma

1. Create a database connection to mysql server.

2. Run the following queries

CREATE DATABASE Library;

USE Library;

CREATE TABLE BOOKS (
    ISBN13 VARCHAR(13) PRIMARY KEY,
    TITLE VARCHAR(255) NOT NULL,
    AVAILABLE TINYINT(1) DEFAULT 1
);

CREATE TABLE AUTHORS (
    AUTHOR_ID INT PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL
);

CREATE TABLE BOOK_AUTHORS (
    ISBN13 VARCHAR(13),
    AUTHOR_ID INT,
    FOREIGN KEY (ISBN13) REFERENCES BOOKS(ISBN13),
    FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHORS(AUTHOR_ID)
);

CREATE TABLE BORROWERS (
    CARD_ID VARCHAR(10) PRIMARY KEY,
    SSN VARCHAR(11) UNIQUE,
    FIRST_NAME VARCHAR(255) NOT NULL,
    LAST_NAME VARCHAR(255) NOT NULL,
    EMAIL VARCHAR(255),
    ADDRESS VARCHAR(255) NOT NULL,
    CITY VARCHAR(255) NOT NULL,
    STATE VARCHAR(2) NOT NULL,
    PHONE VARCHAR(15)
);

-- Create BOOK_LOANS Table
CREATE TABLE BOOK_LOANS (
    LOAN_ID INT AUTO_INCREMENT PRIMARY KEY,
    ISBN13 VARCHAR(13),
    CARD_ID VARCHAR(10),
    DATE_OUT DATE NOT NULL,
    DUE_DATE DATE NOT NULL,
    DATE_IN DATE,
    FOREIGN KEY (ISBN13) REFERENCES BOOKS(ISBN13),
    FOREIGN KEY (CARD_ID) REFERENCES BORROWERS(CARD_ID)
);

-- Create FINES Table
CREATE TABLE FINES (
    LOAN_ID INT,
    FINE_AMT DECIMAL(10, 2) NOT NULL,
    PAID TINYINT(1) DEFAULT 0,
    FOREIGN KEY (LOAN_ID) REFERENCES BOOK_LOANS(LOAN_ID)
);

3. Now go to the Parser directory and run the following commands to insert data

python3 book_parser.py

python3 borrower_parser.py

4. Now go to the backend directory and run the following commands

To get the backend API code running, we need to do the following:

a. Install the required packages to run the code using the following command:

        pip3 install -r requirements.txt

b. Then we need to install the mysql-connector for python. Run the following command:

        pip install mysql-connector-python

c. To execute the backend API code, please run the sqlBackendAPI.py using the following command on the terminal:


        python sqlBackendAPI.py

5. Now go to the frontend directory and run the following command

To start the frontend interface, the following steps must be performed.

1. We need to install the node modules to start our frontend interface. cd into the frontend directory and run the following on the terminal.
    
        npm install

2. After installing the node modules, to start the frontend interface, run the following line on the terminal.

        npm start











