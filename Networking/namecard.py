from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pymysql
from os import environ
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://nap@localhost:3306/namecard'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine(environ.get('dbURL'))
# engine = create_engine('mysql+mysqlconnector://nap@localhost:3306/namecard')

db = SQLAlchemy(app)
CORS(app)


class Namecard(db.Model):
    __tablename__ = 'namecards'

    uid = db.Column(db.String(8), primary_key=True,nullable=True)
    # cid = db.Column(db.String(8), primary_key=True, nullable=False, autoincrement=False)
    name = db.Column(db.String(100), primary_key=True,nullable=False)
    email = db.Column(db.String(100), primary_key=True,nullable=False)
    phone_num = db.Column(db.Integer(), primary_key=True,nullable=True)
    company = db.Column(db.String(100), primary_key=True,nullable=False)
    title = db.Column(db.String(100), primary_key=True,nullable=False)
    industry = db.Column(db.String(100), primary_key=True,nullable=False)

    def __init__(self, uid, name, email, phone_num, company, title, industry):
        self.uid = uid
        # self.cid = cid
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.company = company
        self.title = title
        self.industry = industry

    def json(self):
        return {"uid": self.uid, "name": self.name, "email": self.email, "phone_num":self.phone_num, "company":self.company, "title":self.title, "industry": self.industry}


@app.route("/namecards/<string:uid1>&<string:company1>&<string:industry1>") #all namecards with defined uid
def get_namecards(uid1, company1, industry1):
    # namecards = Namecard.query.filter_by(uid=uid).all()
    # if namecards:
    #     return jsonify({"namecards": [namecard.json() for namecard in namecards]})
    # return jsonify({"message": "No Namecards"}),404

    # conn = pymysql.connect(
    #     host="127.0.0.1",
    #     port=3306,
    #     user="nap",
    #     db="namecard",
    #     cursorclass=pymysql.cursors.DictCursor
    # )
    result = []
    temp_namecards = Namecard.query.filter(Namecard.uid==uid1, Namecard.company.like(company1), Namecard.industry.like(industry1)).all()

    for n in temp_namecards:
        result.append(n.json())
    return jsonify(result)

    # try:
    #     stmt = conn.cursor()
    #     sql = '''SELECT * FROM namecards 
    #     WHERE uid=%s AND company like %s AND industry like %s '''
    #     stmt.execute(sql, (uid, company, industry))
    #     result = stmt.fetchall()
    #     print (result)
    #     return jsonify(result)
    # finally: 
    #     conn.close()
        
@app.route("/namecards/<string:uid>") #all namecards with defined uid
def get_all(uid):
    namecards = Namecard.query.filter_by(uid=uid).all()
    if namecards:
        return jsonify({"namecards": [namecard.json() for namecard in namecards]})
    return jsonify({"message": "No Namecards"}),404


@app.route("/namecards/<string:uid>&<string:name>")
def find_by_name(uid,name):
    namecards = Namecard.query.filter(Namecard.name.like('%'+name+'%'), Namecard.uid==uid)
    if len(namecards.all()) != 0:
        return jsonify({"namecards": [namecard.json() for namecard in namecards]})
    return jsonify({"message": "Namecard not found"}), 404



@app.route("/namecardStats/<string:uid>")
def getNamecardStats(uid) :
    with engine.connect() as conn:
        company_sql = f"SELECT company FROM namecards WHERE uid=\"{uid}\" GROUP BY company ORDER BY count(company) DESC LIMIT 1"
        company = conn.execute(company_sql)
        for row in company:
            c = (row[0])
        industry_sql = f"SELECT industry FROM namecards WHERE uid=\"{uid}\" GROUP BY industry ORDER BY count(industry) DESC LIMIT 1"
        industry = conn.execute(industry_sql)
        for row in industry:
            i = (row[0])

    return jsonify( {"company": c, "industry": i} )
    # conn = pymysql.connect(
    #     host="127.0.0.1",
    #     port=3306,
    #     user="nap",
    #     db="namecard",
    #     charset='utf8mb4',
    #     cursorclass=pymysql.cursors.DictCursor
    # )

    # result = {"company": [], "industry": []}
    
    # try:
    #     # Most popular company
    #     stmt = conn.cursor()
    #     sql = '''SELECT company FROM namecards WHERE uid=%s GROUP BY company ORDER BY count(company) DESC LIMIT 1'''
    #     stmt.execute(sql, (uid))
    #     result["company"] = stmt.fetchone()["company"]
    
    #     stmt1 = conn.cursor()
    #     sql = '''SELECT industry FROM namecards WHERE uid=%s GROUP BY industry ORDER BY count(industry) DESC LIMIT 1'''
    #     stmt1.execute(sql, (uid))
    #     result["industry"] = stmt1.fetchone()["industry"]
        
    #     return jsonify(result)

    # finally: 
    #     conn.close()
    #     return jsonify(result)
    
    


# @app.route("/namecards/<string:uid>&<string:name>")
# def find_by_name(uid,name):
#     namecards = Namecard.query.filter(Namecard.name.like('%'+name+'%'), Namecard.uid==uid)
#     if len(namecards.all()) != 0:
#         return jsonify({"namecards": [namecard.json() for namecard in namecards]})
#     return jsonify({"message": "Namecard not found"}), 404
# <string:uid>&<string:name>&<string:email>&<string:phone_num>&<string:company>&<string:title>&<string:industry>

@app.route("/namecards/create", methods=['POST'])
def create_namecard():
    uid = request.json.get('uid')
    # print(uid)
    name = request.json.get('Name')
    title = request.json.get('Title')
    email = request.json.get('Email')
    industry = request.json.get('Industry')
    phone_num = request.json.get('phone_number')
    company = request.json.get('Company')
    print(uid,name,title,email,industry,phone_num,company)
    
    if (Namecard.query.filter_by(uid=uid, email=email).first()):
        return jsonify({"message": "An email '{}' already exists.".format(email)}), 400

    # data = request.get_json()
    # namecard = Namecard(data)

    # if uid is None or password is None or email is None or name is None:
    #     return jsonify({"message": "Missing field"}), 401
    # missing arguments
    # if User.query.filter_by(uid=uid).first() is not None:# existing user
    #     return jsonify({"message": "An account with this username already exists. Please try another username."}), 400
    
    
    namecard = Namecard(uid=uid, name=name, email=email, phone_num=phone_num, company=company, title=title,industry=industry)
    # user.hash_password(password)
    db.session.add(namecard)
    db.session.commit()
    return jsonify({'message': name}), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)
