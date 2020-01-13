import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from fast_food import Fast_food
from korisnik import Korisnik
from narudzba import Narudzba
from proizvod import Proizvod
from proizvod_fast_food import Proizvod_fast_food
from stavka import Stavka

def unesi_demo_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS fast_food_ovi;

        CREATE TABLE fast_food_ovi (
        id_ INTEGER PRIMARY KEY,
        naziv text NOT NULL,
        adresa text NOT NULL,
        telefon text NOT NULL);

        DROP TABLE IF EXISTS korisnici;

        CREATE TABLE korisnici (
        id INTEGER PRIMARY KEY,
        ime text NOT NULL,
        email text NOT NULL,
        password text NOT NULL);

        DROP TABLE IF EXISTS narudzbe;

        CREATE TABLE narudzbe (
        id INTEGER PRIMARY KEY,
        id_korisnik INTEGER FOREIGN KEY,
        id_fast_food INTEGER FOREIGN KEY);

        DROP TABLE IF EXISTS proizvodi;

        CREATE TABLE proizvodi (
        id INTEGER PRIMARY KEY,
        naziv text NOT NULL);

        DROP TABLE IF EXISTS proizvodi_fast_food;

        CREATE TABLE proizvodi_fast_food (
        id INTEGER PRIMARY KEY,
        id_proizvod INTEGER FOREIGN KEY,
        id_fast_food INTEGER FOREIGN KEY,
        cijena INTEGER NOT NULL);

        DROP TABLE IF EXISTS stavke;

        CREATE TABLE stavke (
        id INTEGER PRIMARY KEY,
        id_narudzba INTEGER FOREIGN KEY,
        id_proizvod_fast_food INTEGER FOREIGN KEY);
        """)
        

        cur.execute("INSERT INTO fast_food_ovi (naziv, adresa, telefon) VALUES (?, ?, ?)", ("Kresina pecenjara", "Pecenjariceva 10", "021/8080-8080"))
        cur.execute("INSERT INTO korisnici (ime, email, password) VALUES (?, ?, ?)", ("Kreso", "kresko@email.com", "kresko"))
        cur.execute("INSERT INTO proizvodi (naziv) VALUES (?)", ("Burger"))
        cur.execute("INSERT INTO proizvodi (naziv) VALUES (?)", ("Pizza skampi"))
        cur.execute("INSERT INTO proizvodi_fast_food (cijena) VALUES (?)", (30)
        conn.commit()

        print("uspjesno uneseni testni podaci u tablicu fast_food_ovi!")

    except Exception as e: 
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()
        
    conn.close()

def procitaj_sve_podatke():
    conn = sqlite3.connect("UPI-FF.db")
    lista_fast_food_ovi = []
    try:

        cur = conn.cursor()
        cur.execute(""" SELECT id, naziv, adresa, telefon FROM fast_food_ovi """)

        podaci = cur.fetchall()
        
        for fast_food in podaci:
            # 0 - id
            # 1 - naziv
            # 2 - adresa
            # 3 - telefon

            f = Fast_food(fast_food[0], fast_food[1], fast_food[2], fast_food[3])
            lista_fast_food_ovi.append(f)

        print("uspjesno dohvaceni svi podaci iz tablice fast_food_ovi!")

        for f in lista_fast_food_ovi:
            print(f)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice fast_food_ovi: ", e)
        conn.rollback()

    conn.close()
    return lista_fast_food_ovi


def sacuvaj_novi_fast_food(naziv, adresa, telefon):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO fast_food_ovi (naziv, adresa, telefon) VALUES (?, ?, ?)", (naziv, adresa, telefon))
        conn.commit()

        print("uspjesno dodan novi fast_food u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju novog fast_food u bazu podataka: ", e)
        conn.rollback()

    conn.close()

def izbrisi_fast_food(_id_fast_food):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("DELETE FROM fast_food_ovi WHERE id=?;", (_id_fast_food))
        conn.commit()

        print("Uspjesno izbrisan fast_food iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri brisanje profesora iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dohvati_fast_food_po_id(_id_fast_food):
    conn = sqlite3.connect("UPI-FF.db")
    profesor = None
    try:

        cur = conn.cursor()
        cur.execute(" SELECT id, naziv, adresa, telefon FROM fast_food_ovi WHERE id = ?", (_id_fast_food))
        podaci = cur.fetchone()

        print("podaci", podaci)
        fast_food = Fast_food(podaci[0], podaci[1], podaci[2], podaci[3])

        print("uspjesno dohvacen fast_food iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju fast_food iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return profesor

def azuriraj_fast_food(_id_fast_food, naziv, adresa, telefon):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("UPDATE fast_food SET naziv = ?, adresa = ?, telefon = ? WHERE id = ?", (naziv, adresa, telefon, _id_fast_food))
        conn.commit()

        print("uspjesno ažuriran fast_food iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju fast_food iz baze podataka: ", e)
        conn.rollback()

    conn.close()