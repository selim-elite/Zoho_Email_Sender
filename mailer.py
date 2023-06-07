import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# Define to/from
sender = 'email'
sender_title = "test title"
recipient = 'email'

# Create message
message = MIMEMultipart()
message['Subject'] = Header('Sent from python', 'utf-8')
message['From'] = formataddr((str(Header(sender_title, 'utf-8')), sender))
message['To'] = recipient

# HTML message body
html = """\
<html>
  <body>
    <p>This is an HTML email message!</p>
  </body>
</html>
"""

# Attach HTML message to MIMEMultipart message
html_part = MIMEText(html, 'html')
message.attach(html_part)

# Create server object with SSL option
server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

# Perform operations via server
server.login('email', 'password')
server.sendmail(sender, [recipient], message.as_string())
server.quit()
