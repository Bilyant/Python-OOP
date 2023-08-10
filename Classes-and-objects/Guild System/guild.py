from player import Player

w
class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def get_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player = self.get_player(player_name)
        if player not in self.players:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player)
        player.guild = 'Unaffiliated'
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        output = [f"Guild: {self.name}"]
        for player in self.players:
            output.append(player.player_info())
        return '\n'.join(output)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
