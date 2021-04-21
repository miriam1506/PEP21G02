"""
Take last free input: any text
change each letter

I will revert the change

"""
# metoda buna pe jumatate
# from random import randrange
# x=input("input any text: ")
# for letter in x:
#     print(chr(ord(letter)+randrange(10)), end="")

# metoda buna
# txt= input("insert text: ")
# for letter in txt:
#     if(ord(letter)%2==1):
#         letter=chr(ord(letter)-1)
#     print(letter,end="")

# 2
input1 = input("Write a text: ")
result = ''
previous=''

for letter in input1:
    if previous=='':
        previous=letter
        result=result + letter
    else:
        l=chr(ord(letter)+ord(previous))
        result = result + l
print(result)

k=input1[0]

result2=k
for letter in result[1:]:
    result2+= chr(ord(letter)-ord(k))

print(result2)

