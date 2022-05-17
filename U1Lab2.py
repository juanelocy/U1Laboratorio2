#funcion 
def suma():
    a=int(input("Ingrese un numero: "))
    b=int(input("Ingrese un numero anterior:"))
    #validacion para ingresar el numero correcto
    #Si b es menor que a se aplica el if
    if (a>b):
        total=a+b
        print("El numero actual es: ", a)
        print("El numero anterior es: ", b)
        print("La suma de los dos numeros es: ",total)
    #Si b es mayor que a se cumple el else y se acaba el programa
    #No se ejecuta la suma
    else:
        print("El numero ", b, " no es anterior a ",a)

#Impresion de la funcion
print(suma())