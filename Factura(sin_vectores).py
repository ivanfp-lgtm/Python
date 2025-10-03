print('Dame precios para hacer una factura, escribe 0 para finalizar el programa')
factura = 0
suma = float(input())
while suma < 0 or suma > 0 :
    factura += suma
    suma = float(input())
print(f'La factura final es de {factura:.2f}€')