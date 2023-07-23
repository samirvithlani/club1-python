import pandas as pd

data = pd.read_csv('./ipl.csv')
data.sort_values("Team", inplace = True)

filter1 = data["Team"]=="mi"
filter2= data["type"]=="batsman"

data.where(filter1 | filter2, inplace = True)

print(data) 