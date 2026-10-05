'''
Valeria Urrutia Lopez 00604583
P2A1 Herencia
'''
class Persona:
    def __init__(self, nombre, apellidos, dni, estado_civil):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.estado_civil = estado_civil

    def get_dni(self):
        return self.dni

    def cambiar_estado_civil(self, nuevo):
        self.estado_civil = nuevo

    def imprimir(self):
        print("Nombre:", self.nombre, self.apellidos)
        print("DNI:", self.dni)
        print("Estado civil:", self.estado_civil)


class Estudiante(Persona):
    def __init__(self, nombre, apellidos, dni, estado_civil, curso):
        super().__init__(nombre, apellidos, dni, estado_civil)
        self.curso = curso

    def matricular(self, nuevo_curso):
        self.curso = nuevo_curso

    def imprimir(self):
        print(" ESTUDIANTE ")
        super().imprimir()
        print("Curso:", self.curso)


class Empleado(Persona):
    def __init__(self, nombre, apellidos, dni, estado_civil, anio, despacho):
        super().__init__(nombre, apellidos, dni, estado_civil)
        self.anio = anio
        self.despacho = despacho

    def reasignar_despacho(self, nuevo):
        self.despacho = nuevo

    def imprimir(self):
        super().imprimir()
        print("Año de incorporación:", self.anio)
        print("Despacho:", self.despacho)


class Profesor(Empleado):
    def __init__(self, nombre, apellidos, dni, estado_civil, anio, despacho, departamento):
        super().__init__(nombre, apellidos, dni, estado_civil, anio, despacho)
        self.departamento = departamento

    def cambiar_departamento(self, nuevo):
        self.departamento = nuevo

    def imprimir(self):
        print(" PROFESOR ")
        super().imprimir()
        print("Departamento:", self.departamento)


class PersonalServicio(Empleado):
    def __init__(self, nombre, apellidos, dni, estado_civil, anio, despacho, seccion):
        super().__init__(nombre, apellidos, dni, estado_civil, anio, despacho)
        self.seccion = seccion

    def trasladar_seccion(self, nueva):
        self.seccion = nueva

    def imprimir(self):
        print(" PERSONAL DE SERVICIO ")
        super().imprimir()
        print("Sección:", self.seccion)


class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.profesores = []
        self.personal = []

    # Alta: según el tipo de objeto, lo mete en su lista
    def alta(self, persona):
        if isinstance(persona, Estudiante):
            self.estudiantes.append(persona)
        elif isinstance(persona, Profesor):
            self.profesores.append(persona)
        elif isinstance(persona, PersonalServicio):
            self.personal.append(persona)

    # Baja: busca por DNI en las tres listas y lo elimina
    def baja(self, dni):
        for lista in (self.estudiantes, self.profesores, self.personal):
            for p in lista:
                if p.get_dni() == dni:
                    lista.remove(p)
                    print("Baja realizada:", dni)
                    return
        print("No se encontró el DNI", dni)

    def imprimir(self):
        for lista in (self.estudiantes, self.profesores, self.personal):
            for p in lista:
                p.imprimir()
                print()


# ---------- Programa de prueba ----------
f = Facultad()

e = Estudiante("Ana", "Pérez", "111A", "soltera", 1)
p = Profesor("Luis", "García", "222B", "casado", 2010, 15, "matemáticas")
s = PersonalServicio("Marta", "López", "333C", "soltera", 2018, 3, "biblioteca")

f.alta(e)
f.alta(p)
f.alta(s)
f.imprimir()

# Probar los métodos pedidos
e.cambiar_estado_civil("casada")
e.matricular(2)
p.reasignar_despacho(20)
p.cambiar_departamento("arquitectura")
s.trasladar_seccion("secretaría")

print("- DESPUÉS DE LOS CAMBIOS - ")
f.imprimir()

f.baja("222B")
print("- DESPUÉS DE LA BAJA -")
f.imprimir()