from operator import itemgetter
import csv
with open("IMDB-Movie-Data.csv",newline = "") as csvfile:
    rows = csv.reader(csvfile)

###################
    
    sorting = sorted(rows,key = lambda x: x[7],reverse = True) #以rating排序
    print("第一題:")
    list_rating=[]
    for index, rows in enumerate(sorting):
        if sorting[index][5] == str(2016): #year=2016的rating放入lis2
            list_rating.append(sorting[index][1])
    for i in range(0,3): #印出前三個
        print(list_rating[i])

###################
    print("第三題")
    row_number = 0 #第幾列
    sum_of_rating = 0 #rating加總
    count_movies = 0 #有幾部電影
    for index in sorting:
        if "Emma Watson" in sorting[row_number][4]: #若包含艾瑪華森
            count_movies += 1
            sum_of_rating += float(sorting[row_number][7]) #加總的動作
        row_number += 1
    print(sum_of_rating/count_movies) #算平均

###################

    print("第二題")
    actor_list=[]
    
    for actor_row in range(1,len(sorting)-1):
        actor_list += sorting[actor_row][4].split("|") #重複的演員名單
    unique_actor_set = set(actor_list)
    unique_actor_list = list(unique_actor_set)
    print(unique_actor_list) #不重複的演員名單

    
    sum_revenue = []
    for actor_num in range(0,len(unique_actor_list)-1):
        for row_number in range(1,len(sorting)):
            if unique_actor_list[actor_num] in sorting[row_number][4]:
                #print(float(sorting[4][9]))
                #print(sum_revenue[actor_num])
                sum_revenue[actor_num] += float(sorting[row_number][9])
                #print (sum_revenue[actor_num])



###################

    #Question (2)
    print("Question (2):")
    rng=[]

    for row in allrows:
    #     # delete header
        if row[0] != "Rank":
            rng.append(row)

    # #split Genre and Actors
    for i in range(len(rng)):
        rng[i][2]=rng[i][2].split("|")
        rng[i][4]=[x for i in rng[i][4].split('|') for x in i.split('| ')]

    #不重複actors list
    actors=[]
    for i in range(len(rng)):# len(rng)=1000
        for j in range(len(rng[i][4])): # len(rng[i][4])=4
            check=False
            if check==False:
                actors.append(rng[i][4][j])
            if rng[i][4][j] in actors:
                check=True

    actors_revenue = [[] for i in range(len(actors))]
    for i in range(len(actors)):
        actors_revenue[i].append(actors[i])


    for i in range(len(actors)):
        for j in range(len(rng)):
            if actors[i] in rng[j]:
                actors_revenue[i].append(rng[j][9])
    
    actors_revenue.sort(key=lambda x:x[1])
    print(actors_revenue[0])



    #Question (4)
    print("Question (4):")
    directorcolumn = [row[3] for row in sortedrows]
    directors={}
    for i in set(directorcolumn):
        if directorcolumn.count(i)>1:
            directors[directorcolumn.count(i)]=i
    for value in reversed(sorted(directors.keys())[-3:]):
        print(directors[value],value)
