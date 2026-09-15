class A: 
    def metodo(self): 
        return "A" 

class B(A): 
    def metodo(self): 
        return "B" + super().metodo() 

class C(A): 
    def metodo(self): 
        return "C" + super().metodo() 

class D(B, C): 
    def metodo(self): 
        return "D" + super().metodo() 



obj = D() 
print(obj.metodo()) 
print(D.mro()) 

# SIN EJECUTAR EL PROGRAMA: 
    # 1. Escribe qué resultado crees que mostrará. 
    # 2. Explica por qué. 
    # 3. Ejecútalo y comprueba la respuesta. 
    # 4. Modifica únicamente el orden de herencia de D y explica cómo cambia el resultado. 
    # 5. Explica qué está haciendo realmente super() en este ejemplo. 


# RESPUESTAS: 
# 1 : 
    # Al ejecutar print(obj.metodo()), el resultado será "DBCA"

# 2: 
    # Cuando llamo a obj.metodo(): 
        # 1. Entra primero en el método de la clase D, que devuelve "D".
        # 2. Como hay un super(), este no salta, sino que busca el siguiente elemento en la lista del MRO, que es B (añadiendo "B").
        # 3. A su vez, el super() dentro de B avanza al siguiente paso del MRO global, que es C (añadiendo "C"), y no salta directamente a A. 
        # 4. Por último, el super() de C llega a la clase base A (añadiendo "A").
        # 5. Se concatena todo y se obtiene "DBCA". 


# 3:
    # El resultado es: 
    # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# 4:
    # Si cmbio la cabecera d ela clase D invirtiendo el orden se sus padres: 

class D(C, B):
    def metodo(self):
        return "D" + super().metodo()

    # Cómo cambia el resultado: pasa a ser [D, C, B, A, object], por lo que el resultdo impreso por obj.metodo() cambia automáticamente a "DCBA".

    # Al poner a C primero en los paréntesis de herencia de D, el algoritmo le da prioridad frente a B, haciendo que el flujo de llamadas de super() recorra primero la rama de C antes que la de B. 

# 5:
    # Lo que está haciendo es navegar de manera dinámica a lo largo de la lista del MRO. Actúa como un puntero que avanza al siguiente eslabón de la cadena ordenada de clases, permitiendo que todas cooperen y ejecuten sus métodos de forma encadenada sin duplicar llamadas. 





# Maite Mesa Badiola - 15 SEPT 2026