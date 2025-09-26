print('Dame una nota')
nota = float(input())
if nota < 0 or nota >10 :
    print('La nota no es valida')
else:
    if nota >= 9 and nota <= 10 :
        print('Sobresaliente')
    else:
        if nota >= 7 and nota < 9 :
            print('Notable')
        else:
            if nota >= 6 and nota < 7 :
                print('Bien')
            else:
                if nota >= 5 and nota < 6 :
                    print('Suficiente')
                else:
                    print('Insuficiente')