f=open("IMDB-Movie-Data.csv","r")
f.readline()
print(f.readline()) #去掉第一列

for i in range(1,1000):
    line1=f.readline() #讀取第二列
    print(line1)
str1=line1.split(",") #轉為字串
#line2=[f.readline()]

    #dic={"Rank":,"Title":."Genre":,"Director":,"Actors":,"Year":,"Runtime (Minutes)":,"Rating":,"Votes":,"Revenue (Millions)":,"Metascore":}

print(str1)
print(str1[3])
