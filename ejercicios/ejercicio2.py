def pares_limite(num):
    for i in range(0, num+1):
        if i % 2 == 0:
            print(i)

def main():
    num = int(input("Ingrese el número límite: "))
    pares_limite(num)

main()