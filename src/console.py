#!/usr/bin/python3


class Console(object):
    __instance = None

    def __new__(cls):
        if Console.__instance is None:
            Console.__instance = object.__new__(cls)
        return Console.__instance

    def print_menu(self):
        print("===== Menu =====")
        print("1 - PC-Humano")
        print("2 - Humano-PC")

    def handle_input(self, prompt):
        human_input = input(prompt)
        return human_input

    def print_out(self, text):
        print(text)
