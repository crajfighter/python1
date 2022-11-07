                                                                # HOTEL MANAGEMENT SYSTEM #

import pymysql
class Connection:
    def __init__(self):
    
        try:
            self._conn=pymysql.connect(host="localhost",user="root",password="",db="hotel")

        except  Exception as e:
            
            print(e)

        else:
             print("Connection Created Successfully")

class Check_in(Connection):
    def __init__(self):
        super().__init__()
        cur=self._conn.cursor()
        a=input("Days:")
        b=input("Names:")
        c=input("Aadhaar Number:")
        d=input("Date:")
        e=input("Enter Number:")
        
        sql="insert into check_in values(%s,%s,%s,%s,%s)"
        data=(a,b,c,d,e)
        cur.execute(sql,data)
        self._conn.commit()
        print("Data Entered Successfully")
        
        self._conn.close()

class Check_out(Connection):
    def __init__(self):
        super().__init__()
        cur=self._conn.cursor()
        f=input("Enter Number:")
        g=input("Guest:")
        h=input("Fare:")
        i=input("Days:")
        j=input("Total Bill:")
        k=input("Data:")
        
        sql2="insert into check_out values(%s,%s,%s,%s,%s,%s)" 
        data2=(f,g,h,i,j,k)
        cur.execute(sql2,data2)
        self._conn.commit() 
        print("Checked Out Successfully:")
        self._conn.close()


while True:
    choice=int(input("Enter Your Choices:"))
    if choice==1:
        Check_in()

    elif choice==2:
        Check_out()

    else:
        print("Invalid Choice:")

    ans=input("continuous......y/n")
    ans=ans.lower()
    if ans!='y':
        break;


print("///////////////////////////////////////////////////*******Bank Management System*******\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

    
