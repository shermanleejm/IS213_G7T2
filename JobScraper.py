import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
import pandas as pd 
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import platform
import json

operatingsystem = platform.system()

app = Flask(__name__)
# if operatingsystem == "Darwin":
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/book'
# elif operatingsystem == "Windows":
#      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/book'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# def getCredentials(os) :
#     credentials = []
#     if os == "mac":
#         with open("./credentials/mac.txt") as f:
#             for line in f:
#                 credentials.append(line.strip())
#     else :
#         with open("./credentials/win.txt") as f:
#             for line in f:
#                 credentials.append(line.strip())
#     output = {
#         "username" : credentials[0],
#         "password" : credentials[1],
#         "port" : credentials[2]
#     }

#     return output

# # EDIT YOUR OS HERE
# os = "mac"

# credentials = getCredentials(os)

# username = credentials["username"]
# password = credentials["password"]
# port = credentials["port"]

# url = f"mysql+mysqlconnector://{username}:{password}@localhost:{port}/nap"

# app.config['SQLALCHEMY_DATABASE_URI'] = url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class JobScraper(db.Model):
#     __tablename__ = "jobs"

# returns dictionary
def internJobsScraper(keyword, location="Singapore"):
    posts = {}

    url = f"https://www.internjobs.com/job/search?keyword={keyword}&location={location}&Action=Search"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.select("a[href*='adzuna']"):
        if a.text != "":
            posts[a.text] = a["href"]
    
    return posts

# returns dictionary
def indeedScraper(keyword) :
    root = "https://sg.indeed.com"

    links = {}

    if " " in keyword:
        keyword.replace(" ", "+")

    url = f"https://sg.indeed.com/jobs?q={keyword}&l=#"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.select("a[class*='jobtitle turnstileLink']"):
        if a["href"][:3] == "/rc":
            links[a.text.strip()] = root + a["href"]

    return links

# print (internJobsScraper("Data"))
# print (indeedScraper("Data"))

@app.route("/jobs/<string:keyword>")
def getJobs(keyword) :
    result = internJobsScraper(keyword)
    result.update(indeedScraper(keyword))
    return json.dumps(result)

if __name__ == '__main__':
    app.run(port=5069, debug=True)