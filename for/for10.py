#Calcula y muestra la suma de los números impares del 1 al 100. 

def suma_impares():
    suma = 0
    for i in range(1, 101):
        if i % 2 != 0:
            suma += i
    return suma

def main():
    print("La suma de los números impares del 1 al 100 es:", suma_impares())

main()