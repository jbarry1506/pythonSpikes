# examples and practice of statically typed python functions
# I don't think I'm doing this correctly or I don't understand it.


def static_string(a_str: str, b_str: str) -> str:
    return f"There once was a {a_str} who lived in a {b_str}."


def static_int(a_int: int, b_int: int) -> int:
    return a_int + b_int


final_string = static_string('woman', 'shoe')
print(final_string)

final_int = static_string(3, 4)
print(final_int)

int_return = static_int(2,3)
print(int_return)

int_return_2 = static_int('4','5')
print(int_return_2)


try:
    final_int = static_string(1, 2)
    print(final_int)
except AssertionError as error:
    print(error)
