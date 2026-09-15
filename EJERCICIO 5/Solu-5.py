# FUNCIÓN QUE NO SE PUEDE MODIFICAR
class Pedido: 
    def calcular_precio(self, tipo, precio, cantidad): 
        if tipo == "normal": 
            return precio * cantidad 
        elif tipo == "vip": 
            return precio * cantidad * 0.8 
        elif tipo == "empleado": 
            return precio * cantidad * 0.5 
        elif tipo == "premium": 
            return precio * cantidad * 0.7 


# REFACTORIZA EL PROGRAMA USITLIZANDO POO PARA QUE SEA POSIBLE CREAR NUEVOS TIPOS DE DESCUENTO SIN MODIFICAR LA CLASE QUE CALCULA EL PEDIDO. 

# IMPLEMENTACIÓN DE: 
    # Cliente normal
    # Cliente VIP
    # Empleado
    # Cliente premium

# AÑADIR EXTRA: 
    # ClienteEstudiante -> 15% de descuento


# Clases para cada tipo de cliente / descuento (Polimorfismo)

# NORMAL - SIN DESCUENTO
class ClienteNormal: 
    def calcular_precio(self, precio, cantidad):
        return precio * cantidad

# VIP - 20% DESCUENTO
class ClienteVIP: 
    def calcular_precio(self, precio, cantidad):
        return (precio * cantidad) * 0.8 #20% DE DESCUENTO

# EMPLEADO - 50% DESCUENTO
class Empleado: 
    def calcular_precio(self, precio, cantidad):
        return (precio * cantidad) * 0.5 #50% DE DESCUENTO

# PREMIUM - 30% DESCUENTO
class ClientePremium: 
    def calcular_precio(self, precio, cantidad): 
        return (precio * cantidad) * 0.7 #30% DE DESCUENTO

    
# Nuevo tipo de cliente añadido sin modificar la clase PEDIDO: 
# ESTUDIANTE - 15% DESCUENTO
class ClienteEstudiante:
    def calcular_precio(self, precio, cantidad):
        return (precio * cantidad) * 0.85 #15% DE DESCUENTO



# CLASE PEDIDO LIMPIA (sin if/elif)
class Pedido: 
    def __init__(self, cliente): 
        # Composición: el pedido tiene un cliente asociado
        self.cliente = cliente

    def calcular_precio(self, precio, cantidad):
        # Delegmos la responsabilidad del cálculo al objeto CLIENTE (Polimorfismo)
        return self.cliente.calcular_precio(precio, cantidad)




# CÓDIGO DE PRUEBA

# Probando un pedido con un cliente VIP (precio 100, cantidad 2)
pedido_vip = Pedido(ClienteVIP())
print("Total VIP:", pedido_vip.calcular_precio(100, 2))  # Resultado esperado: 160.0

# Probando con el nuevo Cliente Estudiante (precio 100, cantidad 2)
pedido_estudiante = Pedido(ClienteEstudiante())
print("Total Estudiante:", pedido_estudiante.calcular_precio(100, 2))  # Resultado esperado: 170.0





# Maite Mesa Badiola - 15 SEPT 2026