CREATE TABLE IF NOT EXISTS Restaurant(
name TEXT,
neighbourhood TEXT,
cuisine TEXT,
review REAL,
PRICE TEXT,
health TEXT
);
INSERT INTO Restaurant(name, neighbourhood, cuisine, review, PRICE, health) VALUES
('The Gourmet Kitchen', 'Downtown', 'Chinese', 4.5, '$$$', 'A'),
('Sushi World', 'Uptown', 'Japanese', 4.7, '$$$$', ''),
('Burger Haven', 'Midtown', 'American', 4.2, '$$', 'B'),
('Candy shack', 'Downtown', 'Indian', 4.3, '$$', 'A'),
('Taco Fiesta', 'Uptown', 'Mexican', 4.0, '$', 'B'),
('Pasta Paradise', 'Midtown', 'Italian', 4.6, '$$$', 'A'),
('Dragon Wok', 'Downtown', 'Chinese', 4.1, '$$', ''),
('BBQ Barn', 'Uptown', 'American', 4.4, '$$$', 'A'),
('Vegan Candy', 'Midtown', 'Japanese', 3.6, '$$', 'A'),
('Seafood Shack', 'Downtown', 'Mexican', 3.0, '$$$$', 'A');
SELECT DISTINCT neighbourhood 
FROM Restaurant;
SELECT DISTINCT cuisine
FROM Restaurant;
SELECT *
FROM Restaurant 
WHERE cuisine = 'Chinese';
SELECT *
FROM Restaurant 
WHERE review >= 4.0;
SELECT *
FROM Restaurant 
WHERE cuisine = 'Italian'
AND PRICE IN ('$$', '$$$');
SELECT *
FROM Restaurant 
WHERE PRICE = '$$$';
SELECT *
FROM Restaurant 
WHERE name LIKE '%Candy%';
SELECT *
FROM Restaurant 
WHERE neighbourhood IN ('Downtown', 'Uptown');
SELECT *
FROM Restaurant 
WHERE health = '';
SELECT *
FROM Restaurant 
ORDER BY review DESC LIMIT 4;




