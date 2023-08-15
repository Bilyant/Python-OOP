from Tournament_project.equipment.elbow_pad import ElbowPad
from Tournament_project.equipment.knee_pad import KneePad
from Tournament_project.teams.indoor_team import IndoorTeam
from Tournament_project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = ['KneePad', 'ElbowPad']
    TEAM_TYPES = ['OutdoorTeam', 'IndoorTeam']

    EQUIPMENT_CLASSES = {
        'KneePad': KneePad,
        'ElbowPad': ElbowPad,
    }
    TEAM_CLASSES = {
        'OutdoorTeam': OutdoorTeam,
        'IndoorTeam': IndoorTeam,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in Tournament.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        new_equipment = Tournament.EQUIPMENT_CLASSES.get(equipment_type)()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in Tournament.TEAM_TYPES:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        new_team = Tournament.TEAM_CLASSES.get(team_type)(team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def get_team(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team

    def get_equipment(self, equipment_type):
        current_equipment = []
        for equipment in self.equipment:
            current_equipment.append(equipment)

        while current_equipment:
            last_equipment = current_equipment.pop()
            if last_equipment.__class__.__name__ == equipment_type:
                return last_equipment

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self.get_team(team_name)
        equipment = self.get_equipment(equipment_type)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.get_team(team_name)
        if team is None:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0

        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    @staticmethod
    def sum_protection(team_equipment):
        equipment_points = 0
        for equipment in team_equipment:
            equipment_points += equipment.protection
        return equipment_points

    def play(self, team_name1: str, team_name2: str):
        first_team = self.get_team(team_name1)
        second_team = self.get_team(team_name2)

        if first_team.__class__.__name__ != second_team.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        first_team_points = first_team.advantage + self.sum_protection(first_team.equipment)
        second_team_points = second_team.advantage + self.sum_protection(second_team.equipment)

        if first_team_points == second_team_points:
            return "No winner in this game."

        winner_team = first_team if first_team_points > second_team_points else second_team
        winner_team.win()
        return f"The winner is {winner_team.name}."

    def get_statistics(self, ):
        teams = sorted(self.teams, key=lambda x: -x.wins)
        output = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]

        for team in teams:
            output.append(team.get_statistics())

        return '\n'.join(output)
