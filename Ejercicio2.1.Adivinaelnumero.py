print("Adivina el numero secreto.")
print("Intenta acertar en el menor numero de intentos, el numero secreto.")

Intentos = 0
Adivinado = False
Numero_secreto=2

while not Adivinado:
	Intento = int(input("Ingresa tu intento: "))
	Intentos += 1

	if Intento == Numero_secreto:
		Adivinado = True
		print (f"Felicidades adivinaste el numero secreto.")
		print(f"Lo lograste en {Intentos} intentos")
	else:
		print("El numero ingresado no es correcto, vuelve a intentarlo")
		


 