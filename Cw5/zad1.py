class Car:

    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok

car1 = Car("Maserati", "1998")
car2 = Car("Porshe", "2018")

print(car1.marka, car1.rok)
print(car2.marka, car2.rok)

car1 = car2

print(car1.marka, car1.rok)
print(car2.marka, car1.rok)
print(car2 == car1)
