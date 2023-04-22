import math

def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero n.

    Args:
    - n (int): El número entero del cual se desea calcular el factorial.

    Returns:
    - int: El factorial de n.
    """
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def aproximacion(x: float, n: int) -> float:
    """
    Aproxima el valor de e^x utilizando una serie de Taylor de n términos.

    Args:
    - x (float): El exponente de la función exponencial.
    - n (int): El número de términos de la serie de Taylor a utilizar.

    Returns:
    - float: Una aproximación del valor de e^x.
    """
    aprox = 0
    for i in range(0,n+1):
        aprox += (x**i) / factorial(i)
    return aprox

def real(x: float) -> float:
    """
    Calcula el valor real de la función exponencial e^x.

    Args:
    - x (float): El exponente de la función exponencial.

    Returns:
    - float: El valor real de e^x.
    """
    return math.e**x

def calcularn(x: float) -> int:
    """
    Calcula el número de términos necesarios para que la aproximación sea precisa hasta 0.1%.

    Args:
    - x (float): El exponente de la función exponencial.

    Returns:
    - int: El número de términos necesarios para que la aproximación sea precisa hasta 0.1%.
    """
    n = 0
    error = 1
    while error > 1e-6:  # mientras el error sea mayor a 0.1%
        n += 1
        approx = aproximacion(x, n)
        verdad = real(x)
        error = abs(verdad - approx) / verdad
    return n
    
if __name__ == "__main__":
    x = float(input("Ingrese x: "))
    n = int(input("Ingrese n: "))
    verdad = real(x)
    approx = aproximacion(x, n)
    error = abs(verdad - approx) / verdad
    nnecesaria = calcularn(x)

    print("El valor real es: " +str(round(verdad,9))+ ", El valor aproximado es: " +str(round(approx,9))+ ", y El error relativo entre estos es: " +str(round(error*100, 6)) + "%." )
    print("El valor de n necesario para alcanzar un error relativo menor al 0.1% es:", nnecesaria)