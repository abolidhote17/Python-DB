import mysql.connector

con=mysql.connector.connect(host='b05apdlzjpvvjwna024q-mysql.services.clever-cloud.com',user='u5ngrimxbf6r50pq',password='18uYqjKe4wwKVO4Ix3Zb',database='b05apdlzjpvvjwna024q')
curs=con.cursor()

'''
curs.execute("alter table Books add Review varchar(500)")
con.commit()
print("altered")
'''

cd=int(input("Enter Bookcode: "))
curs.execute("select*from Books where Bookcode=%d"%cd)
data=curs.fetchall()
if data:
    rev=input("Review: ")

    curs.execute("update Books set Review='%s' where bookcode=%d"%(rev,cd))
    con.commit()
    print("Review updated successfully")
else:
    print("Book not found")

con.close()