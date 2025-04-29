# modelo/producto_control.py
from modelo.producto import Producto # Importando la clase Producto

class ProductoControl(Producto):
    def __init__(self, nombre: str, precio: float, registro_ICA: str, frecuencia_aplicacion: int):
        super().__init__(nombre, precio)
        self.registro_ICA = registro_ICA
        self.frecuencia_aplicacion = frecuencia_aplicacion

    def __str__(self):
        return f"{super().__str__()} | ICA: {self.registro_ICA} | Frecuencia: {self.frecuencia_aplicacion} días"
