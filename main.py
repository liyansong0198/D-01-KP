import numpy as np
import re
f = open("idkp1-10.txt")
# 调用文件的 readline()方法
line = f.readline()  # 每次读取一行内容
profitlist=[]
weightlist=[]
profitdatalist=[]
weightdatalist=[]
profit=[]
weight=[]
dpw=[]
while line:
    # print(line, end='')  # end = ''表示不换行
    # print(line)  # 默认换行
    line = f.readline()
    if line.__contains__("profit"):
        profitdata=re.sub('[.\n]', '', f.readline()).strip(',')
        profitdatalist.append(profitdata)
    elif line.__contains__("weight"):
        weightdata=re.sub('[.\n]', '', f.readline())
        #print(weightdata)
        weightdatalist.append(weightdata)
p_list=[]
w_list=[]
pw_list=[]
t_p_list=[]
t_w_list=[]
pw=[]
for i in range(len(profitdatalist)):
    num=0
    profitlist = str(profitdatalist[i]).split(',')
    weightlist = str(weightdatalist[i]).split(',')
    for j in range(len(profitlist)):
        t_p_list.append(int(profitlist[j]))
        t_w_list.append(int(weightlist[j]))
        num=num+1
        if num==3:
            p_list.append(t_p_list)
            w_list.append(t_w_list)
            pw_list.append(t_p_list+t_w_list)
            t_p_list=[]
            t_w_list=[]
            num=0
    profit.append(profitlist)
    weight.append(weightlist)
    dpw.append(pw_list)
print(pw_list)