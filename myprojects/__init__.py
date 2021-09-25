from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


#Register Blueprints 

from myprojects.books.views import book_blueprint

app.register_blueprint(book_blueprint,url_prfix='/books')