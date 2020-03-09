import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver

keyword = "data"
location = "Singapore"

def internjobsScraper(keyword, location):
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

# print (internjobsScraper("data", "Singapore"))
print (indeedScraper("data internship"))





