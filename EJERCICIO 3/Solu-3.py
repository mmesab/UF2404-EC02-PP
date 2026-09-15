# FUNCIÓN QUE NO SE PUEDE MODIFICAR
def imprimir_informe(figuras): 
    for figura in figuras: 
        print( 
            figura.nombre(), 
            round(figura.area(), 2), 
            round(figura.perimetro(), 2) 
        ) 

# CREAR CLASES NECESARIAS PARA QUE EL CÓDIGO FUNCIONE
    # Rectangulo;
    # Circulo; 
    # TrianguloRectangulo; 

# NO SE PUEDE MODIFICAR imprimir_informe()

# Cada figura debe implementar: 
    # nombre()
    # area()
    # perimetro()

import math


# Rectángulo
class Rectangulo: 
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura

    def nombre(self): 
        return "Rectángulo" 

    def area(self): 
        return self.base * self.altura

    def perimetro(self): 
        return 2 * (self.base + self.altura)

# Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def nombre(self):
        return "Círculo"

    def area(self): 
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

# TriánguloRectangulo
class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def nombre(self):
        return "Triángulo Rectángulo"

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        # Hipotenusa con teorema de Pitágoras
        hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)
        return self.base + self.altura + hipotenusa


# AÑADIR UNA NUEVA FIGURA Cuadrado REUTILIZANDO CÓDIGO CON HERENCIA
# Cuadrado, que hereda de Rectangulo (los dos lados son iguales) 
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    def nombre(self): 
        return "Cuadrado"

    # def area(self): 
    #     return super().area()

    # def perimetro(self): 
    #     return super().perimetro()

    # Al heredar de Rectángulo, la clase Cuadrado ya hereda automáticamente esos métodos. 


# Lista de figuras heterogéneas
figuras = [
    Rectangulo(4, 5),
    Circulo(3),
    TrianguloRectangulo(3, 4),
    Cuadrado(4)
]

# Llamada a la función proporcionada
imprimir_informe(figuras)


# Maite Mesa Badiola - 15 SEPT 2026