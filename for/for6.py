# Solicita una cantidad indeterminada de calificaciones hasta que el usuario ingrese -1.

# Definitivamente esto era más fácil de hacer con while.

def calculadora_promedio():
    suma = 0
    for i in range(100):
        calificacion = float(input("Introduce una calificación (-1 para terminar): "))
        if calificacion == -1.0:
            return (suma / (i))
            break

        elif 0 <= calificacion <= 100:
            suma += calificacion
        else:
            print("Calificación inválida. Debe estar entre 0 y 100.")

def main():
    print("Bienvenido a la calculadora de promedio de calificaciones.")
    print(f"El promedio de las calificaciones es: {calculadora_promedio()}")

main()