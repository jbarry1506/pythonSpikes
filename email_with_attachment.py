# Import smtplib for the actual sending function
import smtplib
import vars

# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Our family reunion'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = vars.jims_email
msg['To'] = COMMASPACE.join(vars.jims_email)
msg.preamble = 'Our family reunion'

pic_file = "/Users/devop/Desktop/Screen Shot 2020-04-14 at 1.50.29 PM.png"
with open(pic_file, 'rb') as fp:
    img = MIMEImage(fp.read())
msg.attach(img)

# Assume we know that the image files are all in PNG format
# for file in pngfiles:
#     # Open the files in binary mode.  Let the MIMEImage class automatically
#     # guess the specific image type.
#     with open(file, 'rb') as fp:
#         img = MIMEImage(fp.read())
#     msg.attach(img)

# Send the email via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()