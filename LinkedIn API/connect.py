from linkedin_v2 import linkedin 

def generateCredentials(path):
    credentials = {}
    data = []
    with open(path) as f:
        for line in f:
            data.append(line.strip())

    for line in data:
        credentials[line.split("=")[0]] = line.split("=")[1]
    return credentials

credentials = generateCredentials("./credentials/linkedin.txt")

API_KEY = credentials["key"]
API_SECRET = credentials["secret"]
RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
# Optionally one can send custom "state" value that will be returned from OAuth server
# It can be used to track your user state or something else (it's up to you)
# Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it
#authorization.state = 'your_encoded_message'
print (authentication.authorization_url)  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)

