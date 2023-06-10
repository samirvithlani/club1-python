#annonymus function
#print

x = lambda name:print("Hello",name)
x("ram")

ans = lambda x,y:x+y
a = ans(10,20)
print(a)


q = lambda x : x**3
print(q(3))

# def demo(a,b):
#     if a>b:
#         return a
#     else:
#         return b


# ans = demo(10,20)
# print(ans)        
    
larger = lambda a,b : a if a>b else b
print(larger(10,20))    



name = input("Enter the name: ")

upr = lambda name: name.upper() if len(name)>3 else name

print(upr(name))


    

