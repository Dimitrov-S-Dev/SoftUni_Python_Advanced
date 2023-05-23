# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args:
#         result += arg
#     for k, v in kwargs.items():
#         if k in result:
#             result = result.replace(k, v)
#
#     return result

def concatenate(*args, **kwargs):
    text = "".join(args)
    for k, v in kwargs.items():
        if k in text:
            text = text.replace("k", v)

    return text
