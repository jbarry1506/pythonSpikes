
little_list = ["Jim", "Lee", "Josh", "Matt", "Mike", "Reuben"]

def full_conditional(lst):
    """How a conditional in a loop usually looks"""
    for name in lst:
        if name == "Lee":
            rubrik_admin = name
        else:
            rubrik_admin = "unknown"
        print(rubrik_admin)


def one_line_conditional(lst):
    """short, simple conditionals can be condensed to one line"""
    for name in lst:
        rubrik_admin = name if name == "Lee" else "unknown"
        print(rubrik_admin)


full_conditional(little_list)

one_line_conditional(little_list)

