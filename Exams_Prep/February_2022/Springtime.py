def start_spring(**kwargs):
    objects = {}

    for name, object_type in kwargs.items():
        if object_type not in objects:
            objects[object_type] = []
        objects[object_type].append(name)

    sorted_objects = sorted(objects.items(), key=lambda x:(-len(x[1]), x[0]))

    output = ""
    for k, v in sorted_objects:
        output += f"{k}:\n"
        for elem in sorted(v):
            output += f"-{elem}\n"

    return output
