N = int(input("Introduce el tamaño de la tabla: "))
tabla = []

print("Introduce los valores de la tabla:")
for i in range(N):
    fila = []
    for j in range(N):
        num = int(input(f"Valor en fila {i}, columna {j}: "))
        fila.append(num)
    tabla.append(fila)

es_identidad = True

for i in range(N):
    for j in range(N):
        if i == j:
            if tabla[i][j] != 1:
                es_identidad = False
        else:
            if tabla[i][j] != 0:
                es_identidad = False

if es_identidad:
    print("La tabla SÍ es una matriz identidad.")
else:
    print("La tabla NO es una matriz identidad.")