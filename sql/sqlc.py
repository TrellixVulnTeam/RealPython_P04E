#Create sqlite3 dba nd table

import sqlite3

with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	#insert multiple records using a tuple
	cities = (\
	('Boston', 'MA', 600000),
	('Chicago', 'IL', 2700000),
	('Houston', 'TX', 2100000),
	('Phoenix', 'AZ', 1500000))
	
	#print(cities)
	c.executemany('INSERT INTO population VALUES(?,?,?)',cities)

# c.execute('SELECT * from population')
# for row in c.fetchall():
	# print(row)