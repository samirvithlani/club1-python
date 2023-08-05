

try:
    no1 = int(input("Enter a number: "))
    no2 = int(input("Enter a number: "))
    x =  no1 / no2

    
except ZeroDivisionError:
    print("Division by zero is not possible")    
except ValueError:
    print("Please enter only numbers")  

except:
    print("Something went wrong")     


print("Bye")    