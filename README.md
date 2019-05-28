# EVentbrite - PythonMind

Adaptación del juego Mastermind o "Mente Maestra", realizada en python 3.

El jugador "Pensador" debe ingresar un número de 4 dígitos distintos de 0-9

El jugador "Adivinador" Intenta adivinar el numero

Por cada intento válido el Jugador Pensador debe responder que tan cerca esta del número correcto respondiendo:
 * [# G] Por cada número correcto en posición correcta.
 * [# R] Por cada número correcto en posicion incorrecta.

El juego termina una vez se haya adivinado el número de forma correcta

## Uso
    Para iniciar la aplicacion se debe localizar el archivo de inicio `src/game.py`

    Y el comando de inicio es el siguiente

        *Si se tiene python3 en PATH: `python3 game.py`

## Control
    Los controles son:
        1- Digitos de 0-9

## Testeo
    Para correr los test nos ubicamos en el directorio raíz de la aplicación y utilizamos el siguiente comando:
        `python3 -m unittest discover`
