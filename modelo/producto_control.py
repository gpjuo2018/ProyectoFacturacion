# modelo/producto_control.py
class ProductoControl:
    def __init__(self, nombre: str, precio: float, registro_ICA: str, frecuencia_aplicacion: int):
        self._nombre = nombre
        self._precio = precio
        self._registro_ICA = registro_ICA
        self._frecuencia_aplicacion = frecuencia_aplicacion

    def __str__(self):
        return f"{self._nombre} - ${self._precio:.2f} | ICA: {self._registro_ICA} | Frecuencia: {self._frecuencia_aplicacion} días"
