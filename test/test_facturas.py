import unittest
from datetime import date
from modelo.factura import Factura
from modelo.producto_control import ProductoControl
from modelo.antibiotico import Antibiotico
from crud.factura_crud import (
    crear_factura,
    leer_facturas,
    buscar_factura,
    eliminar_factura,
    agregar_producto_control,
    agregar_antibiotico,
)

class TestFacturaCRUD(unittest.TestCase):
    def setUp(self):
        """Configurar datos iniciales para las pruebas."""
        self.fecha = date(2025, 5, 6)
        self.factura = crear_factura(self.fecha)
        self.producto_control = ProductoControl("Producto Control X", 50000, "ICA123", 30)
        self.antibiotico = Antibiotico("Antibiótico A", 75000, 500, "Bovinos")

    def test_crear_factura(self):
        """Prueba la creación de una factura."""
        self.assertEqual(self.factura.fecha, self.fecha)
        self.assertIn(self.factura, leer_facturas())

    def test_buscar_factura(self):
        """Prueba la búsqueda de una factura por fecha."""
        factura_encontrada = buscar_factura(self.fecha)
        self.assertEqual(factura_encontrada, self.factura)

    def test_eliminar_factura(self):
        """Prueba la eliminación de una factura."""
        eliminar_factura(self.factura)
        self.assertNotIn(self.factura, leer_facturas())

    def test_agregar_producto_control(self):
        """Prueba agregar un producto control a la factura."""
        agregar_producto_control(self.factura, self.producto_control)
        self.assertIn(self.producto_control, self.factura._mostrar_productos())

    def test_agregar_antibiotico(self):
        """Prueba agregar un antibiótico a la factura."""
        agregar_antibiotico(self.factura, self.antibiotico)
        self.assertIn(self.antibiotico, self.factura._mostrar_productos())

    def test_calcular_total(self):
        """Prueba el cálculo del total de la factura."""
        agregar_producto_control(self.factura, self.producto_control)
        agregar_antibiotico(self.factura, self.antibiotico)
        total_esperado = self.producto_control.precio + self.antibiotico.precio
        self.assertEqual(self.factura._calcular_total(), total_esperado)

