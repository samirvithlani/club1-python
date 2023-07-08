file = open("demo2.txt",'r')
count=0
while True:
    
    line = file.readline()
    if not line:
        break
    
    print(line,end="")
    count+=1

print("\nTotal lines in file: ",count)    
    