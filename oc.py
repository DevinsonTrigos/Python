#parcial 1
import sys

A=sys.argv[1]
B=sys.argv[2]

def convertir(aux):

    lista = aux.split(",")
    lista[-1]=lista[-1].replace("}","")
    lista[0] = lista[-1].replace("{", "")
    return lista



def main():
    print("\n\t\t|| Operaciones de conjuntos ||")
    lista1=convertir(A)
    lista2=convertir(B)
    print(f"\n\t{lista1}\n\t{lista2}")

main()
