import smtplib
import os
file=open("/home/accuracy.txt","r")
aa=file.read()
aa=float(aa)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address="sender_emai"
host_pass ="sender_password"
guest_address ="rec_email"
subject ="Your model get best accuracy"
content ='''Hi vishnupal you get best 
   %f accuracy '''%(aa)
message=MIMEMultipart()
message['From'] =host_address
message['To']=guest_address
message['Subject'] =subject
message.attach(MIMEText(content,'plain'))
session=smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login(host_address,host_pass)
text=message.as_string()
session.sendmail(host_address,guest_address,text)
session.quit()
print("suucess ")

