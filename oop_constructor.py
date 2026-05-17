from numpy.ma.core import make_mask


class Car:
    print("default=")
    def __init__(self): #dafault constructor
        self.make = "Toyota"
        self.model = "Ford"
        self.year = 2020

car = Car()
print(car.make)
print(car.model)
print(car.year)


class Car:
    print("perameterize=")
    def __init__(self, make, model, year): #perameterized
        self.make = make
        self.model = model
        self.year = year
car = Car("honda","civic",2022)
print(car.make)
print(car.model)
print(car.year)