from modul3.app1 import primes
import random


def select_primes(num,limita) :
    i = 0
    fin_list = []
    my_list = primes(limita)
    y = len(my_list)
    for _ in range(num):
        x = random.randint(0,y - 1)
        fin_list.append(my_list.pop(x))
        y -= 1
    print(fin_list)

my_primes = primes(100)
print(my_primes)
select_primes(5,100)
