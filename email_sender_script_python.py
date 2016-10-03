import smtplib	
#connection to server
#for Gmail--smtp.gmail.com
#for yahoo--smtp.mail.yahoo.com
#for outlook--smtp-mail.outlook.com
smtpobj=smtplib.SMTP('smtp.gmail.com', 587)
#first hello packet
smtpobj.ehlo()
#for encription
smtpobj.starttls()
#your login to your mail account
smtpobj.login('YOUR_EMAIL_ADDRESS', 'YOUR_PASSWORD')
#from address,to address ,Subject:something.\n Now your mail body msg
smtpobj.sendmail('manjulyadav93@gmail.com', 'manjulyadav93@gmail.com', 'Subject:Trail mail from python.\nHi Manjul,How are you?Have you got your salary')
#disconnecting from server
smtpobj.quit()
