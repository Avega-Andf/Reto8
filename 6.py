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