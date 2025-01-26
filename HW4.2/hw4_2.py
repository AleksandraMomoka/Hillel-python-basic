lst = [0, 1, 7, 2, 4, 8] #=> (0 + 7 + 4) * 8 = 88
#lst = [1, 3, 5] #=> 30
#lst = [6] #=> 36
#lst = [] #=> 0

sum_even = 0

if lst:
    for i, el in enumerate(lst):
        if i % 2 == 0:
            sum_even += el
    result = sum_even * lst[-1]
    print(result)
else:
    print(0)
