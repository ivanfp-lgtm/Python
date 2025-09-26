print('Dime cual es tu edad')
edad = int(input())
if edad > 120 or edad < 0 :
    print('Esta edad no es valida')
else:
    if edad < 18 :
        print('Menor de edad')
    else:
        print('Mayor de edad')