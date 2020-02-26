print("__________CALCULADORA_______ ")

def suma(x,y):
	resultado= x+y
	return resultado

def resta(x,y):
	resultado=x-y
	return resultado

def multiplicacion(x,y):
	resultado=x*y
	return resultado

def division(x,y):
	resultado=x/y
	return resultado

sw = 10

while sw != 0 :
    x = int(input("valor 1: "))
    y = int(input("valor 2: "))
    print("Operaciones")
    print("a.) suma")
    print("b.) resta")
    print("c.) multiplicacion")
    print("d.) division")

    operacion = input("seleccione una opcion : ")

    if  operacion == "a":
        print(f"el resultado de la suma es: {suma(x,y)}")
    elif  operacion == "b":
        print(f"el resultado de la resta es: {resta(x,y)}")
    elif operacion == "c":
        print(f"el resultado de la suma es: {multiplicacion(x, y)}")
    elif operacion == "d":
        print(f"el resultado de la suma es: {division(x, y)}")
    else:
        print("ERROR, Selecciono una opcion no valida")

    operacion = input("digite 0 para terminar  y cualquier otra tecla para continuar")


