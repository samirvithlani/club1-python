users = {1:"ram", 2:"shyam", 3:"hari"}

value = users.get(1)
print(value)

keys = users.keys()
print(keys)
for i in keys:
    print(i)

value = users.values()    
print(value)
for i in value:
    print(i)
    

for i in users.items():
    print(i)    

newdic = users.fromkeys((1,2,3,4,5,6,7),"shyam")    
print(newdic)

x = users.setdefault(1,"hari")
print(x)

users[11]="krishna" #update

print(users)