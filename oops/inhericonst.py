class Person():
    
    def __init__(self):
        print("Person Constructor")


class User(Person):
    pass
    # def __init__(self):
    #     super().__init__()
    #     print("User Constructor")        
        


u = User()
        