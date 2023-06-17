from functools import reduce

age =[12,34,56,12,3,4,67]

# sum =0
# for i in age:
#     sum =sum +i

# print(sum)    

sum = reduce(lambda a,b: a+b,age)
print(sum)


age1 = list(map(lambda a : a*2,age))
print(age1)

