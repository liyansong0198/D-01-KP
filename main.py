#************************************************************************
# FileName DPO1_KP_Salve.py
# Autor:Liyansong Date:2021.03.30
# Description:      //模块描述
# 本项目是对D{0-1}KP问题的求解主要实现了以下功能
#   1.可正确读入实验数据文件的有效D{0-1}KP数据
#   2.能够绘制任意一组D{0-1}KP数据以重量为横轴、价值为纵轴的数据散点图
#   3.使用回溯算法求解指定D{0-1} KP数据的最优解和求解时间
#   4.任意一组D{0-1} KP数据的最优解、求解时间可保存为txt文件
#   5.能够对一组D{0-1}KP数据按项集第三项的价值:重量比进行非递增排序
# Version：1.0
# FunctionList：  //主要函数以及功能
#   1.getdata() 正确读取数据文件的有效D{0-1}KP数据
#   2.pwscattar() 能够绘制任意一组D{0-1}KP数据以重量为横轴、价值为纵轴的数据散点图
#   3.pwradio_sort() 能够对一组D{0-1}KP数据按项集第三项的价值:重量比进行非递增排序
#   4.recall() 使用回溯算法求解指定D{0-1} KP数据的最优解和求解时间
#   5.main() 主函数，能够选择操作,对回溯算法求解完成的最优解、求解时间保存为txt文件
# History:        //历史修改记录
#************************************************************************
import numpy as np
import matplotlib.pyplot as plt
import operator
import time
import re
# 调用文件的 readline()方法
profit_list=[]
weight_list=[]
#初始化读入价值列表
profitdata_list=[]
#初始化读入重量列表
weightdata_list=[]
#数据读入处理完成后的的价值列表
profit_end_list=[]
#数据读入处理完成后的重量列表
weight_end_list=[]
profit_weight_pwradio_list=[]

#************************************************************************
#   Description：按行读入实验数据文件的有效D{0-1}KP数据，以三个为一组打印输入数据集的
#   重量、价格,九个为一组的价格重量和价格比重量
#   Input:textname数据集的文件名称
#   Output：
#   Return：
#   others
#************************************************************************
def getdata(textname):
    file = open(textname)
    line = file.readline()
    while line:
        # print(line, end='')  # end = ''表示不换行
        # print(line)  # 默认换行
        line = file.readline()
        if line.__contains__("profit"):
            profitdata=re.sub('[.\n]', '', file.readline()).strip(',')
            profitdata_list.append(profitdata)
        elif line.__contains__("weight"):
            weightdata=re.sub('[.\n]', '', file.readline()).strip(',')
            #print(weightdata)
            weightdata_list.append(weightdata)
    for i in range(len(profitdata_list)):
        temporary_profit_list=[]
        temporary_weight_list=[]
        temporary_pw_radio_list = []
        three_profit_list = []
        three_weight_list = []
        three_pw_radio_list = []
        num=0
        profit_list = str(profitdata_list[i]).split(',')
        weight_list = str(weightdata_list[i]).split(',')
        for j in range(len(weight_list)):
            three_profit_list.append(int(profit_list[j]))
            three_weight_list.append(int(weight_list[j]))
            three_pw_radio_list.append(int(profit_list[j])/int(weight_list[j]))
            num=num+1
            if num==3:
                temporary_profit_list.append(three_profit_list)
                temporary_weight_list.append(three_weight_list)
                temporary_pw_radio_list.append(three_profit_list+three_weight_list+three_pw_radio_list)
                three_profit_list = []
                three_weight_list = []
                three_pw_radio_list = []
                num=0
        profit_end_list.append(temporary_profit_list)
        weight_end_list.append(temporary_weight_list)
        profit_weight_pwradio_list.append(temporary_pw_radio_list)
    print('数据读取成功！')
    print('数据读取结果如下')
    print('商品价值')
    print(profit_end_list)
    print('商品重量')
    print(weight_end_list)
    print('重量/价值/重量：价值系数')
    print(profit_weight_pwradio_list)

