#result: [['Section1,value1,value2'],['Section2,value1,value2']

data="""
_____
Section1
_____
value1 
value2
_____
Section2
_____
value1
value2
_____
Section3
_____
value1
value2

"""

def parse_data(data:str):
    my_section = False
    linii=data.splitlines()
    result=[]

    print(linii)
    for line in linii :
        if "_____"== line and my_section is False :
            my_section = True
            print("New section")
        elif "_____"== line and my_section is True :
            my_section=False
            print("End new section")
        elif my_section:
            print("Section name is", line)
            result.append([line])

        print(line)
    return result

var=parse_data(data)
print(var)

#met2
def parse_data(data:str):
    result = []
    my_iter = data.splitlines().__iter__()
    for line in my_iter:
        if line == '':
            continue
        if "_____" == line:
            # section = next(my_iter)
            result.append([next(my_iter)])
            next(my_iter)
            # print("Section is", section)
            # result.append([section])
            continue
        result[-1].append(line)
        # print(line)
    return result
var = parse_data(data)
print(var)

#generator using for

my_list = list(range(1,100))
print(my_list)

my_list = []
for i in range(1,100):
    my_list.append(i)
print(my_list)

my_list=[i for i in range(1,100)]
print(my_list)

my_gen=(i for i in range(1,100))
print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


#tuple
my_tuple=(1,2,3)
print(my_tuple)
print(type(my_tuple))

#ex:
a = 10
b = 20
a,b=b,a
print('a=',a,'b=',b)

#ex2 gen cu pas de 3 folosit  in for pt a obt (1,9,18)
list=[]
gen1=(i for i in range(0,105,3))
for i in gen1:
    print(i)
    next(gen1)
    next(gen1)

#list process

my_list=[1,2,3,4,5,6,7]
for i in my_list.copy():
    print(i)
    my_list.pop(0)
