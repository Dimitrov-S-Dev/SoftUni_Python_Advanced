from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class Fly(ABC):
    @staticmethod
    @abstractmethod
    def fly():
        pass


class Walkable(ABC):
    @staticmethod
    @abstractmethod
    def walk():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"


class RobotDuck(Duck, Walkable, Fly):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


"""

from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    def quack():
        pass

    @staticmethod
    def walk():
        pass

    @staticmethod
    def fly():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"

    @staticmethod
    def walk():
        ---Rubber duck can walk only if you move ---
        raise Exception('I cannot walk by myself')

    @staticmethod
    def fly():
        ---Rubber duck can fly only if you throw it---
        - ('I cannot fly by myself')-


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        ---can only fly to specific height but
        when it reaches it starts landing automatically---
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
        self.height += 1
    def land(self):
        self.height = 0

"""