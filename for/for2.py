#Leer un número ingresado por el usuario
#Mostrar la letra a por cada número del 1 al número ingresado por el usuario

def mostrar_letra(numero):
    for i in range(1, numero+1):
        print("a"*i)

def main():
    num = int(input("Ingresa un número: "))
    mostrar_letra(num)

main()