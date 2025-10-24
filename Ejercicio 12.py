print('Introduce una secuencia de números separados por espacios')
lista = input()
numeros = [float(num) for num in lista.split()]
suma_total = sum(numeros)
print(f'La suma total es {suma_total:.2f}')
