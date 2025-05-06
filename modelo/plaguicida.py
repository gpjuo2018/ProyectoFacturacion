# modelo/plaguicida.py
from modelo.producto_control import ProductoControl

class Plaguicida(ProductoControl):
    def __init__(self, nombre: str, precio: float, registro_ICA: str, frecuencia_aplicacion: int, periodo_carencia: int):
        super().__init__(nombre, precio, registro_ICA, frecuencia_aplicacion)
        self._periodo_carencia = periodo_carencia

    def __str__(self):
        return f"{super().__str__()} | Carencia: {self._periodo_carencia} días"
