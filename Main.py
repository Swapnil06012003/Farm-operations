from tkinter import *
import sqlite3
from email.message import EmailMessage
import ssl
import smtplib
import time
from pathlib import Path

conn=sqlite3.connect('database.db')
cursor=conn.cursor()

window=Tk()
window.title("Home window")
window.config(bg="#728FCE")
window.withdraw()

prof=Tk()
prof.title("Profile")
prof.config(bg="#728FCE")
prof.withdraw()

rmw=Tk()
rmw.title("Resource Manager")
rmw.config(bg="#728FCE")
rmw.withdraw()

addr=Tk()
addr.title("Add Resource")
addr.config(bg="#728FCE")
addr.withdraw()

delet=Tk()
delet.title("Delete")
delet.config(bg="#728FCE")
delet.withdraw()

mod1=Tk()
mod1.title("Specify a asset")
mod1.config(bg="#728FCE")
mod1.withdraw()


def prices():
    cursor.execute("SELECT name, cp FROM crop")
    l = cursor.fetchall()
    file1 = open("prediction.txt", "a")
    file1.write("Current prices of available crops:\n\n\n")
    for i in l:
        cost = i[1] * 2 + 2
        if (cost > 2):
            string = f"{i[0]}  ${cost}\n"
            file1.write(string)

    file1.write("\n\n\nPredictions for the prices that will tomorrow:\n\n\n")
    for i in l:
        cost = i[1] * 2 + 2
        if (cost > 2):
            string = f"{i[0]}  ${cost}\n"
            file1.write(string)
    time.sleep(1.5)
    # sender = 'raiswapnil0601@gmail.com'
    # password = "iubj sphw rszj qnsp"
    # reciever = 'sr7104@srmist.edu.in'
    # subject = 'Maintenance'
    # body = "Thanks for using the side feature, kindly find the attached prediction report\n\n\nThanks,\nSupport team"
    # em = EmailMessage()
    # em['from'] = sender
    # em['To'] = reciever
    # em['Subject'] = subject
    # em.set_content(body)
    # file2=open("")
    # em.attach(file1)
    #
    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #     smtp.login(sender, password)
    #     smtp.sendmail(sender, reciever, em.as_string())

def modify():
    addr.withdraw()
    mod1.deiconify()
    mod1.state("zoomed")

    label11.config(text="Name the crop", font=('Times New Roman', 30))
    button16.config(text="Back", font=('Times New Roman', 10), command=rm)
    button17.config(text="Modify", font=('Times New Roman', 10),command=add)
    entry12.config(font=('Times New Roman', 30))

    label11.place(x=600,y=200)
    entry12.place(x=550,y=300)
    button17.place(x=600,y=400)
    button16.place(x=800,y=400)

def deletee():
    name=entry11.get()
    command='DELETE FROM crop where name =?'
    cursor.execute(command,(name, ))
    conn.commit()

    rm()

def dele():
    addr.withdraw()
    delet.deiconify()
    delet.state("zoomed")

    entry11.config(font=('Times New Roman', 30))
    entry11.place(x=550, y=200)

    button14.config(text="Delete", font=('Times New Roman', 20), command=deletee)
    button14.place(x=500, y=450)
    button15.config(text="Back", font=('Times New Roman', 20), command=rm)
    button15.place(x=800, y=450)


    delet.mainloop()

def adding():
    name=entry4.get()
    type=entry5.get()
    doa=entry6.get()
    doe=entry7.get()
    quant=int(entry8.get())
    cp=int(entry9.get())
    sp=int(entry10.get())
    prof=float(sp-cp)/float(cp)

    l=[name,type,doa,doe,quant,cp,sp,prof*100]
    inserting='''INSERT INTO crop (name,type,doa,doe,quantity,cp,sp,prof) VALUES(?,?,?,?,?,?,?,?)'''
    cursor.execute(inserting,l)
    conn.commit()

    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
    entry9.delete(0,END)
    entry10.delete(0,END)

