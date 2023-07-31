from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

ornament = Ornament()
plant = Plant()
freshwater_fish = FreshwaterFish("freshwater_fish", "fish", 20.5)
saltwater_fish = SaltwaterFish("saltwater_fish", "fish", 22.5)
freshwater_aquarium = FreshwaterAquarium("freshwateraquarium")
saltwater_aquarium = SaltwaterAquarium("salthwateraquarium")
print(freshwater_aquarium.add_fish(freshwater_fish))
print(freshwater_aquarium)




