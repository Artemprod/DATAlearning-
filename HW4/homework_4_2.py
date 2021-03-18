# v1
# import random
# my_list = [random.randint(0, 300) for i in range(10)]
# print(my_list)
# comp_list  = []
# for ind, num in enumerate(my_list):
#     if num > my_list[ind - 1] and ind != 0:
#         comp_list.append(num)
# print(comp_list)
#
# v2

import random
my_list = [random.randint(0, 300) for i in range(10)]
print(my_list)
comp_list  = []
for ind, num in enumerate(my_list):
    if num > my_list[ind - 1] and ind != 0:
        comp_list.append(num)
print(comp_list)
