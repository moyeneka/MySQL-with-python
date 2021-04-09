# MySQL-with-python

Objective
The goal of this assignment is to understand and practice using a high-level language (C++, Java, or Python) to interact with a database via ODBC or JDBC. Your goal is to write a program that runs from the command line. It interacts with an end-user to insert, delete, and update records as well as handle queries on the data. 
1) Find all suppliers and coffees names for a given country
2) Add a new supplier with item(s) that they provide, then show who else provides such item(s)
3) List all items sold by a particular employee
4) Update Item
5) Quit
Implementation
Create the same tables and fill them with the same data as in homework 3. This can be done at the mysql command line. Your program should assume that the database has been created and it has the initial set of tuples in it. You must create a function/method for each menu item. Create more functions/methods as needed for a clean, modular design. Create a program which offers the user the following operations:
Menu of operations

1) Find all suppliers and coffees name in a given country [ Menu option 1. Supplier by Country] Prompt the user for a country. Find and list all available suppliers and coffee from that location. Display all information of those suppliers and coffees.
Expected output:
Supplier ID, Supplier Name, Supplier Phone, Coffee name, Roasting Type
2) Add a new supplier, the show who else provides this item. [ Menu option 2. Add Supplier] Prompt the user to enter a new supplier with name, phone number and country. Add the supplier info to SUPPLIER Table and INVENTORY_MGMT. Please make sure that the new supplier sells one or more of the coffee names in ITEM. Then, prompt the supplier for the name of the coffee that they can provide.
Expected Output:
The full record for the new supplier.
The names of the other suppliers who supply the same coffee.
3) List all items sold by a specific employee [ Menu option 3. Employee Performance] Prompt the user to enter an employee name.
Expected Output:
If the employee is found, display all items sold by that employee that is (item name, roasting type, and total sales per item) for all items sold by that employee, if no item sold by that employee, output a message, e.g., No items sold by this employee

4) Update ITEM: This handles what happens when the company gets a new shipment or makes a sale. Prompt the user to enter the name of an item, update the availability of that item in INVENTORY_MGMT table.
Expected Output:
The name of the item and the quantity before and after the update.

5) Cancel Sales: 
Prompt the user to enter a Transaction ID to cancel sales. It is important to note that you should not delete any transactions, but they should be indicated as cancelled and the items in that sale returned to the inventory. Consider all tables that are affected by this transaction. You may need to update the database scheme.
Expected Output:
Your testing should show the affected tables before and after a cancelled sale.

6) Quit
Disconnect from the database and exit the program.
