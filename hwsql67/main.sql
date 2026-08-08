
CREATE TABLE activities (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    activity_type VARCHAR(50),
    participants INT,
    cost DECIMAL(10, 2),
    duration_minutes INT
);

=
INSERT INTO activities VALUES 
(1, 'Morning Yoga', 'Fitness', 15, 10.00, 60),
(2, 'Beginner Pottery', 'Arts & Crafts', 8, 45.00, 120),
(3, 'Zumba Dance', 'Fitness', 25, 12.00, 45),
(4, 'Oil Painting', 'Arts & Crafts', 12, 50.00, 180),
(5, 'Senior Chess Club', 'Social', 6, 0.00, 90),
(6, 'Community Choir', 'Social', 30, 5.00, 90),
(7, 'Cardio Kickboxing', 'Fitness', 18, 15.00, 60),
(8, 'Watercolor Workshop', 'Arts & Crafts', 10, 40.00, 150);