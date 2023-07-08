file = open("demo2.txt",'r')

# for i in file:
#     print(i,end="")
    

# x = file.read()    
# print(x)
count =0
while 1:
    char = file.read(1)
    count+=1
    if not char:
        break
    
    print(char,end="")

print("\nTotal characters in file: ",count)    
