import players
import console


def is_correct(response):
    if response[0] == 4:
        return True
    return False


thinker = players.ComputerPlayer()
guesser = players.HumanPlayer()
console_manager = console.Console()

console_manager.print_menu()
thinker.think_number()
gameend = False
while not gameend:
    number_guessed = guesser.guess_number()
    thinker_response = thinker.verificate_number(number_guessed)
    gameend = is_correct(thinker_response)
    console_manager.print_out("Respuesta [G: {0} // R: {1}]".format(*thinker_response))
console_manager.print_out("//Juego Terminado//")
