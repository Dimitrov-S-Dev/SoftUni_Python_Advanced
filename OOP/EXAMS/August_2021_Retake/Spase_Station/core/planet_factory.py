from project.planet.planet import Planet


class PlanetFactory:
    @staticmethod
    def create_planet(name, items):
        new_planet = Planet(name)
        new_planet.items.extend(items.split(", "))
        return new_planet
