#!/usr/bin/python3

import psycopg2

db = psycopg2.connect("dbname=news")

cursor = db.cursor()

select_table_query = '''select * from authors;'''

""" We can retrieve query result using cursor methods such as fetchone(), fetchmany(), fetcthall()."""


cursor.execute(select_table_query)
my_value = cursor.fetchall()
print(my_value)



cursor.close()
db.close()


