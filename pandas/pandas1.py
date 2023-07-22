import pandas as pd

df = pd.DataFrame() #blank dataframe
data = ["ram", "shyam", "mohan", "sohan"]
df = pd.DataFrame(data, columns=["Name"])
print(df)