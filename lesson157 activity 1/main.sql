CREATE TABLE IF NOT EXISTS Salesman(
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Commision TEXT
);
INSERT INTO Salesman(Salesman_id, name, city, Commision) VALUES
(5001, 'James', 'New York', 0.15),
(5002, 'Robert', 'Los Angeles', 0.12),
(5003, 'Michael', 'Chicago', 0.10),
(5004, 'William', 'Houston', 0.08),
(5005, 'David', 'Phoenix', 0.05),
(5006, 'Richard', 'Philadelphia', 0.07),
(5007, 'Joseph', 'San Antonio', 0.09),
(5008, 'Thomas', 'San Diego', 0.11),
(5009, 'Charles', 'Dallas', 0.13),
(5010, 'Christopher', 'San Jose', 0.14);    
CREATE TABLE IF NOT EXISTS Customer(
    Customer_id TEXT ,
    name TEXT PRIMARY KEY,
    city TEXT,
    grade TEXT,
    Salesman_id TEXT,
    );
    INSERT INTO Customer(Customer_id, name, city, grade, Salesman_id) VALUES
(3001, 'John', 'New York', 100, 5001),
(3002, 'Alice', 'Los Angeles', 200, 5002),  
(3003, 'Bob', 'Chicago', 150, 5003),
(3004, 'Eve', 'Houston', 250, 5004),
(3005, 'Charlie', 'Phoenix', 300, 5005),
(3006, 'David', 'Philadelphia', 350, 5006),
(3007, 'Frank', 'San Antonio', 400, 5007),
(3008, 'Grace', 'San Diego', 450, 5008),
(3009, 'Hannah', 'Dallas', 500, 5009),
(3010, 'Ivy', 'San Jose', 550, 5010
);
CREATE TABLE IF NOT EXISTS Orders(
    Order_id TEXT PRIMARY KEY,
    purch_amt TEXT,
    ord_date TEXT,
    Customer_id TEXT,
    Salesman_id TEXT
    );
    INSERT INTO Orders(Order_id, purch_amt, ord_date, Customer_id, Salesman_id) VALUES
(7001, 1500, '2023-01-15', 3001, 5001),
(7002, 2000, '2023-02-20', 3002, 5002),
(7003, 2500, '2023-03-10', 3003, 5003),
(7004, 3000, '2023-04-05', 3004, 5004),
(7005, 3500, '2023-05-12', 3005, 5005),
(7006, 4000, '2023-06-18', 3006, 5006),
(7007, 4500, '2023-07-22', 3007, 5007),
(7008, 5000, '2023-08-30', 3008, 5008),
(7009, 5500, '2023-09-15', 3009, 5009),
(7010, 6000, '2023-10-10', 3010, 5010);

SELECT Customer.cust_name , salesman.name,salesman.city
FROM Customer
JOIN Salesman ON Customer.city = Salesman.city;

SELECT Customer.cust_name, Salesman.name, Salesman.city
FROM Customer
JOIN Salesman ON Customer.salesman_id = Salesman.salesman_id;

SELECT Orders.ord_no,Customer.cust_name
FROM Orders 
JOIN Customer ON Orders.customer_id = Customer.customer_id
JOIN Salesman ON Orders.salesman_id = Salesman.salesman_id
WHERE Customer.grade IS NOT NULL ;

SELECT Customer.cust_name AS "Customer",
Customer.city AS "CITY",
Salesman.name AS "Salesman",
Salesman.commission
FROM Customer
JOIN Salesman ON Customer.salesman_id = Salesman.salesman_id
WHERE Salesman.commision BETWEEN 0.12 AND 0.14;


