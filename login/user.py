from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS
from os import environ
# docker is being used for all microservices 

app = Flask(__name__)

CORS(app)



app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') 
# add the above code if docker is used 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/nap'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    pword = db.Column(db.String(100), nullable=False)

    def __init__(self,uid,name,email,pword):
        self.uid = uid
        self.name = name
        self.email = email
        self.pword = pword

    def json(self):
        return {"uid": self.uid, "name": self.name, "email": self.email, "pword": self.pword}

# is uid better or email better to check if the user exists?
# finding an existing user account
@app.route("/users/<string:email>") 
# checking if the user exists
def find_by_account(email):

    user = User.query.filter_by(email = email).first() #means they sign it either with their username
    # retrieves the first result when entered via the first function 

    if user:
        return jsonify(user.json())
    return jsonify({"message": "This User account does not exist, please try again."}), 404


@app.route("/users/<string:email>", methods=['POST'])
# creating a new user, throwing an error in case the user already exists
def create_user(email):
    if (User.query.filter_by(email = email).first()):
        
        return jsonify({"message": "An account with this username already exists.Please try again with another username."}), 400

    data = request.get_json()
    # gets all the other details of the user
    user = User(**data)
    

    try:
        db.session.add(user)
        db.session.commit()
        #   adding all the records using the sql commands
    except:
        return jsonify({"message": "An error occurred when creating the account."}), 500

    return jsonify(user.json()), 201
    # return jsonify({"message":"The account has been successfully created!"}),201

if __name__ == '__main__':
    # host = '0.0.0.1"
    app.run(host = '0.0.0.1',port=5001, debug=True)
# run the programme with any name
# if you dont add this in it will start looking for app.py
