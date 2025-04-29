# modelo/factura.py
from datetime import date
from modelo.producto import Producto

class Factura:
    def __init__(self, fecha: date):
        self.fecha = fecha
        self.productos = []
        self.valor_total = 0.0

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        self.valor_total += producto.precio

    def mostrar_productos(self):
        return [str(p) for p in self.productos]

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)

    def __str__(self):
        return f"Factura del {self.fecha} - Total: ${self.valor_total:.2f} - {len(self.productos)} productos"
