from OOP.EXAMS.April_2022.Medieval_Games.player import Player
from OOP.EXAMS.April_2022.Medieval_Games.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        players_names = []
        for player in players:
            if player in self.players:
                continue
            players_names.append(player.name)
            self.players.append(player)

        return f"Successfully added: {', '.join(players_names)}"

    def add_supply(self, *supplies: Supply):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in ["Food", "Drink"]:
            return
        if player_name not in [p.name for p in self.players]:
            return

        player = self.__find_player_by_name(player_name)
        index = self.__find_last_sustenance_by_type(sustenance_type)
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        player.stamina = min(player.stamina + self.supplies[index].energy, 100)
        supply = self.supplies.pop(index)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):

        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        output = ""
        for player in [first_player, second_player]:
            if player.stamina == 0:
                output += f"Player {player.name} does not have enough stamina.\n"

        if output:
            return output.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        second_player.stamina = max(second_player.stamina - first_player.stamina / 2, 0)
        if second_player.stamina == 0:
            winner = first_player
            return f"Winner: {winner.name}"

        first_player.stamina = max(first_player.stamina - second_player.stamina / 2, 0)
        if first_player.stamina == 0:
            winner = second_player
            return f"Winner: {winner.name}"

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        self.__reduce_stamina_by_age()

        for player in self.players:
            self.sustain(player.name, "Food")

        for player in self.players:
            self.sustain(player.name, "Drink")

    def __str__(self):
        output = "\n".join([str(x) for x in self.players]) + "\n" + "\n".join([x.details() for x in self.supplies])
        return output

    def __find_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def __find_last_sustenance_by_type(self, s_type):
        for index in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[index]
            if supply.__class__.__name__ == s_type:
                return index
        raise Exception(f"There are no {s_type.lower()} supplies left!")

    def __reduce_stamina_by_age(self):
        for player in self.players:
            reduce = player.age * 2
            player.stamina = max(player.stamina - reduce, 0)
