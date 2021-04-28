import math
#functions


def my_func1(arg1,arg2,arg3,kwarg1=' ',kwarg2='\n'):
    print(arg1, arg2, arg3,sep=kwarg1,end=kwarg2)
    return arg1 + arg2 + arg3

my_var1=my_func1('str1','str2','str3','#','$')
print('\n'+ 80*'#')
print(my_var1)

#create function for
#met1
a=input("Introduceti numar:")
def prime_f(a):
    if a%2 == 0:
        return(True)
    else:
        return(False)
print(prime_f(17))

#met2
def is_prime(number):
    for i in range(2,number):
        if (number % i) == 0:
            return False
    return True
print(is_prime(3))


#list
# empty_list=[]
# my_list1=[1,2,3]
# print(my_list1)
# my_list.append(4)
# print(my_list1)

# empty_list.append(10)
# print(empty_list)

#ex3
def primes(limit):
    result=[]
    for i in range(1,limit+1):
        if is_prime(i) is True :
       # result.append(i)
    #return result

#nr prime
#import math
def is_prime(number):
    if(number ==1 or number ==0):
        return False
    elif(number==2):
        return True
    elif(number%2==0):
        return False
    else:
        for i in range(3,int(math.sqrt(number)+1)):
            if(number%i==0):
                return False
    return True

def primes1(limit):
    result=[]
    for i in range(1,limit+1):
        if(is_prime(i)==True):
            result.append(i)
    return result
print(primes(10))

#numere pe biti
#And
print(10&11) #este diferit de (10 and 11)
print((10).__and__(11))
10 #000000000...1010
11 #000000000...1011
#000000000000...1010

#Or
print(10|11)
print((10).__or__(11))
10 #000000000...1010
11 #000000000...1011
#000000000000...1011

#Xor
print(10^11)
print((10).__xor__(11))
10 #000000000...1010
11 #000000000...1011
#000000000000...0001

#Xor negative number
print(-1^3)
print((-1).__xor__(3))
10 #000000000...1111 -1
11 #000000000...0011
#000000000000...1100


