from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from sqlalchemy import and_, or_, not_
import smtplib, ssl
import pika
import json


app = Flask(__name__)

CORS(app)

@app.route("/emailing/<string:emailcheck>")
def checkEmailing(emailcheck):
    return(emailcheck)


@app.route("/emailing/<string:emailcheck>&<string:emailname>&<string:emailsubject>&<string:emailmessage>&<string:senderEmail>&<string:emailPassword>")
def sendEmail(emailcheck, emailname, emailsubject, emailmessage, senderEmail, emailPassword):
    hostname = "localhost" # default broker hostname. Web management interface default at http://localhost:15672
    port = 5672 # default messaging port.
    # connect to the broker and set up a communication channel in the connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
        # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
        # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
    channel = connection.channel()

    # set up the exchange if the exchange doesn't exist
    exchangename="email_topic"
    channel.exchange_declare(exchange=exchangename, exchange_type='topic')

    # prepare the message body content
    # print(emailcheck+" allll emailssss")
    # print(emailname)
        # By default, the message is "transient" within the broker;
        #  i.e., if the monitoring is offline or the broker cannot match the routing key for the message, the message is lost.
        # If need durability of a message, need to declare the queue in the sender (see sample code below).
    
    # receiver_email = emailcheck.split(",")  # Enter receiver address
    # receiver_names = emailname.split(",")
    receiversEmail = emailcheck.split(",")
    receiversName = emailname.split(",")
    for i in range(len(receiversEmail)):
        message = json.dumps( (receiversEmail[i], receiversName[i], emailsubject, emailmessage, senderEmail, emailPassword), default=str) # convert a JSON object to a string

        channel.queue_declare(queue='gmail.email', durable=True) # make sure the queue used by Shipping exist and durable
        channel.queue_bind(exchange=exchangename, queue='gmail.email') # make sure the queue is bound to the exchange
        channel.basic_publish(exchange=exchangename, routing_key="gmail.email", body=message,
            properties=pika.BasicProperties(delivery_mode = 2, # make message persistent within the matching queues until it is received by some receiver (the matching queues have to exist and be durable and bound to the exchange, which are ensured by the previous two api calls)
            )
        )
    # send the message
    # always inform Monitoring for logging no matter if successful or not
    channel.basic_publish(exchange=exchangename, routing_key="", body=message)
    return('sent')
    # close the connection to the broker
    connection.close()
        


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8004, debug=True)
    # sendEmail("testingforlife963@gmail.com", "Test", "TestBody", 'testingforlife369@gmail.com', "Numlock@22")