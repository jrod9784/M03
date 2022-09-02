from pyexpat import model
#from typing_extensions import Self


class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType


class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def details(self):
        print("Vehicle type: " + self.vehicleType)
        print("Year: " + self.year)
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Number of doors: " + self.doors)
        print("Type of roof: " + self.roof)


vehicleType = input("Enter type of vehicle: ")
year = input("Enter year of vehicle: ")
make = input("Enter make of vehicle: ")
model = input("Enter model of vehicle ")
doors = input("Enter how many doors vehicle has: ")
roof = input("Does vehicle have a sunroof or solid roof? ")
car = Automobile(vehicleType, year, make, model, doors, roof)
car.details()
