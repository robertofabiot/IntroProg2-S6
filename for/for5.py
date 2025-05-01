# Genera un número aleatorio entre 1 y 10. El usuario debe adivinarlo. El programa da 
# pistas: "mayor" o "menor". 

# Este programa generalmente es hecho con while. El bucle for fue usado para poner un
# límite de intentos. 

# Otra forma que se me ocurrió para hacerlo usando for es poniendo
# el range(1,10) y que verificara si i == numero_usuario, pero lo veo poco práctico.

import random

def intento(numero_usuario):
    numero = random.randint(1, 10)
    for i in range(2):
        if numero_usuario == numero:
            print("¡Has adivinado el número!")
            print(f"Te tomó {i+1} intentos.")
            break
        elif numero_usuario < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        numero_usuario = int(input("Introduce otro número: "))
    
    if i == 1:
        print("Lo siento, has agotado tus intentos.")
        print(f"El número era: {numero}")


def main():
    print("Adivina el número entre 1 y 10. Tienes 3 intentos.")
    numero_usuario = int(input("Introduce un número: "))
    intento(numero_usuario)

main()