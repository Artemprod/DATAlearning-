class Stationery:

    def __init__(self, title):
        self.title = title


    def draw(self):
        print(f" запуск отрисовки {self.title}")


class Pen(Stationery):

    def draw(self):
        print(f"{self.title} нарисованно синей линией")


class Pencil(Stationery):

    def draw(self):
        print(f"{self.title} нарисованно карандашом")


class Handle(Stationery):

    def draw(self):
        print(f"{self.title} нарисованно жирнющей и растекающейся красной полосой ")

pen = Pen("<Привет>")
pen.draw()

pencil = Pencil("<Привет>")
pencil.draw()

handle = Handle("<Привет>")
handle.draw()