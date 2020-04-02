import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

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

@app.route("/jobs/<string:keyword>")
def getJobs(keyword) :
    result = internJobsScraper(keyword)
    result.update(indeedScraper(keyword))
    data = {'title' : list(result.keys()), 'url' : list(result.values())}

    return json.dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5070, debug=True)