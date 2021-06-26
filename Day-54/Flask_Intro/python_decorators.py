def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# First-class objects, can be passed around as arguments e.g. int/string/float

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


print(calculate(add, 3, 8))


# Nested functions

def outer_function():
    print("I'm outer function.")

    def nested_function():
        print("I'm inner function")

    return nested_function()


inner_function = outer_function
inner_function()
