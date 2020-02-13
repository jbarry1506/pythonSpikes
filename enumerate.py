# enumerate example
animals = ['dog', 'cat', 'monkey', 'Brandon', 'Kyle']

# single argument is zero based
for index, value in enumerate(animals):
    print(index, value)

# 2nd argument is for what index value to start from
for index, value in enumerate(animals, 1):
    print(index, value)