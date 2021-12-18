import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random


color = {0:'blue',
         1:'green',
         2:'yellow',
         3:'red',
         4:'purple',
         5:'orange'}
center_color = 'black'


#kmeans function
#找第一個點c1之後用最大距離找第二個點c2
#尋找第三個之後的點
def kmeans(k):

    center = {} #中心點

    distance = {}
    df = pd.read_csv("cdata.csv")#讀取檔案
    
    SSE = 0
    center['c1'] = (df.iloc[0][0] ,df.iloc[0][1]) #第一個center
    c_distance = (((df['x']-df.iloc[0][0])**2 + (df['y']-df.iloc[0][1])**2)**0.5) #點與c1之距離
    center['c2']=(df.iloc[c_distance.idxmax()][0],df.iloc[c_distance.idxmax()][1]) #第二個center(與c1距離max)
    

    for j in range(3, k+1): #第二題需求:有很多k (此for尋找center的座標)
        center_num = 'c'+str(j) #第c個center = c編號
        dist = {} #距離
        for i in list(center.keys()):
            dist[i] = ((df['x']-center[i][0])**2+(df['y']-center[i][1])**2)**0.5 #j與每個center之距離
        coordinate = pd.DataFrame(dist).min(1).idxmax()
        center[center_num] = (df.iloc[coordinate][0], df.iloc[coordinate][1]) #第j個center的座標
        
        
    

    while True: #分群的循環
        for d in list(center.keys()):

            distance[d] = ((df['x']-center[d][0])**2+(df['y']-center[d][1])**2)**0.5 #算點與center的距離
        cluster = {}
        df['cluster'] = pd.DataFrame(distance).idxmin(axis=1) #選擇距離最近的center並歸類
        dot_cluster = df.groupby(df.cluster) #以cluster分群
        for dot in dot_cluster:
            cluster[dot[0]] = list(zip(list(dot[1]['x']), list(dot[1]['y'])))
        new_center = {}
        center_mean = dot_cluster.aggregate(pd.DataFrame.mean)
        for dot in list(center_mean.index): #算平均當作新的點
            new_center[dot] = (center_mean.loc[dot]['x'], center_mean.loc[dot]['y'])
            
        if new_center == center: #不改變則跳出
            break
        else:
            center = new_center #換新的center
    for i in df.groupby(df.cluster):
        SSE += ((i[1]['x']-center[i[0]][0])**2+(i[1]['y']-center[i[0]][1])**2).sum()


            
    return cluster, center, SSE #cluster分群 center中心點的座標,SSE值


############第一題
clusterq1, centerq1, SSE1 = kmeans(4)#值丟入未知數
for i in list (clusterq1.keys()):
    xarray = []
    yarray = []
    for j in clusterq1[i]: #丟入兩個array(x y)
        xarray.append(j[0])
        yarray.append(j[1])
    ax = df[df['cluster'] == 0].plot.scatter(x='x', y='y', color='blue', label='A') #畫第一類
    ax = df[df['cluster'] == 1].plot.scatter(x='x', y='y', color='green', label='B', ax=ax) #畫第二類
    ax = df[df['cluster'] == 2].plot.scatter(x='x', y='y', color='red', label='c', ax=ax) #畫第三類
    df[df['center_num']==2].plot.scatter(x='x', y='y',color='yellow', label='D', ax=ax) #畫第四類 但不知道哪寫錯畫不出來





S=[] #SSE的圖
for i in range(2,51):
    S.append(kmeans(i)[2])
p = np.arange(2,51,1)
plt.plot(p,S)
plt.xlabel('Number of K')
plt.ylabel('Sum of square error')
plt.show()



S10 = [] #K=10時 SSE的圖
for i in range(0,10):
    S10.append(kmeans(i)[2])
p2 = np.arange(1,11,1)
plt.bar(p2,S10)
plt.xlabel('Fixed k=10')
plt.ylabel('Sum of square error')
plt.show()
