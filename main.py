import numpy as np
import re
import matplotlib.pyplot as plt
import operator
# 调用文件的 readline()方法
profitlist=[]
weightlist=[]
profitdatalist=[]
weightdatalist=[]
profit=[]
weight=[]
dpw=[]
def data(textname):
    f = open(textname)
    line = f.readline()
    while line:
        # print(line, end='')  # end = ''表示不换行
        # print(line)  # 默认换行
        line = f.readline()
        if line.__contains__("profit"):
            profitdata=re.sub('[.\n]', '', f.readline()).strip(',')
            profitdatalist.append(profitdata)
        elif line.__contains__("weight"):
            weightdata=re.sub('[.\n]', '', f.readline()).strip(',')
            #print(weightdata)
            weightdatalist.append(weightdata)
    for i in range(len(profitdatalist)):
        p_list = []
        w_list = []
        pw_list = []
        t_p_list = []
        t_w_list = []
        t_wp_list = []
        num=0
        profitlist = str(profitdatalist[i]).split(',')
        weightlist = str(weightdatalist[i]).split(',')
        for j in range(len(profitlist)):
            t_p_list.append(int(profitlist[j]))
            t_w_list.append(int(weightlist[j]))
            t_wp_list.append(int(profitlist[j])/int(weightlist[j]))
            num=num+1
            if num==3:
                p_list.append(t_p_list)
                w_list.append(t_w_list)
                pw_list.append(t_p_list+t_w_list+t_wp_list)
                t_p_list=[]
                t_w_list=[]
                t_wp_list=[]
                num=0
        profit.append(p_list)
        weight.append(w_list)
        dpw.append(pw_list)
    #print(profitdatalist[0])
    print('数据读取成功！')
    print('数据读取结果如下')
    print('重量')
    print(weight)
    print('价值')
    print(profit)
    print('重量/价值/重量：价值系数')
    print(dpw)
def pwscatter(n):
    #matplotlib画图中文显示会有问题，让中文能够正确显示
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    profitPoint=profitdatalist[0].split(',')
    print(profitPoint)
    #exit;
    weightPoint=weightdatalist[0].split(',')
    #print(weightPoint)
    plt.xlim(0, 2500)
    plt.ylim(0, 2500)
    plt.xlabel('重量')
    plt.ylabel('价值')
    area = np.pi *6*6
    colors1 = '#00CED1'  # 点的颜色
    for i in range(len(profitPoint)):
        plt.scatter(int(weightPoint[i]),int(profitPoint[i]),s=area,c=colors1,alpha=0.4)
    plt.show()
def twpsort(n):
    print(sorted(dpw[n], key=operator.itemgetter(-1), reverse=True))
#def recall(x,y)
if __name__=="__main__":
    textname=input("请输入您要操作的文件名\n")
    data(textname)
    while(1):
        m = int(input('请选择您的操作:\n1.绘制散点图\n2.非递增排序\n3.回溯算法\n'))
        if m == 1:
            n=int(input("请输入您需要绘制散点图的组数\n"))
            pwscatter(n-1)
            continue
        if m == 2:
            n=int(input("请输入非递增排序的组数\n"))
            twpsort(n-1)
            continue
        if m == 3:
            n=int(input("请输入您需要执行的组数\n"))
            totalprofit=[0,0,0]+profit[n-1]
            print(profit)
    # print(profitdatalist[0])
    # print(sorted(dpw[2], key=operator.itemgetter(-1), reverse=True)