import mysql.connector

con=mysql.connector.connect(host='b05apdlzjpvvjwna024q-mysql.services.clever-cloud.com',user='u5ngrimxbf6r50pq',password='18uYqjKe4wwKVO4Ix3Zb',database='b05apdlzjpvvjwna024q')
curs=con.cursor()

print("Name the Author And Publication: ")
at=input("Author: ")
pb=input("Publication: ")

curs.execute("select * from Books where Author='%s' and Publication='%s'"%(at,pb))
data=curs.fetchall()
if data:
    print(data)
else:
    print("Book is not available")

con.close()