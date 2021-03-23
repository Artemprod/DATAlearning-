class Worker:


    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f" Whole name: {self.name} {self.surname}")
        print(f" income: {self.income.get('wage') + self.income.get('bonus')}")


pos = Position('Vitalik', 'Pterov', 'driver', 10, 20)

pos.get_full_name()

