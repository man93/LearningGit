import smtplib	
smtpobj=smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login('manjulyadav93@gmail.com', '!@#$%^&*()_+')
smtpobj.sendmail('manjulyadav93@gmail.com', 'manjulyadav93@gmail.com', 'Subject:Trail mail from python.\nHi Manjul,How are you?Have you got your salary')
smtpobj.quit()
