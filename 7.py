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
