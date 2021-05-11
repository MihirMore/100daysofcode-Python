def add(*args):
    sum1 = 0
    for n in args:
        sum1 += n
    return sum1


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


print(add(2, 4, 5, 6, 8, 12, 3233, 34123, 1231231224, 45233))

calculate(2, add=3, multiply=5)

class Car():

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="GTR")
print(my_car.model)
