import mysql.connector

con=mysql.connector.connect(host='b05apdlzjpvvjwna024q-mysql.services.clever-cloud.com',user='u5ngrimxbf6r50pq',password='18uYqjKe4wwKVO4Ix3Zb',database='b05apdlzjpvvjwna024q')
curs=con.cursor()

cd=int(input("Enter Bookcode: "))
pr=float(input("Enter price to change: "))  

curs.execute("select * from Books where bookcode=%d"%cd)
data=curs.fetchall()
if data:
    curs.execute("update Books set price=%.2f where Bookcode=%d"%(pr,cd))
    con.commit()
    print("price is changed")

else:    
    print("Book doesnot exist")

con.close()