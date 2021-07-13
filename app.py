from flask import Flask, render_template
import datetime

TEMPLATES = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route('/')
def helloWorld():
    return 'Hello World!'

@app.route('/index')
def index():
    data = datetime.datetime.now()
    usuarios = ['Jaqueline', 'rute', 'Ewerton', 'Emyle', 'luize']
    Lista=['https://www.youtube.com/embed/3fP541Qhfd0','https://www.youtube.com/embed/CTIs_RSPr84']

    mostrarUsuarios = True
    return render_template('index.html', dataAtual=data, usuarios=usuarios, mostrarUsuarios=mostrarUsuarios, Lista = Lista)

#app.run(host='0.0.0.0', port=5000)