import unittest
from main import (
    crear_sequencia,
    numeros_senars_majors,
    primera_posicio,
    diagonal_principal
)

class TestFuncions(unittest.TestCase):

    def test_crear_sequencia(self):
        self.assertEqual(crear_sequencia(1, 5), [1, 2, 3, 4, 5])

    def test_crear_sequencia_error(self):
        self.assertEqual(crear_sequencia(5, 1), [])

    def test_numeros_senars_majors(self):
        self.assertEqual(
            numeros_senars_majors([1, 3, 5, 7, 8], 4),
            [5, 7]
        )

    def test_primera_posicio(self):
        self.assertEqual(
            primera_posicio(["a", "b", "c"], "b"),
            1
        )

    def test_diagonal_principal(self):
        matriu = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(diagonal_principal(matriu), [1, 4])


if __name__ == '__main__':
    unittest.main()