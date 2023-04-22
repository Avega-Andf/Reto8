import math

def aproximacion_atan(x= float, n= float) -> float:
    """Calcula una aproximación de la función arcotangente alrededor de 0 para cualquier valor x utilizando los primeros n términos de la serie de Maclaurin."""
    arcotangente_aproximado = 0
    for i in range(0,n+1):
        termino = (-1)**i * x**(2*i + 1) / (2*i + 1)
        arcotangente_aproximado += termino
    return arcotangente_aproximado

def arcotangentereal(x = float)-> float:
    arcotangente = math.atan(x)
    return arcotangente


def calcularn(x):

    n = 0
    arct_real = arcotangentereal(x)
    aprox = aproximacion_atan(x, n)
    error = abs(aprox - arct_real)
    while error > 0.001:
        n += 1
        aprox = aproximacion_atan(x, n)
        error = abs(aprox - arct_real)
    return n
if __name__ == "__main__":
    x = 2
    while x > 1 or x < -1:
        x = float(input("Ingrese un valor en radianes dentro del rango [-1,1]: "))
        if x > 1 or x < -1:
            print("El numero x ingresado no pertenece al rango [-1,1]")
    n = int(input("Ingrese la cantidad de términos de la serie de Maclaurin: "))
    atan_real = arcotangentereal(x)
    aprox = aproximacion_atan(x, n)
    error = abs(aprox - atan_real)
    caln = calcularn(x)
    print("Aproximación:" + str(aprox))
    print("Valor real:" + str(round(atan_real, 3)))
    print("Error:" + str(error))
    print("La cantidad de 'n' necesarios para un error menor al 0.001% son:", caln)

    
