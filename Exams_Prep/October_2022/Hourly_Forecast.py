def forecast(*args):
    locations_output = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": [],
    }
    for location, weather in args:
        locations_output[weather].append(location)

    output = ""

    for weather, locations in locations_output.items():
        for name in sorted(locations):
            output += f"{name} - {weather}\n"

    return output
