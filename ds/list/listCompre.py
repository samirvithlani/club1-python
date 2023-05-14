users = [12,34,56,78,90,23,33]
evnuser =[i for i in users if i %2==0]

city = ["udiapur","agra","jaipur","delhi","mumbai","pune","chennai","kolkata","banglore","hyderabad"]
filcity = [i for i in city if len(i)>6 or i.startswith("b")]
print(filcity)


# for i in users:
#     if i%2==0:
#         evnuser.append(i)



print(evnuser)        