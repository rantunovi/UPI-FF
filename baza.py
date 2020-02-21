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
from recenzija import Recenzija

def ucitaj_proizvode():
    conn = sqlite3.connect("UPI-FF.db")
    lista_proizvoda = []
    with open('static/assets/resources/proizvodi.txt', 'rt') as myfile:
        for myline in myfile:
            lista_proizvoda.append(myline[:-1])
    try:
        cur = conn.cursor()
        for proizvod in lista_proizvoda:
            cur.execute("INSERT INTO proizvodi (naziv) VALUES (?)", (proizvod,))
            conn.commit()
        print("Uspjesno dodani proizvodi u bazu podataka")

    except Exception as e:
        print("Dogodila se greska pri dodavanju proizvoda u bazu podataka: ", e)
        conn.rollback()

    conn.close()

def unesi_demo_podatke():
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS fast_food_ovi;

        CREATE TABLE fast_food_ovi (
        id INTEGER PRIMARY KEY,
        naziv text NOT NULL,
        adresa text NOT NULL,
        ikona text NOT NULL,
        lokacija text NOT NULL, 
        path text NOT NULL);

        DROP TABLE IF EXISTS korisnici;

        CREATE TABLE korisnici (
        id INTEGER PRIMARY KEY,
        ime text NOT NULL,
        adresa text NOT NULL,
        password text NOT NULL,
        token string);

        DROP TABLE IF EXISTS proizvodi;

        CREATE TABLE proizvodi (
        id INTEGER PRIMARY KEY,
        naziv text NOT NULL);

        DROP TABLE IF EXISTS proizvodi_fast_food;

        CREATE TABLE proizvodi_fast_food (
        id INTEGER PRIMARY KEY,
        id_proizvod integer NOT NULL,               
        id_fast_food integer NOT NULL,              
        cijena integer NOT NULL,
        FOREIGN KEY (id_proizvod) REFERENCES proizvodi (id),
        FOREIGN KEY (id_fast_food) REFERENCES fast_food_ovi (id));

        DROP TABLE IF EXISTS stavke;

        CREATE TABLE stavke (
        id INTEGER PRIMARY KEY,
        id_proizvodi_fast_food integer NOT NULL,
        kolicina integer NOT NULL,
        prilozi string NOT NULL,
        FOREIGN KEY (id_proizvodi_fast_food) REFERENCES proizvodi_fast_food (id));

        DROP TABLE IF EXISTS narudzbe;

        CREATE TABLE narudzbe (
        id INTEGER PRIMARY KEY,
        id_korisnik integer NOT NULL,
        id_stavka integer NOT NULL,
        FOREIGN KEY (id_korisnik) REFERENCES korisnici (id),
        FOREIGN KEY (id_stavka) REFERENCES stavke (id));
        

        DROP TABLE IF EXISTS recenzije;

        CREATE TABLE recenzije (
        id INTEGER PRIMARY KEY,
        id_fast_food integer NOT NULL,
        id_korisnik integer NOT NULL,
        komentar string NOT NULL, 
        ocjena integer NOT NULL,
        FOREIGN KEY (id_fast_food) REFERENCES fast_food_ovi(id),
        FOREIGN KEY (id_korisnik) REFERENCES korisnici(id));


        """)
        

        cur.execute("INSERT INTO fast_food_ovi (naziv, adresa, ikona, lokacija, path) VALUES (?, ?, ?, ?, ?)", ('Fast Food "Sesula"', "Dobrilina 1a, Split", "https://www.dobartek.hr/Resources/Restaurant/d2c55707-ffa4-486e-8e73-5e447d00dbd2.jpg", "https://www.google.com/maps?q=Dobrilina+1a,+Split&um=1&ie=UTF-8&sa=X&ved=2ahUKEwjXyKXKtprnAhXRk4sKHcHBDOMQ_AUoAXoECBMQAw", "/sesula"))
        conn.commit()
        cur.execute("INSERT INTO fast_food_ovi (naziv, adresa, ikona, lokacija, path) VALUES (?, ?, ?, ?, ?)", ('"Mirakul" Pizza', "Dubrovacka 20, Split", "https://www.dobartek.hr/Resources/Restaurant/c45cd123-1eb7-43a1-8c7b-8aab857d4c5e.jpg", "https://www.google.com/maps/place/Mirakul/@43.5104958,16.4537034,17z/data=!3m1!4b1!4m5!3m4!1s0x13355e1a5128b9d9:0x8037a2872ff2ea62!8m2!3d43.5104919!4d16.4558921", "/mirakul"))
        conn.commit()
        cur.execute("INSERT INTO fast_food_ovi (naziv, adresa, ikona, lokacija, path) VALUES (?, ?, ?, ?, ?)", ('Fast Food "XXL"', "Dubrovacka 61, Split", "https://www.dobartek.hr/Resources/Restaurant/268bd732-0891-46eb-8c06-a02a30773b39.jpg", "https://www.google.com/maps/place/XXL+Fast+Food/@43.5182153,16.447518,17z/data=!3m1!4b1!4m5!3m4!1s0x13355e0dd5cba36d:0x618073cdc19dd103!8m2!3d43.5182114!4d16.4497067", "/xxl"))
        conn.commit()
        cur.execute("INSERT INTO fast_food_ovi (naziv, adresa, ikona, lokacija, path) VALUES (?, ?, ?, ?, ?)", ('Fast Food "Gajeta"', "Vukovarska 89A, Split", "https://www.dobartek.hr/Resources/Restaurant/6c1997a2-d87b-4b99-9755-f1d42ef92856.jpg", "https://www.google.com/maps/place/Gajeta/@43.5115211,16.4411093,15z/data=!4m8!1m2!2m1!1sgajeta+split!3m4!1s0x13355e17c185a9a1:0xa614eb26db4900b!8m2!3d43.5129251!4d16.4634563", "/gajeta"))
        conn.commit()
        cur.execute("INSERT INTO fast_food_ovi (naziv, adresa, ikona, lokacija, path) VALUES (?, ?, ?, ?, ?)", ('Fast Food "IN"', "Bruna Busica 2, Split", "https://www.dobartek.hr/Resources/Restaurant/c3d21e4c-451b-4d7a-bd72-69d8e1d47946.jpg", "https://www.google.com/maps/place/Fast+Food+In/@43.5063092,16.4626497,17z/data=!3m1!4b1!4m5!3m4!1s0x13355fa23bc2aeff:0xc82b61629eedc02a!8m2!3d43.5063092!4d16.4648384", "/in"))
        conn.commit()
        cur.execute("INSERT INTO fast_food_ovi (naziv, adresa, ikona, lokacija, path) VALUES (?, ?, ?, ?, ?)", ('Fast Food "Vatra"', "Poljicka cesta 30, Split", "https://www.dobartek.hr/Resources/Restaurant/18726fa0-b5b2-453d-9ef6-e7c562ae5a00.jpg", "https://www.google.com/maps/place/Fast+Food+Vatra/@43.5064926,16.4632071,17z/data=!3m1!4b1!4m5!3m4!1s0x13355f3314d1afab:0xb44fd90eaf7cfe32!8m2!3d43.5064887!4d16.4653958", "/vatra"))
        conn.commit()


        cur.execute("INSERT INTO korisnici (ime, adresa, password) VALUES (?, ?, ?)", ("mario_77", "Poljicka 30", "bvc1js"))
        conn.commit()
        cur.execute("INSERT INTO korisnici (ime, adresa, password) VALUES (?, ?, ?)", ("petar12", "Vukovarska 14", "8sd12g"))
        conn.commit()
        cur.execute("INSERT INTO korisnici (ime, adresa, password) VALUES (?, ?, ?)", ("sesula", "Vlasnicka 1", "vlasniksesula"))
        conn.commit()
        cur.execute("INSERT INTO korisnici (ime, adresa, password) VALUES (?, ?, ?)", ("mirakul", "Vlasnicka 2", "vlasnikmirakul"))
        conn.commit()
        cur.execute("INSERT INTO korisnici (ime, adresa, password) VALUES (?, ?, ?)", ("xxl", "Vlasnicka 3", "vlasnikxxl"))
        conn.commit()
        cur.execute("INSERT INTO korisnici (ime, adresa, password) VALUES (?, ?, ?)", ("gajeta", "Vlasnicka 4", "vlasnikgajeta"))
        conn.commit()
        cur.execute("INSERT INTO korisnici (ime, adresa, password) VALUES (?, ?, ?)", ("in", "Vlasnicka 5", "vlasnikin"))
        conn.commit()
        cur.execute("INSERT INTO korisnici (ime, adresa, password) VALUES (?, ?, ?)", ("vatra", "Vlasnicka 6", "vlasnikvatra"))
        conn.commit()
        
        
        cur.execute("INSERT INTO recenzije (id_fast_food, id_korisnik, komentar, ocjena) VALUES (?, ?, ?, ?)", (1, 1, "vrlo dobro", 4))
        conn.commit()
        cur.execute("INSERT INTO recenzije (id_fast_food, id_korisnik, komentar, ocjena) VALUES (?, ?, ?, ?)", (1, 2, "odlicno!", 5))
        conn.commit()
        cur.execute("INSERT INTO recenzije (id_fast_food, id_korisnik, komentar, ocjena) VALUES (?, ?, ?, ?)", (3, 2, "S obzirom da ne postoji ocjena 0, dajem ocjenu 1...", 1))
        conn.commit()

        cur.execute("INSERT INTO stavke (id_proizvodi_fast_food, kolicina, prilozi) VALUES (?, ?, ?)", (1, 3, "majoneza*salata*"))
        conn.commit()

        cur.execute("INSERT INTO narudzbe (id_korisnik, id_stavka) VALUES (?, ?)", (2, 1))
        conn.commit()
        

        items = ["Hamburger", "Cheeseburger", "Piletina", "Cevapi", "Topli sendvic", "Burrito", "Pizza Capricciosa", "Pizza Margharita", "Pizza Picante"]
        for i in items:
            cur.execute("INSERT INTO proizvodi (naziv) VALUES (?)", (i,))        
            conn.commit()
                 

        data = {
            "sesula":{
                "id":1,
                "items":{
                    "hamburger":{
                        "id":1,
                        "price":25
                    },
                    "sendvic":{
                        "id":5,
                        "price":15
                    },   
                    "capricciosa":{
                        "id":7,
                        "price":35
                    }               
                }
            },
            "mirakul":{
                "id":2,
                "items":{
                    "capricciosa":{
                        "id":7,
                        "price":40
                    },
                    "margharita":{
                        "id":8,
                        "price":38
                    },
                    "picante":{
                        "id":9,
                        "price":45
                    }                   
                }
            },
            "xxl":{
                "id":3,
                "items":{
                    "cheeseburger":{
                        "id":2,
                        "price":22
                    },
                    "cevapi":{
                        "id":4,
                        "price":20
                    },
                    "sendvic":{
                        "id":5,
                        "price":14
                    }                   
                }
            },
            "gajeta":{
                "id":4,
                "items":{
                    "hamburger":{
                        "id":1,
                        "price":23
                    },
                    "cheeseburger":{
                        "id":2,
                        "price":25
                    },
                    "burrito":{
                        "id":6,
                        "price":22
                    }                   
                }
            },
            "in":{
                "id":5,
                "items":{
                    "hamburger":{
                        "id":1,
                        "price":26
                    },
                    "piletina":{
                        "id":3,
                        "price":30
                    },
                    "margharita":{
                        "id":8,
                        "price":40
                    }                   
                }
            },
            "vatra":{
                "id":6,
                "items":{
                    "cheeseburger":{
                        "id":2,
                        "price":25
                    },
                    "burrito":{
                        "id":6,
                        "price":23
                    },
                    "capricciosa":{
                        "id":7,
                        "price":38
                    }                   
                }
            } 
        }

        for fastFood in data:
            fastFoodId = data[fastFood].get("id")
            for food in data[fastFood].get("items"):
                food = data[fastFood].get("items")[food]
                cur.execute("INSERT INTO proizvodi_fast_food (id_proizvod, id_fast_food, cijena) VALUES (?, ?, ?)", (food.get("id"), fastFoodId, food.get("price")))
                conn.commit()

        print("uspjesno uneseni testni podaci!")

    except Exception as e: 
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()
        
    conn.close()

def procitaj_sve_ff():
    conn = sqlite3.connect("UPI-FF.db")
    lista_fast_food_ovi = []
    try:

        cur = conn.cursor()
        cur.execute(""" SELECT id, naziv, adresa, ikona, lokacija, path FROM fast_food_ovi """)
        podaci = cur.fetchall()
        
        for fast_food in podaci:
            f = Fast_food(fast_food[0], fast_food[1], fast_food[2], fast_food[3], fast_food[4], fast_food[5])
            lista_fast_food_ovi.append(f)

        print("uspjesno dohvaceni svi podaci iz tablice fast_food_ovi!")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice fast_food_ovi: ", e)
        conn.rollback()

    conn.close()
    return lista_fast_food_ovi

def procitaj_sve_proizvode():
    conn = sqlite3.connect("UPI-FF.db")
    lista_proizvoda = []
    try:
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM proizvodi """)
        podaci = cur.fetchall()
        
        for proizvod in podaci:
            p = Proizvod(proizvod[0], proizvod[1])
            lista_fast_food_ovi.append(f)

        print("uspjesno dohvaceni svi podaci iz tablice proizvodi!")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice proizvodi: ", e)
        conn.rollback()

    conn.close()
    return lista_proizvoda

