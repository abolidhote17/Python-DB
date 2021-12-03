import mysql.connector

con=mysql.connector.connect(host='b05apdlzjpvvjwna024q-mysql.services.clever-cloud.com',user='u5ngrimxbf6r50pq',password='18uYqjKe4wwKVO4Ix3Zb',database='b05apdlzjpvvjwna024q')
curs=con.cursor()

cd=int(input("Enter Bookcode to see details: "))
try:
    curs.execute("select * from Books where Bookcode=%d"%cd)
    data=curs.fetchall()
    for rec in data:
        print("Bookcode      :%d"%rec[0])
        print("Bookname      :%s"%rec[1])
        print("Category      :%s"%rec[2])
        print("Author        :%s"%rec[3])
        print("Publication   :%s"%rec[4])
        print("Edition       :%s"%rec[5])
        print("Price         :%d"%rec[6])
except:
    print("NOT FOUND")

con.close()