# test/test_clientes.py
import unittest
from datetime import date
from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.antibiotico import Antibiotico
from crud.cliente_crud import crear_cliente, leer_clientes, actualizar_cliente, eliminar_cliente

class TestCliente(unittest.TestCase):
    def test_agregar_factura_y_calculo_total(self):
        cliente = Cliente("Carlos Pérez", "12345678")
        factura1 = Factura(date.today())
        factura2 = Factura(date.today())

        prod1 = Antibiotico("Antibovino", 50000, 500, "Bovino")
        prod2 = Antibiotico("Antiporcino", 60000, 550, "Porcino")

        factura1.agregar_producto(prod1)
        factura2.agregar_producto(prod2)

        cliente.agregar_factura(factura1)
        cliente.agregar_factura(factura2)

        self.assertEqual(len(cliente.facturas), 2)
        self.assertAlmostEqual(cliente.calcular_total_compras(), 110000)

    def test_crud_cliente(self):
        cliente = crear_cliente("Juan Pérez", "98765432")
        self.assertIn(cliente, leer_clientes())
        actualizar_cliente("98765432", nuevo_nombre="Juan Actualizado")
        self.assertEqual(cliente.nombre, "Juan Actualizado")
        eliminar_cliente("98765432")
        self.assertNotIn(cliente, leer_clientes())

if __name__ == '__main__':
    unittest.main()
