#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src.console import Console
from src.factory import *


class Game(object):
    """docstring for Game"""

    def __init__(self):
        super(Game, self).__init__()
        self.console_manager = Console()
        self.factory = None
        self.thinker = None
        self.guesser = None

    def mainloop(self):
        game_end = False
        self.thinker.think()
        while not game_end:
            number_guessed = self.guesser.think()
            thinker_response = self.thinker.analize(number_guessed)
            game_end = self.guesser.analize(thinker_response)
        self.console_manager.print_out("El número correcto es {}".format(number_guessed))

    def game_initialize(self):
        game_initializated = False
        while not game_initializated:
            self.console_manager.print_menu()
            game_type = int(self.console_manager.handle_input("Elija el modo de juego: "))
            if game_type == 1:
                self.factory = PcVsHumanFactory()
                game_initializated = True
            elif game_type == 2:
                self.factory = HumanVsPcFactory()
                game_initializated = True
            else:
                self.console_manager.print_out("Opción no válida // ")
        self.thinker = self.factory.give_thinker_player()
        self.guesser = self.factory.give_guesser_player()


def main():
    game = Game()
    game.game_initialize()
    game.mainloop()


if __name__ == '__main__':
    main()
