users = ["ram","neha","parth","priya","ajay","naman"]
# fillist =[]

# for i in users:
#     if len(i)>4:
#         fillist.append(i)

# print(fillist)        

fillist = list(filter(lambda name: len(name)>4,users))
print(fillist)

data = [24,45,67,89,90,56,67]

nl = list(filter(lambda x: x >30 and x % 2==0 ,data))
print(nl)
#return palindrome name using filter lambda function
users2 =list(filter(lambda name: name == name[::-1],users))
print(users2)
