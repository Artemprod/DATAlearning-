from time import sleep
import random
from itertools import cycle

# _______ вариант 1___________



# class TrafficLight:
#
#     light = ['red', 'yellow', 'green']
#
#     def running(self):
#         sleep(7)
#         print(TrafficLight.light[0])
#         sleep(2)
#         print(TrafficLight.light[1])
#         sleep(4)
#         print(TrafficLight.light[2])
#
#
# lighter_1 = TrafficLight()
#
# lighter_1.running()

# _______ вариант 2___________


# class TrafficLight:
#
#     light = ['red', 'yellow', 'green']
#
#     def running(self):
#         sleep_time = 7
#         for i in TrafficLight.light:
#             sleep(sleep_time)
#             print(i)
#             sleep_time -= 5
#             if sleep_time < 0:
#                 sleep_time = random.randint(1, 10)
#
#
# lighter_1 = TrafficLight()
# lighter_1.running()

# _______ вариант 3___________


class TrafficLight:

    light = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        stop_cycle = 0
        for i in cycle(TrafficLight.light):
            sleep(2)
            print(i)
            stop_cycle += 1
            if stop_cycle > 15:
                break

lighter = TrafficLight()
lighter.running()