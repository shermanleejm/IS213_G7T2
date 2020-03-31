from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from sqlalchemy import and_, or_, not_
import smtplib, ssl

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
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

@app.route("/mail/<string:uid>&<string:emailcheck>&<string:emailsubject>&<string:emailmessage>&<string:senderEmail>&<string:emailPassword>")
def sendEmail(uid, emailcheck, emailsubject, emailmessage,senderEmail,emailPassword):
    
    port = 465  # For SSL
    #driver.execute_script("window.localStorage.getItem('checked');")
    smtp_server = "smtp.gmail.com"
    sender_email = senderEmail  # Enter your address
    password = emailPassword#input("Type your password and press enter: ")
    receiver_email = emailcheck.split(",")  # Enter receiver address
    message_array=[]
    for rec in range(len(receiver_email)):
        name=receiver_email[rec][:receiver_email[rec].find("@")]
        message = """\
    Subject: """+emailsubject+"""

    Dear """+ name + ",\n" +emailmessage
        message_array.append(message)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
        except:
            return jsonify({"message": "Wrong password."})
        else:
            for msg in range(len(message_array)):
                server.sendmail(sender_email, receiver_email[msg], message_array[msg])
            message_array=[]
    return jsonify({"message": "Email(s) sent."})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8004, debug=True)
