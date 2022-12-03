import math
import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class PruebaEcuacionSegundoGrado(unittest.TestCase):
    def test_solucionESG_parametrosNumericos_raicesReales(self):
        # Arrange
        ecuacionSegundoGrado=EcuacionSegundoGrado()
        parametroA = 3
        parametroB = -5
        parametroC = 1

        RaizEsperada1 = "1.43"
        RaizEsperada2 = "0.23"

        # Do
        ecuacionSegundoGrado.definirParametros(parametroA, parametroB, parametroC)
        RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()

        # Assert
        self.assertEqual(RaizEsperada1, RaizActual1)
        self.assertEqual(RaizEsperada2, RaizActual2)

    def test_solucionESG_parametrosNumericos_raicesComplejasConjugadas(self):
        # Arrange
        ecuacionSegundoGrado = EcuacionSegundoGrado()
        parametroA = 1
        parametroB = 2
        parametroC = 3

        RaizEsperada1 = "-1.00+1.41i"
        RaizEsperada2 = "-1.00-1.41i"

        # Do
        ecuacionSegundoGrado.definirParametros(parametroA, parametroB, parametroC)
        RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()

        # Assert
        self.assertEqual(RaizEsperada1, RaizActual1)
        self.assertEqual(RaizEsperada2, RaizActual2)

    def test_solucionESG_parametrosNoNumericos_lanzaException(self):
        # Arrange
        ecuacionSegundoGrado = EcuacionSegundoGrado()

        # Assert
        self.assertTrue(True)
        with self.assertRaises(ValueError):
            ecuacionSegundoGrado.definirParametros("3.1", "5.2", "c")

    def test_solucionESG_parametrosNumericos_raicesReales_subTest(self):
        # Arrange
        ecuacionSegundoGrado=EcuacionSegundoGrado()

        items = (
            {"Case": "Caso 01", "a": 3, "b": -5, "c": 1, "RaizEsperada1": "1.43", "RaizEsperada2": "0.23"},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 1, "RaizEsperada1": "-1.00", "RaizEsperada2": "-1.00"},
            {"Case": "Caso 03", "a": -1, "b": 2, "c": -1, "RaizEsperada1": "1.00", "RaizEsperada2": "1.00"},
            {"Case": "Caso 04", "a": 1, "b": 0, "c": -18, "RaizEsperada1": "4.24", "RaizEsperada2": "-4.24"},
            {"Case": "Caso 05", "a": 1, "b": 4, "c": 0, "RaizEsperada1": "0.00", "RaizEsperada2": "-4.00"},
            {"Case": "Caso 06", "a": 1, "b": 4, "c": 4, "RaizEsperada1": "-2.00", "RaizEsperada2": "-2.00"},
            {"Case": "Caso 07", "a": 1, "b": 3, "c": 2, "RaizEsperada1": "-1.00", "RaizEsperada2": "-2.00"},
        )

        # Do
        for item in items:
            with self.subTest(item["Case"]):
                ecuacionSegundoGrado.definirParametros(item["a"], item["b"], item["c"])
            RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()

            # Assert
            self.assertEqual(item["RaizEsperada1"], RaizActual1)
            self.assertEqual(item["RaizEsperada2"], RaizActual2)

    def test_solucionESG_parametrosNumericos_raicesComplejasConjugadas_subTest(self):
        # Arrange
        ecuacionSegundoGrado=EcuacionSegundoGrado()

        items = (
            {"Case": "Caso 01", "a": 1, "b": 1, "c": 1, "RaizEsperada1": "-0.50+0.87i", "RaizEsperada2": "-0.50-0.87i"},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 3, "RaizEsperada1": "-1.00+1.41i", "RaizEsperada2": "-1.00-1.41i"},
        )

        # Do
        for item in items:
            with self.subTest(item["Case"]):
                ecuacionSegundoGrado.definirParametros(item["a"], item["b"], item["c"])
            RaizActual1, RaizActual2 = ecuacionSegundoGrado.solucionESG()

            # Assert
            self.assertEqual(item["RaizEsperada1"], RaizActual1)
            self.assertEqual(item["RaizEsperada2"], RaizActual2)

    def test_solucionESG_parametrosNoNumericos_lanzaException_subTest(self):
        ecuacionSegundoGrado = EcuacionSegundoGrado()

        items = (
            {"Case": "Caso 01", "a": "a", "b":  "b", "c": "c"},
            {"Case": "Caso 02", "a": "a", "b": 1, "c": 1},
            {"Case": "Caso 03", "a": 1, "b": "aa", "c": 1},
            {"Case": "Caso 03", "a": 1, "b": "3,1", "c": 1},
        )

        for item in items:
            with self.subTest(item["Case"]):
                self.assertTrue(True)
                with self.assertRaises(ValueError):
                    ecuacionSegundoGrado.definirParametros(item["a"], item["b"], item["c"])
