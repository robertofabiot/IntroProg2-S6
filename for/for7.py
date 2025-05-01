#Solicita un número positivo y cuenta cuántos dígitos tiene.

#Añadí una validación.

def contar_digitos(numero):
    contador = 0
    for i in str(numero):
        contador += 1
    return contador

def main():
    while True:
        try:
            numero = int(input("Introduce un número entero y positivo: "))
            if numero < 0:
                raise ValueError("El número debe ser positivo.")
            break
        except ValueError:
            print("El número debe ser entero y positivo. Intente de nuevo.")

    print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")

main()