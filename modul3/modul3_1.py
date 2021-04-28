def enc_dec(text, key):
    result = ''
    for letter in text:
        number = ord(letter)
        result += (chr(number ^ key))
    return result


output = enc_dec("Hello World", 129)
print(output)

output_dec = enc_dec(output, 129)
print(output_dec)


# ex3 while
def add_numbers():
    sum = 0
    num_list = []
    while sum <= 100:
        if sum==100:
            break
        n = int(input("Enter numbers: "))
        if n >= 0:
            sum = sum + n
            num_list.append(n)
    else:

        return sum
    return num_list


print(add_numbers())
