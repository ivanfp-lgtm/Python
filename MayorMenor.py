print('Dime la cantidad de números que vas a introducir')
N = int(input())
numeros = []
print('Escribe los números')
for i in range(N):
    num = float(input())
    while num < 0:
        print("El número tiene que ser positivo")
        num = float(input())
    numeros.append(num)
mayor = max(numeros)
menor = min(numeros)
print(f"El número mayor es: {mayor:.0f}")
print(f"El número menor es: {menor:.0f}")