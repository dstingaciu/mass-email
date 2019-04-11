import smtplib, ssl, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""  # Enter your address
receiver_email = ""  # Enter receiver address
password = "" #Enter API password/email password


message = MIMEMultipart("alternative")
message["Subject"] = "Test Subject" #Insert Email subject
message["From"] = sender_email #Sender's Email
#message["To"] = receiver_email #Who you're sending it (cc)

# Create the plain-text and HTML version of your message
html = """\
<!DOCTYPE html>

<body>
<h1>Test</h1>
</body>

</html>
"""

# Turn these into plain/html MIMEText objects
htTXT = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(htTXT)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    with open("admitted.csv") as file: #If you have a csv of emails
      reader = csv.reader(file)
      next(reader)
      for email in reader:
        print("Sending to: ".join(email))
        server.sendmail(
          sender_email, 
          email, 
          message.as_string()
        )
    #server.sendmail(sender_email, receiver_email, message.as_string()) If you just want to send it to one person