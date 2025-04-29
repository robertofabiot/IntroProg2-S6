def tabla_multiplicar(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num*i}")

def main():
    print("CALCULADORA DE TABLAS DE MULTIPLICAR")
    num = int(input("Ingrese el número: "))
    tabla_multiplicar(num)
    
main()