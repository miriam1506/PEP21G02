def factorial(number):
    n=int(number)
    for i in range (1,n):
        n=n*i
    return
factorial(4)
print(factorial(4))

def factorial(n):
    if n<= 1:
        return 1
    else:
        return n * factorial (n-1)

factorial(4)
print(factorial(4))

#append vs extend
a = [1,2,3]
b = [3,4,5]
a.append(b)
a.extend(b)
print(a)

#sets

my_empty_set = set()
print(my_empty_set)

#my_set = set([1,2,3])
#print(my_set)

set_a = set([1,2,3,4])
set_b = set([3,4,5,6])

#set operations

result = set_a.union(set_b)
print(result)

result = set_a.difference(set_b)
print(result)

result = set_b.difference(set_a)
print(result)

#result = set_a.difference_update(set_b)
#print(result)

#result = set_a.difference_update(set_b)
#print(set_a)

result = set_a.symmetric_difference(set_b)
print(result)


#local,nonlocal,global variables

g_var1 = 'a'

def check_g():
    global g_var1
    g_var1 = 'c'
    ln_var1 = 'd'
    print(g_var1)
    def check_n():
        nonlocal ln_var1
        print('in n function: ', ln_var1)
    check_n()

check_g()

print(g_var1)
g_var1='c'
print(g_var1)
