# DEA模型的直接算法
def statistics():   # 录入数据
    a = [200,100,100,100,100]
    b = [100,200,100,100,200]
    c = [100,100,300,200,100]
    d = [100,100,100,100,100]
    e = [100,100,100,100,100]
    dmu = [a, b, c, d, e]  # 经营个体列表
    return(dmu)
def data_clear1(dmu):  # 清洗数据(经营个体列表)
    k = len(dmu[0]) # 5
    li1 = []
    for i in range(k):
        z = 0
        for j in dmu:
            z+=j[i]
        li1.append(z)
    min0=min(li1)
    for i in range(k):  # 倍数计算
        li1[i]/=min0
    for i in range(5):
        for j in range(k):
            dmu[i][j]=int(dmu[i][j]*10/li1[j])
    return dmu
def data_clear2(dmu):
    li=[]
    for i in dmu:
        li.append(sum(i))
    k=min(li)
    for i in range(5):
        li[i]/=k
    for i in range(5):
        for j in range(5):
            dmu[i][j]=int(dmu[i][j]/li[i])

    return dmu
def creat_wij():
    liqz1 = []
    k1 = 0.01  # 数据精度
    g = k1
    k2 = g
    b = int(10 / k1)  # 保留位数处理数
    while k1 < 1:
        while k2 < (1 - k1):
            w2 = [int(k1 * b+0.3) / b, int((k2) * b+0.3) / b, int((1 - k1 - k2) * b+0.3) / b]  # 列表录入
            k2 += g
            liqz1.append(w2)
        k1 += int((k1+g)*b)/b
        k2 = g

    liqz2 = []
    k = 0.01  # 数据精度
    g = k
    b = int(1 / g)  # 保留位数处理数
    while k < 1:
        w2 = [int(k * b + 0.3) / b, int((1 - k) * b + 0.3) / b]  # 列表录入
        k = k + g
        liqz2.append(w2)
    wij = [liqz1, liqz2]
    return wij
def main_operation(dmu,li_wij):   # 主要DEA运算(经营个体列表，录入权重列表)
    li3 = []
    liq = []
    for j in range(len(li_wij[0])):
        h1 = 0
        for i in dmu:
            for k in range(3):
                h1 += li_wij[0][j][k] * i[k]
        liq.append([h1, li_wij[0][j]])
    li3.append(max(liq))
    lip = []
    for j in range(len(li_wij[1])):
        h2 = 0
        for i in dmu:
            for k in range(2):
                h2 += li_wij[1][j][k] * i[k]
        lip.append([h2, li_wij[1][j]])
    li3.append(min(lip))
    return li3
def main(): # 主函数
    dmu = statistics()
    # dmu = data_clear2(dmu)
    dmu = data_clear1(dmu)
    li_wij = creat_wij()
    li3_max = main_operation(dmu, li_wij)
    print(li3_max)
    h_max = li3_max[0][0] / li3_max[1][0]  # 总效率最高值
    wij = li3_max[0][1] + li3_max[1][1]  # 权重系数配表（总效率最高）
    for i in range(5):
        wij[i]=int(wij[i]*10000)
        wij[i]/=10000
    print(wij)
    # wij=[0.3, 0.01, 0.69, 0.99, 0.01]
    li_ef = []  # 各dmu的DEA效率值
    for i in range(5):
        li_e = []
        for j in range(5):
            li_e.append(dmu[i][j] * wij[j])
        li_e1 = (li_e[0] + li_e[1] + li_e[2])
        li_e2 = (li_e[3] + li_e[4])
        li_ef.append(li_e1/li_e2)
    li_eff=[0,0,0,0,0]
    for j in range(5):
        l = li_ef[j]
        li_eff[j] = int(l*1000)/1000
    print(li_eff)

main()
