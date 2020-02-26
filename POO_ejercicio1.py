class coche():

    #METODO CONSTRUCTOR#
    def __init__(self):

       self.__largochasis = 250
       self.__anchochasis = 120
       self.__ruedas = 4 #encapsulamiento#
       self.__enmarcha = False

    def arranque(self, arrancamos):
        self.enmarcha = arrancamos

        if (self.enmarcha):
            chequeo = self.__chequeo_interno()

        if (self.enmarcha and chequeo):
            return "el coche esta en movimiento"

        elif(self.__enmarcha and chequeo== False):
            return "algo anda mal en el chequeo,NO podemos arrancar"

        else:
            return "el coche no se ha movido"

    def estado(self):
        print(
            f"el coche tiene {self.__ruedas} ruedas un ancho de {self.__anchochasis} m  y un largo de {self.__largochasis} ")

    def __chequeo_interno(self):
        print("REALIZANDO CHEQUEO INTERNO")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="ok"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="ok"):
            return  True
        else:
            return False


print(" -----------primer objeto-------------")
micoche = coche()
print(micoche.arranque(True))
micoche.estado()

print(" -----------Segundo objeto-------------")
micoche2 = coche()
print(micoche2.arranque(False))
micoche2.ruedas=6
micoche2.estado()