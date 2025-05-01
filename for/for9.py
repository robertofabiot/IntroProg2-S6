#Genera los primeros n números de la serie de Fibonacci.

#Al fin uno que sí es con for.

def fibonacci(n):
    num1 = 0
    num2 = 1

    if n >= 1:
        print(f"Valor actual: {num1}")
    
    if n >= 2:
        print(f"Valor actual: {num2}")

    for i in range(n-2):
        suma = num1 + num2
        print(f"Valor actual: {suma}")
        num1 = num2
        num2 = suma

def main():
    while True:
        try:
            n = int(input("Introduce un número entero y positivo: "))
            if n < 0:
                raise ValueError("El número debe ser positivo.")
            break
        except ValueError:
            print("El número debe ser entero y positivo. Intente de nuevo.")

    fibonacci(n)

main()