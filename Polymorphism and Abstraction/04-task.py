class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    """Each person could be represented by their names, separated by a single space."""

    def __repr__(self):
        return f'{self.name} {self.surname}'

    """ When you concatenate two people, you should return a new instance of a person who will take 
        the first name from the first person and the surname from the second person."""

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: []):
        self.name = name
        self.people = people

    """When you access the length of a group instance, you should receive the total number of people in the group."""

    def __len__(self):
        return len(self.people)

    """When you concatenate two groups, you should return a new instance of a group which will have 
    a name -string in the format "{first_name} {second_name}" and all the people in the two groups 
    will participate in the new one too."""

    def __add__(self, other):
        return Group(name=f'{self.name} {other.name}', people=self.people + other.people)

    """Each group should be represented in the format 
        "Group {name} with members {members' names separated by comma and space}"""

    def __repr__(self):
        members = ', '.join([str(p) for p in self.people])
        return f'Group {self.name} with members {members}'

    """You could iterate over a group, and each person (element of the group) should be represented 
        in the format "Person {index}: {person's name}"""

    def __getitem__(self, idx):
        return f'Person {idx}: {str(self.people[idx])}'


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
