class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compras = []
    
    def actualizar_informacion(self, direccion=None, telefono=None):
        if direccion is not None:
            self.direccion = direccion
        if telefono is not None:
            self.telefono = telefono
    
    def registrar_compra(self, compra):
        self.historial_compras.append(compra)
    
    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Historial de Compras: {self.historial_compras}"