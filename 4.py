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
