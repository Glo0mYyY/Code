class Bike:
    def __init__(self, name  = ""):
        self.name = name
    gear = 0
    def shift_gear_up(self):
        self.gear = self.gear + 1

bike1 = Bike(name="Harley")

bike1.gear = 3

print(bike1.name, bike1.gear)
bike1.shift_gear_up()
print(bike1.name, bike1.gear)
