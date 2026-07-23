CREATE TABLE IF NOT EXISTS zoo_animal(
    animal_id INT PRIMARY KEY,
    name TEXT NOT NULL,

    species TEXT NOT NULL,
    age_years INT NOT NULL,
    weight_kg REAL NOT NULL
    
);

INSERT INTO zoo_animal VALUES(1,'lion','big cat',5,190.0);
INSERT INTO zoo_animal VALUES(2,'tiger','big cat',3,150.0);
INSERT INTO zoo_animal VALUES(3,'elephant','pachyderm',5,190.0);
INSERT INTO zoo_animal VALUES(4,'giraffe','ungulate',5,190.0);
INSERT INTO zoo_animal VALUES(5,'penguin','water bird',2,5.0);
INSERT INTO zoo_animal VALUES(6,'rhino','big pachyderm',5,190.0);
INSERT INTO zoo_animal VALUES(7,'cheetah','big cat',4,190.0);
INSERT INTO zoo_animal VALUES(8,'panda','bear',7,190.0);

SELECT * FROM zoo_animal;
SELECT DISTINCT species FROM zoo_animal;
SELECT COUNT(DISTINCT species) AS unique_species FROM zoo_animal;
SELECT COUNT(animal_id)AS older_than_5 FROM zoo_animal WHERE age_years > 5;
SELECT SUM(weight_kg) AS total_weight FROM zoo_animal;
SELECT AVG(weight_kg) AS average_weight FROM zoo_animal;
SELECT
COUNT(animal_id) AS total_animals,
COUNT(DISTINCT species) AS unique_species,
SUM(weight_kg) AS total_weight_kg,
AVG(weight_kg) AS average_weight
FROM zoo_animal;
