import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('test1.db')
sth = connection.cursor()

# Create table (with correct syntax)
sth.execute('create table sample_data(id INT, name varchar(255), age INT, city VARCHAR(255))')

# Insert sample records
sth.execute("insert into sample_data(id, name, age, city) values (101, 'arun', 30, 'city1')")
sth.execute("insert into sample_data(id, name, age, city) values (102, 'vijay', 25, 'city2')")
sth.execute("insert into sample_data(id, name, age, city) values (103, 'leo', 33, 'city3')")
sth.execute("insert into sample_data(id, name, age, city) values (104, 'raj', 40, 'city4')")

# Commit changes and close connection
connection.commit()
connection.close()