#************************************************************************
#   Description：绘制任意一组D{0-1}KP数据以重量为横轴、价值为纵轴的数据散点图
#   Input:n 绘制数据的的组数
#   Output：
#   Return：
#   others
#************************************************************************
def pw_scatter(n):
    #matplotlib画图中文显示会有问题，让中文能够正确显示
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    profit_Point=profitdata_list[0].split(',')
    weight_Point=weightdata_list[0].split(',')
    plt.title('重量价值散点图')
    plt.xlim(0, 2100)
    plt.ylim(0, 2100)
    plt.xlabel('重量')
    plt.ylabel('价值')
    area = np.pi *6*6
    colors1 = '#00CED1'  # 点的颜色
    for i in range(len(profit_Point)):
        plt.scatter(int(weight_Point[i]),int(profit_Point[i]),s=area,c=colors1,alpha=0.4)
    plt.show()

#************************************************************************
#   Description：对一组D{0-1}KP数据按项集第三项的价值:重量比进行非递增排序
#   Input:n 数据的的组数
#   Output：
#   Return：
#   others：
#************************************************************************
def pwradio_sort(n):
    twp_sort=sorted(profit_weight_pwradio_list[n], key=operator.itemgetter(-1), reverse=True)
    print(twp_sort)

#************************************************************************
#   Description:使用回溯算法求解指定D{0-1} KP数据的最优解和求解时间
#   Input: max_hieght:背包的最大容量 x:列表的一维下标 y:列表的二维下标
#   totalprofit:背包中总价值 totalweight:背包中总重量
#   Output:
#   Return:
#   others:
#************************************************************************
def recall(max_height,x,y,new_profit,new_weight,totalprofit,totalweight):
    if y != 3:
        totalprofit=totalprofit+new_profit[x][y]
        totalweight=totalweight+new_weight[x][y]
    if totalweight>max_height:
        return 0
    if x == len(new_profit)-1:
        ret.append(totalprofit)
        return 0
    for i in range(4):
        recall(max_height,x+1,i,new_profit,new_weight,totalprofit,totalweight)
    return 0
#************************************************************************
#   Description:使用动态规划算法求解指定D{0-1} KP数据的最优解和求解时间
#   Input: max_hieght:背包的最大容量 n=数组中的组数
#   totalprofit:背包中总价值 totalweight:背包中总重量
#   Output:
#   Return:
#   others:
#************************************************************************
def dp(n,m):
    dp_profit=profit_end_list[n]
    dp_weight=profit_end_list[n]
    dp_result=[];
    for i in range(max_weight + 1):
         dp_result.append(0)
    print(dp_profit)
    for i in range(len(dp_profit)):
        for j in range(max_weight,-1,-1):
            for k in range(3):
                if j>=dp_weight[i][k]:
                    dp_result[j]=max(dp_result[j],dp_[j-dp_weight[i][k]]+dp_profit[i][k])
    print(dp_result)
if __name__=="__main__":
    textname=input("请输入您要操作的文件名\n")
    getdata(textname)
    while(1):
        m = int(input('请选择您的操作:\n1.绘制散点图\n2.非递增排序\n3.回溯算法\n4.动态规划算法\n'))
        if m == 1:
            n=int(input("请输入您需要绘制散点图的组数\n"))
            pw_scatter(n-1)
        if m == 2:
            n=int(input("请输入非递增排序的组数\n"))
            pwradio_sort(n-1)
        if m == 3:
            n=int(input("请输入您需要执行的组数\n"))
            max_height=int(input("请输入本组中背包的最大重量\n"))
            new_profit=[[0,0,0]]+profit_end_list[n-1]
            new_weight=[[0,0,0]]+weight_end_list[n-1]
            x=0
            y=0
            totalprofit=0
            totalweight=0
            ret=[];
            t = time.time()
            recall(max_weight,x,y,new_profit,new_weight,totalprofit,totalweight)
            ret.sort()
            print(int(ret[-1]))
            t1 = time.time()
            solve_time=t1-t
            print(solve_time)
            file = open("1.txt", "w+")
            file.write("组数\t最优解\t求解时间\n")
            file.write(str(n)+ "\t" + str(ret[-1])+"\t"+str(solve_time)+ "\n")
            file.close()
        if m==4:
            n = int(input("请输入您需要执行的组数\n"))
            max_weight = int(input("请输入本组中背包的最大重量\n"))
            dp(n-1,max_weight)