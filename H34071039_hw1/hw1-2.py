import pandas as pd
import numpy as np


# Raw data file
file_to_load = "purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)




players = len(purchase_data["SN"].unique()) #直接計算數量
print(players)

#######
items = len(purchase_data["Item ID"].unique()) #不同item id的個數
avg_price = purchase_data["Price"].mean() #平均價格
num_purchases = purchase_data["Price"].count() #計算個數
total_purchases = purchase_data["Price"].sum() #計算總和

ans_col = [[items,avg_price,num_purchases,total_purchases]]
df = pd.DataFrame(ans_col, columns = ["Number of Unique Items","Average Price","Number of Purchases","Total Revenue"]) #做成表格
print(df)


########

gender = purchase_data.groupby("Gender") #以gender做分類
gender_count = gender["SN"].nunique() #分類後的不重複sn個數
gender_perc = (gender_count/players)*100

gender_form = pd.DataFrame({"Percentage of Players":gender_perc,"Total Count":gender_count})
print(gender_form)

########

avg_gender_price = gender["Price"].mean() #以gender分類後的price平均
total_gender_price = gender["Price"].sum() #以gender分類後的price總和
per_gender_price = total_gender_price/gender_count

purchase_analy = pd.DataFrame({"Purchase Count":gender_count,"Average Purchase Price":avg_gender_price,"Total Purchase Value":total_gender_price,"Avg Purchase Total per Person":per_gender_price})

print(purchase_analy)


########

purchase_data["Age Group"] = pd.cut(purchase_data["Age"],[0,9.9,14.9,19.9,24.9,29.9,34.9,39.9,100],labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]) #pd.cut用法 (資料，分群，標籤)
age = purchase_data.groupby("Age Group") #以age group做分類
age_count = age["SN"].nunique() #不重複的數量
age_perc = (age_count/players)*100

age_demo = pd.DataFrame({"Percentage of Players":age_perc,"Total Count":age_count})

print(age_demo)

########
avg_age_price = age["Price"].mean() #以age分類後的price平均
total_age_price = age["Price"].sum() #以age分類後的price總和
per_age_price = total_age_price/age_count

age_purchase_analy = pd.DataFrame({"Purchase Count":age["Purchase ID"].count(),"Average Purchase Price":avg_age_price,"Total Purchase Value":total_age_price,"Avg Purchase Total per Person":per_age_price})

print(age_purchase_analy)

########

sn = purchase_data.groupby("SN") #以sn做分類
sn_count = sn["SN"].nunique() #不重複的數量
avg_sn_value = sn["Price"].mean() #以sn分類後的price平均
total_sn_value = sn["Price"].sum() #以sn分類後的price總和
per_sn_value = total_sn_value/sn_count



top_spenders = pd.DataFrame({"Purchase Count":sn["Purchase ID"].count(),"Average Purchase Price":avg_sn_value,"Total Purchase Value":total_sn_value}).sort_values("Total Purchase Value", ascending = False)

print(top_spenders.head(5))

########

item = purchase_data.groupby(["Item ID","Item Name"]) #用Item ID與Item Name分類
item_count = item["Purchase ID"].count() #以item分類後計算數量
item_price = item["Price"].agg(max) #以item分類後取最大
total_item_price = item["Price"].sum() #以item分類後計算總和

pop_items = pd.DataFrame({"Purchase Count":item_count,"Item Price":item_price,"Total Purchase Value":total_item_price}).sort_values("Purchase Count", ascending = False)

print(pop_items.head(5))


########

profit_items = pd.DataFrame({"Purchase Count":item_count,"Item Price":item_price,"Total Purchase Value":total_item_price}).sort_values("Total Purchase Value", ascending = False)
print(profit_items.head(5))






