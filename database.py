import sqlite3

#create sql database
conn = sqlite3.connect('test.db')

#or use an existing database in memory
#conn = sqlite3.connect(':memory:')

#create a cursor
c = conn.cursor()

#create table 
c.execute("""CREATE TABLE customers (
		first_name text,
		last_name text,
		email text,
		value real
	)""")

#commit
conn.commit()

#close
conn.close()

