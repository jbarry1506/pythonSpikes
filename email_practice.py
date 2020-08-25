import smtplib
import vars

jims_email = vars.jims_email
pw = vars.email_pw

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(jims_email, pw)
except Exception as e:
    print('Something went wrong with Login.')
    print(e)

try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()   # optional
    # ...send emails
except Exception as e:
    print('Something went wrong in SSL')
    print(e)

sent_from = vars.jims_email
to = [vars.jims_email]
subject = 'OMG Super Important Message2'
body = "Hey, what's up?\n\n- You"

email_text = ("""\
From: {}
To: {}
Subject: {}

{}
""").format(sent_from, ", ".join(to), subject, body)

try:
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except Exception as e:
    print("The email wasn't sent.")
    print(e)
