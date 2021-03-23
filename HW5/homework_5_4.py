from time import sleep
from random import randint

class Car:

    direction = ['east', 'west', 'north', 'south']

    def __init__(self, speed, color, name, is_polise = bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

        if self.is_polise == True:
            print('stop the car and get out! ')



    def go(self):
        start_cheking = ['Hello driver. We need to check the system before you will able to drive',
                         'checking system', 'system checked!', 'start engine']

        for i in start_cheking:
            sleep(2)
            print(i)
            for p in range(3):
                if i == 'start engine':
                    break
                else:
                    sleep(1)
                    p = ' . '
                    print(p)


    def stop(self):
        print('car is stopped')

    def turn(self):
        print(Car.direction[randint(0, 3)])

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('speed limit')


class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('speed limit')


class PoliceCar(Car):
    pass



car = PoliceCar(20,'whit', 'name', True)
car.is_polise
car.show_speed()
car.go()
