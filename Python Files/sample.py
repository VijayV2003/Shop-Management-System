import mysql.connector as sql
import datetime
conn=sql.connect(host='localhost',user='root',passwd='manager',database='electronics')
#if conn.is_connected():
 # print("Successfully Connected")
c1=conn.cursor()
c1.execute("select Product_name,Product_no from elect")
data=c1.fetchall()
print("Product name      Product number")
for i in data:
    print(i)
