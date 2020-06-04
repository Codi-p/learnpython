# python
# The basic skill of Build Database
# There are two ways to using a database.
# 1. use 'sqlite3'  build a memory database
# 2. use commercial database
# 3. 

import os
import sys
import sqlite3


con = sqlite3.connect(":memory:")
query = """CREATE TABLE sales
                (customer VARCHAR(20),
                 product VARCHAR(40),
                 amount FLOAT,
                 date DATE);"""
con.execute(query)
con.commit()

data =[('Richard Lucas','Notepad',2.50,'2020-01-02'),
       ('Jenny Kim','Binder',4.15,'2020-01-15'),
       ('Svetlana Crow','Computer',375.00,'2020-03-11'),
       ('Stephen Randolph','Print',789,'2020-04-25'),
       ('Tony Cheng','Pen',0.50,'2020-02-13')]
statement = "INSERT INTO sales VALUES(?,?,?,?)"
con.executemany(statement, data)
con.commit()

cursor =con.execute("SELECT * FROM sales")
rows =cursor.fetchall()

row_counter =  0
for row in rows:
    print(row)
    row_counter +=1
print('Number of rows: %d' %(row_counter))

