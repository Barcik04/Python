class Fruit:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def isfresh(self):
        return False

class Apple(Fruit):
    def __init__(self):
        super().__init__("red", 220)

    def isfresh(self):
        return self.color == "red"

class Banana(Fruit):
    def __init__(self):
        super().__init__("yellow", 195)

    def isfresh(self):
        return self.color == "yellow"

class Orange(Fruit):
    def __init__(self):
        super().__init__("orange", 250)

    def isfresh(self):
        return self.color == "orange"

Apple = Apple()
Banana = Banana()
Orange = Orange()

for i in [Apple, Banana, Orange]:
    print(f'{i.__class__.__name__}:   Color = {i.color},   weight = {i.weight},   is it Fresh: {i.isfresh()}')
