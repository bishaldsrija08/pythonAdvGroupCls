def decorator_with_args(func):
    def wrapper(*args, **kwarks):
        print("Decorator with arguments:")
        print("Positional arguments:", args)
        print("Keyword arguments:", kwarks)
        return func(*args, **kwarks)
    return wrapper

@decorator_with_args
def my_function(x, y, z=0):
    print(f"Function called with x={x}, y={y}, z={z}")
my_function(1, 2, z=3)