no1 =int(input("enter number 1"))
no2 =int(input("enter number 2"))


if no1 > no2 and no1 % 2==0:
    print("no1 is greater and even")
elif no1 > no2 and no1 % 2 !=0:
    print("no1 is greater and odd")
elif no1 < no2 and (no1 %2 ==0 or no2 %2 ==0):
    print("true")
            
