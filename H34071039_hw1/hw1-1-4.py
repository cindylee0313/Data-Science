import pandas as pd
print("Q4")
df = pd.read_csv(r'IMDB-Movie-Data.csv')
dire_num = df['Director'].value_counts().nlargest(3,keep = 'all') #算每個導演合作過的演員，取前三大
print(dire_num)
