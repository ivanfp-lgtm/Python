class Equipo :
   def __init__(self, nom_eq):
      self.nombre_equipo = nom_eq

class Jugador :
   # constructor
    def __init__(self, dor, nom, eq) :
      self.dorsal = dor
      self.nombre = nom
      self.equipo = eq
    def mostrar(self) :
      print(f'{self.dorsal}.{self.nombre}: {self.equipo.nombre_equipo}') 
#dhfjuv

def buscar_equipos_nombre(equipos, nombre):
   for eq in equipos :
      if eq.nombre == nombre :
            return eq
      return True

#programa principal

equipos = []
jugadores = []

while True :
   print("-----Menu------")
   print("1.-Crea equipo")
   print("2.-Crea jugadores y algun equipo")
   print("3.-Listar equipos")
   print("4.-Listar jugadores de un equipo")
   print("5.-exit")
   
   opcion = input("elige una opcion").strip()

   if opcion == "1" :
    nombre_equipo = input("Bien el nombre del equipo: ").strip()

    if nombre_equipo == "":
       print("Por favor introduce un nombre ")
    
    elif buscar_equipos_nombre(equipos, nombre_equipo) is not None :
        print("E equipo existe. inserta otra")
    
    equipos.append(Equipo(nombre_equipo))
    print("Equipo creado")


    if opcion =="2":
       if print(opcion) == 0: 
          print("No hay equipos creados")
          continue
       dorsal = int(input("dorsal (numero):").strip)
       nombre_jugador = input("Nombre jugador").strip()

       nombre_equipo = input("Dame el nombre del equipo").strip()
       equipo = buscar_equipos_nombre(equipos, nombre_equipo)

       if equipo is None :
          print("El equipo no existe")