# this is not finished, still trying to understand

def kwarg_func(**kwargs):
    for i in kwargs:
        print(i)


def main():
    args = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'B', 'A', 'START']
    kwarg_func()


if __name__ == "__main__":
    main()