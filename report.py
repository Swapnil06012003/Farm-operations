import sqlite3
conn=sqlite3.connect('databas.db')
cursor=conn.cursor()
cursor.execute("SELECT name,prof FROM crop ORDER BY prof DESC")
l=cursor.fetchall()
file1 = open("MyFile11.txt","a")
file1.write("Profit percentage distribution\n\n\n\n")
file1.write("Percentage")
file1.write("    ")
file1.write("Asset")
file1.write("\n")
file1.write("\n")
for i in l:
    str1=i[0]
    str2=str(i[1])
    file1.write(str2)
    file1.write("         ")
    file1.write(str1)
    file1.write("\n")

file1.write("\n\n\n")
file1.write("Contribution to net profit\n\n\n\n")
cursor.execute("SELECT cp,sp,name,quantity FROM crop")
l=cursor.fetchall()

sum=0
for i in l:
    sum=sum+(i[1]-i[0])*i[3]



for i in l:
    str1=i[2]
    num=((i[1]*i[3])/sum)*100

    num="%.2f"%num
    str2=str(num)

    file1.write(str2)
    file1.write("         ")
    file1.write(str1)
    file1.write("\n")

file1.write("\n\n\n")


sum=0;
cursor.execute("SELECT sp,quantity,name,type from crop")
l=cursor.fetchall()

cost=0

def knap(l,dp,index,cost):
    if(index==len(l)):
        return 0
    if(dp[index] != -1):
        return cost
    cost1=cost+l[index]
    knap(l,dp,index+1,cost1)
    knap(l,dp,index+1,cost)
    dp[index]=max(cost,cost1)
    return dp[index]
for i in l:
    sum=sum+i[0]*i[1]

mean=sum/len(l)
median=l[len(l)/2]
limit=0.1*mean
weak=[]
for i in l:
    if(i[0]*i[1]<limit):
        weak.append(i[2])

strong=[]
if(abs(mean-median)<10000):
    dp=[]
    strong=knap(l,dp,0,cost)



conn.commit()
conn.close()