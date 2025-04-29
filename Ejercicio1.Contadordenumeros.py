n = int(input("Ingresa un número entero positivo: "))

if n > 0:
    print(f"Números pares desde 1 hasta {n}:")
    for numero in range(1, n + 1):
        if numero % 2 == 0:
            print(numero)
else:
    print("Por favor, ingresa un número entero positivo.")
