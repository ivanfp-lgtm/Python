# MiniArcade.py
import random
import time

def pedir_opcion():
    while True:
        op = input("Elige una opción: ").strip()
        if op in {"0", "1", "2", "3", "4"}:
            return op
        print("Opción no válida. Intenta de nuevo.")

def pedir_jugada():
    while True:
        ju = input("Elige tu jugada: ").strip()
        if ju in {"1", "2", "3"}:
            return ju
        print("Opción no válida. Intenta de nuevo.")

def pedir_dificultad():
    while True:
        dif = input("Elige tu dificultad: ").strip()
        if dif in {"1", "2", "3", "4"}:
            return dif
        print("Opción no válida. Intenta de nuevo.")

def juego_ppt():
    print('')
    print('Piedra, Papel o Tijera:')
    print('-----------------------')
    print('1) Piedra')
    print('2) Papel')
    print('3) Tijera')
    print('')
    jugada = pedir_jugada()
    if jugada == "1":
        jum = "Piedra"
    elif jugada == "2":
        jum = "Papel"
    elif jugada == "3":
        jum = "Tijera"

    jupc = random.randint(1, 3)
    if jupc == 1:
        jupcm = "Piedra"
    elif jupc == 2:
        jupcm = "Papel"
    elif jupc == 3:
        jupcm = "Tijera"

    if jugada == "1" and jupc == 3 or jugada == "2" and jupc == 1 or jugada == "3" and jupc == 2 :
        resultado = "Has ganado!"
    elif jugada == "1" and jupc == 1 or jugada == "2" and jupc == 2 or jugada == "3" and jupc == 3 :
        resultado = "Empate!"
    elif jugada == "1" and jupc == 2 or jugada == "2" and jupc == 3 or jugada == "3" and jupc == 1 :
        resultado = "Has perdido!"

    print('')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('')
    print(f'La jugada del BOT es {jupcm}')
    print(f'Tu jugada es {jum}')
    print('')
    print(f'{resultado}')
    return

    """
    Juega con el ordenador a piedra papel o tijera... 
    Tu eliges y elemento y el programa, de forma aleatoria otro ..
    ¿quien ganará de los dos ?
    """

def juego_adivina():
    print('')
    print('Adivina el número')
    print('-----------------')
    print('1) Fácil')
    print('2) Medio')
    print('3) Difícil')
    print('')

    dificultad = pedir_dificultad()
    print('')

    if dificultad == "1":
        limite = 20
        tiempo_limite = 30
        numero_secreto = random.randint(1, limite)
        print('Has elegido la dificultad fácil, tienes 30s para adivinar un número del 1 al 20')
    elif dificultad == "2":
        limite = 50
        tiempo_limite = 60
        numero_secreto = random.randint(1, limite)
        print('Has elegido la dificultad media, tienes 1 min para adivinar un número del 1 al 50')
    elif dificultad == "3":
        limite = 100
        tiempo_limite = 60
        numero_secreto = random.randint(1, limite)
        print('Has elegido la dificultad difícil, tienes 1 min para adivinar un número del 1 al 100')
    elif dificultad == "4":
        limite = 100
        tiempo_limite = 120
        numero_secreto = round(random.uniform(1, limite), 1)
        print('Has elegido la dificultad SECRETA imposible, tienes 2 min para adivinar un número del 1 al 100 con una cifra decimal')

    print('')
    inicio = time.time()

    while True:
        tiempo_pasado = time.time() - inicio
        if tiempo_pasado >= tiempo_limite:
            print('Tiempo!')
            print(f"El número secreto era: {numero_secreto}")
            print("")
            return

        intento = input("Introduce tu número: ")

        try:
            if dificultad == "4":
                intento = float(intento)
            else:
                intento = int(intento)
        except:
            print('Opción no válida. Intenta de nuevo.')
            continue

        if intento < 1 or intento > limite:
            print('')
            print(f'El número debe estar entre 1 y {limite}.')
            print('')
            continue

        if intento < numero_secreto:
            print('')
            print('Más alto!')
            print('')
        elif intento > numero_secreto:
            print('')
            print('Más bajo!')
            print('')
        else:
            tiempo_fin = round(time.time() - inicio, 2)
            print('')
            print(f'Correcto! Has adivinado el número en {tiempo_fin:.0f} segundos.')
            return
        
    """
    Este es el de clase!! 
    Adivina un numero en el menor tiempo dedicado !!! 
    """

def juego_calculo_mental_expres():
    print('')
    print('Cálculo mental')
    print('--------------')
    print('Responde correctamente el mayor número de operaciones en menos de 1 min')
    
    inicio = time.time()
    puntuacion = 0

    operadores = ["+", "-", "*"]

    while True:
        tiempo_pasado = time.time() - inicio
        if tiempo_pasado >= 60:
            print('')
            print('Tiempo!')
            print('')
            print(f'Puntuación final: {puntuacion} puntos')
            return

        op = random.choice(operadores)

        if op == "+":
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            resultado_correcto = a + b
        elif op == "-":
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            resultado_correcto = a - b
        elif op == "*":  # multiplicación
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            resultado_correcto = a * b

        print('')
        print(f'Operación: {a} {op} {b}')
        print('')
        respuesta = input('Respuesta: ')
        print('')

        try:
            respuesta = int(respuesta)
        except:
            print('Respuesta no válida. Fin del juego.')
            print('')
            print(f'Puntuación final: {puntuacion} puntos')
            return

        if respuesta == resultado_correcto:
            puntuacion += 1
            print('Correcto!')
        else:
            print(f'Incorrecto! La respuesta era {resultado_correcto}.')
            print('')
            print(f'Puntuación final: {puntuacion} puntos')
            return
    
    """
    Lanza un reto de cálculo mental con límite de tiempo total.
    - preguntas: nº de operaciones
    - tiempo_total: segundos para todo el test
    Devuelve la puntuación final (int).
    """

def juego_eco_invertido():
    print('')
    print('Eco invertido')
    print('-------------')
    print('')
    
    linea = input('Escribe algo: ')
    print('')

    invertida = linea[::-1]
    num_caracteres = len(linea)
    num_vocales = sum(1 for c in linea.lower() if c in 'aeiouáéíóúàèìòùü')

    print(f'Invertido: {invertida}')
    print('')
    print(f'Número de caracteres: {num_caracteres}')
    print('')
    print(f'Número de vocales: {num_vocales}')
    return
    
    """
    Pide líneas de texto y responde con:
      - cadena invertida
      - nº de caracteres y nº de vocales
    Finaliza si el usuario envía una línea vacía.
    """

def main():
    print("Bienvenido/a al Mini Arcade 👾")
    while True:
        print("\n=== MINI ARCADE ===")
        print("1) Piedra, Papel o Tijera")
        print("2) Adivina el número")
        print("3) Juego cálculo mental")
        print("4) Juego del eco invertido")
        print("0) Salir")
        
        opcion = pedir_opcion()
        if opcion == "1":
            juego_ppt()
        elif opcion == "2":
            juego_adivina()
        elif opcion == "3":
            #aqui faltan cosas
            juego_calculo_mental_expres()
        elif opcion == "4":
            juego_eco_invertido()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        time.sleep(0.8)

if __name__ == "__main__":
    main()
