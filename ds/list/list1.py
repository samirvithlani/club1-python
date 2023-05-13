#list allows any type of data
#list allows duplicate data
#list allows indexing
#list allows slicing
#list is mutable --> we can change the data
#list is dynamic --> we can increase or decrease the size of list
#list is represented by []
#list is a collection of elements
#list is a ordered collection of elements 
#list is a heterogeneous collection of elements
#list is a growable collection of elements

list1 =[10,20,34,54,5,89]
print(list1)

l = len(list1)
print(l)

# print(list1[0])
# print(list1[1])


# for i in range(0,l):
#     print(list1[i],end=" ")

list1.append(100)
list1.extend([9,8,77])
list1.insert(0,7)
#removing = list1.pop()
removing = list1.pop(0)
print("removing....",removing)

cnt = list1.count(1000)
print("count of 100 is ",cnt)
ind = list1.index(100)
print("index of  is ",ind)


#list1.sort(reverse=True)
list1.reverse()

#l1 = list1.copy()


for i in list1:
    print(i,end=" ")