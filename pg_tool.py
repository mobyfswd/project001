#!/usr/bin/python3

import psycopg2

db = psycopg2.connect("dbname=news")

cursor = db.cursor()

select_table_query = '''select * from authors;'''


join_table_query = '''select title, name
from articles, authors
where articles.author = authors.id;'''

join_table_query_2 = '''
select title, name
from articles join authors
on articles.author = authors.id;
'''


""" We can retrieve query result using cursor methods such as fetchone(), fetchmany(), fetcthall()."""


def run_cursor_fa(a_query):
    """ execute an existing query and return the fetchall results from the cursor

    """
    cursor.execute(a_query)

    return cursor.fetchall()


def output_to_screen(results):
    """
    output to the screen the results of a db query
    """ 
    print()
    print("[*] ", end='')
    print(str(results))


if __name__ == '__main__':

    print('in main')

# TODO: indent properly later when not using vim as editor
# output select using sql
output_to_screen(run_cursor_fa(select_table_query))

#output join using sql
output_to_screen(run_cursor_fa(join_table_query))

#output join using different sql
output_to_screen(run_cursor_fa(join_table_query_2))

cursor.close()
db.close()


