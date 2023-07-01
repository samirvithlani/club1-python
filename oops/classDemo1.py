class Vehicle():
    print("This is a Vehicle class")
    #instance variable, class variable
    #it will create a copy of this variable for each object
    name = "Car"
    
    def getCarData(self,name):
       # print(self)
        #local variable
        print(name)
        print(self.name)
        print("This is a car")



veh = Vehicle()    
#print(veh.name)
veh.getCarData("bmw")
    
    