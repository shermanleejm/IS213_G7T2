WELCOME TO NETWORKING ASSISTANCE PLATFORM

Prerequisites: 
1. You need docker installed.
2. This application requires RabbitMQ installed as well
3. You need to have MySQL installed with a user callled nap with 
data and structure global privileges and no password
    SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, FILE, INDEX, 
    ALTER, CREATE TEMPORARY TABLES, CREATE VIEW, EVENT, TRIGGER, 
    SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EXECUTE


Steps for a great experince
0. Navigate your cmd or terminal window to IS213_G7T2 and install the following python packages
    pip install flask
    pip install flask_sqlalchemy
    pip install flask_cors
    pip install pika

1. Launch RabbitMQ server through the command: 
    rabbitmq-server 

2. Retrieve the docker images for user and namecard:
    docker pull shermanlee/user:1.0.0
    docker pull shermanlee/namecard:1.0.0
    docker pull shermanlee/job:1.0.0

3. Run namecard.py at port 8001
    docker run -p 8001:8001 -e dbURL=mysql+mysqlconnector://nap@host.docker.internal:3306/namecard shermanlee/namecard

4. Run user.py at port 8000
    docker run -p 8000:8000 -e dbURL=mysql+mysqlconnector://nap@host.docker.internal:3306/user shermanlee/user

5. Run Emailing.py in the Email folder
    (depending on where your terminal working dir is)
    python Email/Emailing.py

6. Run 3 instances of EmailSender.py in Email_Sender folder
    (depending on where your terminal working dir is)
    python Email_Sender/EmailSender.py

7. Run job.py at port 5070
    docker run -p 5070:5070 shermanlee/job

8. Open login.html in UI folder in your web browser
    UI/login.html