import smtplib
#from email.mime.text import MIMEText

gmail_user = 'hackscorpionmora@gmail.com'  
gmail_password = '123456mora'

sent_from = gmail_user  
to = ['kahnchana@gmail.com', 'bhanuka.15@cse.mrt.ac.lk']  
subject = 'OMG Super Important Message'  
body = 'Hey, whats up?\n\n- You'

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.quit()
print ('Email sent!')
print ('Something went wrong...')

##import smtplib
##server = smtplib.SMTP('smtp.gmail.com', 587)
##
### Log in to the server
##server.login("hackscorpionmora@gmail.com","123456mora")
##
### Send mail
##msg = "\nHello!"
##server.sendmail("bhanukarc@gmail.com","kahnchana@gmail.com", msg)
