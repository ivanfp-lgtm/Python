print('Dame una nota')
nota1 = float(input())
if nota1 < 0 or nota1 > 10 :
    print('La nota no es valida')
else:
    print('Dame otra nota')
    nota2 = float(input())
    if nota2 < 0 or nota2 > 10 :
        print('La nota no es valida')
    else:
        print('Dame otra nota')
        nota3 = float(input())
        if nota3 < 0 or nota3 > 10 :
            print('La nota no es valida')
        else:
            if nota1 < 4 and nota2 < 4 and nota3 < 4 :
                print('La nota final es 0')
            else:
                if nota1 < 4 or nota2 < 4 or nota3 < 4 :
                    print('La nota final es 2')
                else:
                    if nota1 >= 4 and nota2 >= 4 and nota3 >= 4 :
                        notaf = (nota1 * 0.3) + (nota2 * 0.2) + (nota3 * 0.5)
                        print(f'La nota final es {notaf}')