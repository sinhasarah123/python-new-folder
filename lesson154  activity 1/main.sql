CREATE TABLE IF NOT EXISTS BOOK(
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating REAL NOT NULL,
    pages INTEGER NOT NULL,
    pub_year INTEGER NOT NULL

);
INSERT INTO book VALUES (1, 'The Great Gatsby', 'Fiction', 4.5, 180, 1925);
INSERT INTO book VALUES (2, 'To Kill a Mockingbird', 'Fiction', 4.8, 281, 1960);
INSERT INTO book VALUES (3, '1984', 'Dystopian', 4.7, 328, 1948);
INSERT INTO book VALUES (4, 'Animal Farm', 'Dystopian', 4.5, 180, 1948);
INSERT INTO book VALUES (5, 'Harry Potter', 'Fiction', 4.5, 180, 1925);
INSERT INTO book VALUES (6, 'little prince', 'Fiction', 4.5, 180, 1925);
INSERT INTO book VALUES (7, 'The tale of two cities', 'Fiction', 4.5, 180, 1925);
INSERT INTO book VALUES (8, 'The Catcher in the Rye', 'Fiction', 4.5, 180, 1925);
SELECT * FROM BOOK;

SELECT title, rating FROM book ORDER BY rating ASC;
SELECT title, rating FROM book ORDER BY rating DESC;
SELECT title, genre FROM book ORDER BY genre ASC;
SELECT title, genre FROM book ORDER BY genre DESC;
SELECT title, rating FROM book ORDER BY rating DESC LIMIT 3;
SELECT title, pub_year FROM book ORDER BY pub_year ASC LIMIT 5;
SELECT genre,COUNT(*)AS book_count FROM book GROUP BY genre;
SELECT genre ,SUM(pages)AS total_pages ,AVG(rating)AS average_rating 
FROM book 
GROUP BY genre;
SELECT genre , COUNT(*) AS book_count 
FROM book
GROUP BY genre
HAVING COUNT(*) > 2;



