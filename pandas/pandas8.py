import pandas as pd

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],'Age':[27, 24, 22, 32],'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df =pd.DataFrame(data)
filter1 = df["Name"]=="Jai"
df.where(filter1, inplace = True)
df["Name"] = df["Name"].str.upper()
df["Address"] = df["Address"].str.upper()
print(df)
