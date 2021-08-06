import sqlite3
connection=sqlite3.connect('Movies.db')
cursor=connection.cursor()


command1=""" CREATE TABLE IF NOT EXISTS Movies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT, director TEXT,year INTEGER) """

cursor.execute(command1)


cursor.execute(" INSERT INTO Movies VALUES ('Dhoom 3','Amir Khan','Katrina Kaif',' Vijay Krishna Acharya',2013)")
cursor.execute(" INSERT INTO Movies VALUES ('Don','Amitabh Bachchan','Zeenat Aman','Chandra Barot',1978)")
cursor.execute(" INSERT INTO Movies VALUES ('Swades','Sharukh Khan','Gayatri Joshi','Ashutosh Gowariker',2004)")
cursor.execute(" INSERT INTO Movies VALUES ('3 Idiots','Amir Khan','Kareena Kapoor',' Rajkumar Hirani',2009)")



cursor.execute("SELECT * FROM Movies")
results=cursor.fetchall()

cursor.execute("SELECT * FROM Movies WHERE actor='Amitabh Bachchan'")
results2=cursor.fetchall()

#print the results
print('Movies: \n', results)
print('\n')
print("Information:\n",results2)
