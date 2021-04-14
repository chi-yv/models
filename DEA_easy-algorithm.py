# DEA模型的直接算法
def statistics():   # 录入数据
    a = [540, 695, 669, 629, 163]
    b = [491, 532, 535, 958, 739]
    c = [439, 418, 349, 678, 348]
    d = [382, 495, 370, 258, 573]
    e = [311, 493, 373, 362, 39]
    dmu = [a, b, c, d, e]  # 经营个体列表
    return(dmu)
def data_clear(dmu):  # 清洗数据(经营个体列表)
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
            dmu[i][j]=int(dmu[i][j]/li1[j])
    return dmu
def creat_wij(): # 录入权重列表
    liqz1 = []
    liqz2 = []
    k = 10  # 权重系数控制
    for i1 in range(1, k):
        for i2 in range(1, k):
            for i3 in range(1, k):
                ii = i1 + i2 + i3
                w1 = [i1 / ii, i2 / ii, i3 / ii]
                liqz1.append(w1)
    for i4 in range(1, k):
        for i5 in range(1, k):
            ij = i4 + i5
            w2=[i4 / ij, i5 / ij]  # 权重系数列表
            liqz2.append(w2)
    liqz=[liqz1,liqz2]
    return liqz
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

dmu=statistics()
dmu=data_clear(dmu)
li_wij=creat_wij()
li3=main_operation(dmu,li_wij)
h_max=li3[0][0]/li3[1][0]   # 总效率最高值
wij=li3[0][1]+li3[1][1]     # 权重系数配表（总效率最高）
for i in range(5):
    wij[i]=int(wij[i]*10000)/10000
li_efficiency=[]    # 各dmu的DEA效率值
for i in range(5):
    li_e=[]
    for j in range(5):
        li_e.append(dmu[i][j]*wij[j])
    li_e=(li_e[0]+li_e[1]+li_e[2])/(li_e[3]+li_e[4])/h_max
    li_efficiency.append(li_e)
for i in range(5):
    if li_efficiency[i]>=1:
        li_efficiency[i]=1.0
print(wij)
print(li_efficiency)
