import unittest
import io
import sys


from src.console import Console


class TestConsole(unittest.TestCase):

    def test_console_instanciate(self):
        instance = Console()
        self.assertIsInstance(instance, Console, 'No se pudo instanciar la consola')

    def test_console_is_single_instance(self):
        console_one = Console()
        console_two = Console()

        self.assertEqual(console_one, console_two, "No son misma instancia")

    def test_print_out(self):
        expected_output = "Prueba de salida\n"
        console = Console()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        console.print_out("Prueba de salida")
        sys.stdout = sys.__stdout__
        self.assertEqual(expected_output, capturedOutput.getvalue())
