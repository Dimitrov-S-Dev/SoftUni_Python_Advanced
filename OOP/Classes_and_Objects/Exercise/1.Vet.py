from typing import List


class Vet:
    animals: List[str] = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str) -> str:
        if len(self.animals) >= Vet.space:
            return "Not enough space"

        self.animals.append(animal_name)
        Vet.animals.append(animal_name)

        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"

        Vet.animals.remove(animal_name)
        self.animals.remove(animal_name)

        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. " \
               f"{Vet.space - len(Vet.animals)} space left in clinic"
