#CS PROJECT FOR 2020-2021
#GROCERY STORE MANAGEMENT SYSETEM
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="123456",database="GROCERYSTORE5")
if mycon.is_connected():
    print("Successfully connected to mysql database")
mycursor=mycon.cursor()
database_query="Create database if not exists GROCERYSTORE5"
mycursor.execute(database_query)
print("_________________________________________________________________________________")


#_______________________________________________________________________________________
#CREATING TABLE CUSTOMER
CUSTOMER_query="Create table CUSTOMER(CUSTOMER_NAME varchar(30),MOBILE_NO varchar(15),PAYMENT_DUE float)"
mycursor.execute(CUSTOMER_query)
print("Table CUSTOMER Successfully Made")
C='y'
while C=='y':
        a=input("Enter the CUSTOMER_NAME")
        b=input("Enter the 10 digit MOBILE_NO.")
        c=float(input("Enter the PAYMENT_DUE"))
        CUSTOMER_insert_query="insert into CUSTOMER(CUSTOMER_NAME,MOBILE_NO,PAYMENT_DUE)values('{}','{}',{})".format(a,b,c)
        mycursor.execute(CUSTOMER_insert_query)
        mycon.commit()
        print("Customer Added Successfully")
        C=input("Do you wish to continue?")
        if C=='y':
            continue
        else:
            pass
        

print("_________________________________________________________________________________")


#_______________________________________________________________________________________
#CREATING TABLE PRODUCT
PRODUCT_query="Create table PRODUCT(PRODUCT_NAME varchar(30),PRODUCT_COST float)"
mycursor.execute(PRODUCT_query)
print("Table PRODUCT Successfully Made")
A='y'
while A=='y':
        d=input("Enter the PRODUCT_NAME")
        e=float(input("Enter the PRODUCT_COST"))
        PRODUCT_insert_query="insert into PRODUCT(PRODUCT_NAME,PRODUCT_COST)values('{}',{})".format(d,e)
        mycursor.execute(PRODUCT_insert_query)
        mycon.commit()
        print("Product Added Successfully")
        A=input("Do you wish to continue?")
        if A=='y':
            continue
        else:
            pass


print("_________________________________________________________________________________")


#_______________________________________________________________________________________
#CREATING TABLE WORKER
WORKER_query="Create table WORKER(WORKER_NAME varchar(30),WORKER_AGE integer,WORKER_YEARS float,WORKER_FAMILY integer)"
mycursor.execute(WORKER_query)
print("Table WORKER Successfully Made")
B='y'
while B=='y':
        f=input("Enter the WORKER_NAME")
        g=int(input("Enter the WORKER_AGE"))
        h=float(input("Enter the number of YEARS worked by the worker"))
        i=int(input("Enter the number of FAMILY MEMBERS of the worker"))
        WORKER_insert_query="insert into WORKER(WORKER_NAME,WORKER_AGE,WORKER_YEARS,WORKER_FAMILY)values('{}',{},{},{})".format(f,g,h,i)
        mycursor.execute(WORKER_insert_query)
        mycon.commit()
        print("Worker Added Successfully")
        B=input("Do you wish to continue?")
        if B=='y':
            continue
        else:
            pass


print("_________________________________________________________________________________")


#_______________________________________________________________________________________
#CREATING TABLE SUPPLIER 
SUPPLIER_query="Create table SUPPLIER(SUPPLIER_NAME varchar(30),SUPPLIER_AGE integer,SUPPLIER_YEARS float,SUPPLIER_CONTRACTC date,SUPPLIER_CONTRACTE date)"
mycursor.execute(SUPPLIER_query)
print("Table SUPPLIER Successfully Made")
D='y'
while D=='y':
        j=input("Enter the SUPPLIER_NAME")
        k=int(input("Enter the SUPPLIER_AGE"))
        l=float(input("Enter the number of YEARS of contract with the SUPPLIER"))
        m=input("Enter the date of COMMENCEMENT of the CONTACT with SUPPLIER")
        n=input("Enter the date of EXPIRY of the CONTACT with SUPPLIER")
        SUPPLIER_insert_query="insert into SUPPLIER(SUPPLIER_NAME,SUPPLIER_AGE,SUPPLIER_YEARS,SUPPLIER_CONTRACTC,SUPPLIER_CONTRACTE)values('{}',{},{},'{}','{}')".format(j,k,l,m,n)
        mycursor.execute(SUPPLIER_insert_query)
        mycon.commit()
        print("Supplier Added Successfully")
        D=input("Do you wish to continue?")
        if D=='y':
            continue
        else:
            pass


print("_________________________________________________________________________________")

