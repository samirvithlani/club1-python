users = ["raj","parth","priya","sanjay"]
userupr = list(map(lambda x: x.upper(),users))

numbers = [1,2,3,4,5,6,7,8]
numberssqr = list(map(lambda x: x*x,numbers))
numberssqr2 = list(map(lambda x: x**2 if x%2==0 else x**3,numbers))
print(numberssqr)
print(numberssqr2)

# for i in users:
#     userupr.append(i.upper())

print(userupr)   

l1 = [1,2,3]
l2 = [4,5,6]
x = list(map(lambda i,j: i+j,l1,l2))
# for i,j in zip(l1,l2):
#     x = x + [i+j]

print(x)    
months =["jan","feb","mar","apr"]
#m =[['j','a','n'],['f','e','b'],['m','a','r'],['a','p','r']]

m = list(map(list,months))
print(m)

    

 