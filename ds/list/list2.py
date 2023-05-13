data = [["raj","raj@gmail.com",23],["jay","jay@gmail.com",24],["parth","parth@gmail.com",25]]

# x = data[0][1]
# print(x)

data[0][1]="raj1@gmai2.com"
data[2][2]=26

for i in data:
    for j in i:
        print(j,end=" ")
    print()    
        