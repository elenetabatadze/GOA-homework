def clean_integers(lst):
    ints = [x for x in lst if type(x) == int]
    return ints if len(lst) - len(ints) == 1 else lst