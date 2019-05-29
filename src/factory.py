from src.behavior import *
from src.players import *


class AbstractFactory(object):
    """docstring for AbstractFactory"""

    def __init__(self):
        super(AbstractFactory, self).__init__()

    def give_thinker_player(self):
        pass

    def give_guesser_player(self):
        pass


class PcVsHumanFactory(AbstractFactory):
    """docstring for PcVsHumanFactory"""

    def __init__(self):
        super(PcVsHumanFactory, self).__init__()

    def give_thinker_player(self):
        behavior = ComputerThinkerBehavior()
        return ComputerPlayer(behavior)

    def give_guesser_player(self):
        behavior = HumanGuesserBehavior()
        return HumanPlayer(behavior)


class HumanVsPcFactory(AbstractFactory):
    """docstring for PcVsHumanFactory"""

    def __init__(self):
        super(HumanVsPcFactory, self).__init__()

    def give_thinker_player(self):
        behavior = HumanThinkerBehavior()
        return HumanPlayer(behavior)

    def give_guesser_player(self):
        behavior = ComputerGuesserBehavior()
        return ComputerPlayer(behavior)
