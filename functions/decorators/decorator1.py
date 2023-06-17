#python decorators is funciton that takes another function as an argument,
# adds some kind of functionality and returns another function, all of this without 
# altering the source code of the original function that we passed in.

def throw_party(func): #
    #func = order
    def inner(): #5
        print("Hey there") #6
        func() #7 #order
    
    return inner  #4

@throw_party #2
def order():
    print("Ordering food")  #8
    
order()    #1