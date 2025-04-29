from modelo.cliente import Cliente

clientes = []  # Lista para almacenar clientes

def crear_cliente(nombre: str, cedula: str) -> Cliente:
    cliente = Cliente(nombre, cedula)
    clientes.append(cliente)
    return cliente

def leer_clientes() -> list:
    return clientes

def actualizar_cliente(cedula: str, nuevo_nombre: str = None) -> bool:
    for cliente in clientes:
        if cliente.cedula == cedula:
            if nuevo_nombre:
                cliente.nombre = nuevo_nombre
            return True
    return False

def eliminar_cliente(cedula: str) -> bool:
    global clientes
    clientes = [c for c in clientes if c.cedula != cedula]
    return True