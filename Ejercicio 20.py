def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print('Dame 2 números para calcular el MCD')
x = int(input('Introduce el primer número: '))
y = int(input('Introduce el segundo número: '))

print(f'El MCD de {x} y {y} es:', mcd(x, y))

rango = input('Introduce un número para ver si es primo, o un rango separado por espacios para ver los números primos que hay entre ellos: ').split()

if len(rango) == 1:
    n = int(rango[0])
    if esPrimo(n):
        print(f'{n} es primo.')
    else:
        print(f'{n} no es primo.')
else:
    inicio = int(rango[0])
    fin = int(rango[1])
    print(f'Números primos entre {inicio} y {fin}:')
    for i in range(inicio, fin + 1):
        if esPrimo(i):
            print(i, end=" ")
    print()