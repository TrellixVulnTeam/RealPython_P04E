#JOIN

import sqlite3

with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	
	c.execute("""SELECT population.city,\
	population.population, regions.region FROM\
	population, regions WHERE population.city=regions.city order by\
	population.city ASC""")
	
	rows=c.fetchall()
	
	for r in rows:
		print(r[0],r[1],r[2])
