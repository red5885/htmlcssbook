from flask import Flask,render_template
import pages

def index():
    pages = ['p20', 'p27', 'p58']
    return render_template('index.html', pages = pages)

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.cfg')

    app.register_blueprint(pages.bp)
    app.add_url_rule('/', 'index', index)
    return app


if (__name__ == '__main__'):
    app = create_app()
    app.run()