#data =[[10,200,30],[20,34,56],[34,5,78],[56,7,34],[78,90,100]]
#data = [[10,200,300],[]]
data =[]
sales=[]
sum =0

for i in range(5):
    data.append([])
    for j in range(3):
        data[i].append(int(input("Enter the number: ")))
    
    

for i in data:
    for j in i:
        sum = sum + j    
    sales.append(sum)
    sum=0

print(sales)
max = sales[0]
ind =0
for i in sales:
    if i > max:
        ind = sales.index(i)+1
        max = i

print(max)     
print(ind)   



