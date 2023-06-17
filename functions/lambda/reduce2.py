
from  functools import reduce

data = [100,2,45,67,89,98]


larger = reduce(lambda a,b:a if a>b else b,data)
# larger =data[0]

# for i in data:
#     if i > larger:
#         larger =i

print(larger)        
    

