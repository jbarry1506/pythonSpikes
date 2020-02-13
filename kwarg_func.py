# how to use args, kwargs, splats, & double splats


# single splat splits lists into arguments
def args_func(*args):
    if args:
        for i in args:
            for j in i:
                print(j)
            print('\n')


# double splat splits keyword arguments
def kwargs_func(**kwargs):
    if kwargs:
        for i, j in kwargs.items():
            print(i, j)


def main():
    # a list of lists
    sarg = [['up', 'up'], ['down', 'down'], ['left', 'right'], ['left', 'right'], ['B', 'A'], 'START']
    # just a standard list
    sarg2 = ['down', 'down+left', 'left', 'B+A']

    # see what happens when we call the args_func
    args_func(sarg, sarg2)

    # dictionary
    skwarg = {'owl': {'sound': 'hoot',
                      'eyes': 'big round',
                      'ears': 'big pointy',
                      'mouth': 'pointy beak'},
              'wolf':{'sound': 'a-wooOOO',
                      'eyes': 'what big eyes',
                      'ears': 'what big ears',
                      'mouth': 'what big teeth'}
              }

    # keyword arguments for the **kwargs
    kwargs_func(pooh='bother', tigger='bounce')

    # double splat the dictionary for **kwargs
    kwargs_func(**skwarg)


if __name__ == "__main__":
    main()