from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            p_name = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
            self.pokemons.remove(p_name)
            return f"You have released {pokemon_name}"
        except StopIteration:
            return "Pokemon is not caught"

    def trainer_data(self):
        output = ""
        output += f"Pokemon Trainer {self.name}\n"
        output += f"Pokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            output += f"- {p.pokemon_details()}\n"

        return output


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())