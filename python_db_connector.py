# Micheal oyenekan

import mysql.connector
from tabulate import tabulate
           
def open_database (hostname,user_name,mysql_pw,database_name):
      global conn
      conn= mysql.connector.connect(host= hostname, 
      user= user_name,  
      password= mysql_pw, 
      database= database_name 
    ) 
      global cursor
      cursor = conn.cursor() 

def printFormat(result):
    header=[]
    for cd in cursor.description:# get headers
        header.append(cd[0])
    print('')
    print('Query Result:')
    print('')
    print(tabulate(result, headers=header))# print results in table format

# select and display query
def executeSelect (query):
    cursor.execute(query)
    printFormat(cursor.fetchall())

def  insert(table,values):
     query ="INSERT into " + table + " values (" + values + ")" +';'
     cursor.execute(query)
     conn.commit()


def executeUpdate(query): # use this function for delete and update
    cursor.execute(query)
    conn.commit()


def close_db ():  # use this function to close db
    cursor.close()
    conn.close()

##### Test #######
mysql_username = 'moyeneka' # please change to your username
mysql_password =''  # please change to your MySQL password

open_database('localhost',mysql_username,mysql_password,mysql_username) # open database   

print(' ')
print('Menu: ')
print("1: Suppliers by Country")
print("2: Add Supplier")
print("3: Employee Performance")
print("4: Update Item")
print("5: Cancel Sales")
print("q: Quit the program")
option = ""
while option != "q":
    option = input("Select an option: ")
    if option == "1":
       country = input("Enter a country: ")
       executeSelect("select s.SupplierID, s.Name, PhoneNumber, i.Name, RoastingType from Item i, Supplier s," +
                      "InventoryMGMT where i.ItemID = im.ItemID and im.SupplierID = s.SupplierID and Address= '" + country +"'" +";")
    elif option == "2":
        Name = input("Enter supplier Name: ")
        PhoneNumber = input("Enter supplier PhoneNumber: ")
        country = input("Enter supplier Country: ")
        print("-------Coffee Name------")
        executeSelect("select Name from Item")
        coffeeName = input("Enter Coffee Name from the above ouput: ")
        cursor.execute("SELECT Max(SupplierID) FROM Supplier")
        maxId = cursor.fetchone()[0]
        maxID = maxId + 1    
        sql = "INSERT INTO Supplier VALUES (%s, %s, %s,%s)"
        args= maxID, Name, PhoneNumber, country
        cursor.execute(sql, args) 
        conn.commit()
        cursor.execute("SELECT ItemID FROM Item where Name= '" + coffeeName+ "'" +";")
        ItemID = cursor.fetchone()[0]
        sql = "INSERT INTO InventoryMGMT VALUES (%s, %s, %s,%s)"
        TotalItemSales3Months = 0
        TotalAvailable = 0
        args= ItemID,maxID, TotalItemSales3Months, TotalAvailable
        cursor.execute(sql, args) 
        conn.commit()
        executeSelect("SELECT SupplierID, Name, PhoneNumber, Address FROM Supplier where SupplierID =" + str(maxID) + ";" )
        executeSelect("SELECT s.Name, i.Name FROM Supplier s, Item i, InventoryMGMT im where i.ItemID = im.ItemID and im.SupplierID = s.SupplierID and i.Name =" +  "'" + coffeeName + "'" +";")
       
    elif option == "3":
       print('=======================================')
    else:
        print('=======================================')

close_db()# close database






