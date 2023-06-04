def student(x,**kwargs):
    print(kwargs)
    print("x--->",x)
    print()


#student(name="ram",email="ram@gmail.com",age=23)    
student(x=100,name="ram",email="ram@gmail.com",age=23,password="ram123")    