def add_one(some_list):
    some_list = [str(i) for i in some_list]
    num = "".join(some_list)
    calculate = int(num) + 1
    result = [int(i) for i in str(calculate)]
    return result

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

