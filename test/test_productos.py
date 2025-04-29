# test/test_productos.py
import unittest
from datetime import date
from modelo.plaguicida import Plaguicida
from modelo.fertilizante import Fertilizante
from modelo.antibiotico import Antibiotico

class TestProductos(unittest.TestCase):
    
    def test_creacion_plaguicida(self):
        producto = Plaguicida("MataPlagas", 35000, "ICA555", 20, 10)
        self.assertEqual(producto.nombre, "MataPlagas")
        self.assertEqual(producto.periodo_carencia, 10)
        self.assertIn("Carencia", str(producto))

    def test_creacion_fertilizante(self):
        fecha = date(2023, 5, 20)
        producto = Fertilizante("SuperFert", 45000, "ICA777", 30, fecha)
        self.assertEqual(producto.fecha_ultima_aplicacion, fecha)
        self.assertIn("Última aplicación", str(producto))

    def test_creacion_antibiotico_valido(self):
        producto = Antibiotico("Antibovino", 50000, 500, "Bovino")
        self.assertEqual(producto.dosis, 500)
        self.assertEqual(producto.tipo_animal, "Bovino")
        self.assertIn("Dosis", str(producto))

    def test_dosis_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            Antibiotico("MalAntibiotico", 40000, 300, "Caprino")  # fuera de rango

if __name__ == '__main__':
    unittest.main()
