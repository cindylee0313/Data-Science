import pandas as pd
print("Q2")
df=pd.read_csv(r"IMDB-Movie-Data.csv") 
actor_uni = df["Actors"].split("|")
print(actor_uni)
