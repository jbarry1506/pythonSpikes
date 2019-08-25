# BASIC DECORATOR EXAMPLE

def my_decorator_1(func):
    def wrapper(func):
        func()
        print("this is the decorator for my_basic_func_1")

    return wrapper(func)


@my_decorator_1
def my_basic_func_1():
    print("Basic function 1.")


my_basic_func_1


# BASIC DECORATOR EXAMPLE - WITH GLOBAL VARIABLE CONDITIONAL
my_conditions = ["yes","no"]

def my_decorator_2(func):
    def wrapper(func):
        if my_condition == "yes":
            func()
            print("This is decorated")
        else:
            print("nothing to do.")

    return wrapper(func)

for i in my_conditions:
    my_condition = i
    @my_decorator_2
    def my_basic_func():
        print("This is the first function.")
