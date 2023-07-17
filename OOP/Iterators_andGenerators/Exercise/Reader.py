def read_next(*args):
    for arg in args:
        for elem in arg:
            yield elem
