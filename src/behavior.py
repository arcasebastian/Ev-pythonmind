import random
from console import Console


class GenericBehavior:
    def __init__(self):
        self.console_manager = Console()

    def think(self):
        pass

    def guess(self):
        pass

    def verificate(self, number_guessed):
        pass

    def convert_to(self, number_to_convert):
        response = [int(x) for x in number_to_convert]
        return response

    def convert_from(self, list_to_convert):
        response = '{}'.format(*list_to_convert)
        return int(response)

    def is_valid_number(self, number_guessed):
        unique_values = []
        converted_guess = self.convert_to(number_guessed)
        for value in converted_guess:
            if value not in unique_values:
                unique_values.append(value)
        return len(number_guessed) == 4 and len(unique_values) == 4


class HumanBehavior(GenericBehavior):
    """docstring for HumanBehavior"""

    def __init__(self):
        super().__init__()
        self.final_guess = None

    def guess(self):
        self.console_manager.print_out("Ingrese el número a probar: ")
        while True:
            number_guessed = self.console_manager.handle_input()
            if self.is_valid_number(number_guessed):
                self.final_guess = number_guessed
                return self.final_guess
            else:
                self.console_manager.print_out("Número no Válido. Pruebe Nuevamente")

    def think(self):
        self.console_manager.print_out("Ingrese el número pensado")
        while True:
            number_thinked = self.console_manager.handle_input()
            if self.is_valid_number(number_thinked):
                self.final_number = number_thinked
                self.final_number
                break
            else:
                self.console_manager.print_out("Número no Válido. Pruebe Nuevamente")

    def verificate(self, number_guessed):
        response = []
        converted_guess = self.convert_to(number_guessed)
        self.console_manager.print_out("Numero adivinado: {0}{1}{2}{3}".format(*converted_guess))
        response.append(self.correct_digits('G'))
        response.append(self.correct_digits('R'))
        return response

    def correct_digits(self, symbol):
        self.console_manager.print_out("Cuantos digitos son {}:".format(symbol))
        digit_input = self.console_manager.handle_input()
        return int(digit_input)

    def analize(self, response):
        self.console_manager.print_out("Respuesta [G: {0} // R: {1}]".format(*response))
        if response[0] == 4:
            return True


class ComputerBehavior(GenericBehavior):
    def __init__(self):
        super().__init__()
        self.final_number = None
        self.is_first_guess = True
        self.guess_history = []
        self.response_history = []

    def think(self):
        numbers = [x for x in range(0, 10)]
        selected_numbers = []
        while len(selected_numbers) < 4:
            new_number = self.select_number(numbers)
            selected_numbers.append(new_number)
            numbers.remove(new_number)
        self.final_number = selected_numbers

    def select_number(self, numbers):
        chosen = random.choice(numbers)
        return chosen

    def verificate(self, number_guessed):
        converted_guess = self.convert_to(number_guessed)
        result = [0, 0]
        for i in range(0, 4):
            if converted_guess[i] == self.final_number[i]:
                result[0] += 1
            else:
                if converted_guess[i] in self.final_number:
                    result[1] += 1
        return(result)

    def guess(self):
        if self.is_first_guess:
            self.is_first_guess = False
            final_guess = '0123'
            self.last_valid_guess = final_guess
        else:
            final_guess = self.do_guesses()
            self.last_valid_guess = final_guess
        self.guess_history.append(self.convert_to(final_guess))
        return final_guess

    def do_guesses(self):
        last_guess = int(self.last_valid_guess)
        while True:
            last_guess = '{:0>4}'.format(int(last_guess) + 1)
            if self.is_valid_number(last_guess):
                if self.try_with(last_guess):
                    return last_guess

    def try_with(self, last_guess):
        for i in range(len(self.guess_history)):
            self.final_number = self.guess_history[i]
            response = self.verificate(last_guess)
            if response != self.response_history[i]:

                return False
        return True

    def analize(self, response):
        self.response_history.append(response)
        if response[0] == 4:
            return True
        return False
