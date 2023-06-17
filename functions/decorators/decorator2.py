def division(func): #2 func(10,2) 
    def inner(a,b): #4 10,2
        print("I am dividing",a,"and",b) #5
        if b == 0: #6
            print("Cannot divide by zero")
            return
    
        return func(a,b) #7 #3 div(10,2)
    
    return inner #3


@division
def div(a,b):
    x = a/b#8
    print(x)

div(10,0) #1    
    