import json
import sys
import os
import random
import datetime
import pika
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from sqlalchemy import and_, or_, not_
import smtplib, ssl

hostname = "localhost" # default hostname
port = 5672 # default port
# connect to the broker and set up a communication channel in the connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
    # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
    # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
channel = connection.channel()
# set up the exchange if the exchange doesn't exist
exchangename="email_topic"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

def receiveEmail():
    # prepare a queue for receiving messages
    channelqueue = channel.queue_declare(queue="gmail.email", durable=True) # 'durable' makes the queue survive broker restarts so that the messages in it survive broker restarts too
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='gmail.email') # bind the queue to the exchange via the key
        # any routing_key with two words and ending with '.order' will be matched

    # set up a consumer and start to wait for coming messages
    channel.basic_qos(prefetch_count=1) # The "Quality of Service" setting makes the broker distribute only one message to a consumer if the consumer is available (i.e., having finished processing and acknowledged all previous messages that it receives)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) # 'auto_ack=True' acknowledges the reception of a message to the broker automatically, so that the broker can assume the message is received and processed and remove it from the queue
    channel.start_consuming() # an implicit loop waiting to receive messages; it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("Received an order by " + __file__)
    
    receiver_email, receiver_name, emailsubject, emailmessage, senderEmail, emailPassword = json.loads(body)
    result = sendEmail(receiver_email, receiver_name, emailsubject, emailmessage, senderEmail, emailPassword)
    # print processing result; not really needed
    print(result ) # convert the JSON object to a string and print out on screen
    print() # print a new line feed to the previous json dump
    print() # print another new line as a separator


def sendEmail(receiver_email, receiver_name, emailsubject, emailmessage, senderEmail, emailPassword):
    port = 465  # For SSL
    #driver.execute_script("window.localStorage.getItem('checked');")
    smtp_server = "smtp.gmail.com"
    sender_email = senderEmail  # Enter your address
    password = emailPassword#input("Type your password and press enter: ")
        
    message = """\
    Subject: """+emailsubject+"""

    Dear """+ receiver_name + ",\n" +emailmessage


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
        except:
            return ("FAIL")
        else:
            server.sendmail(sender_email, receiver_email, message)
    return ("Email(s) sent to" + str(sender_email))


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("This is " + os.path.basename(__file__) + ": shipping for an order...")
    receiveEmail()