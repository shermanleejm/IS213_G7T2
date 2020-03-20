import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
import pandas as pd 
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

def getCredentials(os) :
    credentials = []
    if os == "mac":
        with open("./credentials/mac.txt") as f:
            for line in f:
                credentials.append(line.strip())
    else :
        with open("./credentials/win.txt") as f:
            for line in f:
                credentials.append(line.strip())
    output = {
        "username" : credentials[0],
        "password" : credentials[1],
        "port" : credentials[2]
    }

    return output

# EDIT YOUR OS HERE
os = "mac"

credentials = getCredentials(os)

username = credentials["username"]
password = credentials["password"]
port = credentials["port"]

url = f"mysql+mysqlconnector://{username}:{password}@localhost:{port}/jobscraper"

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class JobScraper(db.Model):
    __tablename__ = "jobs"

def internJobsScraper(keyword, location="Singapore"):
    posts = {}

    url = f"https://www.internjobs.com/job/search?keyword={keyword}&location={location}&Action=Search"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.select("a[href*='adzuna']"):
        if a.text != "":
            posts[a.text] = a["href"]
    
    return posts

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



if __name__ == '__main__':
    app.run(port=5001, debug=True)