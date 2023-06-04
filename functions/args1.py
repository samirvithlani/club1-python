
# def student(name):
#     print(name)

# student("Ravi","Raj","Ramesh","Rajesh")

def users(x,*args):
    print(type(args))
    print("x....",x)
    print(args)

users("ram","shyam","mohan","sohan")  


def users(*args,**kwargs):
    print(type(args))
    print(type(kwargs))
    print("args....",args)
    print("kwargs....",kwargs)
    

users(100,200,300,name="ram",email="ram@")    