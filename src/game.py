#!/usr/bin/python3
# -*- coding: utf-8 -*-

from players import *
from console import Console


class Game(object):
    """docstring for Game"""

    def __init__(self):
        super(Game, self).__init__()
        self.console_manager = Console()
        self.thinker = None
        self.guesser = None

    def mainloop(self):
        game_end = False
        self.game_initialize()
        self.thinker.think_number()
        while not game_end:
            number_guessed = self.guesser.guess_number()
            thinker_response = self.thinker.verificate_number(number_guessed)
            game_end = self.guesser.analize_response(thinker_response)
        self.console_manager.print_out("El número correcto es {}".format(number_guessed))

    def game_initialize(self):
        game_initializated = False
        while not game_initializated:
            self.console_manager.print_menu()
            game_type = int(self.console_manager.handle_input())
            if game_type == 1:
                self.thinker = ComputerPlayer()
                self.guesser = HumanPlayer()
                game_initializated = True
            elif game_type == 2:
                self.thinker = HumanPlayer()
                self.guesser = ComputerPlayer()
                game_initializated = True
            else:
                self.console_manager.print_out("Opción no válida // ")

    def is_correct(self, response):
        if response[0] == 4:
            return True
        return False


def main():
    game = Game()
    game.mainloop()


if __name__ == '__main__':
    main()
