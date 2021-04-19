name='Maria'
age= 20
print("name: ", name ," , age: ", age)
#result=type(name)
#print(name)
#result=type(age)
#print(age)

print(name*5)
result1=type(name*5)
print(result1)

result = id(name)
print(result)

print(8+8)
print((8).__add__(8))

print(8 * 'text')
print((8).__mul__ ('text'))
print(('text').__mul__(8))

print(8-8)
print((8).__sub__(8))

print(8/8)
print((8).__truediv__(8))

#Float
var = (8).__truediv__(8)
print(type(var))

print(8**8)
print((8).__pow__(8))
print(pow(8 ,8))

#y=(-4 + ((4**2 -4*3*5)**(1/2))/(2*3)
#print (y)

a=3
b=4
c=5
x = (-b +((b**2) - 4*a*c)**(1/2))/(2*a)
print(x)

#prin metode
a=3
b=4
c=5
#bsqr = b.__pow__(2)
#multi=(4).__mul__(a.__mul__(c))
#dif=(bsqr).__sub__(multi)
#var=(1).__truediv__(2)
#rad=dif.__pow__(var)
#dif2=rad.__sub__(b)
#multi2=(2).__mul__(a)
#impartire=dif2.__truediv__(multi)
#x=impartire
#print(x)

bsqr= b.__pow__(2)
multi= (4).__mul__(a.__mul__(c))
dif= bsqr.__sub__(multi)
dif=float(dif)
var=(1).__truediv__(2)
rad=dif.__pow__(var)
b= complex(b)
dif2=(-b).__sub__(rad)
mul1=(2).__mul__(a)
ec= dif2.__truediv__(mul1)
print(ec)

#Complex

nr1=1.0 + 1.0j
nr2=3+5j
print(nr1+nr2)
print(type(nr1+nr2))

#String
my_str1 = 'My String1'
my_str2='''
My
multi
string
'''
print(my_str1)
my_str2=r"My string \n no multi line" #raw line
print(my_str2)
my_str2=f"""My string {my_str1}"""
print(my_str2)

#dir
info=dir(my_str2)
print(info)

var1 = 'this is my name'
cap=var1.capitalize()
print(cap)
format1 = var1.format('an Apple')
print(format1)

phone="0728.996.123"
split1=phone.split("8")
print(split1)
split1=phone.rsplit(sep=".",maxsplit=1)#right
print(split1)
split1=phone.split(sep=".",maxsplit=1)#left
print(split1)

#input
#name=input('Give me your name: ')
#print(var1,input('Give me your name:'))

#slice
text="My Text"
first_letter= "My Text"[1:4]
print(first_letter)
slice1=text[0:6:2]
print(slice1)

#text = input('Enter text here:')
slice1=text[0:5]
slice2=text[5:11]
print(slice2 + slice1)
#print(slice1)
#print(slice2)

#negative step
reverse=text[::-1]
print(reverse)

reverse1=slice1[::-1]
reverse2=slice2[::-1]
print(reverse2+reverse1)

#True,False
my_boo=True
print(type(my_boo))
print(id(True))

x= True + False
print(x)
print(dir(True))
x=True.__add__(False)
print(x)

#None

my_none=None

x=print('')
print(x)

print(bool(0+0j))
print(bool(0.0))
