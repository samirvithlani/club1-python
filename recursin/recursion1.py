#10
def printNo(no):
    
    if no == 0:
        return
    
    printNo(no-1) 
    print(no)

printNo(10)    