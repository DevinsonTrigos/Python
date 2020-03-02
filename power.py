
import sys

aux=sys.argv[1].split("={")
po=sys.argv[2].split("=")
tipo=sys.argv[3]
set_name = aux[0]

def convertir(aux):

    lista = aux[1].split(",")
    lista[-1]=lista[-1].replace("}","")
    return lista

def potencia_dir():

   conjunto = convertir(aux)
   t_datos = len(conjunto)
   sw = 1

   if po[1] == '0':
       print("\n\t->Conjunto vacio = { Ø }\n\t")
   elif po[1] == '1' :
       print(f"\n\t->{set_name}**{po[1]}= {conjunto}\n\t")
   elif po[1] >= '2' or po[1]<='100':
       print(f"\n\t->{set_name}**{po[1]} = {producto_cartesiano(conjunto,sw)}\n\t")

   else :
       print("Error de limite en la potencia")


#def potencia(c):

   # if len(c) == 0:
      #  return [[]]
    #r = potencia(c[:-1])
    #return r + [s + [c[-1]] for s in r]
def producto_cartesiano(c,sw):

    from itertools import product
    lista = []
    if sw >= int('1'):
        for elemento in product(c, repeat=(int(po[1]))):
            #print(elemento, end=' , ')
            lista.append(elemento)

    else:
        print("Error")

    return lista

def directo(tipo):

    if tipo == '-vd':
        potencia_dir()
    elif tipo == '-vl':
        print("funcion en desarrollo")
    else:
        print("Error,  parametros no validos")

def mostrar():
    print("\n\t\t|| Potencia de un conjunto ||")
    print(f"\n\t->{set_name} = {convertir(aux)}")
    print(f"\n\t->Potencia = {po[1]}")
    directo(tipo)

mostrar()
