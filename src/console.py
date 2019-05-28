class Console(object):
    __instance = None

    def __new__(cls):
        if Console.__instance is None:
            Console.__instance = object.__new__(cls)
        return Console.__instance

    def print_menu(self):
        print("===== Menu =====")
        print("PC-Humano (Modo Único)")

    def handle_input(self):
        human_input = input()
        return human_input

    def print_out(self, text):
        print(text)
