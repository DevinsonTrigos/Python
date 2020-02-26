class Vehiculos():
    def __init__(self,marca,modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha= True

    def acelerar(self):
        self.acelera= True

    def frenar(self):
        self.frena= True

    def estado(self):
        print(f"Marca: {self.marca} \n Modelo: {self.modelo} \n"
              f"Marcha: {self.enmarcha} \n Acelerando: {self.acelera} \n"
              f"Frenando: {self.frena}")

class VElectricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.auntonomia = 100

    def cargarEnergia(self):
        self.cargado = True

class coche(Vehiculos):
    def desplazamiento(self):
        print("me desplazo utilizando 4 ruedas")


class moto(Vehiculos):
    stun=""
    def Stun(self):
        self.stun = "llevo la moto parada"
    def desplazamiento(self):
        print("me desplazo utilizando 2 ruedas")
    def estado(self):#sobreescribo para agragar una propiedad exclusiva de las  motos
        print(f"Marca: {self.marca} \n Modelo: {self.modelo} \n"
              f"Marcha: {self.enmarcha} \n Acelerando: {self.acelera} \n"
              f"Frenando: {self.frena} \n Stun: {self.stun}" )

class Furgoneta(Vehiculos):
    def desplazamiento(self):
        print("me desplazo utilizando 6 ruedas")
    def carga(self,cargar):
        self.cargado = cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return  "la furgoneta esta vacia"


mimoto=moto("Honda","cbr")
mimoto.Stun()
mimoto.estado()

mifurgoneta= Furgoneta("Renault","Kango")
print(mifurgoneta.carga(True))

print(isinstance(mimoto,Vehiculos))#COMPROBAR QUE UN OBJETO PERTENECE A UNA CLASE



#__________________HERENCIA MULTIPLE_________________________
class bicicletaElectrica(VElectricos,Vehiculos):
         pass

mibici = bicicletaElectrica("yamaha","swe43")
print(mibici.marca)
print(mibici.cargarEnergia())

#_________________POLIMORFISMO____________________
mivehiculo = moto("suzuki","gixer160")
mivehiculo.desplazamiento()
mivehiculo1 = coche("toyota","350")
mivehiculo1.desplazamiento()
mivehiculo2 = Furgoneta("mazda","djh458")
mivehiculo2.desplazamiento()

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

vehiculo=moto("ferrary","580")#

desplazamientoVehiculo(vehiculo)