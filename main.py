print("sumar 2 numeros")
num1 = input("Ingrese numero 1: ")
num2 = input("Ingrese numero 2: ")
try:
    suma = int(num1) + int(num2)
    #int -> transformar a numero entero
    print(f"la suma es: {suma} y {suma}, ademas es {suma}")
    #la "f" es para mostrar variables entre {}, en vez de usar la coma (,). es más práctico
except BaseException as error:
    #si hay un error, pasa lo de abajo, en vez de "caerse"
    print("ingreso erroneo de datos")
    
print("termino")
# ctr + s = grabar/guardar
