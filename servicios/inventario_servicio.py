from modelos.producto import Producto

class InventarioServicio:

    """Gestiona las operaciones relacionadas al inventario """

    def __init__(self):
        self.productos = [] # Se usa una lista para almacenar los productos

    # AÑADIR UN PRODUCTO AL INVENTARIO 
    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if self.__buscar_por_id(id_producto):
            return False, "El ID del producto ya existe dentro del inventario"
    
        if cantidad < 0:
            return False, "La cantidad no puede ser negativa"
        if precio <= 0:
            return False, "El precio debe ser mayor a 0"
        
        nuevo = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo)
        return True, " Producto agregado exitosamente"
    
    # LISTAR LOS PRODUCTOS DEL INVENTARIO 
    def listar_productos(self):
        if not self.productos:
            print("El inventario se encuentra vacío.")
            return
        
        print("\n Inventario:")
        print("=" * 60)
        for p in self.productos:
            print(p)
        print("=" * 60)

    # Buscar el producto por su ID 
    def __buscar_por_id(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                return p
        return None
    
    # Buscar el producto por su nombre 
    def buscar_por_nombre(self, texto):
        resultados = []
        texto = texto.lower()
        for p in self.productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    # Actualizar el producto 
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto = self.__buscar_por_id(id_producto)
        if not producto:
            return False, " Producto no encontrado"
        
        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)
        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)
        
        return True, " Producto actualizado"
    
    # Eliminar un producto del inventario
    def eliminar_producto(self, id_producto):
        producto = self.__buscar_por_id(id_producto)
        if not producto:
            return False, " Producto no encontrado"
        
        self.productos.remove(producto)
        return True, " Producto eliminado"
