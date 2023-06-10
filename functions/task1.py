def demo(name):
    dict ={}
    for i in name:
        dict[i.upper()] = i.lower()
        
    return dict
    
name = input("Enter the name: ")    
x =demo(name)    
print(x)