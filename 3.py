# Se solicita al usuario ingresar un número mayor que 2
x = int(input("Ingresa un número mayor que 2: "))

# Se itera desde x hasta 2, decrementando de 1 en 1
for i in range(x, 1, -1):
    # Si el número es par (es decir, su residuo al dividir entre 2 es cero), se imprime
    if i % 2 == 0:
        print(i)