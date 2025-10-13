factura = []
print('Dame precios para hacer una factura, escribe 0 para finalizar el programa')
suma = float(input())
while suma < 0 or suma > 0 :
    factura.append(suma)
    suma = float(input())
total = sum(factura)
print(f'La factura final es de {total:.2f}€')