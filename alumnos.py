class Persona():
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.edad = input("Edad: ")
        self.nacionalidad = input("Nacionalidad:")

class Empleado(Persona):
    def __init__(self):
        # self.nombre = input("nombre del alumno:")
        super().__init__()
        self.cargo = input("Cargo:")
        self.salario = input("Salario:")

    def resultado(self):
        if int(self.salario) < 500000:
            print("Usted es POBRE\n busque mejores ingresos")
        elif int(self.salario) < 2000000:
            print("Usted es de Clase MEDIA\n")
        else:
            print("Usted es RICO\n AYUDE AL MUNDO")

class Independiente(Persona):
    def __init__(self):
        # self.nombre = input("nombre del alumno:")
        super().__init__()
        self.oficio = input("Negocio:")
        self.ingresos = input("Ingresos:")

    def resultado(self):
        if int(self.ingresos) < 1000000:
            print("Su negocio puede ir a la QUIEBRA\n busque la forma de impulsarlo")
        elif int(self.ingresos) < 5000000:
            print("Su negocio es estable\n cree campañas de marketing")
        else:
            print("Su negocio es muy buneo\n Busque la forma de expandirse")

class Alumno(Persona):

    def __init__(self):
        #self.nombre = input("nombre del alumno:")
        super().__init__()
        self.nota =  input("nota final:")

    def imprimir(self):
        print(f"Alumno: {self.nombre} \n Nota: {self.nota} \n")

    def resultado(self):
        if int(self.nota) < 300 :
            print("Reprobado\n ")

        else:
            print("Aprovado")

#polimorfismo#
def resultadoPersona(persona):
    persona.resultado()

sw = 1

while sw <= 10:
    sw = sw + 1
    print("___________________________\nTIPOS DE PERSONAS")
    print("a. ESTUDIANTE")
    print("b. EMPLEADO")
    print("c. INDEPENDIENTE")
    op = input("Digite el ipo de persona:")
    if op== "a":
        print("...Registrando Alumno...")
        persona = Alumno()
        #persona.resultado()#
        resultadoPersona(persona)
    elif op =="b":
        print("...Registrando Empleado...")
        persona = Empleado()
       # persona.resultado()#
        resultadoPersona(persona)
    elif op =="c":
        print("...Registrando Independiente...")
        persona = Independiente()
       # persona.resultado()#
        resultadoPersona(persona)
    else:
       print("...programa en proceso...")



