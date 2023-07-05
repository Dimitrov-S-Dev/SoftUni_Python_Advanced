class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        output = f"Player: {self.name}\n"
        output += f"Sprint: {self.__sprint}\n"
        output += f"Dribble: {self.__dribble}\n"
        output += f"Passing: {self.__passing}\n"
        output += f"Shooting: {self.__shooting}"

        return output
