from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, g, url_for
from flask_cors import CORS
from os import environ
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from flask import Blueprint

# docker is being used for all microservices 

app = Flask(__name__)

CORS(app)



# add the above code if docker is used 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') 
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/user'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self,uid,name,email,password):
        self.uid = uid
        self.name = name
        self.email = email
        self.password = password

    def json(self):
        return {"uid": self.uid, "name": self.name, "email": self.email, "password": self.password}
    
    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

@app.route('/users/login',  methods=['POST'])
def verify_password():
    uid = request.json.get('uid')
    password = request.json.get('password')
    user = User.query.filter_by(uid = uid).first() #means they sign it either with their username

    if not user or not user.verify_password(password):
            return jsonify({"message": "Please check your login details and try again."}), 400 # if user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
    return jsonify({'username': user.uid}), 201


# is uid better or email better to check if the user exists?
# finding an existing user account
@app.route("/users/<string:uid>") 
# checking if the user exists
def find_by_account(uid):

    user = User.query.filter_by(uid = uid).first() #means they sign it either with their username
    # retrieves the first result when entered via the first function 

    if user:
        return jsonify(user.json())
    return jsonify({"message": "This User account does not exist, please try again."}), 404


@app.route("/users/signup", methods=['POST'])
# creating a new user, throwing an error in case the user already exists
def new_user():
    uid = request.json.get('uid')
    password = request.json.get('password')
    name = request.json.get('name')
    email = request.json.get('email')

    if uid is None or password is None or email is None or name is None:
        return jsonify({"message": "Missing field"}), 401
    # missing arguments
    if User.query.filter_by(uid=uid).first() is not None:# existing user
        return jsonify({"message": "An account with this username already exists. Please try another username."}), 400
    
    user = User(uid=uid, name=name, email=email, password=password)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.uid}), 201

# def create_user(email):
#     if (User.query.filter_by(email = email).first()):
        
#         return jsonify({"message": "An account with this username already exists.Please try again with another username."}), 400

#     data = request.get_json()
#     # gets all the other details of the user
#     user = User(**data)
#     try:
#         db.session.add(user)
#         db.session.commit()
#         #   adding all the records using the sql commands
#     except:
#         return jsonify({"message": "An error occurred when creating the account."}), 500

#     return jsonify(user.json()), 201
#     # return jsonify({"message":"The account has been successfully created!"}),201

if __name__ == '__main__':
    # host = '0.0.0.1"
    app.run(host = '0.0.0.0',port=8000, debug=True)
# run the programme with any name
# if you dont add this in it will start looking for app.py
