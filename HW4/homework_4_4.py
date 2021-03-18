import random
my_list = [random.randint(0, 10) for i in range(20)]
count_el = [i for i in my_list if my_list.count(i) == 1]
print(f"initial list - {my_list}, \n sorted list - {count_el}")