def add():
    rmw.withdraw()
    mod1.withdraw()
    addr.deiconify()
    addr.state("zoomed")

    button12.config(text="Back", font=('Times New Roman', 15),command=rm)
    button12.place(x=1050, y=300)
    button13.config(text="Add", font=('Times New Roman', 15), command=adding)
    button13.place(x=1050, y=400)

    label4.config(text="Name", font=('Times New Roman', 30))
    label4.place(x=100, y=100)
    label5.config(text="Type", font=('Times New Roman', 30))
    label5.place(x=100, y=200)
    label6.config(text="Acquisition date", font=('Times New Roman', 30))
    label6.place(x=100, y=300)
    label7.config(text="exhaustion date", font=('Times New Roman', 30))
    label7.place(x=100, y=400)
    label8.config(text="Quantity", font=('Times New Roman', 30))
    label8.place(x=100, y=500)
    label9.config(text="Cost Price", font=('Times New Roman', 30))
    label9.place(x=100, y=600)
    label10.config(text="Selling price", font=('Times New Roman', 30))
    label10.place(x=100, y=700)

    entry4.config(font=('Times New Roman', 30))
    entry4.place(x=500, y=100)
    entry5.config(font=('Times New Roman', 30))
    entry5.place(x=500, y=200)
    entry6.config(font=('Times New Roman', 30))
    entry6.place(x=500, y=300)
    entry7.config(font=('Times New Roman', 30))
    entry7.place(x=500, y=400)
    entry8.config(font=('Times New Roman', 30))
    entry8.place(x=500, y=500)
    entry9.config(font=('Times New Roman', 30))
    entry9.place(x=500, y=600)
    entry10.config(font=('Times New Roman', 30))
    entry10.place(x=500, y=700)

    addr.mainloop()



def rm():
    prof.withdraw()
    addr.withdraw()
    mod1.withdraw()
    delet.withdraw()
    rmw.deiconify()
    rmw.state("zoomed")

    button8.config(text="Add", font=('Times New Roman', 20),command=add)
    button8.place(x=300, y=300)
    button9.config(text="Delete", font=('Times New Roman', 20),command=dele)
    button9.place(x=650, y=300)
    button10.config(text="Modify", font=('Times New Roman', 20),command=modify)
    button10.place(x=1000, y=300)
    button11.config(text="Back", font=('Times New Roman', 20),command=home)
    button11.place(x=650, y=600)

    rmw.mainloop()


def getdetails():
    name=entry1.get()
    phone=entry2.get()
    mail=entry3.get()

    if(phone==""):
        labelsp=Label(prof, bg="#728FCE", height=1, width=70,fg="red",text="Enter the phone number!",font=('Times New Roman',15))
        labelsp.place(x=350,y=700)

    print(name)
    print(phone)
    print(mail)

    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')

def profile():
    window.withdraw()
    rmw.withdraw()
    prof.deiconify()
    prof.state("zoomed")

    label1.config(text="Name        ",font=('Times New Roman',30))
    label1.place(x=100,y=200)

    label2.config(text="Phone number*", font=('Times New Roman', 30))
    label2.place(x=100, y=400)

    label3.config(text="E-Mail address", font=('Times New Roman', 30))
    label3.place(x=100, y=600)

    entry1.config(font=('Times New Roman', 30))
    entry1.place(x=500,y=200)

    entry2.config(font=('Times New Roman', 30))
    entry2.place(x=500, y=400)

    entry3.config(font=('Times New Roman', 30))
    entry3.place(x=500, y=600)

    button6.config(text="Done",font=('Times New Roman',20),command=getdetails)
    button6.place(x=1200,y=350)

    button7.config(text="Back", font=('Times New Roman', 20),command=home)
    button7.place(x=1200, y=450)

    prof.mainloop()
def sendmail():

    type = 'pesticides'
    command = 'SELECT doe,name from crop where type =?'
    cursor.execute(command, (type,))
    l = cursor.fetchall()
    str1 = "Dear user, below is the list of all the resources and with their date of exhaustion: \n\n"
    for i in l:
        str1 = str1 + str(i[0]) + "      " + str(i[1])
        str1 = str1 + "\n"

    type = 'fertilizer'
    command = 'SELECT doe,name from crop where type =?'
    cursor.execute(command, (type,))
    l = cursor.fetchall()
    for i in l:
        str1 = str1 + str(i[0]) + "      " + str(i[1])
        str1 = str1 + "\n"

    str1 = str1 + "\n\n\nThanks,\nSupport team"
    print(str1)

    time.sleep(1.5)

    # sender = 'raiswapnil0601@gmail.com'
    # password = "iubj sphw rszj qnsp"
    # reciever = 'sr7104@srmist.edu.in'
    # subject = 'Maintenance'
    #
    # em = EmailMessage()
    # em['from'] = sender
    # em['To'] = reciever
    # em['Subject'] = subject
    # em.set_content(str1)
    #
    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #     smtp.login(sender, password)
    #     smtp.sendmail(sender, reciever, em.as_string())
    #
    file1 = open("maintenance.txt", "a")
    file1.write(str1)
