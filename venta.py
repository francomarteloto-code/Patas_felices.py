from datetime import datetime

class Venta:
    def __init__(self, cliente, items):  
        # items será una lista de tuplas (producto, cantidad)
        self.cliente = cliente
        self.items = items
        self.fecha = datetime.now()
        self.total = self.calcular_total()
        
    def calcular_total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.items)
    
    def registrar_venta(self, inventario, umbral_minimo=5):
        # Descuenta stock de cada producto
        for producto, cantidad in self.items:
            if not inventario.disminuir_stock(producto, cantidad):
                print("No se pudo registrar la venta")
                return False
        
        # Registrar compra en cliente
        self.cliente.registrar_compra(self)
        print(f"Venta registrada: {self.mostrar_informacion()}")

        # 🚨 Verificar alerta de stock mínimo automáticamente
        alerta = inventario.generar_alerta(umbral_minimo)
        if "!" in alerta and "No hay productos" not in alerta:
            print(alerta)

        return True
    
    def mostrar_informacion(self):
        productos = ", ".join(f"{producto.nombre} (x{cantidad})" for producto, cantidad in self.items)
        return f"Cliente: {self.cliente.nombre}, Productos: {productos}, Total: {self.total}"
