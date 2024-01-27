from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        """
        Adds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}".
        Remember to change the player's guild in the player class.
        If he is already in the guild, returns "Player {player_name} is already in the guild."
        If the player is in another guild, returns "Player {player_name} is in another guild."
        """
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        self.players.append(player)
        player.guild = self.name
        return f'\nWelcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        """
        Removes the player from the guild and returns "Player {player_name} has been removed from the guild."
        Remember to change the player's guild in the player class to "Unaffiliated".
        If there is no such player in the guild, returns "Player {player_name} is not in the guild."
        """
        player_to_remove = [p for p in self.players if p.name == player_name]
        if player_to_remove not in self.players:
            return f'Player {player_name} is not in the guild.'
        self.players.remove(player_to_remove)
        player_to_remove.guild = 'Unaffiliated'
        return f'Player {player_name} has been removed from the guild.'

    def guild_info(self):
        """
        :return:
        "Guild: {guild_name}
        {first_player's info}
        {Nth-player's info}"
        """
        result = [f'Guild: {self.name}']
        for pl in self.players:
            result.append(pl.player_info())
        return '\n'.join(result)
