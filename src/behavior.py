#!/usr/bin/python3

import random
from console import Console


class GenericBehavior(object):
    def __init__(self):
        self.console_manager = Console()

    def convert_to(self, number_to_convert):
        response = [int(x) for x in number_to_convert]
        return response

    def is_valid_number(self, number_guessed):
        unique_values = []
        converted_guess = self.convert_to(number_guessed)
        for value in converted_guess:
            if value not in unique_values:
                unique_values.append(value)
        return len(number_guessed) == 4 and len(unique_values) == 4

    def think(self):
        pass

    def analize(self, response):
        pass


class HumanThinkerBehavior(GenericBehavior):
    """docstring for HumanBehavior"""

    def __init__(self):
        super().__init__()
        self.my_number = None

    def think(self):
        while True:
            number_thinked = self.console_manager.handle_input("Ingrese el número pensado: ")
            if self.is_valid_number(number_thinked):
                self.my_number = number_thinked
                break
            else:
                self.console_manager.print_out("Número no Válido. Pruebe Nuevamente")

    def analize(self, response):
        digits = []
        self.console_manager.print_out("Numero adivinado: {}".format(response))
        digits = self.correct_digits()
        return digits

    def correct_digits(self):
        digit_input = self.console_manager.handle_input("Ingrese la respuesta [G-R]: ")
        response = self.convert_to(digit_input.split('-'))
        return response


class HumanGuesserBehavior(GenericBehavior):
    def __init__(self):
        super().__init__()
        self.my_guess = None

    def think(self):
        while True:
            number_guessed = self.console_manager.handle_input("Ingrese el número a probar: ")
            if self.is_valid_number(number_guessed):
                self.my_guess = number_guessed
                return self.my_guess
            else:
                self.console_manager.print_out("Número no Válido. Pruebe Nuevamente")

    def analize(self, response):
        self.console_manager.print_out("Respuesta [G: {0} // R: {1}]".format(*response))
        if response[0] == 4:
            return True


class GenericComputerBehavior(GenericBehavior):
    """docstring for GenericComputerBehavior"""

    def __init__(self):
        super(GenericComputerBehavior, self).__init__()

    def verificate(self, my_number, other_number):
        converted_number = self.convert_to(other_number)
        result = [0, 0]
        print('{} {}'.format(my_number, converted_number))
        for i in range(0, 4):
            if converted_number[i] == my_number[i]:
                result[0] += 1
            else:
                if converted_number[i] in my_number:
                    result[1] += 1
        return(result)


class ComputerThinkerBehavior(GenericComputerBehavior):
    def __init__(self):
        super().__init__()
        self.my_number = None

    def think(self):
        numbers = [x for x in range(0, 10)]
        selected_numbers = []
        while len(selected_numbers) < 4:
            new_number = self.select_number(numbers)
            selected_numbers.append(new_number)
            numbers.remove(new_number)
        self.my_number = selected_numbers

    def select_number(self, numbers):
        chosen = random.choice(numbers)
        return chosen

    def analize(self, response):
        return self.verificate(self.my_number, response)


class ComputerGuesserBehavior(GenericComputerBehavior):
    def __init__(self):
        super().__init__()
        self.is_first_guess = True
        self.guess_history = []
        self.response_history = []

    def think(self):
        print(self.guess_history)
        print(self.response_history)
        if self.is_first_guess:
            self.is_first_guess = False
            self.last_valid_guess = '0123'
        else:
            my_guess = self.do_guesses()
            self.last_valid_guess = my_guess
        self.guess_history.append(self.convert_to(my_guess))
        return self.last_valid_guess

    def do_guesses(self):
        last_guess = int(self.last_valid_guess)
        while True:
            last_guess = '{:0>4}'.format(int(last_guess) + 1)
            if self.is_valid_number(last_guess):
                if self.try_with(last_guess):
                    return last_guess

    def try_with(self, last_guess):
        for i in range(len(self.guess_history)):
            response = self.verificate(self.guess_history[i], last_guess)
            if response != self.response_history[i]:
                return False
        return True

    def analize(self, response):
        self.response_history.append(response)
        if response[0] == 4:
            return True
        return False
