# 1
import itertools

for num in itertools.count(1):
    if num > 15:
        break
    else:
        print(num)

# 2
end = 0
for num_cycle in itertools.cycle('this is amazing and '):
    if end > 20:
        break
    else:
        print(num_cycle)
    end += 1

