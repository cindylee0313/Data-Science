import pandas as pd
print("Q3")
df = pd.read_csv (r'IMDB-Movie-Data.csv')

print(df[["Emma Watson" in x for x in df["Actors"]]]["Rating"].sum()/len(df[["Emma Watson" in x for x in df["Actors"]]]))