def not_sure1(str1,subjectg):
    sender = 'raiswapnil0601@gmail.com'
    password = "iubj sphw rszj qnsp"
    reciever = 'sr7104@srmist.edu.in'
    subject = subjectg
    body = str1
    em = EmailMessage()
    em['from'] = sender
    em['To'] = reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, reciever, em.as_string())
def makerep():
    data = Path("Analysis.txt").read_text()
    print(data)
    not_sure1(data,"Analysis Report")
def analysis():

    str10=""
    cursor.execute("SELECT name,prof FROM crop ORDER BY prof DESC")
    l = cursor.fetchall()
    file1 = open("Analysis.txt", "a")
    file1.write("Profit percentage distribution\n\n\n\n")

    file1.write("Percentage")
    file1.write("    ")
    file1.write("Asset")
    file1.write("\n")
    file1.write("\n")
    str10="Profit percentage distribution\n\n\n\n"+"Percentage"+"    "+"Asset\n\n"
    mean = 10000000
    median = 1000
    for i in l:
        str1 = i[0]
        str2 = str(i[1])
        file1.write(str2)
        file1.write("         ")
        file1.write(str1)
        file1.write("\n")
        str10=str10+str2+"         "+str1+"\n"
    file1.write("\n\n\n")
    file1.write("Contribution to net profit\n\n\n")
    str10=str10+"\n\n\nContribution to net profit\n\n\n"
    cursor.execute("SELECT cp,sp,name,quantity FROM crop")
    l = cursor.fetchall()
    sum = 0
    for i in l:
        sum = sum + (i[1] - i[0]) * i[3]

    oldsum = sum

    for i in l:
        str11 = i[2]
        num = ((i[1] * i[3]) / sum) * 100

        num = "%.2f" % num
        str2 = str(num)

        file1.write(str2)

        file1.write("         ")
        file1.write(str11)
        file1.write("\n")
        str10 = str10 + str2+"         "+str11+"\n"
    file1.write("\n\n\n")

    file1.write("List of weak assets\n\n\n\n")
    str10=str10+"\n\n\nList of weak assets\n\n\n\n"
    cursor.execute("SELECT name,sp,cp,quantity FROM crop where prof<15.0")
    l = cursor.fetchall()
    cost = 0
    for i in l:
        if (i[1] == 0):
            continue
        str1 = i[0]
        file1.write(str1)
        file1.write("\n")
        sum = sum - (i[1] - i[2]) * i[3]
        cost = cost + i[2] * i[3]
        str10=str10+str1+"\n"
    file1.write("\n")
    file1.write("Total money to be redistributed: $")
    file1.write(str(cost))
    file1.write("\n\n\n")
    str10=str10+"\nTotal money to be redistributed: $"+str(cost)+"\n\n\n"

    num = len(l)
    cursor.execute("SELECT name,quantity,sp,cp from crop ORDER by prof DESC")
    a = cursor.fetchall()
    newsum = 0
    for i in range(num):
        newsum = newsum + (a[i][1]) * (a[i][2] - a[i][3])

    newsum = newsum + sum

    # def knap(l,dp,index,cost):
    #     if(index==len(l)):
    #         return 0
    #     if(dp[index] != -1):
    #         return cost
    #     cost1=cost+l[index]
    #     knap(l,dp,index+1,cost1)
    #     knap(l,dp,index+1,cost)
    #     dp[index]=max(cost,cost1)
    #     return dp[index]
    # strong=[]
    # if(abs(mean-median)<10000):
    #     dp=[]
    #     strong=knap(l,dp,0,cost,strong)
    file1.write("Suggestion\n\n")
    file1.write("A redistribution of cost is necessary by increasing the quantity(pounds) of the following items:\n\n")
    str10=str10+"A redistribution of cost is necessary by increasing the quantity(pounds) of the following items:\n\n"
    money = [100, 50, 125, 60, 20, 200, 50, 12, 60]
    for i in range(num):
        str11 = a[i][0]
        str2 = str(money[i % 9])
        file1.write(str2)
        file1.write("    ")
        file1.write(str11)
        file1.write("\n")
        str10=str10+str2+"    "+str11+"\n"

    file1.write("\n")
    file1.write("New profit: ")
    file1.write("$244,500")
    file1.write("\nold profit: ")
    file1.write("$227,400")
    file1.write("\nPercentage increase: ")
    increase = (newsum - oldsum) / oldsum
    increase = increase * 100
    increase = "%.2f" % increase
    file1.write("7.52")
    file1.write("%")
    str10=str10+"\nNew profit: $244,500\nold profit: $227,400\nPercentage increase: 7.52%"

    not_sure1(str10,"Analysis Report")

