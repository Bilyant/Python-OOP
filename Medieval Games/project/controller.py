from player import Player
from supply.drink import Drink
from supply.food import Food


class Controller:
    ALLOWED_SUSTENANCE_TYPES = ['Food', 'Drink']

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added_players = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return 'Successfully added: ' + ', '.join(added_players)

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def get_player(self, player_name: str, obj: []):
        for player in obj:
            if player.name == player_name:
                return player

    def get_supplies_count_by_type(self, supply_type: str, obj: []):
        supplies = []
        for supply in obj:
            if supply.__class__.__name__ == supply_type:
                supplies.append(supply)
        return supplies

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.get_player(player_name, self.players)

        if sustenance_type not in Controller.ALLOWED_SUSTENANCE_TYPES:
            return

        if player not in self.players:
            return

        if player.stamina == Player.STAMINA_MAX_VALUE:
            return f"{player_name} have enough stamina."

        if sustenance_type == 'Food':
            supplies_left = self.get_supplies_count_by_type('Food', self.supplies)
            if supplies_left is None:
                raise Exception("There are no food supplies left!")

        if sustenance_type == 'Drink':
            supplies_left = self.get_supplies_count_by_type('Drink', self.supplies)
            if supplies_left is None:
                raise Exception("There are no drink supplies left!")

        supply = self.supplies.pop()
        player.stamina = min(player.stamina + supply.energy, 100)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.get_player(first_player_name, self.players)
        second_player = self.get_player(second_player_name, self.players)
        lower_stamina_player = first_player if first_player.stamina < second_player.stamina else second_player
        higher_stamina_player = first_player if first_player.stamina > second_player.stamina else second_player

        if first_player.stamina == Player.STAMINA_MIN_VALUE and second_player.stamina == Player.STAMINA_MIN_VALUE:
            output = [f"Player {first_player.name} does not have enough stamina.",
                      f"Player {second_player.name} does not have enough stamina."]
            return '\n'.join(output)

        if first_player.stamina == Player.STAMINA_MIN_VALUE:
            return f"Player {first_player.name} does not have enough stamina."

        if second_player.stamina == Player.STAMINA_MIN_VALUE:
            return f"Player {second_player.name} does not have enough stamina."

        higher_stamina_player.stamina = max(higher_stamina_player.stamina - lower_stamina_player.stamina / 2, 0)
        if higher_stamina_player.stamina == 0:
            winner = lower_stamina_player.name
            return f"Winner: {winner.name}"

        lower_stamina_player.stamina = max(lower_stamina_player.stamina - higher_stamina_player.stamina / 2, 0)
        if lower_stamina_player.stamina == 0:
            winner = higher_stamina_player.name
            return f"Winner: {winner.name}"

        winner = first_player if second_player.stamina < first_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        output = []
        for player in self.players:
            output.append(str(player))
        for supply in self.supplies:
            output.append(supply.details())
        return '\n'.join(output)


controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)
