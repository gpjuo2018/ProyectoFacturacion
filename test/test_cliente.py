import unittest
import modelo.cliente as cliente
import modelo.factura as factura

class TestFacturacion(unittest.TestCase):
    def test_creacion_cliente(self):
        cliente_obj = cliente.Cliente("Pedro Gómez", 111222333)
        self.assertEqual(cliente_obj.obtener_nombre(), "Pedro Gómez")
        self.assertEqual(cliente_obj.obtener_cedula(), 111222333)
        self.assertEqual(len(cliente_obj.obtener_facturas()), 0)

    def test_agregar_factura_a_cliente(self):
        cliente_obj = cliente.Cliente("Pedro Gómez", 111222333)
        factura_obj = factura.Factura(cliente_obj)
        cliente_obj.agregar_factura(factura_obj)
        self.assertEqual(len(cliente_obj.obtener_facturas()), 1)
        self.assertEqual(cliente_obj.obtener_facturas()[0], factura_obj)


    def test_obtener_facturas_vacias(self):
        cliente_obj = cliente.Cliente("Pedro Gómez", 111222333)
        self.assertEqual(cliente_obj.obtener_facturas(), [])

    def test_agregar_varias_facturas(self):
        cliente_obj = cliente.Cliente("Pedro Gómez", 111222333)
        factura1 = factura.Factura(cliente_obj)
        factura2 = factura.Factura(cliente_obj)
        cliente_obj.agregar_factura(factura1)
        cliente_obj.agregar_factura(factura2)
        self.assertEqual(len(cliente_obj.obtener_facturas()), 2)
        self.assertIn(factura1, cliente_obj.obtener_facturas())
        self.assertIn(factura2, cliente_obj.obtener_facturas())

# Ejecutar las pruebas
unittest.main(argv=[''], exit=False)