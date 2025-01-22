#lst = [1, 2, 3, 4, 5, 6] #=> [[1, 2, 3], [4, 5, 6]]
#lst = [1, 2, 3] #=> [[1, 2], [3]]
#lst = [1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
#lst = [1] #=> [[1], []]
lst = [] #=> [[], []]

lst_mid = (len(lst) + 1) // 2

lst_first_part = lst[:lst_mid]
lst_second_part = lst[lst_mid:]

print([lst_first_part, lst_second_part])