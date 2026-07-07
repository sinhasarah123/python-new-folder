CREATE TABLE Persons(
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
INSERT INTO Persons(PersonID,LastName,FirstName,Address,City) VALUES(1,'Doe','John','123 Main St','Anytown');
INSERT INTO Persons(PersonID,LastName,FirstName,Address,City) VALUES(2,'Sinha','Sarah','12345','bangalore');
INSERT INTO Persons(PersonID,LastName,FirstName,Address,City) VALUES(3,'joules','cat','16767','bangalore');
SELECT * FROM Persons;

SELECT FirstName,City FROM Persons WHERE City='bangalore';
