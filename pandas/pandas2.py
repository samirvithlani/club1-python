import pandas as pd

data = {'Name': ["ram", "shyam", "mohan", "sohan"],'Marks':[89,78,67,56],'collages':["A","B","C","D"],'city':["pune","mumbai","delhi","chennai"]}

#select * from tname
df = pd.DataFrame(data)
#print(df)
print(df[['Name','Marks']])