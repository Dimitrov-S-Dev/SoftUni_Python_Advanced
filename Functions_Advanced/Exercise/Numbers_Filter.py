# def even_odd_filter(**kwargs):
#     if "odd" in kwargs:
#         kwargs["odd"] = [x for x in kwargs["odd"] if x % 2 != 0]
#     if "even" in kwargs:
#         kwargs["even"] = [x for x in kwargs["even"] if x % 2 == 0]
#
#     return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
#


def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs["odd"] = list(filter(lambda x: x % 2 != 0, kwargs["odd"]))
    if "even" in kwargs:
        kwargs["even"] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
