import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1212",
    database="movies name"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE intresting_movies (name VARCHAR(256), Lead_Actor CHAR(20), Actress CHAR(20), Year int,director_name char(20))")

mycursor.excute("SHOW TABLE")
for td in mycursor:
    print(tb)