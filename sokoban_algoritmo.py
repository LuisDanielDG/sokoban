import os
import time

# Valores de los elementos del mapa
PERSONAJE = int(input("Personaje: "))
CAMINO = int(input("Camino: "))
PARED = int(input("Pared: "))
META = int(input("Meta: "))
PERSONAJE_META = int(input("Personaje_meta: "))

class Laberinto:
    """
        Los valores de cada elemento se piden al iniciar el programa:
        PERSONAJE
        CAMINO
        PARED
        META
        PERSONAJE_META
    """

    def __init__(self) -> None:
        self.pasos = 0
        self.elegirMapa()
        self.cargarNivel()

    def elegirMapa(self) -> None:
        #Muestra las opciones disponibles
        print("Mapas disponibles:")
        print("1 - mapa01")
        print("2 - mapa02")
        opcion = input("Elige un mapa: ")
        #Repite la pregunta hasta que la opcion sea valida
        while opcion != "1" and opcion != "2":
            opcion = input("Opcion no valida, elige 1 o 2: ")
        #Define el archivo del nivel segun la opcion
        if opcion == "1":
            self.archivo = "mapa01.lab"
        else:
            self.archivo = "mapa02.lab"
        #Limpia la consola despues de elegir
        os.system("cls" if os.name == "nt" else "clear")

    def imprimirMapa(self) -> None:
        #Asigna un simbolo a cada tipo de casilla
        simbolos = {
            PERSONAJE: "🙉 ",
            CAMINO: "   ",
            PARED: "🧱 ",
            META: "🔳 ",
            PERSONAJE_META: "🙈 ",
        }
        #Imprime el mapa fila por fila
        for fila in self.mapa:
            print("".join(simbolos[casilla] for casilla in fila))

    def cargarNivel(self) -> None:
        #Busca el archivo en la misma carpeta que el programa
        carpeta = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(carpeta, self.archivo)
        #Lee el archivo y convierte cada caracter en un numero
        self.mapa = []
        with open(ruta, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    self.mapa.append([int(caracter) for caracter in linea])
        #Crea una matriz que cuenta cuantas veces se piso cada casilla
        self.visitas = [[0 for casilla in fila] for fila in self.mapa]
        #Busca la posicion inicial del personaje
        for indice_fila, fila in enumerate(self.mapa):
            for indice_columna, casilla in enumerate(fila):
                if casilla == PERSONAJE or casilla == PERSONAJE_META:
                    #Actualiza la posicion del personaje
                    self.personaje_fila = indice_fila
                    self.personaje_columna = indice_columna
                    return

    def verificarMeta(self) -> bool:
        #Comprueba que el nivel tenga una meta
        hay_meta = any(casilla == META or casilla == PERSONAJE_META for fila in self.mapa for casilla in fila)
        if not hay_meta:
            print("El nivel no es valido, falta la meta.")
            return False

        #Comprueba si el personaje llego a la meta
        if self.posicionPersonaje() == PERSONAJE_META:
            self.imprimirMapa()
            print(f"Laberinto completado. Pasos realizados: {self.pasos}.")
            return False

        return True

    def posicionPersonaje(self, fila: int = 0, columna: int = 0, valor: int = None):
        #Calcula la posicion solicitada respecto al personaje
        f = self.personaje_fila + fila
        c = self.personaje_columna + columna
        if valor is None:
            #Devuelve el contenido de la casilla
            return self.mapa[f][c]
        #Actualiza el contenido de la casilla
        self.mapa[f][c] = valor

    def derecha(self) -> bool:
        if (
            self.posicionPersonaje() == PERSONAJE
            and (self.posicionPersonaje(0,1) == CAMINO or self.posicionPersonaje(0,1) == META)
        ):
            if self.posicionPersonaje(0,1) == CAMINO:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,CAMINO)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,1,PERSONAJE)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            else:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,CAMINO)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,1,PERSONAJE_META)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            #Indica que si se pudo mover
            return True
        elif (
            self.posicionPersonaje() == PERSONAJE_META
            and (self.posicionPersonaje(0,1) == CAMINO or self.posicionPersonaje(0,1) == META)
        ):
            if self.posicionPersonaje(0,1) == CAMINO:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,META)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,1,PERSONAJE)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            else:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,META)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,1,PERSONAJE_META)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            #Indica que si se pudo mover
            return True
        #Si no se cumplio ninguna condicion, no se pudo mover
        return False

    def izquierda(self) -> bool:
        if (
            self.posicionPersonaje() == PERSONAJE
            and (self.posicionPersonaje(0,-1) == CAMINO or self.posicionPersonaje(0,-1) == META)
        ):
            if self.posicionPersonaje(0,-1) == CAMINO:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,CAMINO)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,-1,PERSONAJE)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            else:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,CAMINO)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,-1,PERSONAJE_META)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            #Indica que si se pudo mover
            return True
        elif (
            self.posicionPersonaje() == PERSONAJE_META
            and (self.posicionPersonaje(0,-1) == CAMINO or self.posicionPersonaje(0,-1) == META)
        ):
            if self.posicionPersonaje(0,-1) == CAMINO:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,META)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,-1,PERSONAJE)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            else:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,META)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,-1,PERSONAJE_META)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            #Indica que si se pudo mover
            return True
        #Si no se cumplio ninguna condicion, no se pudo mover
        return False

    def abajo(self) -> bool:
        if (
            self.posicionPersonaje() == PERSONAJE
            and (self.posicionPersonaje(1,0) == CAMINO or self.posicionPersonaje(1,0) == META)
        ):
            if self.posicionPersonaje(1,0) == CAMINO:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,CAMINO)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(1,0,PERSONAJE)
                #Actualiza la posicion del personaje
                self.personaje_fila += 1
            else:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,CAMINO)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(1,0,PERSONAJE_META)
                #Actualiza la posicion del personaje
                self.personaje_fila += 1
            #Indica que si se pudo mover
            return True
        elif (
            self.posicionPersonaje() == PERSONAJE_META
            and (self.posicionPersonaje(1,0) == CAMINO or self.posicionPersonaje(1,0) == META)
        ):
            if self.posicionPersonaje(1,0) == CAMINO:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,META)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(1,0,PERSONAJE)
                #Actualiza la posicion del personaje
                self.personaje_fila += 1
            else:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,META)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(1,0,PERSONAJE_META)
                #Actualiza la posicion del personaje
                self.personaje_fila += 1
            #Indica que si se pudo mover
            return True
        #Si no se cumplio ninguna condicion, no se pudo mover
        return False

    def arriba(self) -> bool:
        if (
            self.posicionPersonaje() == PERSONAJE
            and (self.posicionPersonaje(-1,0) == CAMINO or self.posicionPersonaje(-1,0) == META)
        ):
            if self.posicionPersonaje(-1,0) == CAMINO:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,CAMINO)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(-1,0,PERSONAJE)
                #Actualiza la posicion del personaje
                self.personaje_fila -= 1
            else:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,CAMINO)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(-1,0,PERSONAJE_META)
                #Actualiza la posicion del personaje
                self.personaje_fila -= 1
            #Indica que si se pudo mover
            return True
        elif (
            self.posicionPersonaje() == PERSONAJE_META
            and (self.posicionPersonaje(-1,0) == CAMINO or self.posicionPersonaje(-1,0) == META)
        ):
            if self.posicionPersonaje(-1,0) == CAMINO:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,META)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(-1,0,PERSONAJE)
                #Actualiza la posicion del personaje
                self.personaje_fila -= 1
            else:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,META)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(-1,0,PERSONAJE_META)
                #Actualiza la posicion del personaje
                self.personaje_fila -= 1
            #Indica que si se pudo mover
            return True
        #Si no se cumplio ninguna condicion, no se pudo mover
        return False

    def intentarMover(self, direccion: int) -> bool:
        #Intenta moverse en la direccion indicada y devuelve si pudo
        if direccion == 0:
            return self.derecha()
        elif direccion == 1:
            return self.abajo()
        elif direccion == 2:
            return self.izquierda()
        else:
            return self.arriba()

    def mover(self) -> None:
        #Direcciones: 0 derecha, 1 abajo, 2 izquierda, 3 arriba
        cambios_fila = [0, 1, 0, -1]
        cambios_columna = [1, 0, -1, 0]
        #Cuenta una visita mas a la casilla donde esta el personaje
        self.visitas[self.personaje_fila][self.personaje_columna] += 1
        mejor_direccion = None
        menos_visitas = None
        #Busca la casilla vecina que no sea pared y tenga menos visitas
        for direccion in range(4):
            fila = self.personaje_fila + cambios_fila[direccion]
            columna = self.personaje_columna + cambios_columna[direccion]
            if self.mapa[fila][columna] != PARED:
                if menos_visitas is None or self.visitas[fila][columna] < menos_visitas:
                    menos_visitas = self.visitas[fila][columna]
                    mejor_direccion = direccion
        #Se mueve hacia esa casilla
        self.intentarMover(mejor_direccion)

    def algoritmo(self) -> None:
        #Limite de pasos para no quedar en un ciclo infinito
        self.pasos = 0
        limite = 1000
        #Repite hasta que el personaje llegue a la meta
        while self.posicionPersonaje() != PERSONAJE_META:
            self.mover()
            self.pasos += 1
            #Limpia la consola y muestra el avance
            os.system("cls" if os.name == "nt" else "clear")
            if self.posicionPersonaje() != PERSONAJE_META:
                self.imprimirMapa()
                #Pausa para poder ver el movimiento
                time.sleep(0.3)
            #Si se pasa del limite, el personaje no pudo llegar
            if self.pasos >= limite:
                print("El personaje no encontro la meta.")
                exit()

    def jugar(self) -> None:
        #Imprime el mapa antes del movimiento
        self.imprimirMapa()
        #Se llama al algoritmo para resolverlo
        self.algoritmo()


laberinto = Laberinto()
while laberinto.verificarMeta():
    laberinto.jugar()