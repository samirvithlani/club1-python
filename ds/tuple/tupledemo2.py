users = (("user1","password1"),("user2","password2"),("user3","password3"))

for i in users:
    for j in i:
        print(j)
    print("**********")    


print(users[1][1])    