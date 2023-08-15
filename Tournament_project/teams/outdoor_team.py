from Tournament_project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    BUDGET = 1000.0
    ADVANTAGE_POINTS_INCREASE = 115

    def __init__(self, name: str, country: str, advantage: int,):
        super().__init__(name, country, advantage, budget=OutdoorTeam.BUDGET)

    def win(self):
        self.advantage += OutdoorTeam.ADVANTAGE_POINTS_INCREASE
        self.wins += 1
