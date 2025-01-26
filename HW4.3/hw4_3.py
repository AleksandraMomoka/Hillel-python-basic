import random


lst = []
lenth_lst = random.randrange(3, 10)

for i in range(lenth_lst):
    lst.append(random.randint(0, 100))

new_lst = [lst[0], lst[2], lst[-2]]

print(lst)
print(new_lst)
