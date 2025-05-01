import unittest
from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):
    def test_raices_reales_diferentes(self):
        ecuacionSegundoGrado = EcuacionSegundoGrado()
        ecuacionSegundoGrado.a = 1
        ecuacionSegundoGrado.b = -3
        ecuacionSegundoGrado.c = 2
        raiz_esperada_1 = 2.0
        raiz_esperada_2 = 1.0

        raiz_actual_1, raiz_actual_2 = ecuacionSegundoGrado.solucionESG()

        self.assertEqual(raiz_actual_1, raiz_esperada_1)
        self.assertEqual(raiz_actual_2, raiz_esperada_2)

    def test_raices_reales_iguales(self):
        ecuacionSegundoGrado = EcuacionSegundoGrado()
        ecuacionSegundoGrado.a = 1
        ecuacionSegundoGrado.b = 2
        ecuacionSegundoGrado.c = 1
        raiz_esperada_1 = -1.0
        raiz_esperada_2 = -1.0

        raiz_actual_1, raiz_actual_2 = ecuacionSegundoGrado.solucionESG()

        self.assertEqual(raiz_actual_1, raiz_esperada_1)
        self.assertEqual(raiz_actual_2, raiz_esperada_2)

    def test_raices_complejas(self):
        datosPrueba = [
            {
                "a": 1, "b": 2, "c": 5,
                "raiz1": complex(-1, 2),
                "raiz2": complex(-1, -2),
                "Case": "Caso 01"
            },
            {
                "a": 2, "b": 1, "c": 2,
                "raiz1": complex(-0.25, 0.9682458365518543),
                "raiz2": complex(-0.25, -0.9682458365518543),
                "Case": "Caso 02"
            },
        ]

        for item in datosPrueba:
            with self.subTest(item["Case"]):
                ecuacionSegundoGrado = EcuacionSegundoGrado()
                ecuacionSegundoGrado.a = item["a"]
                ecuacionSegundoGrado.b = item["b"]
                ecuacionSegundoGrado.c = item["c"]

                raiz_actual1, raiz_actual2 = ecuacionSegundoGrado.solucionESG()
                self.assertEqual(raiz_actual1, item["raiz1"])
                self.assertEqual(raiz_actual2, item["raiz2"])

    def test_parametros_no_numericos_lanza_exception_subTest(self):
        datos_prueba = [
            {
                "a": "a", "b": 2, "c": 1,
                "Case": "Caso 01"
            },
            {
                "a": 1, "b": "b", "c": 2,
                "Case": "Caso 02"
            },
            {
                "a": 1, "b": 2, "c": "c",
                "Case": "Caso 03"
            },
        ]

        for item in datos_prueba:
            with self.subTest(item["Case"]):
                ecuacionSegundoGrado = EcuacionSegundoGrado()
                ecuacionSegundoGrado.a = item["a"]
                ecuacionSegundoGrado.b = item["b"]
                ecuacionSegundoGrado.c = item["c"]

                with self.assertRaises(TypeError):
                    ecuacionSegundoGrado.solucionESG()
