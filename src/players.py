from behavior import *


class GenericPlayer:
    def __init__(self):
        self.behavior = None

    def guess_number(self):
        return self.behavior.guess()

    def think_number(self):
        return self.behavior.think()

    def verificate_number(self, guessed_number):
        return self.behavior.verificate(guessed_number)


class HumanPlayer(GenericPlayer):
    def __init__(self):
        super().__init__()
        self.behavior = HumanBehavior()


class ComputerPlayer(GenericPlayer):
    def __init__(self):
        super().__init__()
        self.behavior = ComputerBehavior()
