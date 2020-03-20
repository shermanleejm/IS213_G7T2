from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import and_, or_, not_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/nap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#CORS is to cross resource sharing
db = SQLAlchemy(app)
CORS(app)


class Email(db.Model):
    __tablename__ = 'namecards'
    uid = db.Column(db.String(8), primary_key=True)
    cid = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_num = db.Column(db.Integer)
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
        return {"uid": self.uid,"cid": self.cid,"name": self.name, "email": self.email,"phone_num": self.phone_num,
        "company": self.company,"title": self.title,"industry": self.industry}


@app.route("/email/<string:uid>")
def get_all(uid):
    email = Email.query.filter_by(uid=uid).all()
    if email:
        return jsonify({"email": [emails.json() for emails in email]})
    return jsonify({"message": "======"})   


@app.route("/email/<string:uid>&<string:company>&<string:industry>")
def find_by_company_indust(uid, company, industry):
    email = Email.query.filter_by(uid=uid, company=company, industry=industry).all()
    if email:
        return ({"email": [emails.json() for emails in email]})
    return jsonify({"message": "______ not found."}), 404
    
@app.route("/email/<string:uid>&<string:either>")
def find_by_companyOrindust(uid,either):
    email = Email.query.filter(Email.uid==uid,(or_(Email.company.like('%'+either+'%'), Email.industry.like('%'+either+'%')))).all()
    if email:
        return ({"email": [emails.json() for emails in email]})
    return jsonify({"message": "______ not found."}), 404

# @app.route("/email/<string:uid>&<string:either>")
# def find_by_either(either):
#     email = Email.query.filter(
#         and_(uid=uid,((company=either | title=either, industry=either))))
#     if len(email.all()) != 0:
#         return ({"email": [emails.json() for emails in email]})
#     return jsonify({"message": "______ not found."}), 404


# @app.route("/book/<string:isbn13>", methods=['POST'])
# def create_book(isbn13):
#     if (Book.query.filter_by(isbn13=isbn13).first()):
#         return jsonify({"message": "A book with isbn13 '{}' already exists.".format(isbn13)}), 400

#     data = request.get_json()
#     book = Book(isbn13, **data)

#     try:
#         db.session.add(book)
#         db.session.commit()
#     except:
#         return jsonify({"message": "An error occurred creating the book."}), 500

#     return jsonify(book.json()), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)
