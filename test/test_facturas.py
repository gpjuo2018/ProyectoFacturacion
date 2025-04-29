# test/test_facturas.py
import unittest
from datetime import date
from modelo.factura import Factura
from modelo.plaguicida import Plaguicida

class TestFactura(unittest.TestCase):
    def test_agregar_producto_y_valor_total(self):
        factura = Factura(date.today())
        plaguicida = Plaguicida("MataTodo", 30000, "ICA998", 15, 7)

        factura.agregar_producto(plaguicida)

        self.assertEqual(len(factura.productos), 1)
        self.assertEqual(factura.valor_total, 30000)

if __name__ == '__main__':
    unittest.main()
