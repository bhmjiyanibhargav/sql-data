#!/usr/bin/env python
# coding: utf-8
Question 1. What is a database? Differentiate between SQL and NoSQL databases. Answer : A database is a structured collection of data that can be accessed, managed, and updated easily. It serves as a central repository of information for an organization, making it easier to store, retrieve, and analyze data.

SQL and NoSQL are two different types of databases. SQL databases are relational databases that use Structured Query Language (SQL) for managing and querying data. They are typically used for applications where data is highly structured, and relationships between data are well defined. SQL databases are highly scalable and are commonly used in enterprise applications.

On the other hand, NoSQL databases are non-relational databases that do not use SQL for managing and querying data. They are typically used for applications where data is unstructured or semi-structured, and relationships between data are not well defined. NoSQL databases are highly scalable and can handle large amounts of data in real-time.

Some of the key differences between SQL and NoSQL databases include:

a. Data Structure: SQL databases store data in tables with predefined columns and data types, while NoSQL databases store data in documents, key-value pairs, or graphs. b. Scalability: SQL databases are vertically scalable, which means they can handle increased traffic by increasing the hardware resources of a single server. NoSQL databases are horizontally scalable, which means they can handle increased traffic by adding more servers to a cluster. c. Querying: SQL databases use SQL queries for managing and querying data, while NoSQL databases use proprietary APIs or query languages. d.ACID Compliance: SQL databases are generally ACID (Atomicity, Consistency, Isolation, Durability) compliant, which means they guarantee data consistency and integrity even in the event of system failures. NoSQL databases are generally BASE (Basically Available, Soft state, Eventually consistent) compliant, which means they prioritize availability and scalability over data consistency and integrity.

Overall, SQL databases are ideal for applications that require complex queries and transactions, while NoSQL databases are ideal for applications that require high scalability and performance.Question 2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example. Answer :DDL stands for Data Definition Language, which is a set of SQL statements used for defining the structure of a database and its objects such as tables, indexes, views, and procedures.

Here are some examples of commonly used DDL statements and their purposes:

A.CREATE: The CREATE statement is used to create a new database object such as a table, view, index, or procedure. For example, the following SQL statement creates a new table named "customers":

CREATE
   id INT PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   email VARCHAR(50) NOT NULL UNIQUE
);```
B.DROP: The DROP statement is used to delete an existing database object such as a table, view, index, or procedure. For example, the following SQL statement drops the "customers" table:

DROP TABLE customers;

C. ALTER: The ALTER statement is used to modify an existing database object such as a table, view, index, or procedure. For example, the following SQL statement adds a new column "phone" to the "customers" table:

ALTER TABLE customers ADD COLUMN phone VARCHAR(20);

D. TRUNCATE: The TRUNCATE statement is used to delete all data from an existing table, but it does not delete the table structure. For example, the following SQL statement deletes all data from the "customers" table:

TRUNCATE TABLE customers; In summary, DDL statements such as CREATE, DROP, ALTER, and TRUNCATE are used to define, modify, and delete database objects such as tables, views, indexes, and procedures. These statements are essential for managing the structure and contents of a database and ensuring data integrity and consistency.Question 3. What is DML? Explain INSERT, UPDATE, and DELETE with an example. Answer:DML stands for Data Manipulation Language, which is a set of SQL statements used for manipulating the data within a database. DML statements are used to insert, update, or delete data from the tables in a database.

Here are some examples of commonly used DML statements and their purposes:

A. INSERT: The INSERT statement is used to insert new data into a table. For example, the following SQL statement inserts a new row into the "customers" table: INSERT INTO customers (id, name, email) VALUES (1, 'John Doe', 'johndoe@example.com');

B. UPDATE: The UPDATE statement is used to update existing data in a table. For example, the following SQL statement updates the email address for the customer with id=1 in the "customers" table: UPDATE customers SET email='johndoe@gmail.com' WHERE id=1;

C. DELETE: The DELETE statement is used to delete data from a table. For example, the following SQL statement deletes the row with id=1 from the "customers" table: DELETE FROM customers WHERE id=1;

In summary, DML statements such as INSERT, UPDATE, and DELETE are used to manipulate the data within a database. These statements are essential for adding new data, modifying existing data, and removing unwanted data from the tables in a database.

Question 4. What is DQL? Explain SELECT with an example. Answwer. QL stands for Data Query Language, which is a set of SQL statements used for retrieving data from one or more tables in a database. DQL statements are used to query and retrieve data from the tables in a database.

Here is an example of a commonly used DQL statement: SELECT: The SELECT statement is used to retrieve data from one or more tables in a database. For example, the following SQL statement retrieves all the data from the "customers" table:

SELECT * FROM customers;

The asterisk (*) symbol in the SELECT statement represents all the columns in the "customers" table. You can also specify specific columns to retrieve by listing them after the SELECT keyword. For example, the following SQL statement retrieves only the "name" and "email" columns from the "customers" table:

Question 5. Explain Primary Key and Foreign Key. Answer :Primary Key and Foreign Key are important concepts in relational database design that help establish relationships between tables in a database.

A. Primary Key: A primary key is a column or set of columns in a table that uniquely identifies each row in that table. A primary key constraint ensures that the values in the primary key column(s) are unique and not null. A primary key is used to ensure data integrity and consistency by preventing duplicate rows and maintaining referential integrity.

For example, consider a "students" table with columns "id", "name", and "email". The "id" column can be set as the primary key to ensure that each student has a unique ID number:

CREATE
   id INT PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   email VARCHAR(50) NOT NULL
);```

