# UNA TIENDA GESTIONA PEDIDOS CON DISTINTOS TIPOS DE PRODUCTO: 

# EXISTEN INICIALMENTE: 
    # ProductoFisico
    # ProductoDigital
    # Suscripcion

# TODOS COMPARTEN: 
    # id
    # nombre
    # precio_base

    # (Pero calculan su precio final de forma distinta.)
        # PRODUCTO FÍSICO:
            # precio_base + coste_envio

        # PRODUCTO DIGITAL:
            # precio_base

        # SUSCRIPCIÓN (Recibe además el número de meses)
            # precio_base * meses

# CREAR TAMBIÉN CLASE Pedido
    # DEBE PERMITIR: 
        # agregar(producto)
        # eliminar(id_producto)
        # calcular_total()

# AÑADE ESTAS CONDICIONES: 
    # Un pedido no puede contener dos productos con el mismo ID
    # Todos los precios deben ser válidos. 
    # calcular_total() no debe preguntar qué clase de producto está procesando mediante if type(...)
    # El pedido debe seguir funcionando sin modificaciones si aparece un nuevo tipo de producto compatible. 

# FINALMENTE CREA: 
    # ProductoDescuento (Recibirá un porcentaje de descuento)


# 1. CLASE BASE ABSTRANCTA / GENERAL PARA LOS PRODUCTOS: 
class Producto: 
    def __init__(self, id_prod, nombre, precio_base): 
        if precio_base < 0: 
            raise ValueError("El precio no puede ser negativo.")
        self.id = id_prod
        self.nombre = nombre
        self.precio_base = precio_base

    def calcular_precio(self): 
        raise NotImplementedError("Las subclases deben implemente este método.")


# 2. CLASES DE PRODUCTOS ESPECÍFICAS (HERENCIA Y POLIMORFISMO)
class ProductoFisico(Producto): 
    def __init__(self, id_prod, nombre, precio_base, coste_envio): 
        super().__init__(id_prod, nombre, precio_base)
        if coste_envio < 0: 
            raise ValueError("El coste de envío no puede ser negativo.")
        self.coste_envio = coste_envio

    def calcular_precio(self): 
        return self.precio_base + self.coste_envio

class ProductoDigital(Producto): 
    def calcular_precio(self): 
        return self.precio_base

class Suscripcion(Producto):
    def __init__(self, id_prod, nombre, precio_base, meses):
        super().__init__(id_prod, nombre, precio_base)
        if meses <= 0:
            raise ValueError("El número de meses debe ser mayor a 0.")
        self.meses = meses

    def calcular_precio(self):
        return self.precio_base * self.meses


# 3. CLASE ProductoDescuento 
class ProductoDescuento(Producto): 
    def __init__(self, producto, porcentaje_descuento):
        # Hereda los datos del producto original para mantener la interfaz
        super().__init__(producto.id, producto.nombre, producto.precio_base)
        self.producto_original = producto
        if not (0 <= porcentaje_descuento <= 100): 
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        self.porcentaje_descuento = porcentaje_descuento

    def calcular_precio(self):
        precio_original = self.producto_original.calcular_precio()
        return precio_original * (1 - self.porcentaje_descuento / 100)


# CLASE Pedido
class Pedido: 
    def __init__(self): 
        self.productos = []

    def agregar(self, producto): 
        for p in self.productos: 
            if p.id == producto.id: 
                raise ValueError(f"Error: Ya existe un producto con el id '{producto.id}' en el pedido.")

        # Añade el producto a la lista interna
        self.productos.append(producto)

    def eliminar(self, id_producto): 
        for p in self.productos: 
            if p.id == id_producto: 
                self.productos.remove(p) 
                return

        raise ValueError(f"Error: No se encontró ningún producto con el id '{id_producto}'")

    def calcular_total(self): 
        total = 0
        for producto in self.productos: 
            total += producto.calcular_precio()
        return total





# CÓDIGO DE PRUEBA: 

# Crear instancias de diferentes tipos de productos
p_fisico = ProductoFisico("F01", "Teclado mecánico", 50.0, 5.0)       # 50 + 5 = 55.0
p_digital = ProductoDigital("D01", "E-Book Python", 20.0)             # 20.0
suscripcion = Suscripcion("S01", "Plataforma Online", 15.0, 3)         # 15 * 3 = 45.0

# Crear el pedido y añadir los productos
mi_pedido = Pedido()
mi_pedido.agregar(p_fisico)
mi_pedido.agregar(p_digital)
mi_pedido.agregar(suscripcion)

# Calcular total preliminar (55 + 20 + 45 = 120.0)
print("Total inicial del pedido:", mi_pedido.calcular_total())

# Añadir un producto con un 20% de descuento sobre el producto digital
p_descuento = ProductoDescuento(p_digital, 20)  # 20 - 20% = 16.0
p_descuento.id = "D02" 
mi_pedido.agregar(p_descuento)

# Nuevo total del pedido (120.0 + 16.0 = 136.0)
print("Total con descuento aplicado:", mi_pedido.calcular_total())



# Maite Mesa Badiola - 15 SEPT 2026