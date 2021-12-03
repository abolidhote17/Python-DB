import mysql.connector

try:
    cd=int(input('Enter a book code    : '))
    nm=input('Enter Book name          : ')
    ct=input('Enter category of book   : ')
    at=input('Enter name of Author     : ')
    pb=input('Enter Publication        : ')
    ed=input('Enter edition            : ')
    pr=float(input('Enter price of book: '))
    rw=input('Give Review: ')

    con=mysql.connector.connect(host='b05apdlzjpvvjwna024q-mysql.services.clever-cloud.com',user='u5ngrimxbf6r50pq',password='18uYqjKe4wwKVO4Ix3Zb',database='b05apdlzjpvvjwna024q')
    curs=con.cursor() 
    curs.execute("insert into Books values(%d,'%s','%s','%s','%s','%s',%.2f,'%s')"%(cd,nm,ct,at,pb,ed,pr,rw)) 
    con.commit()
    print("Book added successfully")
    con.close()

except:
    print("Invalid input...Please try again...")