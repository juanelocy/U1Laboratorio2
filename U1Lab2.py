def suma():
    a=int(input("Ingrese un numero: "))
    b=int(input("Ingrese un numero anterior:"))
    if (a>b):
        total=a+b
        print("El numero actual es: ", a)
        print("El numero anterior es: ", b)
        print("La suma de los dos numeros es: ",total)
    else:
        print("El numero ", b, " no es anterior a ",a)

print(suma())