# EL RETO 8
### Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.


```python
# Se utiliza un ciclo for para iterar desde el número 1 hasta el 100.
# En cada iteración se imprime el número actual y su cuadrado.
for i in range(1,101):
    print(i, "y su cuadrado es: " ,i**2)
```

### Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
# Imprimir números impares del 1 al 999
for i in range(1, 1000, 2):  # iterar desde 1 hasta 999 de dos en dos
    print(i)  # imprimir el número actual

# Imprimir números pares del 2 al 1000
for i in range(2, 1001, 2):  # iterar desde 2 hasta 1000 de dos en dos
    print(i)  # imprimir el número actual
```
### Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

```python
# Se solicita al usuario ingresar un número mayor que 2
x = int(input("Ingresa un número mayor que 2: "))

# Se itera desde x hasta 2, decrementando de 1 en 1
for i in range(x, 1, -1):
    # Si el número es par (es decir, su residuo al dividir entre 2 es cero), se imprime
    if i % 2 == 0:
        print(i) 
```

### Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.



```python
# Función para calcular el factorial de un número
def calcularfactorial(n):
    # Inicializar la variable factorial en 1
    factorial = 1
    # Bucle para multiplicar los números del 1 al n y calcular el factorial
    for i in range(1,n+1):
        factorial = i * factorial
        # Imprimir el factorial de cada número en el bucle
        print(i, "! =", factorial)
    # Devolver el factorial del número dado
    return factorial

# Pedir al usuario un número y calcular los factoriales de los números del 1 al n
if __name__ == "__main__":
    # Pedir al usuario que ingrese un número natural
    n = int(input("Ingrese un número natural: "))
    # Llamar a la función para calcular los factoriales y guardar el resultado en la variable "fact"
    fact = calcularfactorial(n)

```
### Calcular el valor de 2 elevado a la potencia n usando ciclos for.


```python
# Pedir al usuario el número hasta el cual quiere elevar 2 y asignarlo a la variable n
n = int(input("Ingresa hasta cuál número quieres elevar el 2: "))

# Inicializar la variable x en 1 para poder multiplicarla posteriormente
x = 1

# Bucle para calcular la potencia de 2
for i in range(0, n+1):
    x *= 2

# Imprimir el resultado de la potencia de 2
print("2 elevado a la potencia ", n, "es igual a: ", x)

```

### Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

```python
# Pedir al usuario un número natural y un número real
x = float(input("Ingrese un número real: "))
n = int(input("Ingrese a que numero quieres elevarlo: "))

# Inicializar la variable resultado en 1
resultado = 1

# Bucle para multiplicar el número real consigo mismo n veces y calcular la potencia
for i in range(n):
    resultado *= x

# Imprimir el resultado
print("El resultado de", x, "elevado a la", n, "es:", resultado)
```
### Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.


```python
# Función para calcular las tablas de multiplicar de un número
def calculartablas(n):
    # Inicializar la variable tabla en 1
    tabla = 1
    # Bucle para multiplicar el número por los números del 1 al 10 y calcular las tablas
    for i in range(1,11):
        tabla =  n * i
        print(str(n) + " * " + str(i) + " = " +str(tabla) )
    return tabla

# Bucle para imprimir las tablas del 1 al 10 utilizando la función calculartablas()
if __name__ == "__main__":
    n : int = 1
    for n in range(1,11):
        print("TABLA DEL " +str(n))
        tabla1 = calculartablas(n)
        n += 1
```

### Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

```python
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
```
### Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.


```python
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
```
### Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

```python
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
```



#### :D