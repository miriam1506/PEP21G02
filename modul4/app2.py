multi_dimensional_list = [[1, [2, [3]]], [4, [5, [6]]], [7, [8, [9]]]]
#met1
fin_list=[]
for i in multi_dimensional_list:
    list2=i
    fin_list.append(list2.pop(0))
    for j in list2:
        list3=j
        fin_list.append(list3.pop(0))
        for k in list3:
            list4=k
            fin_list.append(list4.pop(0))
print(fin_list)

#met2
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def flatten_list(data:list):
    fin_list = []
    for i in data:
        if type(i) == int:
            fin_list.append(i)
            continue
        print(i)
        for j in i:
            if type(j) == int:
                fin_list.append(j)
                continue
            print(j)
            for m in j:
                if type(m) == int:
                    fin_list.append(m)
                    continue
                print(m)
                for n in m:
                    if type(n) == int:
                        fin_list.append(n)
                        continue
                    print(n)
    return fin_list
result = flatten_list(multi_dimensional_list)
print(result)

#recursivitate
def flatten_list(data :list):
    fin_list = []
    for i in data:
        if type(i) == int:
            fin_list.append(i)
            continue
        print(i)
        fin_list.extend(flatten_list(i))
    return fin_list

result=flatten_list(multi_dimensional_list)
print(result)
