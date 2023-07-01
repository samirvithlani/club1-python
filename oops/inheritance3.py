
class President():
    
    salary = 10000
    tax =20
    
class Gov():
    
    grant =1000
    tax =10




class Person(President,Gov):
    
    def personData(self):
        print(self.grant)
        print(self.salary)
        print(self.tax)


p = Person()
p.personData()        