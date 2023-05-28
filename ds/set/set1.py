#data = {} # it is a dictionary
data = set({"raj","ram","amit","parth","kush"}) # it is a set
print(data)
print(type(data))

data.add("raja")
print(data)

data.update(["anil","kamal"])
data.remove("amit")
data.discard("kamal")
removedelm = data.pop()
print(removedelm)
x = data.union({"raj","ram","amit","parth","priya"})
print(x)


d = data.difference({"ram"})
print("d..",d)

#data.difference_update({"ram"})
i = data.intersection({"ram"})
print("i...",i)
#data.intersection_update({"ram"})


print("data...",data)

#data.symmetric_difference_update({"ram"})
print("subset -->",data.issubset({"ram"}))
print("superset -->",data.issuperset({"ram"}))
print("data...",data)
