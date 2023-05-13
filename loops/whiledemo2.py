no = int(input("Enter a number: "))
rem =0
sum =0

l = len(str(no))
print(l)

while no>0:
    rem = no % 10
    sum = sum+ rem**l
    no = no//10
    

print(sum)    
    