from flask import Flask,render_template
from pages.views import *

def create_app():
    app = Flask(__name__)
    app.confit.from_pyfile('config.cfg')

    #TODO started converting examples to a bluepring.
    app.add_url_rule('index')

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

def index():
    pages = ['p20', 'p27']
    return render_template('index.html', pages = pages)
