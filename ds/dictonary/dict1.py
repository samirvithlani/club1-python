#key value pair dictornary


ranks = {1:"king",2:"queen",3:"jack",4:"ace",5:"joker",1:"New king",6:"queen","a":"Amit"}
print(ranks)

ranks.update({2:"New jack"})

removedvalu = ranks.pop(1)
print("removedvalu",removedvalu)

removedata = ranks.popitem()
print("removedata",removedata)

for i,j in ranks.items():
    print(i,j)
    
    