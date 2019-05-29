import unittest

from src.players import HumanPlayer, ComputerPlayer
from src.behavior import *


class TestHumanPlayer(unittest.TestCase):
    def test_instanciate(self):
        behavior = HumanThinkerBehavior()
        self.instance = HumanPlayer(behavior)
        self.assertIsInstance(self.instance, HumanPlayer)


class TestComputerPlayer(unittest.TestCase):
    def test_instanciate(self):
        behavior = ComputerThinkerBehavior()
        self.instance = ComputerPlayer(behavior)
        self.assertIsInstance(self.instance, ComputerPlayer)
