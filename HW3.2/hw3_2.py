#lst = [12, 3, 4, 10]# => [10, 12, 3, 4]
#lst = [1]#=> [1]
#lst = []# => []
lst = [12, 3, 4, 10, 8]# => [8, 12, 3, 4, 10]

if len(lst) == 0:
    print(lst)
else:
    swap_element = lst.pop()
    lst.insert(0, swap_element)
    print(lst)