no1 = int(input("Enter a number: "))
no2 = int(input("Enter a number: "))

try:
    x = no1 / no2
    print(x)
except ZeroDivisionError:
    print("Division by zero is not possible")  

print("Bye")      