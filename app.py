from bottle import Bottle, run, \
     template, debug, get, request, redirect, post, route, static_file
import os, sys

from baza import unesi_demo_podatke, procitaj_sve_podatke, sacuvaj_novi_fast_food, dohvati_fast_food_po_id, azuriraj_fast_food, izbrisi_fast_food, sacuvaj_novog_korisnika
unesi_demo_podatke()
#procitaj_sve_podatke()

dirname = os.path.dirname(sys.argv[0])
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

@app.get('/order')
def index():
    return template('order.html', data = None)

@app.get('/register')
def index():
    return template('register.html', data = None)

class User(object):
    def __init__(self, name, em, pw):
        self.name = name
        self.em = em
        self.pw = pw

@app.post('/register')
def createUser():
    name = request.forms.get('username')
    email = request.forms.get('email')
    password = request.forms.get('password')

    sacuvaj_novog_korisnika(name, email, password)
    #procitaj_sve_podatke()
    redirect('/order')

run(app, host="127.0.0.1", port="8080")