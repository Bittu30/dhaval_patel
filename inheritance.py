class Vehicle:
    def general_usage(self):
        print("general use: transportation")


class Car(Vehicle):
    def __init__(self):
        print("I am car")
        self.wheel = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("Commute to work, go to vacation")


class Motorcycle(Vehicle):
    def __init__(self):
        print("I am motorcycle")
        self.wheel = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("Commute to work, go to road trip")


s = Car()
s = Motorcycle()

print(issubclass(Car, Motorcycle))
