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

    def is_valid_number(self, number_guessed):
        unique_values = []
        converted_guess = self.convert_to(number_guessed)
        for value in converted_guess:
            if value not in unique_values:
                unique_values.append(value)
        return len(unique_values) == 4


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
                return self.final_number
            else:
                self.console_manager.print_out("Número no Válido. Pruebe Nuevamente")

    def verificate(self, number_guessed):
        self.console_manager.print_out("Numero pensado: {0}{1}{2}{3}".format(*number_guessed))


class ComputerBehavior(GenericBehavior):
    def __init__(self):
        super().__init__()
        self.final_number = None

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
