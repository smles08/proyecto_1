import unittest

from capa1.lector import LectorArchivo


class TestLectorArchivo(unittest.TestCase):

    def setUp(self):
        self.lector = LectorArchivo("datos/foro.txt")

    def test_cargar_foro(self):
        mensajes = self.lector.leer_foro()

        self.assertIsInstance(mensajes, list)
        self.assertGreater(len(mensajes), 0)

    def test_estructura_mensaje(self):
        mensajes = self.lector.leer_foro()

        for mensaje in mensajes:
            self.assertIn("usuario", mensaje)
            self.assertIn("fecha", mensaje)
            self.assertIn("mensaje", mensaje)

    def test_mensajes_no_vacios(self):
        mensajes = self.lector.leer_foro()

        for mensaje in mensajes:
            self.assertTrue(mensaje["usuario"])
            self.assertTrue(mensaje["mensaje"])


if __name__ == "__main__":
    unittest.main()