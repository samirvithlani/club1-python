from multipledispatch import dispatch
class Data():
    
    @dispatch(list)
    def getData(self,list):
        print("Data is list",list)
        print(type(list))
    @dispatch(tuple)                                    
    def getData(self,tuple):
        print(type(tuple))
        print("Data is tuple",tuple)
        
    @dispatch(dict)    
    def getData(self,dict):
        print(type(dict))
        print("Data is dict",dict)
     
    # @dispatch(kwargs=dict)    
    # def getData(**kwargs):
    #     print("Data is dict",kwargs)    
    
    
    
d = Data()
d.getData([1,2,3,4])
d.getData({1:2,3:4})

        
        