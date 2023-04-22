import math

def factorial(n):
    """
    Calcula el factorial de un número entero n.

    Args:
        n (int): El número del cual se desea calcular el factorial.

    Returns:
        int: El factorial de n.
    """
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def aproximacion_seno(x, n):
    """
    Calcula una aproximación de la función seno alrededor de 0 para cualquier valor x
    utilizando los primeros n términos de la serie de Maclaurin.

    Args:
        x (float): El valor de x para el cual se desea aproximar el seno.
        n (int): El número de términos de la serie de Maclaurin a utilizar en la aproximación.

    Returns:
        float: La aproximación de sen(x) utilizando los n términos de la serie de Maclaurin.
    """
    seno_aproximado = 0
    for i in range(0, n+1):
        termino = (-1)**i * x**(2*i + 1) / factorial(2*i + 1)
        seno_aproximado += termino
    return seno_aproximado

def senoreal(x):
    """
    Calcula el valor real de la función seno para un valor de x dado.

    Args:
        x (float): El valor de x para el cual se desea calcular el seno.

    Returns:
        float: El valor de sen(x).
    """
    seno = math.sin(x)
    return seno

def calcularn(x):
    """
    Calcula el número de términos de la serie de Maclaurin necesarios para alcanzar un error menor
    que 0.001 en la aproximación del seno de x.

    Args:
        x (float): El valor de x para el cual se desea aproximar el seno.

    Returns:
        int: La cantidad de términos necesarios para alcanzar el error deseado.
    """
    n = 0
    seno_real = senoreal(x)
    aprox = aproximacion_seno(x, n)
    error = abs(aprox - seno_real)
    while error > 0.001:
        n += 1
        aprox = aproximacion_seno(x, n)
        error = abs(aprox - seno_real)
    return n

if __name__ == "__main__":
    x = float(input("Ingrese un valor en radianes: "))
    n = int(input("Ingrese la cantidad de términos de la serie de Maclaurin: "))
    seno_real = senoreal(x)
    aprox = aproximacion_seno(x, n)
    error = abs(aprox - seno_real)
    caln = calcularn(x)
    print("Aproximación:" + str(aprox))
    print("Valor real:" + str(round(seno_real, 3)))
    print("Error:" + str(error))
    print("La cantidad de 'n' necesarios para un error menor al 0.001% son:", caln)

    