import random

numero_aleatorio = random.randint(1, 20)

print("He generado un número entre 1 y 20. ¡Intenta adivinarlo!")

intentos = 0
adivinado = False


while not adivinado:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1
    
    if intento == numero_aleatorio:
        adivinado = True
        print(f"¡Felicidades! Adivinaste el número {numero_aleatorio}.")
        print(f"Lo lograste en {intentos} intentos.")

    else:
        print("El número no es correcto, vuelve a intentarlo.")