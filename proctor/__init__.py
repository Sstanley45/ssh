from flask import Flask, render_template 
from proctor.forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  
db = SQLAlchemy(app) 


app.config['SECRET_KEY'] = '2d25a401fb7c6446df91a69f'

from proctor import routes