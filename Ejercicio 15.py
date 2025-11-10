numeros = []
while True:
    n = float(input("Escribe un número (0 para terminar): "))
    if n == 0:
        break
    numeros.append(n)

buscar = float(input("¿Qué número quieres buscar? "))
posiciones = []

for i in range(len(numeros)):
    if numeros[i] == buscar:
        posiciones.append(i)

if len(posiciones) == 0:
    print("Ese número no aparece en la lista.")
else:
    print("El número aparece en las posiciones:", posiciones)