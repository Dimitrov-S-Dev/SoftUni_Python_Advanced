def flights(*args):
    output = {}
    for index in range(0, len(args) - 1, 2):
        destination = args[index]
        if destination == "Finish":
            break
        passengers = args[index + 1]
        if destination not in output.keys():
            output[destination] = 0
        output[destination] += passengers

    return output
