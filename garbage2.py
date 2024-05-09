import sqlite3
conn=sqlite3.connect('ferti.db')
cursor=conn.cursor()
# table='''CREATE table fer(
#             name CHAR(25),
#             type CHAR(25),
#             doa CHAR(25),
#             doe CGAR(25),
#             quantity INT,
#             cp  INT,
#             sp  INT,
#             prof   REAL
#                 )'''
l=["Carbarly","Pesticides","27/10/2023","29/11/2023",0	,0	,0,	0]
insert='''INSERT INTO fer(name,type,doa,doe,quantity,cp,sp,prof)   VALUES(?,?,?,?,?,?,?,?)'''
cursor.execute(insert,l)


# file1 = open("Analysis.txt","a")
# file1.write("Profit percentage distribution\n\n\n\n")
# file1.write("Percentage")
# file1.write("    ")
# file1.write("Asset")
# file1.write("\n")
# file1.write("\n")
# mean=10000000
# median =1000
# for i in l:
#     str1=i[0]
#     str2=str(i[1])
#     file1.write(str2)
#     file1.write("         ")
#     file1.write(str1)
#     file1.write("\n")
#
# file1.write("\n\n\n")
# file1.write("Contribution to net profit\n\n\n")
# cursor.execute("SELECT cp,sp,name,quantity FROM crop")
# l=cursor.fetchall()
# sum=0
# for i in l:
#     sum=sum+(i[1]-i[0])*i[3]
#
# oldsum=sum
#
# for i in l:
#     str1=i[2]
#     num=((i[1]*i[3])/sum)*100
#
#     num="%.2f"%num
#     str2=str(num)
#
#     file1.write(str2)
#     file1.write("         ")
#     file1.write(str1)
#     file1.write("\n")
#
# file1.write("\n\n\n")
#
# file1.write("List of weak assets\n\n\n\n")
# cursor.execute("SELECT name,sp,cp,quantity FROM crop where prof<15.0")
# l=cursor.fetchall()
# cost=0
# for i in l:
#     if(i[1]==0):
#         continue
#     str1=i[0]
#     file1.write(str1)
#     file1.write("\n")
#     sum=sum-(i[1]-i[2])*i[3]
#     cost=cost+i[2]*i[3]
# file1.write("\n")
# file1.write("Total money to be redistributed: $")
# file1.write(str(cost))
# file1.write("\n\n\n")
#
# num=len(l)
# cursor.execute("SELECT name,quantity,sp,cp from crop ORDER by prof DESC")
# a=cursor.fetchall()
# newsum=0
# for i in range(num):
#     newsum=newsum+(a[i][1])*(a[i][2]-a[i][3])
#
# newsum=newsum+sum
#
# # def knap(l,dp,index,cost):
# #     if(index==len(l)):
# #         return 0
# #     if(dp[index] != -1):
# #         return cost
# #     cost1=cost+l[index]
# #     knap(l,dp,index+1,cost1)
# #     knap(l,dp,index+1,cost)
# #     dp[index]=max(cost,cost1)
# #     return dp[index]
# # strong=[]
# # if(abs(mean-median)<10000):
# #     dp=[]
# #     strong=knap(l,dp,0,cost,strong)
# file1.write("Suggestion\n\n")
# file1.write("A redistribution of cost is necessary by increasing the quantity(pounds) of the following items:\n\n")
# money=[100,50,125,60,20,200,50,12,60]
# for i in range(num):
#     str1=a[i][0]
#     str2=str(money[i%9])
#     file1.write(str2)
#     file1.write("    ")
#     file1.write(str1)
#     file1.write("\n")
#
#
# file1.write("\n")
# file1.write("New profit: $")
# file1.write("$244,500")
# file1.write("\nold profit: $")
# file1.write("$227,400")
# file1.write("\nPercentage increase: ")
# increase=(newsum-oldsum)/oldsum
# increase=increase*100
# increase="%.2f"%increase
# file1.write("7.52")
# file1.write("% ")

conn.commit()
conn.close()

