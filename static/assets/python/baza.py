import sqlite3
conn = sqlite3.connect("fakultet.db")

cur = conn.cursor()

cur.executescript("""

CREATE TABLE grupe 
(id text PRIMARY KEY,
naziv text NOT NULL);

CREATE TABLE studenti (
id integer PRIMARY KEY,
ime text NOT NULL,
prezime text NOT NULL,
grupa_id text DEFAULT NULL,
FOREIGN KEY (grupa_id) REFERENCES grupe (id));

CREATE TABLE profesori (
id text PRIMARY KEY,
titula text NOT NULL,
ime text NOT NULL,
prezime text NOT NULL);

CREATE TABLE kolegiji (
id integer PRIMARY KEY,
naziv text NOT NULL,
profesor_id integer NOT NULL,
FOREIGN KEY (profesor_id) REFERENCES profesori (id));

CREATE TABLE grupe_kolegiji (
grupa_id integer not NULL,
kolegij_id integer not NULL,
PRIMARY KEY (grupa_id, kolegij_id)
FOREIGN KEY (grupa_id) REFERENCES grupe (id),
FOREIGN KEY (kolegij_id) REFERENCES kolegiji (id));""")