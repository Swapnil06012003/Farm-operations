import sqlite3
from email.message import EmailMessage
import ssl
import smtplib
import os
conn=sqlite3.connect('ferti.db')
cursor=conn.cursor()
cursor.execute("SELECT name, cp FROM fer")
l=cursor.fetchall()

# file1=open("prediction.txt","a")
# file1.write("Current prices of available crops:\n\n\n")
# for i in l:
#     cost=i[1]*2+2
#     if(cost>2):
#         string=f"{i[0]}  {cost}\n"
#         file1.write(string)
#
# file1.write("\n\n\nPredictions for the prices that will tomorrow:\n\n\n")
# for i in l:
#     cost=i[1]*2+2
#     if(cost>2):
#         string=f"{i[0]}  {cost}\n"
#         file1.write(string)

# table='''CREATE table crop(
#             name CHAR(25),
#             type CHAR(25),
#             doa CHAR(25),
#             doe CGAR(25),
#             quantity INT,
#             cp  INT,
#             sp  INT,
#             prof   REAL
#                 )'''
# l=["Boric acid","pesticides","30/06/2023","30/09/2023",0	,0	,0,	0]
# insert='''INSERT INTO crop(name,type,doa,doe,quantity,cp,sp,prof)   VALUES(?,?,?,?,?,?,?,?)'''
# cursor.execute(insert,l)
# abcd='Spinach'
# command='DELETE FROM crop WHERE name = ?'
type='Pesticides'
command='SELECT doe,name from fer where type =?'
cursor.execute(command,(type, ))
l=cursor.fetchall()
str1="Dear user, below is the list of all the resources and with their date of exhaustion: \n\n"
for i in l:
    str1=str1+str(i[0])+"      "+str(i[1])
    str1=str1+"\n"

type='Fertilizer'
command='SELECT doe,name from fer where type =?'
cursor.execute(command,(type, ))
l=cursor.fetchall()
for i in l:
    str1=str1+str(i[0])+"      "+str(i[1])
    str1=str1+"\n"

str1=str1+"\n\n\nThanks,\nSupport team"
print(str1)

sender = 'raiswapnil0601@gmail.com'
password = "iubj sphw rszj qnsp"
reciever = 'sr7104@srmist.edu.in'
subject =   'Maintenance'
body=str1
em = EmailMessage()
em['from'] = sender
em['To'] = reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, reciever, em.as_string())

file1 = open("maintenance.txt","a")
file1.write(str1)
conn.commit()
conn.close()
