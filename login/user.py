from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, g, url_for
from flask_cors import CORS
from os import environ
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from flask import Blueprint
import pymysql
import passlib 

# docker is being used for all microservices 

app = Flask(__name__)

CORS(app)

# add the above code if docker is used 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://nap@localhost:3306/user'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    emailpassword = db.Column(db.String(1000), nullable=False)

    def __init__(self,uid,name,email,password, emailpassword):
        self.uid = uid
        self.name = name
        self.email = email
        self.password = password
        self.emailpassword = emailpassword

    def json(self):
        return {"uid": self.uid, "name": self.name, "email": self.email, "password": self.password, "emailPassword": self.emailpassword}
    
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
    emailpassword = request.json.get('emailpassword')

    if uid is None or password is None or email is None or name is None:
        return jsonify({"message": "Missing field"}), 401
    # missing arguments
    if User.query.filter_by(uid=uid).first() is not None:# existing user
        return jsonify({"message": "An account with this username already exists. Please try another username."}), 400
    
    user = User(uid=uid, name=name, email=email, password=password, emailpassword=emailpassword)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.uid}), 201

@app.route("/users/changepassword/<string:userid>&<string:newPassword>", methods=["POST"])
def changePassword(userid, newPassword) :
    newHash = pwd_context.encrypt(newPassword)
    conn = pymysql.connect(
        host="localhost",
        user="nap",
        db="user",
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        stmt = conn.cursor()
        sql = '''UPDATE users SET `password`=%s WHERE uid=%s '''
        stmt.execute( sql, (newHash, userid) )
        return jsonify({"status": "success"}), 201
    except: 
        return jsonify({"status": "failure"})
    finally: 
        conn.close()

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

@app.route("/updateUser/<string:uid>", methods=["POST"])
def updateUser(uid):
    data = request.get_json()
    print (type(data))
    try:
        conn = pymysql.connect(
            host="localhost",
            user="nap",
            db="user",
            cursorclass=pymysql.cursors.DictCursor
        )

        password = data["password"]
        password = pwd_context.encrypt(password)
        print (password)
        stmt = conn.cursor()

        sql = "UPDATE users SET `name`=%s, `email`=%s, `password`=%s, `emailpassword`=%s WHERE `uid`=%s"

        stmt.execute(sql, (data["name"], data["email"], password, data["email_password"], uid))

    except:
        return jsonify({"status": "failure"}), 200

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    # host = '0.0.0.1"
    app.run(host = '0.0.0.0',port=8000, debug=True)
# run the programme with any name
# if you dont add this in it will start looking for app.py
