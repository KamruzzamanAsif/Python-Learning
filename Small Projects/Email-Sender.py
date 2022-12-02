import smtplib

SenderAddress = 'asif420kamruzzaman@gmail.com'
password = 'ikqeahuixwmzybkp' # a temp app password (now removed)
# to make app password: go to google account > Security > Signing in to Google > Apps password

ReceiverAddress = 'asif720kamruzzaman@gmail.com'

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this is a email form python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for i in range (3):
    server.sendmail(SenderAddress, ReceiverAddress, body)
server.quit()
