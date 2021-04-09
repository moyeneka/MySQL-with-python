CREATE TABLE Supplier(
SupplierID int, 
Name char(50) NOT NULL,
PhoneNumber  char(25) NOT NULL,
Address varchar(50) NOT NULL,
PRIMARY KEY 	(SupplierID),
CHECK (SupplierID>= '1' AND SupplierID<='10')
);

CREATE TABLE Item(
ItemID int, 
Name char(50) NOT NULL,
PricePerLb  decimal(5,2) NOT NULL,
RoastingType char(1) ,
PRIMARY KEY 	(ItemID),
CHECK (ItemID>= '1' AND ItemID<='13')
);

CREATE TABLE Employee(
EmployeeID int,
Name char(50) NOT NULL,
Occupation  char(25) NOT NULL,
PhoneNumber  char(25) NOT NULL,
Address varchar(50) NOT NULL,
PRIMARY KEY 	(EmployeeID),
CHECK (EmployeeID>= '1' AND EmployeeID<='10')
);

CREATE TABLE Sales(
TransId  int,
ItemID int,
Discount int NOT NULL,
PurchaseDate  date NOT NULL,
EmployeeID int,
PRIMARY KEY 	(TransId), 
FOREIGN KEY (ItemID) 
	REFERENCES Item(ItemID),
FOREIGN KEY (EmployeeID)
	REFERENCES Employee(EmployeeID)
);

CREATE TABLE InventoryMGMT(
ItemID int,
SupplierID int,
TotalItemSales3Months int NOT NULL,
TotalAvailable int NOT NULL,
PRIMARY KEY 	(ItemID,SupplierID ), 
FOREIGN KEY (ItemID) 
	REFERENCES Item(ItemID),
FOREIGN KEY (SupplierID) 
	REFERENCES Supplier(SupplierID)
);