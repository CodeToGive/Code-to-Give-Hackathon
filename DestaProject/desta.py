from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir, 'desta.db')

db = SQLAlchemy(app)

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped')

@app.cli.command('db_seed')
def db_seed():
    bus1 = Business(email = 'desta@org', name = 'desta', tag = 'salon', password = '1010')
    bus2 = Business(email = 'onyx@org', name = 'desta', tag = 'salon', password = '2020')
    
    db.session.add(bus1) 
    db.session.add(bus2)
    db.session.commit()
    print('db seeded')

@app.route("/")
def hello_world():
    return "<p>Hello, World! A good time to be alive</p>"

@app.route("/home")
def welcome():
    return "<h1>Welcome to Desta Businesses!</h1>"

app.route("/businesses")
def businesses():
    bus_list = Business.query.all()
    

# database models
class Business(db.Model):
    __tablename__ = 'businesses'
    email = db.Column(db.String(length=50),nullable=False, unique=True, primary_key=True )
    name = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String())
    phone_no = db.Column(db.String(length=12))
    password=db.Column(db.String(),nullable=False)
    website=db.Column(db.String(length=20))
    instagram= db.Column(db.String())
    tag = db.Column(db.String())

    