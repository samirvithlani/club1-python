# mutable , immutable, string immutability

name = "ram"

name = name.upper()
print(name)
sant = "hello this is instagram"

sant = sant.capitalize()
sant = sant.title()
print(sant)


#manupulation

email = "  ram@gmail.com  "
print(len(email))
#email = email.replace("a","@",2)
email = email.strip()
print(len(email))
print(email)


word = "java"
word = word.rstrip()
print(len(word))
print(word)
#name.lstrip()

#booelan

fname = "java//"
print(fname.isalnum())
print(fname.isalpha())
print(fname.isdigit())
print(fname.islower())
print(fname.isupper())
print(fname.isspace())
print(fname.istitle())

print(fname.startswith("jv"))
print(fname.endswith("//"))

print(fname.find("a"))
print(fname.rfind("a"))
print(fname.index("a"))
print(fname.rindex("a"))
print(fname.count("a"))


print(name)

fname = fname +"python"
print(fname)



data = "hello,this,is,python"
x = data.split("i")
print(x)



x = 'A'
c ='65'
print(ord(x))
print(chr(int(c)))