B. `Foreign Key`:
    A foreign key is a column or set of columns in one table that refers to the primary key of another table. A foreign key constraint ensures that the values in the foreign key column(s) match the values in the primary key column(s) of the referenced table. A foreign key is used to establish relationships between tables and maintain referential integrity.

For example, consider a "courses" table with columns "id", "name", and "instructor_id". The "instructor_id" column can be set as a foreign key to refer to the "id" column in the "instructors" table:

```CREATE TABLE courses (
   id INT PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   instructor_id INT NOT NULL,
   FOREIGN KEY (instructor_id) REFERENCES instructors(id)
);```

In this example, the "instructor_id" column in the "courses" table refers to the "id" column in the "instructors" table. This establishes a relationship between the two tables and ensures that every instructor ID in the "courses" table corresponds to a valid ID in the "instructors" table.Question 6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method. Answer :In the below code, we first import the mysql.connector library and then use the mysql.connector.connect() method to connect to the MySQL database. We pass in the necessary connection details such as the hostname, username, password, and database name.

Next, we create a cursor object using the cursor() method of the database connection object. The cursor is a control structure that allows us to execute SQL queries and retrieve results.

We then use the execute() method of the cursor object to execute a SQL query. The SQL query is passed as an argument to the execute() method.

Finally, we use the fetchall() method of the cursor object to retrieve the results of the SQL query. The results are returned as a list of tuples. We then iterate through the list and display the results using a for loop.

In summary, the cursor() and execute() methods are used to execute SQL queries in Python. The cursor() method creates a cursor object, and the execute() method is used to execute SQL queries on the database using the cursor object.
# In[1]:


import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SQL query
mycursor.execute("SELECT * FROM customers")

# Fetch the results
result = mycursor.fetchall()

# Display the results
for row in result:
    print(row)

Question 7. Give the order of execution of SQL clauses in an SQL query. Answer : The order of execution of SQL clauses in an SQL query is as follows:

A. FROM: This clause specifies the tables from which data is to be retrieved.

b. JOIN: If the query involves a join, the join clause is executed next to combine the specified tables.

C. WHERE: This clause is used to filter the rows based on a specified condition.

D.GROUP BY: This clause is used to group the rows based on one or more columns.

E. HAVING: If the query involves a GROUP BY clause, the HAVING clause is used to filter the groups based on a specified condition.

F. SELECT: This clause is used to select the columns to be retrieved from the specified tables.

G. DISTINCT: If the query involves the DISTINCT keyword, it is executed after the SELECT clause to remove any duplicates.

H. ORDER BY: This clause is used to sort the results based on one or more columns.

I. LIMIT/OFFSET: These clauses are used to limit the number of rows returned or to skip a certain number of rows.

Note that not all SQL queries will necessarily use all of these clauses. The order of execution may also vary depending on the specific query and the database management system being used. However, the above order provides a general idea of the sequence in which the clauses are executed in an SQL query.

 
# In[ ]:




