user ={"name":"admin","password":"admin"}

def loginRequired(func):
    
    def inner(name,email):
        if name == "" or email == "":
            print("Please enter name and email")
            return
        elif name ==user["name"] and email == user["password"]:
            print("Welcome",name)
            func(name,email)
        else:
            print("Invalid credentials")    
    
    return inner


@loginRequired
def showData(name,email):
    print("show data..")
    
showData("admin","admin1")    
        