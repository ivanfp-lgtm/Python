print('Adivina el número entre en 1 y el 10')
numero = int(input())
while numero < 7 or numero > 7 :
    if numero < 0 or numero > 10:
        print('Este número no es valido')
        print('Prueva uno diferente')
        numero = int(input())
    else:
        if numero < 7 :
            print('Muy bajo')
            print('Intentalo otra vez')
            numero = int(input())
        else:
            if numero > 7 :
                print('Muy alto')
                print('Intentalo otra vez')
                numero = int(input())
print('Adivinaste el número')