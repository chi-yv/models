# DEA模型的直接算法
def statistics():   # 录入数据
    a = [400,100,400,200,100]
    b = [100,200,600,100,100]
    c = [100,400,600,100,100]
    d = [200,100,600,100,100]
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
def dmu_operation(dmu,li_wij):   # 主要DEA运算(经营个体列表，录入权重列表)
    li3 = []
    liq = []
    for j in range(len(li_wij[0])):
        h1 = 0
        s1=[]
        for i in dmu:
            for k in range(3):
                h1 += li_wij[0][j][k] * i[k]
            s1.append(h1)
            h1=0
        liq.append([s1, li_wij[0][j]])

    lip = []
    for j in range(len(li_wij[1])):
        h2 = 0
        s2=[]
        for i in dmu:
            for k in range(2):
                h2 += li_wij[1][j][k] * i[k+3]
            s2.append(h2)
            h2=0
        lip.append([s2, li_wij[1][j]])
    h0=0
    li_d=[]
    for i in range(len(li_wij[0])):
        for j in range(len(li_wij[1])):
            for k in range(5):
                li_d.append(liq[i][0][k] / lip[j][0][k])
                h0 += liq[i][0][k] / lip[j][0][k]
            li3.append([h0, liq[i][1], lip[j][1], li_d])
            li_d = []
            h0 = 0

    return li3
def li3_operation(li3): # 对li3进行约束处理
    li4=[]
    li5=[]
    for i in range(len(li3)):
        li4.append(li3[i][3])
    for i in range(len(li4)):
        li5.append(min(li4[i]))
    for i in range(len(li3)):
        for j in range(5):
            li3[i][3][j]*=li5[i]
        li3[i][0]=sum(li3[i][3])
    return li3
def main():
    dmu = statistics()
    # dmu = data_clear2(dmu)
    dmu = data_clear1(dmu)
    li_wij = creat_wij()
    li3 = dmu_operation(dmu, li_wij)
    li3=li3_operation(li3)
    li3_max = max(li3)
    print(li3_max)
    # h_max = li3_max[0] / 5  # 总效率最高值
    wij = li3_max[1] + li3_max[2]  # 权重系数配表（总效率最高）
    for i in range(5):
        wij[i]=int(wij[i]*10000)
        wij[i]/=10000
    print(wij)
    li_ef=[0,0,0,0,0]
    for i in range(5):
        li_ef[i]=int(li3_max[3][i]*1000)/1000
    print(li_ef)

main()
