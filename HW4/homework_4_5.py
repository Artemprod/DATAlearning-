import functools

my_list = [el for el in range(100,1001)  if el % 2 == 0]

multiplay_list = functools.reduce(lambda x,y: x * y , my_list)
print(multiplay_list)
