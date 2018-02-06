#version 3.6 to high!!!
print ('before')
import pymssql
import hello
# import sqlserver
# import sqlservice
print ('after')

server="127.0.0.1"
database="GiantSql"
user="sa"
password="sbf"

# conn = pymssql.connect(server, user, password, database)
conn = pymssql.connect(server, user, password, database)
print ('con')
cursor = conn.cursor()
print ('cursor')
# cursor.execute('SELECT * FROM dictionarys WHERE id!=%s', '2')
str="SELECT TOP 1000 * FROM [GiantSql].[dbo].[Dictionarys]"
cursor.execute(str)
row = cursor.fetchone()
print ('en' + row)
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()