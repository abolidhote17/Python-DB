import mysql.connector

con=mysql.connector.connect(host='b05apdlzjpvvjwna024q-mysql.services.clever-cloud.com',user='u5ngrimxbf6r50pq',password='18uYqjKe4wwKVO4Ix3Zb',database='b05apdlzjpvvjwna024q')
curs=con.cursor()

ct=input('Enter Category to search list: ')

curs.execute("select * from Books where Category='%s'" %ct)
data=curs.fetchall()

if data:
    for rec in data:
        print('Books of category %s' %ct)
        print(rec[1])
if not data:
    print("Not Found")

con.close()

