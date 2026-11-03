class Car:
    def __init__(self, name, year, color, for_sale = False):
        self.model = name
        self.age = year
        self.color = color
        self.sale = for_sale
    def drive(self):
        print(f"you drive {self.model} car")

class bicycle(Car):
    pass       
car1 = Car("toyota", "2026", "red", True)
car2 = Car("merc", 2024, "blue")
bike1 = bicycle("merc", 2024, "blue")
print(car1.model, car1.sale)
print(car2.model, car2.sale)
car1.drive()
bike1.drive()