#Leer dos n�meros e imprimir los n�meros entre ellos
def mostrar_numeros(inicio=0, fin=0):
    if(inicio<fin):
        for i in range(inicio, fin+1):
            print(i, end=" ")
    else:
        for i in range(fin, inicio+1):
            print(i, end=" ")
        
def main():
    inicio = int(input("Ingrese el primer n�mero: "))
    fin = int(input("Ingrese el segundo n�mero: "))
    mostrar_numeros(inicio, fin)

main()