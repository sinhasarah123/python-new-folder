CREATE TABLE IF NOT EXISTS companyrecords(
name TEXT,
SALARY INT,
AGE INT,
EXPERIENCE INT,
COLLEGE TEXT

);
INSERT INTO companyrecords (name, SALARY,AGE, EXPERIENCE, COLLEGE) VALUES
('John Doe', 60000, 30, 5, 'MIT'),
('Jane Smith', 75000, 28, 3, 'Stanford'),
('Emily Johnson', 50000, 25, 2, 'Harvard'),
('Michael Brown', 80000, 35, 10, 'Yale'),
('Jessica Davis', 70000, 32, 7,'Princeton');


SELECT * FROM companyrecords;