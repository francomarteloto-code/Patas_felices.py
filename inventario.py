class Inventario:
    def __init__(self):
        self.lista_de_productos = []
    
    def agregar_producto(self, producto):
        self.lista_de_productos.append(producto)
            
    def actualizar_inventario(self, producto, cantidad):
        for prod in self.lista_de_productos:
            if prod.nombre == producto.nombre:
                prod.actualizar_cantidad(cantidad)

    def disminuir_stock(self, producto, cantidad):
        for prod in self.lista_de_productos:
            if prod.nombre == producto.nombre:
                if prod.cantidad >= cantidad:
                    prod.cantidad -= cantidad
                    return True
                else:
                    print(f"Stock insuficiente para {producto.nombre}")
                    return False
        print("Producto no encontrado en inventario")
        return False

    def generar_alerta(self, umbral_minimo):
        alertas = [prod.nombre for prod in self.lista_de_productos if prod.cantidad < umbral_minimo]
        return f"!Productos por debajo del umbral: {', '.join(alertas)}!" if alertas else "!No hay productos por debajo del umbral!"
