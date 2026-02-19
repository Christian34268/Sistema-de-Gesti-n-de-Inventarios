from modelos.producto import Producto

ARCHIVO_INVENTARIO = "inventario.txt"  # Aqui se guardara el inventario

class InventarioServicio:

    """Gestiona las operaciones relacionadas al inventario """

    def __init__(self):
        self.productos = []  # Se usa una lista para almacenar los productos
        self.__cargar_desde_archivo()  # Función añadida para cargar los archivos al iniciar el programa
    
    
    # Se incorpora una acutalización del menú para cargar los productos al iniciar 
    """|MANEJO DE ARCHIVOS|"""
    
    # CARGAR LOS PRODUCTOS DESDE EL ARCHIVO AL INICIAR
    def __cargar_desde_archivo(self):
        """Se lee el inventario.txt y reconstruye la lista de productos al comenzar el programa"""
        try:        
            with open(ARCHIVO_INVENTARIO, "r") as archivo:    # Abre en modo lectura
                lineas = archivo.readlines()     # Lee todas las lineas del archivo
        
        except FileNotFoundError:
            print("El archivo de inventario no existe. Se creará uno nuevo al guardar.")
            with open(ARCHIVO_INVENTARIO, "w") as archivo:  # creara un archivo vacio si no existe 
                pass
            return
        
        except PermissionError:
            print("No posee la autoridad necesaria para leer el archivo de inventario.")
            return
        
        else:  # Si el archivo no tuvo ningun error ingresa aqui
            for línea in lineas:
                línea = línea.strip()
                if línea:  # Verifica que la linea no este vacia
                    partes = línea.split("|")
                    id_producto, nombre, cantidad, precio = partes 
                    producto = Producto(int(id_producto), nombre, int(cantidad), float(precio))
                    self.productos.append(producto)  # Agrega el producto a la lista de productos

    """Se guarda el inventario actual en el archivo de texto sobreescribiendo el contenido anterior"""
    def __guardar_en_archivo(self):
        try:
            with open(ARCHIVO_INVENTARIO, "w") as archivo:  # Abre en modo escritura (sobrescribe)
                for producto in self.productos:
                    linea = f"{producto.get_id()}|{producto.get_nombre()}|{producto.get_cantidad()}|{producto.get_precio()}\n"
                    archivo.write(linea)  # Escribe cada producto

        except PermissionError:
            print("No posee la autoridad necesaria para escribir en el archivo de inventario.")

        """FINALIZA EL APARTADO DE MODIFICACION DEL CODIGO PARA MANEJO  DE ARCHIVOS"""

    
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
        self.__guardar_en_archivo()  # Guardar cambios en archivo
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
        
        self.__guardar_en_archivo()  # Guardar cambios en archivo
        return True, " Producto actualizado"
    
    # Eliminar un producto del inventario
    def eliminar_producto(self, id_producto):
        producto = self.__buscar_por_id(id_producto)
        if not producto:
            return False, " Producto no encontrado"
        
        self.productos.remove(producto)
        self.__guardar_en_archivo()  # Guardar cambios en archivo
        return True, " Producto eliminado exitosamente"
        return True, " Producto eliminado"
