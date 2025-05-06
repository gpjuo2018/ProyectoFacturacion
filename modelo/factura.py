# modelo/factura.py
from datetime import date
from modelo.producto_control import ProductoControl
from modelo.antibiotico import Antibiotico

class Factura:
    def __init__(self, fecha: date):
        self._fecha = fecha
        self._productos_control = []  # Lista para productos de control
        self._antibioticos = []       # Lista para antibióticos
        self._valor_total = 0.0

    def _agregar_producto_control(self, producto: ProductoControl):
        self._productos_control.append(producto)
        self._valor_total += producto._precio

    def _agregar_antibiotico(self, antibiotico: Antibiotico):
        self._antibioticos.append(antibiotico)
        self._valor_total += antibiotico._precio

    def _mostrar_productos(self):
        productos_control = [str(p) for p in self._productos_control]
        antibioticos = [str(a) for a in self._antibioticos]
        return productos_control + antibioticos

    def _calcular_total(self):
        return self._valor_total

    def __str__(self):
        total_productos = len(self._productos_control) + len(self._antibioticos)
        return f"Factura del {self._fecha} - Total: ${self._valor_total:.2f} - {total_productos} productos"
