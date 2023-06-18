users =["raj","parth","priya","pankti","neha"]

def checkelm(func):
    def inner(elm):
        for i in users:
            if i == elm:
                func(elm)
                break
            else:
                print("User not found")
        
    return inner


@checkelm
def getUsers(elm):
    print(users)            


getUsers("rajvi")    