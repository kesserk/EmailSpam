#Writing an Email Spammer in Python

#First, Importing the Simple Mail Transfer Protocol Module

import smtplib
from prompt_toolkit import prompt

#Specifying the From and To addresses
print("I am not responsible for what you do with this, this is for educational use only. If this is used for anything else I will not be taken into account of YOUR actions.")
toaddress = input("To address: ")

#Now,Specifying the Gmail Login

username = input("Email Login: ")
password = prompt("Password: ", is_password = True)
number = int(input('Number of times for spam: '))
fromaddress = username
#Writing the message which will appear in the mail

message = input("Messages to be sent: ")
#Creating a connection with the Gmail server

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

#Creating a for loop to send multiple mails

for i in range (0,number):
  server.sendmail(fromaddress,toaddress,message)
  print(i+1,': messages sent')
print("---------------------")
print("mail sent.")

#closing the server
server.quit()