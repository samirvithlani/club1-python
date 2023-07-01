#constrictor is special function which has same name as class name.....

#__init__ is a constructor

class Student():
    
    name =""
    #to initialize the instance variable of class
    def __init__(self,name):
        self.name = name
        print("This is a constructor default..",name)



stu = Student("raj") #constructor will be called automatically        
print(stu.name) #raj
stu2 = Student("raj2") #constructor will be called automatically
print(stu2.name) #raj2
        