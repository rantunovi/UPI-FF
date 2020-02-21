from bottle import Bottle, run, \
     template, debug, get, request, redirect, post, route, static_file
import os, sys
import json
import uuid
from baza import unesi_demo_podatke, procitaj_sve_ff, sacuvaj_novi_fast_food, naziv_ff_po_id, azuriraj_fast_food, izbrisi_fast_food, sacuvaj_novog_korisnika, usernameExists, getPassword, spremi_recenziju, dohvati_recenzije, dohvati_id_korisnika_po_usernameu, dohvati_username_po_id, procitaj_sve_proizvode, dohvati_proizvod_po_id, dohvati_jelovnik, dohvati_path, id_ff_po_nazivu, azuriraj_user_token, dohvati_id_po_nazivu_proizvoda, sacuvaj_novi_proizvod, sacuvaj_novi_proizvod_cijenu

unesi_demo_podatke()

dirname = os.path.dirname(sys.argv[0])
template_path = dirname + '\\views'
app = Bottle()
debug(True)

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.jpg>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/assets/resources')

@app.route('/static/<filename:re:.*\.css.map>')
def send_cssmap(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'/static/assets/js')

@app.route('/static/<filename:re:.*\.js.map>')
def send_jsmap(filename):
    return static_file(filename, root=dirname+'/static/assets/js')


@app.route('/')
def index():
    data = {"developer_name": "Renato",
           "developer_organization": "PMF"}
    return template('index.html', data = data)

@app.get('/login')
def index():
    return template('login.html')

@app.get('/order')
def index():
    data = procitaj_sve_ff()
    return template('order', data = data, template_lookup=[template_path])

@app.get('/register')
def index():
    return template('register.html')

@app.get('/restaurants/<name>')
def index(name):
    ff_id = id_ff_po_nazivu(name)

    jelovnik = dohvati_jelovnik(ff_id)
    recenzije = dohvati_recenzije(ff_id)
    nazivFF = naziv_ff_po_id(ff_id)
    data = [jelovnik, recenzije, nazivFF]
    return template('restaurant.html', data = data, template_lookup=[template_path])

@app.get('/restaurantedit/<name>')
def index(name):
    ff_id = id_ff_po_nazivu(name)

    jelovnik = dohvati_jelovnik(ff_id)
    recenzije = dohvati_recenzije(ff_id)
    nazivFF = naziv_ff_po_id(ff_id)
    data = [jelovnik, recenzije, nazivFF]
    return template('restaurantedit.html', data = data, template_lookup=[template_path])


def reg_auth(username, adresa, password):
    if usernameExists(username):
        return "Korisnicko ime je zauzeto."
    else:
        if username == None:
            return "Morate unijeti korisnicko ime."
        else:
            if len(username) < 3 or  ' ' in username:
                return "Username je kraci od 3 znaka i/ili sadrzi razmak(e)."

    adr = []
    adr = adresa.split()
    if len(adr) == 2:
        if not adr[0].isalpha() or not adr[1].isdigit():
            return "Pogresan unos adrese. Format adrese mora biti: 'ulica broj'."
    else:
        return "Pogresan unos adrese. Format adrese mora biti: 'ulica broj'."

    if len(password) < 6 or ' ' in password:
        return "Lozinka je kraca od 6 znakova i/ili sadrzi razmak(e)."

    return "Podaci su ispravni."


@app.route('/register', method="POST")
def createUser():
    jsonData = request.json
    name = jsonData[('username')]
    adresa = jsonData[('adresa')]
    password = jsonData[('password')]

    result = reg_auth(name, adresa, password)
    data = {"msg: result"}

    if(result == "Podaci su ispravni."):
        sacuvaj_novog_korisnika(name, adresa, password)
        return {
            "success":True,
            "message":"Registered."
        }
    else:
        return {
            "success":False,
            "message":result
        }

def generateToken():
    stringLength = 8

    randomString = uuid.uuid4().hex 
    randomString  = randomString.lower()[0:stringLength]

    return randomString


def login_auth(username, password):
    if not usernameExists(username):
        return "Korisnicko ime nije registrirano. Provjerite unos."
    else:
        if str(getPassword(username)[0]) != str(password):
            return "Lozinka je netocna."
        else:
            return "Podaci su ispravni."    
            

@app.route('/login', method="POST")
def loginUser():
    jsonData = request.json
    name = jsonData[('username')]
    password = jsonData[('password')]
    token = generateToken()

    result = login_auth(name, password)
    
    if(result == "Podaci su ispravni."):
        azuriraj_user_token(name, token)
        vlasnik = False
        if name in ["sesula", "mirakul", "xxl", "gajeta", "in", "vatra"]:
            vlasnik = True
        
        return {
            "success":True,
            "message":"Registered.",
            "username":name,
            "vlasnik":vlasnik
        }
    else:
        return {
            "success":False,
            "message":result
        }

def saveReview_auth(reviewDesc, rating):
    if reviewDesc != "" and rating != None: 
        return "Podaci recenzije neispravni."
    else:
        return "Podaci su ispravni." 

@app.route('/reviews', method="POST")
def saveReview():
    jsonData = request.json
    reviewDesc = jsonData[('reviewDesc')]
    rating = jsonData[('rating')]
    username = jsonData[('username')]
    nazivFF = jsonData[('restaurant_name')]

    if reviewDesc != "" and rating != None: 
        spremi_recenziju(id_ff_po_nazivu(nazivFF), dohvati_id_korisnika_po_usernameu(username)[0], reviewDesc, rating)
        return {
            "success":True,
            "message":"Recenzija spremljena."
        }
    else:
        return {
            "success":False,
            "message":"Vrijednosti recenzije nepotpune."
        }

def addFood_auth(foodName, foodPrice):
    if foodName != "" and int(foodPrice) > 0:
        return "Podaci su ispravni."
    else:
        return "Podaci o novom proizvodu su neispravni."
        
@app.route('/addfood', method="POST")
def addFood():
    jsonData = request.json
    foodName = jsonData[('foodName')]
    foodPrice = jsonData[('foodPrice')]
    nazivFF = jsonData[('restaurant_name')]

    if foodName != "" and int(foodPrice) > 0: 
        sacuvaj_novi_proizvod(foodName)
        sacuvaj_novi_proizvod_cijenu(id_ff_po_nazivu(nazivFF), foodName, foodPrice)
        return {
            "success":True,
            "message":"Proizvod spremljen."
        }
    else:
        return {
            "success":False,
            "message":"Podaci o proizvodu nisu valjani."
        }

#run(app, host="127.0.0.1", port="8080")
