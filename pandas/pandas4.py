#working with missing data
import pandas as pd

data = pd.read_csv("./ipl.csv")

df = pd.DataFrame(data)
#print(df)
#df = df.isnull()
#df = df.dropna()
df = df.fillna(0)
print(df)