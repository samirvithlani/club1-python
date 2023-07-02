#overloading....

from multipledispatch import dispatch
#pip install multipledispatch

class Shape():
    
    @dispatch()
    def area(self):
        print("Area of shape")
    @dispatch(float,int)    
    def area(self,pi,r):
        print("Area of circle",pi*r*r)
    @dispatch(int,int)        
    def area(self,h,w):
        print("Area of rectangle",h*w)
    @dispatch(int)    
    def area(self,h):
        print("Area of square",h*h)
    

s = Shape()
s.area(3.14,12)