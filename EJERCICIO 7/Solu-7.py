# IMPLEMENTA UN SISTEMA DE CURSOS: 

# CREA (CLASES): 
    # Persona
    # Alumno
    # Profesor
    # Curso

        # (Alumno y Profesor heredan de Persona)


# UN CURSO TIENE (ATRIBUTOS): 
    # un nombre
    # un profesor
    # alumnos
    # una capacidad máxima de alumnos

# DEBE PERMITIR (MÉTODOS REQUERIDOS): 
    # matricular(alumno)
    # desmatricular(alumno)
    # cambiar_profesor(profesor)

# CONDICIONES: 
    # Únicamente pueden matricularse objetos Alumno
    # Solamente un Profesor puede ser profesor del curso 
    # Un alumno no puede matricularse dos veces
    # Debe respetarse la capacidad máxima. 

        # EXTRA:
        # IMPLEMENTAR __str__() PARA MOSTRAR UN CURSO DE FORMA LEGIBLE. 


# 1. CLASE BASE Y DERIVADAS (HERENCIA)
class Persona: 
    def __init__(self, nombre):
        self.nombre = nombre

class Alumno(Persona): 
    pass

class Profesor(Persona):
    pass

# 2. CLASE CURSO
class Curso: 
    def __init__(self, nombre, profesor, capacidad_maxima): 
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self.alumnos = []  # Lista de alumnos matriculados

        # Verificar que el profesor inicial sea correcto
        self.cambiar_profesor(profesor)

    def matricular(self, alumno): 
        # CONDICIÓN: sólo se pueden matricular objetos Alumno
        if not isinstance(alumno, Alumno):
            raise TypeError("Error: Solo se pueden matricular alumnos.")

        # CONDICIÓN: no se puede matricular el mismo alumno dos veces
        if alumno in self.alumnos:
            raise ValueError(f"Error: El alumno '{alumno.nombre}' ya está matriculado en este curso.")

        # CONDICIÓN: debe respetarse la capacidad máxima
        if len(self.alumnos) >= self.capacidad_maxima:
            raise ValueError("No se puede matricular: se ha alcanzado la capacidad máxima del curso.")

        self.alumnos.append(alumno)

    def desmatricular(self, alumno): 
        if alumno in self.alumnos: 
            self.alumnos.remove(alumno)
        else:
            raise ValueError(f"El alumno '{alumno.nombre}' no está matriculado en este curso.")

    def cambiar_profesor(self, nuevo_profesor): 
        # CONDICIÓN: Solo un profesor por curso. 
        if not isinstance(nuevo_profesor, Profesor): 
            raise TypeError("Error: El nuevo profesor ebe ser un objeto de la clase Profesor.")
        self.profesor = nuevo_profesor

    def __str__(self): 
        nombre_alumnos = ", ".join([a.nombre for a in self.alumnos])
        return(f"Curso: {self.nombre} | "
               f"Profesor: {self.profesor.nombre} | "
               f"Capacidad: {len(self.alumnos)}/{self.capacidad_maxima} | "
               f"Alumnos matriculados: [{nombre_alumnos}]")





# PRUEBA. 

# Crear profesores y alumnos
prof = Profesor("Carlos Pérez")
alt1 = Alumno("Ana Gómez")
alt2 = Alumno("Marc Vila")

# Crear el curso con capacidad máxima de 2
python_curso = Curso("Programación en Python", prof, capacidad_maxima=2)

# Matriculaciones
python_curso.matricular(alt1)
python_curso.matricular(alt2)

# Imprimir información de forma legible (gracias a __str__)
print(python_curso)

# Intentar matricular a un alumno repetido lanzará un ValueError:
# python_curso.matricular(alt1)

# Intentar superar la capacidad máxima (al intentar meter un 3º alumno) lanzará un ValueError:
# alt3 = Alumno("Júlia Puig")
# python_curso.matricular(alt3)




# Maite Mesa Badiola - 15 SEPT 2026
