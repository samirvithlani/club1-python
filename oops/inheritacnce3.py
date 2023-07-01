class Calc():
    
    no1 = 0
    no2 = 0
    

class Add(Calc):
    
    def __init__(self) :
        self.no1 = 10
        self.no2 = 20
    
    def add(self):
        return self.no1 + self.no2

class Sub(Calc):
    
    def __init__(self) :
        self.no1 = 10
        self.no2 = 20
    
    def sub(self):
        return self.no1 - self.no2

add = Add()
ans = add.add()        
print(ans)
sub = Sub()
subans = sub.sub()
print(subans)