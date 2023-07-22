import pandas as pd

data = pd.read_csv("./ipl.csv",index_col="Team")
df = pd.DataFrame(data)
#print(df)
#print(df[["Team"]])

first = df.loc["csk"]
second = df.loc["gt"]
print(first)

print(second)