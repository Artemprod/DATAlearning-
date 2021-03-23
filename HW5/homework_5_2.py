class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_of_road(self):
        mass = int(input('input needed mass: '))
        centi_amount = int(input('input needed centi: '))
        result = self.__width * self.__length * mass * centi_amount
        print(result)
        return result


road = Road(1, 2)
road.mass_of_road()