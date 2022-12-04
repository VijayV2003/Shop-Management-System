import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='manager')
c1=conn.cursor()
c1.execute("create database electronics")
print("data base created")
