# Python Decorator Function


def decorator_function(function):
    def wrapper_function():
        function()

    return wrapper_function()