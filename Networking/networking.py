from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/nap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


class Namecard(db.Model):
    __tablename__ = 'namecards'

    uid = db.Column(db.String(8), primary_key=True)
    cid = db.Column(db.String(8), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_num = db.Column(db.Integer(), nullable=True)
    company = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100), nullable=False)

    def __init__(self, uid, cid, name, email, phone_num, company, title, industry):
        self.uid = uid
        self.cid = cid
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.company = company
        self.title = title
        self.industry = industry

    def json(self):
        return {"uid": self.uid, "cid": self.cid, "name": self.name, "email": self.email, "phone_num":self.phone_num, "company":self.company, "title":self.title, "industry": self.industry}


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

@app.route("/namecards/<string:uid>&<string:email>", methods=['POST'])
def create_namecard(uid,email):
    if (Namecard.query.filter_by(uid=uid, email=email).first()):
        return jsonify({"message": "An email '{}' already exists.".format(email)}), 400

    data = request.get_json()
    namecard = Namecard(data)

    try:
        db.session.add(namecard)
        db.session.commit() 
    except:
        return jsonify({"message": "An error occurred creating the namecard."}), 500

    return jsonify(book.json()), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)
