# Funciones para la interfaz de la consola

from Clases.cliente import Cliente
from Clases.inventario import Inventario
from Clases.mascota import Gato, Perro
from Clases.venta import Venta
from Clases.producto import Producto


def registtar_mascota():
    tipo = input("Ingrese el tipo de mascota (Perro/Gato): ").strip().lower()
    nombre = input("Ingrese el nombre de la mascota: ").strip()
    edad = int(input("Ingrese la edad de la mascota: ").strip())
    salud = input("Ingrese la salud de la mascota (Buena/Regular/Mala): ").strip().lower()
    precio = float(input("Ingrese el precio de la mascota: ").strip())
    
    if tipo == 'perro':
        raza = input("Raza del perro: ").strip()
        nivel_de_energia = input("Nivel de energía del perro (Alto/Medio/Bajo): ").strip().lower()
        mascota_obj = Perro(nombre, edad, salud, precio, raza, nivel_de_energia)
    elif tipo == 'gato':
        raza = input("Raza del gato: ").strip()
        independencia = input("Nivel de independencia del gato (Alto/Medio/Bajo): ").strip().lower()
        mascota_obj = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Tipo de mascota no válido.")
        return
    
    return mascota_obj


def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría del producto: ").strip()
    precio = float(input("Ingrese el precio del producto: ").strip())
    cantidad = int(input("Ingrese la cantidad del producto: ").strip())
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto


def registrar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente


def registrar_venta(clientes, inventario):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    items = []
    while True:
        nombre_producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ").strip()
        if nombre_producto.lower() == "fin":
            break
        producto = next((p for p in inventario.lista_de_productos if p.nombre == nombre_producto), None)
        if producto:
            # 🚨 Validar que la cantidad ingresada sea un número
            while True:
                entrada = input(f"Ingrese la cantidad de {producto.nombre}: ")
                if entrada.isdigit():
                    cantidad = int(entrada)
                    break
                else:
                    print("⚠️ Error: Debe ingresar un número válido.")
            items.append((producto, cantidad))
        else:
            print("Producto no encontrado.")
    
    if items:
        venta = Venta(cliente, items)
        if venta.registrar_venta(inventario):  # La alerta se dispara automáticamente
            print("Venta registrada exitosamente.")
    else:
        print("No se han registrado productos para la venta.")


def mostrar_menu():
    print("\n --- Menú de gestión  de Patas Felices ---")
    print("1. Registrar Mascota")
    print("2. Registrar Cliente")
    print("3. Registrar Producto")
    print("4. Registrar Venta")
    print("5. Mostrar informacion a cerca de Mascotas")
    print("6. Mostrar informacion a cerca de Clientes")
    print("7. Mostrar informacion a cerca de Productos")
    print("8. Generar alerta de inventario")
    print("9. Salir ")


def main():
    mascotas = []
    clientes = []
    inventario = Inventario()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            mascota = registtar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("Mascota registrada exitosamente.")
        
        elif opcion == '2':
            cliente = registrar_cliente()
            clientes.append(cliente)
            print("Cliente registrado exitosamente.")
        
        elif opcion == '3':
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print("Producto registrado exitosamente.")
        
        elif opcion == '4':
            registrar_venta(clientes, inventario)
        
        elif opcion == '5':
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())
        
        elif opcion == '6':
            for cliente in clientes:
                print(cliente.mostrar_informacion())
        
        elif opcion == '7':
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_informacion())
        
        elif opcion == '8':
            umbral_minimo = int(input("Ingrese el umbral mínimo de inventario: ").strip())
            print(inventario.generar_alerta(umbral_minimo))

        elif opcion == '9':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
