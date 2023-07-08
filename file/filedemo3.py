file = open("demo2.txt",'r')
count=0

for i in file:
     for word in i.split():
         count+=1
         print(word)

print("Total words in file: ",count)         