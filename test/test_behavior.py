import unittest
from unittest.mock import patch

from src.behavior import *


class TestHumanThinkerBehavior(unittest.TestCase):
    def setUp(self):
        self.instance = HumanThinkerBehavior()

    def test_is_instance(self):
        self.assertIsInstance(self.instance, HumanThinkerBehavior)

    @patch('builtins.input', return_value='1234')
    def test_think(self, input):
        self.instance.think()
        self.assertEqual(self.instance.my_number, '1234')

    @patch('builtins.input', return_value='2-1')
    def test_correct_digits(self, input):
        expected = [2, 1]
        obtained = self.instance.correct_digits()
        self.assertEqual(expected, obtained)

    @patch('builtins.input', return_value='entrada')
    def test_correct_digits_wrong_input(self, input):
        expected = [5, 0]
        obtained = self.instance.correct_digits()
        self.assertEqual(expected, obtained)

    def test_valid_response(self):
        self.assertTrue(self.instance.valid_response([1, 3]))
        self.assertFalse(self.instance.valid_response([4, 1]))
        self.assertTrue(self.instance.valid_response([0, 0]))


class TestHumanGuesserBehavior(unittest.TestCase):
    def setUp(self):
        self.instance = HumanGuesserBehavior()

    @patch('builtins.input', return_value='1234')
    def test_think(self, input):
        self.assertEqual(self.instance.think(), '1234')

    def test_analize(self):
        self.assertTrue(self.instance.analize([4, 0]))
        self.assertFalse(self.instance.analize([0, 2]))
        self.assertFalse(self.instance.analize([1, 5]))
        self.assertFalse(self.instance.analize([8, 2]))


class TestComputerThinkerBehavior(object):
    ,
