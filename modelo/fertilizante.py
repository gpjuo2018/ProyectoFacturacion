# modelo/fertilizante.py
from modelo.producto_control import ProductoControl
from datetime import date

class Fertilizante(ProductoControl):
    def __init__(self, nombre: str, precio: float, registro_ICA: str, frecuencia_aplicacion: int, fecha_ultima_aplicacion: date):
        super().__init__(nombre, precio, registro_ICA, frecuencia_aplicacion)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

    def __str__(self):
        return f"{super().__str__()} | Última aplicación: {self.fecha_ultima_aplicacion}"
