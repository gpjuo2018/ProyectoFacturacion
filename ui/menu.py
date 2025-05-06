from crud.cliente_crud import crear_cliente, leer_clientes, buscar_cliente
from crud.factura_crud import crear_factura, agregar_producto_control, agregar_antibiotico
from modelo.plaguicida import Plaguicida
from modelo.fertilizante import Fertilizante
from modelo.antibiotico import Antibiotico
from datetime import date

def mostrar_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear cliente")
        print("2. Ver todos los clientes")
        print("3. Buscar cliente por cédula")
        print("4. Agregar factura a un cliente")
        print("5. Agregar producto a una factura")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            cedula = input("Ingrese la cédula del cliente: ")
            cliente = crear_cliente(nombre, cedula)
            print(f"Cliente creado: {cliente._nombre} ({cliente._cedula})")
        
        elif opcion == "2":
            clientes = leer_clientes()
            if clientes:
                print("\n--- Lista de Clientes ---")
                for cliente in clientes:
                    print(f"{cliente._nombre} - Cédula: {cliente._cedula}")
            else:
                print("No hay clientes registrados.")
        
        elif opcion == "3":
            cedula = input("Ingrese la cédula del cliente a buscar: ")
            cliente = buscar_cliente(cedula)
            if cliente:
                print(f"Cliente encontrado: {cliente._nombre} - Cédula: {cliente._cedula}")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == "4":
            cedula = input("Ingrese la cédula del cliente: ")
            cliente = buscar_cliente(cedula)
            if cliente:
                fecha = date.today()
                factura = crear_factura(fecha)
                cliente._agregar_factura(factura)
                print(f"Factura creada para el cliente {cliente._nombre} en la fecha {fecha}.")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == "5":
            cedula = input("Ingrese la cédula del cliente: ")
            cliente = buscar_cliente(cedula)
            if cliente:
                if cliente._facturas:
                    print("\n--- Facturas del Cliente ---")
                    for i, factura in enumerate(cliente._facturas):
                        print(f"{i + 1}. {factura}")
                    factura_index = int(input("Seleccione el número de la factura: ")) - 1
                    factura = cliente._facturas[factura_index]
                    
                    print("\n--- Tipos de Productos ---")
                    print("1. Plaguicida")
                    print("2. Fertilizante")
                    print("3. Antibiótico")
                    tipo_producto = input("Seleccione el tipo de producto: ")
                    
                    nombre = input("Ingrese el nombre del producto: ")
                    precio = float(input("Ingrese el precio del producto: "))
                    
                    if tipo_producto == "1":
                        registro_ICA = input("Ingrese el registro ICA: ")
                        frecuencia_aplicacion = int(input("Ingrese la frecuencia de aplicación (días): "))
                        periodo_carencia = int(input("Ingrese el periodo de carencia (días): "))
                        producto = Plaguicida(nombre, precio, registro_ICA, frecuencia_aplicacion, periodo_carencia)
                        agregar_producto_control(factura, producto)
                    
                    elif tipo_producto == "2":
                        registro_ICA = input("Ingrese el registro ICA: ")
                        frecuencia_aplicacion = int(input("Ingrese la frecuencia de aplicación (días): "))
                        fecha_ultima_aplicacion = date.fromisoformat(input("Ingrese la fecha de última aplicación (YYYY-MM-DD): "))
                        producto = Fertilizante(nombre, precio, registro_ICA, frecuencia_aplicacion, fecha_ultima_aplicacion)
                        agregar_producto_control(factura, producto)
                    
                    elif tipo_producto == "3":
                        dosis = int(input("Ingrese la dosis (kg): "))
                        tipo_animal = input("Ingrese el tipo de animal: ")
                        producto = Antibiotico(nombre, precio, dosis, tipo_animal)
                        agregar_antibiotico(factura, producto)
                    
                    print(f"Producto agregado a la factura: {producto}")
                else:
                    print("El cliente no tiene facturas.")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

