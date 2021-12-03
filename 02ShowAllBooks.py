import mysql.connector

con=mysql.connector.connect(host='b05apdlzjpvvjwna024q-mysql.services.clever-cloud.com',user='u5ngrimxbf6r50pq',password='18uYqjKe4wwKVO4Ix3Zb',database='b05apdlzjpvvjwna024q')
curs=con.cursor()
curs.execute("select * from Books")
data=curs.fetchall()

for rec in data:
    print(rec)

con.close()
    