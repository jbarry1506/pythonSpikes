# practice merging two dictionaries

x = {
    'a': 1,
    'b': 2,
    'c': 3
}

y = {'d': 4, 'e': 5, 'f': 6}

def combine_dicts(**x_dict, **y_dict):
    whole_dict = x_dict + y_dict
    print(whole_dict)