# from Animal import Animal
# from cheetah import Cheetah
# from keeper import Keeper
# from lion import Lion
# from tiger import Tiger
# from vet import Vet
# from worker import Worker
# from caretaker import Caretaker
#
#
# class Zoo:
#     def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
#         self.name = name
#         self.__budget = budget
#         self.__animal_capacity = animal_capacity
#         self.__workers_capacity = workers_capacity
#         self.animals = []
#         self.workers = []
#
#     def add_animal(self, animal: Animal, price):
#         if len(self.animals) >= self.__animal_capacity:
#             return "Not enough space for animal"
#         if self.__budget < price:
#             return "Not enough budget"
#         self.animals.append(animal)
#         self.__budget -= price
#         return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
#
#     def hire_worker(self, worker: Worker):
#         if len(self.workers) >= self.__workers_capacity:
#             return "Not enough space for worker"
#         self.workers.append(worker)
#         return f"{worker.name} the {worker.__class__.__name__} hired successfully"
#
#     def get_worker(self, worker_name):
#         for worker in self.workers:
#             if worker.name == worker_name:
#                 return worker
#
#     def fire_worker(self, worker_name):
#         worker = self.get_worker(worker_name)
#         if worker is None:
#             return f"There is no {worker_name} in the zoo"
#         self.workers.remove(worker)
#         return f"{worker_name} fired successfully"
#
#     def calc_workers_salaries(self):
#         total = 0
#         for worker in self.workers:
#             total += worker.salary
#         return total
#
#     def pay_workers(self):
#         worker_salaries_sum = self.calc_workers_salaries()
#         if self.__budget >= worker_salaries_sum:
#             self.__budget -= worker_salaries_sum
#             return f"You payed your workers. They are happy. Budget left: {self.__budget}"
#         return "You have no budget to pay your workers. They are unhappy"
#
#     def calc_animals_expenses(self):
#         total = 0
#         for animal in self.animals:
#             total += animal.money_for_care
#         return total
#
#     def tend_animals(self):
#         animals_expenses_sum = self.calc_animals_expenses()
#         if self.__budget >= animals_expenses_sum:
#             self.__budget -= animals_expenses_sum
#             return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
#
#     def profit(self, amount):
#         self.__budget += amount
#
#     def get_animals_by_type(self, animal_type: str):
#         animals_of_given_type = []
#         for animal in self.animals:
#             if animal.__class__.__name__ == animal_type:
#                 animals_of_given_type.append(animal)
#         return animals_of_given_type
#
#     def animals_status(self):
#         output = [f"You have {len(self.animals)} animals"]
#
#         animals_of_type_lion = self.get_animals_by_type('Lion')
#         output.append(f'----- {len(animals_of_type_lion)} Lions:')
#         for animal in animals_of_type_lion:
#             output.append(str(animal))
#
#         animals_of_type_tigers = self.get_animals_by_type('Tiger')
#         output.append(f'----- {len(animals_of_type_tigers)} Tigers:')
#         for animal in animals_of_type_tigers:
#             output.append(str(animal))
#
#         animals_of_type_cheetahs = self.get_animals_by_type('Cheetah')
#         output.append(f'----- {len(animals_of_type_cheetahs)} Cheetahs:')
#         for animal in animals_of_type_cheetahs:
#             output.append(str(animal))
#
#         return '\n'.join(output)
#
#     def get_workers_by_type(self, worker_type: str):
#         workers_of_given_type = []
#         for worker in self.workers:
#             if worker.__class__.__name__ == worker_type:
#                 workers_of_given_type.append(worker)
#         return workers_of_given_type
#
#     def workers_status(self):
#         output = [f"You have {len(self.workers)} workers"]
#
#         workers_of_type_keepers = self.get_workers_by_type('Keeper')
#         output.append(f'----- {len(workers_of_type_keepers)} Keepers:')
#         for worker in workers_of_type_keepers:
#             output.append(str(worker))
#
#         workers_of_type_caretakers = self.get_workers_by_type('Caretaker')
#         output.append(f'----- {len(workers_of_type_caretakers)} Caretakers:')
#         for worker in workers_of_type_caretakers:
#             output.append(str(worker))
#
#         workers_of_type_vets = self.get_workers_by_type('Vet')
#         output.append(f'----- {len(workers_of_type_vets)} Vets:')
#         for worker in workers_of_type_vets:
#             output.append(str(worker))
#
#         return '\n'.join(output)
#
#
# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
