"""
Get text from input:abcdefg
return: aceg

"""
x=input("Get input: ")

y1=ord(x[0:1])+0
z1=chr(y1)
y2=ord(x[1:2])+1
z2=chr(y2)
y3=ord(x[2:3])+2
z3=chr(y3)
y4=ord(x[3:4])+3
z4=chr(y4)
y5=ord(x[4:5])+4
z5=chr(y5)
y6=ord(x[5:6])+5
z6=chr(y6)
y7=ord(x[6:7])+6
z7=chr(y7)
print(z1,z2,z3,z4,z5,z6,z7,sep="")

#met2
x=input("input=")

if (x[0] == "a"):
    z1 = x[0]
elif (x[0] == "b"):
    z1 = chr(ord(x[0]) + 1)
elif (x[0] == "c"):
    z1 = chr(ord(x[0]) + 2)
elif (x[0] == "d"):
    z1 = chr(ord(x[0]) + 3)
elif (x[0] == "e"):
    z1 = chr(ord(x[0]) + 4)
elif (x[0] == "f"):
    z1 = chr(ord(x[0]) + 5)
elif(x[0]=="g"):
    z1 = chr(ord(x[0]) + 6)
if (x[1] == "a"):
    z2 = x[0]
elif (x[1] == "b"):
    z2 = chr(ord(x[1]) + 1)
elif (x[1] == "c"):
    z2 = chr(ord(x[1]) + 2)
elif (x[1] == "d"):
    z2 = chr(ord(x[1]) + 3)
elif (x[1] == "e"):
    z2 = chr(ord(x[1]) + 4)
elif (x[1] == "f"):
    z2 = chr(ord(x[1]) + 5)
elif(x[1]=="g"):
    z2 = chr(ord(x[1]) + 6)
if (x[2] == "a"):
    z3 = x[0]
elif (x[2] == "b"):
    z3 = chr(ord(x[2]) + 1)
elif (x[2] == "c"):
    z3 = chr(ord(x[2]) + 2)
elif (x[2] == "d"):
    z3 = chr(ord(x[2]) + 3)
elif (x[2] == "e"):
    z3 = chr(ord(x[2]) + 4)
elif (x[2] == "f"):
    z3 = chr(ord(x[2]) + 5)
elif(x[2]=="g"):
    z3 = chr(ord(x[2]) + 6)
if (x[3] == "a"):
    z4 = x[0]
elif (x[3] == "b"):
    z4 = chr(ord(x[3]) + 1)
elif (x[3] == "c"):
    z4 = chr(ord(x[3]) + 2)
elif (x[3] == "d"):
    z4= chr(ord(x[3]) + 3)
elif (x[3] == "e"):
    z4 = chr(ord(x[3]) + 4)
elif (x[3] == "f"):
    z4 = chr(ord(x[3]) + 5)
elif(x[3]=="g"):
    z4 = chr(ord(x[3]) + 6)
print(z1,z2,z3,z4,sep="")

#met3
x = input("input=")
z1 = chr(ord(x[0]) + (ord(x[0]) - ord('a')))
z2 = chr(ord(x[1]) + (ord(x[1]) - ord('a')))
z3 = chr(ord(x[2]) + (ord(x[2]) - ord('a')))
z4 = chr(ord(x[3]) + (ord(x[3]) - ord('a')))
z5 = chr(ord(x[4]) + (ord(x[4]) - ord('a')))
z6 = chr(ord(x[5]) + (ord(x[5]) - ord('a')))
z7 = chr(ord(x[6]) + (ord(x[6]) - ord('a')))
print(f'{z1}{z2}{z3}{z4}{z5}{z6}{z7}')
