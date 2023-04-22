# Pedir al usuario el número hasta el cual quiere elevar 2 y asignarlo a la variable n
n = int(input("Ingresa hasta cuál número quieres elevar el 2: "))

# Inicializar la variable x en 1 para poder multiplicarla posteriormente
x = 1

# Bucle para calcular la potencia de 2
for i in range(0, n+1):
    x *= 2

# Imprimir el resultado de la potencia de 2
print("2 elevado a la potencia ", n, "es igual a: ", x)
