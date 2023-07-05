from animal import Animal
from caretaker import Caretaker
from cheetah import Cheetah
from keeper import Keeper
from lion import Lion
from tiger import Tiger
from vet import Vet
from worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity == len(self.animals):
            return f"Not enough space for animal"
        if price > self.__budget:
            return f"Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} " \
               f"added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return f"Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} " \
               f"hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries = sum(w.salary for w in self.workers)

        if workers_salaries > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= workers_salaries
        return f"You payed your workers. They are happy. " \
               f"Budget left: {self.__budget}"

    def tend_animals(self):
        animals_money_care = sum(a.money_for_care for a in self.animals)

        if animals_money_care > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_money_care
        return f"You tended all the animals. They are happy. " \
               f"Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = f"You have {len(self.animals)} animals\n"
        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        output += f"----- {len(lions)} Lions:\n" + '\n'.join(lions) + '\n'

        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        output += f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers) + '\n'

        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        output += f"----- {len(cheetahs)} Cheetahs:\n" + '\n'.join(cheetahs)

        return output

    def workers_status(self):

        output = f"You have {len(self.workers)} workers\n"
        keepers = [repr(w) for w in self.workers if isinstance(w, Keeper)]
        output += f"----- {len(keepers)} Keepers:\n" + '\n'.join(keepers) + '\n'

        caretakers = [repr(w) for w in self.workers if isinstance(w, Caretaker)]
        output += f"----- {len(caretakers)} Caretakers:\n" + '\n'.join(caretakers) + '\n'

        vets = [repr(w) for w in self.workers if isinstance(w, Vet)]
        output += f"----- {len(vets)} Vets:\n" + '\n'.join(vets)

        return output