#_______________________________________________________________________________________
#WRITING ON A CSV FILE FOR OFFERS
import csv
f=open("Offers.csv",'a')
f1=csv.writer(f)
W='y'
while W=='y':
        o=input("Enter the PRODUCT_NAME")
        p=int(input("Enter the percentage off on Product"))
        f1.writerow(['PRODUCT_NAME',o])
        f1.writerow(['OFFER AVAILABLE',p])
        print("Succesfully Written")
        W=input("Do you wish to continue?")
        if W=='y':
            continue
        else:
            pass

        f.close()
       
print("_________________________________________________________________________________")

#_______________________________________________________________________________________
#WRITING ON A TEXT FILE FOR STOCKS
f2=open("Stocks.txt",'a')
STOCKS=[]
str1=input("Enter stocks avilable for MILK in cartons")
str2=input("Enter stocks avilable for EGGS in cartons")
str3=input("Enter stocks avilable for BREAD in cartons")
str4=input("Enter stocks avilable for BUTTER in cartons")
STOCKS=[str1,str2,str3,str4]
f2.writelines(STOCKS)
print("Successfully Written")
f2.close()

print("_________________________________________________________________________________")

#_______________________________________________________________________________________
#WRITING ON A BINARY FILE FOR TRANSPORT DETAILS
import pickle
l=[]
n=int(input("Enter number of vehicles"))
for i in range(n):
    Transport={}
    TRANSPORT_NUMBER=input("Enter the TRANSPORT_NAME")
    TRANSPORT_TYPE=input("Enter the TRANSPORT_TYPE")
    Transport['TRANSPORT_NUMBER']=TRANSPORT_NUMBER
    Transport['TRANSPORT_TYPE']=TRANSPORT_TYPE
    l.append(Transport)
f3=open("Transport.dat",'ab')
pickle.dump(l,f3)
print("Successsfully loaded into the file")
f3.close()

print("_________________________________________________________________________________")

#_______________________________________________________________________________________
#MENU DRIVEN PROGRAM
print("GROCERY SHOP MANAGEMENT SYSTEM")
print("1 LOGIN")
print("2.EXIT")
choice=int(input("Enter your choice"))
if choice==1:
    user_name=input("Enter your user name")
    password=input("Enter your user password")
    if user_name=="Kashish" and password=="1233456":
        print("Successfully logged in")
    else:
        print("Incorrect user name and password")
    print("WELCOME TO 24x7 GROCERY SHOP")
    print("What would you like to do?")
    print("1.View Customer Details")
    print("2.View Product Details")
    print("3.View Worker Details")
    print("4.View Supplier Details")
    print("5.View Offers")
    print("6.View Stocks Available In Store")
    print("7.View Transport Details Available In Store")
    ch=int(input("What do you wish to do?"))
    
    print("_________________________________________________________________________________")


#_______________________________________________________________________________________
    if ch==1:
        CUSTOMER_View_query="Select * from CUSTOMER"
        mycursor.execute(CUSTOMER_View_query)
        for i in mycursor:
            print("Customer Deatils:",i)
        
        print("_________________________________________________________________________________")


#_______________________________________________________________________________________    
    elif ch==2:
        PRODUCT_View_query="Select * from PRODUCT"
        mycursor.execute(PRODUCT_View_query)
        for j in mycursor:
            print("Product Deatils:",j)
        
        print("_________________________________________________________________________________")


#_______________________________________________________________________________________    
    elif ch==3:
        WORKER_View_query="Select * from WORKER"
        mycursor.execute(WORKER_View_query)
        for k in mycursor:
            print("Worker Deatils:",k)
            
        print("_________________________________________________________________________________")


#_______________________________________________________________________________________    
    elif ch==4:
        SUPPLIER_View_query="Select * from SUPPLIER"
        mycursor.execute(SUPPLIER_View_query)
        for l in mycursor:
            print("Supplier Deatils:",l)
            
        print("_________________________________________________________________________________")


#_______________________________________________________________________________________    
    elif ch==5:
        import csv
        f=open("Offers.csv",'r')
        f1=csv.reader(f)
        for offers in f1:
            print("The Offers available in the store are",offers)
        f.close()
        
        print("_________________________________________________________________________________")


#_______________________________________________________________________________________
    elif ch==6:
        f2=open("Stocks.txt",'r')
        stocks=f2.read()
        print("The stocks available in the store are",stocks)
        f2.close()
        
        print("_________________________________________________________________________________")


#_______________________________________________________________________________________
    elif ch==7:
        import pickle
        f3=open("Transport.dat",'rb')
        x=pickle.load(f3)
        print("The Transport Details are",x)
        
        print("_________________________________________________________________________________")


#_______________________________________________________________________________________
        
        
elif choice==2:
       print("Thankyou for visiting!")
                 

print("_________________________________________________________________________________")


#_______________________________________________________________________________________       