#parcia 1

import sys

A=sys.argv[1]
B=sys.argv[2]

def convertir(aux):

    lista = aux.split(",")
    lista[-1]=lista[-1].replace("}","")
    lista[0] = lista[0].replace("{", "")
    return lista



def main():
    print("\n\t\t|| Operaciones de conjuntos ||")
    lista1=convertir(A)
    lista2=convertir(B)
    print(f"\n\t{lista1}\n\t{lista2}")
    Union(lista1, lista2)
    #diferencia(lista1,lista2)

def Union(A, B):
    c1=set(A)
    c2=set(B)
    result= c1.union(c2)
    print(result)

main()
#def Diferencia (A,B):
    # A-B

