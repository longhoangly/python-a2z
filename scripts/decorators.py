import time


def exe_time(func):
    def wrapper(*args, **kwargs):
        print()
        print(f"Calling function: {func.__name__} with args {args}, {kwargs}")
        before_exe_time = time.time()
        result = func(*args, **kwargs)
        after_exe_time = time.time()
        print(f"{func.__name__} time of execution {after_exe_time - before_exe_time}ms")
        print(f"{func.__name__} finished execution, output {result}")
        print()
        return result

    return wrapper


@exe_time
def say_hello():
    print("Hello!")


@exe_time
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


# Run the functions
say_hello()
print(add(3, 4))