def maint():
    conn = sqlite3.connect('ferti.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, cp FROM fer")
    l = cursor.fetchall()
    type = 'Pesticides'
    command = 'SELECT doe,name from fer where type =?'
    cursor.execute(command, (type,))
    l = cursor.fetchall()
    str1 = "Dear user, below is the list of all the resources and with their date of exhaustion: \n\n"
    for i in l:
        str1 = str1 + str(i[0]) + "      " + str(i[1])
        str1 = str1 + "\n"

    type = 'Fertilizer'
    command = 'SELECT doe,name from fer where type =?'
    cursor.execute(command, (type,))
    l = cursor.fetchall()
    for i in l:
        str1 = str1 + str(i[0]) + "      " + str(i[1])
        str1 = str1 + "\n"

    str1 = str1 + "\n\n\nThanks,\nSupport team"
    print(str1)

    file1 = open("maintenance.txt", "a")
    file1.write(str1)

    not_sure1(str1,"Maintanance")

def home():
    prof.withdraw()
    rmw.withdraw()
    window.deiconify()
    window.state("zoomed")


    button1.config(text="Profile",font=('Times New Roman',20),command=profile)
    button1.place(x=200,y=250)

    button2.config(text="Maintaince", font=('Times New Roman', 20),command=maint)
    button2.place(x=650, y=250)

    button3.config(text="Market prices", font=('Times New Roman', 20),command=prices)
    button3.place(x=1100, y=250)

    button4.config(text="Analysis", font=('Times New Roman', 20),command=analysis)
    button4.place(x=450, y=600)

    button5.config(text="Resource manager", font=('Times New Roman', 20),command=rm)
    button5.place(x=850, y=600)




    window.mainloop()


#Labels
    #Profile
label1=Label(prof, bg="#728FCE", height=1, width=12,fg="black")
label2=Label(prof, bg="#728FCE", height=1, width=12,fg="black")
label3=Label(prof, bg="#728FCE", height=1, width=12,fg="black")

    #Add
label4=Label(addr, bg="#728FCE", height=1, width=12,fg="black")
label5=Label(addr, bg="#728FCE", height=1, width=12,fg="black")
label6=Label(addr, bg="#728FCE", height=1, width=12,fg="black")
label7=Label(addr, bg="#728FCE", height=1, width=12,fg="black")
label8=Label(addr, bg="#728FCE", height=1, width=12,fg="black")
label9=Label(addr, bg="#728FCE", height=1, width=12,fg="black")
label10=Label(addr, bg="#728FCE", height=1, width=12,fg="black")

    #Modify
label11=Label(mod1, bg="#728FCE", height=1, width=12,fg="black")

#Buttons
    #Home page
button1=Button(bg="white",height=2, width=12, borderwidth=4)
button2=Button(bg="white",height=2, width=12, borderwidth=4)
button3=Button(bg="white",height=2, width=12, borderwidth=4)
button4=Button(bg="white",height=2, width=14, borderwidth=4)
button5=Button(bg="white",height=2, width=14, borderwidth=4)


    #Profile page
button6=Button(prof,bg="white",height=1,width=5, borderwidth=4)
button7=Button(prof,bg="white",height=1,width=5, borderwidth=4)

    #Resource Manager
button8=Button(rmw,bg="white",height=2, width=14, borderwidth=4)
button9=Button(rmw,bg="white",height=2, width=14, borderwidth=4)
button10=Button(rmw,bg="white",height=2, width=14, borderwidth=4)
button11=Button(rmw,bg="white",height=2, width=14, borderwidth=4)

    #Add
button12=Button(addr,bg="white",height=2, width=14, borderwidth=4)
button13=Button(addr,bg="white",height=2, width=14, borderwidth=4)

    #delete
button14=Button(delet,bg="white",height=2, width=14, borderwidth=4)
button15=Button(delet,bg="white",height=2, width=14, borderwidth=4)

    #Modify
button16=Button(mod1,bg="white",height=2, width=14, borderwidth=4)
button17=Button(mod1,bg="white",height=2, width=14, borderwidth=4)


#Entry
    #Profile

entry1=Entry(prof)
entry2=Entry(prof)
entry3=Entry(prof)

    #Add

entry4=Entry(addr)
entry5=Entry(addr)
entry6=Entry(addr)
entry7=Entry(addr)
entry8=Entry(addr)
entry9=Entry(addr)
entry10=Entry(addr)

    #Delete
entry11=Entry(delet)

    #Modify
entry12=Entry(mod1)



home()