from bottle import Bottle, run, \
template, debug, get, route, static_file, post, request

import os, sys

dirname = os.path.dirname(sys.argv[0])

app = Bottle()
debug(True)

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

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

class User(object):
    def __init__(self, name, em, pw):
        self.name = name
        self.em = em
        self.pw = pw

@app.post('/create')
def createUser():
    name = request.forms.get('username')
    email = request.forms.get('email')
    password = request.forms.get('password')
    user = User(name, email, password)
    UsersTxt = open("login_data.txt", "w")
    UsersTxt.write('{};{};{}\n'.format(user.name, user.em, user.pw))
    UsersTxt.close()

    
#def writeToTxt((User)listOfUsers):
#    for u in listOfUsers:
#        UsersTxt.write(u.name)

run(app, host='localhost', port = 8080)


