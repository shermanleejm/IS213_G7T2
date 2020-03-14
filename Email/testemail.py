import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "testingforlife369@gmail.com"  # Enter your address
password = "Numlock@22"#input("Type your password and press enter: ")
receiver_email = ["testingforlife963@gmail.com"]  # Enter receiver address
message_array=[]
for rec in range(len(receiver_email)):
    name=receiver_email[rec][:receiver_email[rec].find("@")]
    message = """\
Subject: Hi there

Hi {}.""".format(name)
    message_array.append(message)


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    try:
        server.login(sender_email, password)
    except:
        print("WRONG PASSWORD")
    else:
        for msg in range(len(message_array)):
            server.sendmail(sender_email, receiver_email[msg], message_array[msg])
        message_array=[]