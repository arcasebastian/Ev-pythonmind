import unittest
from src.factory import PcVsHumanFactory, HumanVsPcFactory
from src.players import *


class TestPcVsHumanFactory(unittest.TestCase):

    def setUp(self):
        self.factory_instance = PcVsHumanFactory()

    def test_factory_instanciate(self):
        self.assertIsInstance(self.factory_instance, PcVsHumanFactory, 'No se pudo instanciar PcVsHuman')

    def test_give_thinker(self):
        thinker = self.factory_instance.give_thinker_player()
        self.assertIsInstance(thinker, ComputerPlayer, 'No es una instacia de ComputerPlayer')

    def test_give_guesser(self):
        guesser = self.factory_instance.give_guesser_player()
        self.assertIsInstance(guesser, HumanPlayer, 'No es una instacia de HumanPlayer')


class TestHumanVsPcFactory(unittest.TestCase):
    def setUp(self):
        self.factory_instance = HumanVsPcFactory()

    def test_factory_instanciate(self):
        self.assertIsInstance(self.factory_instance, HumanVsPcFactory, 'No se pudo instanciar PcVsHuman')

    def test_give_thinker(self):
        thinker = self.factory_instance.give_thinker_player()
        self.assertIsInstance(thinker, HumanPlayer, 'No es una instacia de HumanPlayer')

    def test_give_guesser(self):
        guesser = self.factory_instance.give_guesser_player()
        self.assertIsInstance(guesser, ComputerPlayer, 'No es una instacia de ComputerPlayer')
