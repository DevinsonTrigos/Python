
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
   cont = int(po[1])
   lista =[]
   if po[1] == '0':
       print("\n\t->Conjunto vacio = { Ø }\n\t")
       lista.append(conjunto)
       crear_archivo(lista)
   elif po[1] == '1' :
       print(f"\n\t->{set_name}**{po[1]}= {conjunto}\n\t")
       lista.append(conjunto)
       crear_archivo(lista)
   elif po[1] >= '2' or po[1]<='100':
       print(f"\n\t->{set_name}**{po[1]} = {producto_cartesiano(conjunto,cont)}\n\t")
       lista.append(producto_cartesiano(conjunto,cont))
       crear_archivo(lista)
   else :
       print("Error de limite en la potencia")


#def potencia(c):

   # if len(c) == 0:
      #  return [[]]
    #r = potencia(c[:-1])
    #return r + [s + [c[-1]] for s in r]

def potencia_uno_uno():

    conjunto = convertir(aux)
    t_datos = len(conjunto)
    sw = 1
    lista=[]
    if po[1] >= '0':
        print("\n\t->Conjunto vacio = { Ø }\n\t")
        lista.append(conjunto)
        crear_archivo(lista)
    if po[1] >= '1':
        print(f"\n\t->{set_name}^1= {conjunto}\n\t")
        lista.append(conjunto)
        crear_archivo(lista)
    if po[1] >= '2' or po[1] <= '100':
        sw=2
        i=2
        while i <= int(po[1]):
            print(f"\n\t->{set_name}^{i} = {producto_cartesiano(conjunto, i )}\n\t")
            lista.append(producto_cartesiano(conjunto, i))
            crear_archivo(lista)
            i +=1

    else:
        print("Error de limite en la potencia")


def producto_cartesiano(c,cont):

    from itertools import product
    lista = []
    for elemento in product(c, repeat=(cont)):

            src=''.join(elemento)
            lista.append(src)

    return lista

def directo(tipo):

      if tipo[0] == '-':
           potencia_dir()
      elif tipo[0] == '+':
           potencia_uno_uno()
      else:
            print("Error,  parametros no validos")


def crear_archivo(lista):

     from io import open
     # creacion
     archivo_texto = open("conjunto_potencia.txt", "w")
     archivo_texto.write(f"\n\t {set_name}=")
     for elemento in lista:
         archivo_texto.write(f" {elemento} ")

     archivo_texto.write("\n ")
     archivo_texto.close()

     print("\n\n\t\tLos datos se han enviado ha tu archivo conjunto_potencia.txt")

def mostrar():
    print("\n\t\t|| Potencia de un conjunto ||")
    print(f"\n\t->{set_name} = {convertir(aux)}")
    print(f"\n\t->Potencia = {po[1]}")
    directo(tipo)

mostrar()
