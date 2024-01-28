from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    """
    If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) 
    to the animals' list, reduce the budget, and return 
    "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
    If you have the capacity, but no budget, return "Not enough budget"
    In any other case, you do not have space, and you should return "Not enough space for animal"
    """
    def add_animal(self, animal: Animal, price):
        if self.budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.budget -= price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        if self.budget < price and len(self.animals) < self.__animal_capacity:
            return 'Not enough budget'
        return 'Not enough space for animal'

    """
    If you have not exceeded the capacity of workers in the zoo for the worker 
    (instance of Keeper/Caretaker/Vet), add him to the workers and return 
    "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
    Otherwise, return "Not enough space for worker"
    """
    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    """
    If there is a worker with that name in the workers' list, remove him and return 
    "{worker_name} fired successfully"
    Otherwise, return "There is no {worker_name} in the zoo"
    """
    def fire_worker(self, worker_name):
        worker_to_fire = None
        try:
            worker_to_fire = [w for w in self.workers if w.name == worker_name][0]
        except IndexError:
            return f'There is no {worker_name} in the zoo'
        self.workers.remove(worker_to_fire)
        return f'{worker_name} fired successfully'

    """
    If you have enough budget to pay the workers (sum their salaries) pay them and return 
    "You payed your workers. They are happy. Budget left: {left_budget}"
    Otherwise, return "You have no budget to pay your workers. They are unhappy"
    """
    def pay_workers(self):
        workers_salaries = sum([w.salary for w in self.workers])
        if self.budget >= workers_salaries:
            self.budget -= workers_salaries
            return f'You payed your workers. They are happy. Budget left: {self.budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    """	
    If you have enough budget to take care of the animals, reduce the budget and return 
    "You tended all the animals. They are happy. Budget left: {left_budget}"
    Otherwise, return "You have no budget to tend the animals. They are unhappy."
    """
    def tend_animals(self):
        tending_animals_sum = sum([a.money_for_care for a in self.animals])
        if self.budget >= tending_animals_sum:
            self.budget -= tending_animals_sum
            return f'You tended all the animals. They are happy. Budget left: {self.budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    """
    Increase the budget with the given amount of profit
    """
    def profit(self, amount):
        self.budget += amount

    """
      Returns:
      "You have {total_animals_count} animals
      ----- {amount_of_lions} Lions:
      {lion1}
      …
      {lionN}
      ----- {amount_of_tigers} Tigers:
      {tiger1}
      …
      {tigerN}
      ----- {amount_of_cheetahs} Cheetahs:
      {cheetah1}
      …
      {cheetahN}"
      """
    def animals_status(self):
        result = [f'You have {len(self.animals)} animals']
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        all_animals = [lions, tigers, cheetahs]
        for a_group in all_animals:
            result.append(f'----- {len(a_group)} {a_group[0].__class__.__name__}s:')
            for a in a_group:
                result.append(repr(a))
        return '\n'.join(result)

    """
    Returns:
    "You have {total_workers_count} workers
    ----- {amount_of_keepers} Keepers:
    {keeper1}
    …
    {keeperN}
    ----- {amount_of_caretakers} Caretakers:
    {caretaker1}
    …
    {caretakerN}
    ----- {amount_of_vets} Vets:
    {vet1}
    …
    {vetN}"
    """
    def workers_status(self):
        result = [f'You have {len(self.workers)} workers']
        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']
        all_workers = [keepers, caretakers, vets]
        for w_group in all_workers:
            result.append(f'----- {len(w_group)} {w_group[0].__class__.__name__}s:')
            for w in w_group:
                result.append(repr(w))
        return '\n'.join(result)
