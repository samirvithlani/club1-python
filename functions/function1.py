def test():
    print("Hello from function1.py")
    print("wo return type with no arguments")

def demo():
    return 100
    
test()    

x = demo()
print(x)
print(demo())

def sum(a,b):
    c = a+b
    #return c
    return a+b

ans = sum(10,20)
print(ans)

def sqr():
    a =10
    return a*a

print(sqr())