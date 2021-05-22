from flask import Flask,render_template
import pages

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

def index():
    pages = ['p20', 'p27']
    return render_template('index.html', pages = pages)

app.add_url_rule('/', 'index', index)
app.add_url_rule('/p20', 'p20', pages.views.p20)
app.add_url_rule('/p27', 'p27', pages.views.p27)
