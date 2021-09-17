from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import os
from flask_marshmallow import Marshmallow

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir, 'desta.db')

db = SQLAlchemy(app)
ma = Marshmallow(app)

# create a database
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created')

# delete a database
@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped')

# mock data
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

# create a business
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']

    test = Business.query.filter_by(email=email).first()
    if test:
        return jsonify(message="Email already exists")
    else:
        password = request.form['password']
        name = request.form['name']
        business = Business(email=email, password=password, name=name)
        db.session.add(business)
        db.session.commit()
        return jsonify(message="Business created successfully"), 201

# view all businesses
@app.route('/businesses', methods=['GET'])
def businesses():
    businesses_list = Business.query.all()
    result = businesses_schema.dump(businesses_list)
    return jsonify(result)

# view a business
@app.route('/business_details/<string:email>', methods=['GET'])
def business_details(email:str):
    business = Business.query.filter_by(email=email).first()
    if business:
        result = business_schema.dump(business)
        return jsonify(result)
    else: 
        return jsonify(message="That business does not exist")

# modify business
@app.route('/update_business', methods=['PUT'])
def update_business():
    email=request.form['email']
    business = Business.query.filter_by(email=email).first()
    if business:
        business.name = request.form['name']
        business.description = request.form['description']
        business.phone_no = request.form['phone_no']
        business.password = request.form['password']
        business.website = request.form['website']
        business.instagram = request.form['instagram']
        business.tag = request.form['tag']
        db.session.commit()
        return jsonify(message =  "You updated a business"), 202
    else:
        return jsonify(message="That business does not exist"), 404

# delete a business
@app.route('/remove_business', methods=['DELETE'])
def remove_business():
    email=request.args.get('email')
    business = Business.query.filter_by(email=email).first()
    if business:
        db.session.delete(business)
        db.session.commit()
        return jsonify(message='You deleted a business'), 202
    else:
        return jsonify('That business does not exist'), 404


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

class BusinessSchema(ma.Schema):
    class Meta:
        fields = ('email','name','description', 'phone_no', 'password', 'website', 'instagram','tag')


business_schema = BusinessSchema()
businesses_schema = BusinessSchema(many=True)
