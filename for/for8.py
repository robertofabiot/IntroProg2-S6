# Implementa un menú con las opciones: 
# 1. Saludar 
# 2. Mostrar fecha 
# 3. Salir 

# Honestamente, aquí ya no sabía qué hacer con el for. 

def saludar():
    nombre = input("¿Cuál es tu nombre? ")
    print(f"¡Hola, {nombre}!")

def mostrar_fecha():
    from datetime import datetime
    fecha = datetime.now()
    print(f"Fecha actual: {fecha.strftime('%Y-%m-%d')}")

def main():
    print("Bienvenido.")
    print("""1. Saludar 
2. Mostrar fecha 
3. Salir""" )
    for i in range(1000):
        opcion = int(input("Elige una opción (1-3): "))
        if opcion == 1:
            saludar()
        elif opcion == 2:
            mostrar_fecha()
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

main()