def leer_personas(fichero):
    personas = []

    with open(fichero, "r", encoding="utf-8") as fich:
        for lineas in fich:
            token=lineas.strip().split(";")

            if len(token)!=2 :
                continue
            nombre = token[0]
            edad =int(token[1])

            personas.append((nombre, edad))
    return personas

def obtiene_edad(persona):
    return persona[1]

def persona_mas_joven(personas):
    joven = personas[0]

    for persona in personas :
        if obtiene_edad(persona) < obtiene_edad(joven) :
            joven = persona
    return joven

def persona_mas_viejo(personas):
    viejo = personas[0]

    for persona in personas :
        if obtiene_edad(persona) > obtiene_edad(viejo) :
            viejo = persona
    return viejo




# --- Programa principal ---
personas = leer_personas("personas.txt")

if personas:
    joven = persona_mas_joven(personas)
    vieja = persona_mas_viejo(personas)

    print(f"La persona más joven es: {joven[0]} ({joven[1]} años)")
    print(f"La persona más vieja es: {vieja[0]} ({vieja[1]} años)")

else:
    print("No hay datos válidos en el fichero.")