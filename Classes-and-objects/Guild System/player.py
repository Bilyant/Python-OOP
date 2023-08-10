class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}  # skills of each player and its mana cost
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        output = [
            f"Name: {self.name}",
            f"Guild: {self.guild}",
            f"HP: {self.hp}",
            f"MP: {self.mp}",
                  ]
        for skill_name, skill_mana_cost in self.skills.items():
            output.append(f"==={skill_name} - {skill_mana_cost}")

        return '\n'.join(output) + '\n'
