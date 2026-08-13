import sqlite3
import pandas as pd
conn=sqlite3.connect('cricket.db')
cursor=conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player_Match;
CREATE TABLE Team(
    team_id INTEGER PRIMARY KEY,
    team_name TEXT 
);
CREATE TABLE Match(
    match_id INTEGER PRIMARY KEY,
    Season_id INTEGER,
    match_winner INTEGER,
    win_margin INTEGER,
);
CREATE TABLE Player_match(
    match_id INTEGER,
    player_id INTEGER,
);
INSERT INTO TEAM VALUES 
(1,'India'),
(2,'Pakistan'),
(3,'Australia'),
(4,'England'),
(5,'South Africa'),
(6,'New Zealand'),
(7,'Sri Lanka'),
(8,'West Indies');
INSERT INTO MATCH VALUES
(1,2020,1,10),
(2,2020,2,5),
(3,2020,3,15),
(4,2020,4,20),
(5,2020,5,25),
(6,2020,6,30),
(7,2020,7,35),
(8,2020,8,40);
INSERT INTO Player_match VALUES
(1,101),
(1,102),
(1,103),
(2,104),
(2,105),
(3,106),
(3,107),
(4,108),
(4,109),
(5,110),
(5,111),
(6,112),
(6,113),
(7,114),
(7,115),
(8,116),
(8,117);
""")
conn.commit()
print('Database ready!')
tables=pd.read_sql("""SELECT "
     FROM Match;""",conn)
     print(matches)
     print('Rows and columns:',matches.shape)
teams=pd.read_sql("""SELECT * 
FROM Team;""",conn)
print(teams)
