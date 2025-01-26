#lst = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
#lst = [0] #-> [0]
#lst = [1, 0, 13, 0, 0, 0, 5] #-> [1, 13, 5, 0, 0, 0, 0]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

not_null_lst = []
null_lst = []

for el in lst:
    if el != 0:
        not_null_lst.append(el)
    else:
        null_lst.append(el)
result_lst = not_null_lst + null_lst

print(result_lst)
