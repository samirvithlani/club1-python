class Employer():
    
    salary = 10000
    
    def setEmployeeSalary(self,exp):
        return self.salary + exp
    
class Employee(Employer):
    
    def getEmployeeSalary(self):
        self.salary = self.setEmployeeSalary(10)    
        return self.salary



emp = Employee()
x = emp.getEmployeeSalary()    
print(x)

print(emp.salary)