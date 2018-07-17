"""
Live de Python #56 - Desenvolvimento web com Python e Flask - Bruno Rocha

set WORKON_HOME=%cd%

* Windows
set FLASK_APP=app.py
set FLASK_ENV=development

* Linux
export FLASK_APP=app.py
export FLASK_ENV=development

set FLASK_APP=app:create_app
extport FLASK_APP=app:create_app.
"""
import views
import contact
import db
import admin
from flask import Flask


def create_app():
    """Function ?."""
    # app = Flask(__name__, template_folder='/template/bar.html', static_folder='/static')
    app = Flask(__name__)

    db.configure(app)

    views.configure(app)
    
    # configurar extensões
    contact.configure(app)

    # Flask Admin
    admin.configure(app)

    # configurar as variáveis
    app.config['SECRET_KEY'] = 'kdjlkhgslskglg'
    return app
