data ={1:[10,20,30],2:[40,50,60],3:[70,80,90]}
print(data)
data[2].append(70)
data[3].remove(80)
data.update({4:[100,200]})
data[1].pop()






sum =0
for i in data.items():
    for x in i:
        print(x)
    for l in x:
        print(l)
        sum = sum + l
    print("sum =",sum)
    sum = 0    
    print("-----")    
    
    
   
   #find max list from all 