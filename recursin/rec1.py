def fact(no):
    
    if no ==0 or no == 1:
        return 1
    
    return no * fact(no-1)


print(fact(5))