def sacuvaj_novog_korisnika(username, adresa, password):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO korisnici (ime, adresa, password) VALUES (?, ?, ?)", (username, adresa, password))
        conn.commit()

        print("uspjesno dodan novi korisnik u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju novog korisnika u bazu podataka: ", e)
        conn.rollback()

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

def naziv_ff_po_id(_id_fast_food):
    conn = sqlite3.connect("UPI-FF.db")
    naziv = ""
    try:

        cur = conn.cursor()
        cur.execute(" SELECT naziv FROM fast_food_ovi WHERE id = ?", (_id_fast_food,))
        naziv = cur.fetchone()

        print("uspjesno dohvacen naziv fast fooda iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju fast_food iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return naziv[0]

def id_ff_po_nazivu(nazivFF):
    conn = sqlite3.connect("UPI-FF.db")
    id = 0
    try:
        cur = conn.cursor()
        cur.execute(" SELECT id FROM fast_food_ovi WHERE naziv LIKE ?", ("%" + nazivFF + "%",))
        id = cur.fetchone()

        print("uspjesno dohvacen id fast fooda iz baze podataka po nazivu")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju fast food id iz baze podataka po nazivu: ", e)
        conn.rollback()

    conn.close()
    return id[0]

def azuriraj_fast_food(_id_fast_food, naziv, adresa, telefon):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("UPDATE fast_food SET naziv = ?, adresa = ?, telefon = ? WHERE id = ?", (naziv, adresa, telefon, _id_fast_food))
        conn.commit()

        print("uspjesno azuriran fast_food iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri azuriranju fast_food iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def azuriraj_user_token(username, token):
    conn = sqlite3.connect("UPI-FF.db")
    try:
        cur = conn.cursor()
        cur.execute("UPDATE korisnici SET token = ? WHERE ime = ?", (token, username))
        conn.commit()

        print("uspjesno azuriran token korisnika")

    except Exception as e: 
        print("Dogodila se greska pri azuriranju fast_food iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def usernameExists(username):
    conn = sqlite3.connect("UPI-FF.db")
    exists = False
    try:

        cur = conn.cursor()
        cur.execute("SELECT * FROM korisnici WHERE ime=?", (username,))
        podaci = cur.fetchone()

        if podaci != None:
            exists = True
    
    except Exception as e: 
        print("Dogodila se greska pri dohvacanju fast_food iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return exists

def getPassword(username):
    conn = sqlite3.connect("UPI-FF.db")
    pw = None
    try:

        cur = conn.cursor()
        cur.execute("SELECT (password) FROM korisnici WHERE ime=?", (username,))
        pw = cur.fetchone()

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju lozinke iz baze podataka po korisnickom imenu: ", e)
        conn.rollback()

    conn.close()
    return pw

def dohvati_proizvod_po_id(id_proizvod):
    conn = sqlite3.connect("UPI-FF.db")
    naziv = ""
    try:

        cur = conn.cursor()
        cur.execute("SELECT (naziv) FROM proizvodi WHERE id=?", (id_proizvod,))
        naziv = cur.fetchone()
        
    except Exception as e: 
        print("Dogodila se greska pri dohvacanju proizvoda po id: ", e)
        conn.rollback()

    conn.close()
    return naziv

def dohvati_id_po_nazivu_proizvoda(ime):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("SELECT id FROM proizvodi WHERE naziv=?", (ime,))
        id = cur.fetchone()

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju user id-a: ", e)
        conn.rollback()

    conn.close()
    return id

def dohvati_recenzije(_id_fast_food):
    conn = sqlite3.connect("UPI-FF.db")
    lista_recenzija=[]
    try:

        cur = conn.cursor()
        cur.execute("SELECT * FROM recenzije WHERE id_fast_food = ? ", (_id_fast_food,))

        podaci = cur.fetchall()
        for p in podaci:
            r=Recenzija(p[0], p[1], str(dohvati_username_po_id(p[2]))[2:-3], p[3], p[4])
            lista_recenzija.append(r)
        print("Uspjesno dohvaceni svi podaci o recenziji")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju recenzija: " , e)
        conn.rollback()

    conn.close()
    return lista_recenzija

def dohvati_jelovnik(_id_fast_food):
    conn = sqlite3.connect("UPI-FF.db")
    jelovnik=[]
    try:

        cur = conn.cursor()
        cur.execute("SELECT * FROM proizvodi_fast_food WHERE id_fast_food=?", (_id_fast_food,))
        podaci=cur.fetchall()
        
        for p in podaci:
            pf=Proizvod_fast_food(p[0], dohvati_proizvod_po_id(p[1])[0], p[2], p[3])
            jelovnik.append(pf)
        print("Uspjesno dohvacen jelovnik")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju jelovnika: ", e)
        conn.rollback()

    conn.close()
    return jelovnik

def dohvati_id_korisnika_po_usernameu(ime):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("SELECT id FROM korisnici WHERE ime=?", (ime,))
        id = cur.fetchone()

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju user id-a: ", e)
        conn.rollback()

    conn.close()
    return id

def dohvati_username_po_id(id):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("SELECT ime FROM korisnici WHERE id=?", (id,))
        ime = cur.fetchone()

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju username-a: ", e)
        conn.rollback()

    conn.close()
    return ime

def spremi_recenziju(id_fast_food, id_korisnik, komentar, ocjena):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO recenzije (id_fast_food, id_korisnik, komentar, ocjena) VALUES (?, ?, ?, ?)", (id_fast_food, id_korisnik, komentar, ocjena))
        conn.commit()

        print("uspjesno dodana nova recenzija u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju nove recenzije u bazu podataka: ", e)
        conn.rollback()

def dohvati_path(_id_fast_food):
    conn = sqlite3.connect("UPI-FF.db")
    path = ""
    try:

        cur = conn.cursor()
        cur.execute("SELECT (path) FROM fast_food_ovi WHERE id=?", (_id_fast_food,))
        path = cur.fetchone()
        
    except Exception as e: 
        print("Dogodila se greska pri dohvacanju path: ", e)
        conn.rollback()

    conn.close()
    return path

def sacuvaj_novi_proizvod(imeProizvoda):
    conn = sqlite3.connect("UPI-FF.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO proizvodi (naziv) VALUES (?)", (imeProizvoda,))          
        conn.commit()
        
        print("uspjesno dodan novi proizvod u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju novog proizvoda u bazu podataka: ", e)
        conn.rollback()

def sacuvaj_novi_proizvod_cijenu(id_fast_food, naziv, cijena):
    conn = sqlite3.connect("UPI-FF.db")
    try:
        cur = conn.cursor()
        id_proizvod = dohvati_id_po_nazivu_proizvoda(naziv)[0]
        cur.execute("INSERT INTO proizvodi_fast_food (id_proizvod, id_fast_food, cijena) VALUES (?, ?, ?)", (id_proizvod, id_fast_food, cijena))
        conn.commit()
        
        print("uspjesno dodani novi proizvod i cijena u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju novog proizvoda u bazu podataka: ", e)
        conn.rollback()
        
def sacuvaj_narudzbu(id_fast_food, naziv, cijena):
    conn = sqlite3.connect("UPI-FF.db")
    try:
        cur = conn.cursor()
        id_proizvod = dohvati_id_po_nazivu_proizvoda(naziv)[0]
        cur.execute("INSERT INTO proizvodi_fast_food (id_proizvod, id_fast_food, cijena) VALUES (?, ?, ?)", (id_proizvod, id_fast_food, cijena))
        conn.commit()
        
        print("uspjesno dodani novi proizvod i cijena u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju novog proizvoda u bazu podataka: ", e)
        conn.rollback()
