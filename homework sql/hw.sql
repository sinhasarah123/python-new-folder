CREATE TABLE IF NOT EXISTS CUSTOMERS(
NAME TEXT,
PRODUCT TEXT,
COUNTRY TEXT
);
INSERT INTO CUSTOMERS (NAME, PRODUCT, COUNTRY) VALUES
('John', 'Burger', 'Netherlands'),
('Alice', 'Pasta', 'Italy'),
('Bob', 'Sushi', 'Japan'),
('Emma', 'Salad', 'France'),
('David', 'Steak', 'Australia'),
('Lily', 'Chicken', 'Vietnam'),
('Oran', 'Sandwich', 'USA'),
('Caroline', 'Pizza', 'USA'),
('Sarah', 'Coffee', 'Spain'),
('TOry', 'Tea', 'Ireland');
SELECT *
FROM CUSTOMERS 
WHERE NAME LIKE '%Or%';
SELECT *
FROM CUSTOMERS
WHERE NAME LIKE '%a%';
