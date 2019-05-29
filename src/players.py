#!/usr/bin/python3


class GenericPlayer(object):
    def __init__(self):
        self.behavior = None

    def think(self):
        return self.behavior.think()

    def analize(self, response):
        return self.behavior.analize(response)


class HumanPlayer(GenericPlayer):
    def __init__(self, behavior):
        super().__init__()
        self.behavior = behavior


class ComputerPlayer(GenericPlayer):
    def __init__(self, behavior):
        super().__init__()
        self.behavior = behavior
