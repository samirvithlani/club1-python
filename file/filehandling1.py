#//relative paath 
#//absolute path
#//d: \file\demo.txt
#
#file = open("../../demo1.txt",'a')
file = open("D:\\royal\\club-1-python\\demo2.txt",'a')
file.write("Hello World")
file.write("100")
file.writelines(["\nHello World","\n100"])
file.close()
print("File Created")