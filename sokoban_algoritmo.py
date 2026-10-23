import os

class Sokoban:
    """
        0 - personaje
        1 - caja
        2 - pared
        3 - meta
        4 - camino
        5 - caja_meta
        6 - personaje_meta
    """

    def __init__(self) -> None:
        #Define los niveles disponibles
        self.niveles = [[
            [2,2,2,2,2,2,2,2],
            [2,4,4,0,4,4,4,2],
            [2,4,4,4,3,1,4,2],
            [2,4,4,1,4,3,4,2],
            [2,4,4,4,4,4,4,2],
            [2,2,2,2,2,2,2,2]
        ],
        [
            [2,2,2,2,2,2,2,2],
            [2,4,4,0,4,4,4,2],
            [2,4,1,4,3,1,4,2],
            [2,4,4,4,4,4,4,2],
            [2,4,4,4,4,4,3,2],
            [2,2,2,2,2,2,2,2]
        ],
        [
            [2,2,2,2,2,2,2,2],
            [2,4,4,4,4,4,4,2],
            [2,4,4,4,4,1,4,2],
            [2,4,4,4,4,4,4,2],
            [2,3,4,4,4,4,0,2],
            [2,2,2,2,2,2,2,2]
        ]]

        #Selecciona el primer nivel
        self.nivel_actual = 0
        self.cargarNivel()

    def imprimirMapa(self) -> None:
        #Asigna un simbolo a cada tipo de casilla
        simbolos = {
            0: "🙉 ",
            1: "📦 ",
            2: "🧱 ",
            3: "🔳 ",
            4: "   ",
            5: "✅ ",
            6: "🙈 ",
        }
        #Imprime el mapa fila por fila
        for fila in self.mapa:
            print("".join(simbolos[casilla] for casilla in fila))

    def cargarNivel(self) -> None:
        #Carga el nivel actual
        self.mapa = [fila[:] for fila in self.niveles[self.nivel_actual]]
        #Busca la posicion inicial del personaje
        for indice_fila, fila in enumerate(self.mapa):
            for indice_columna, casilla in enumerate(fila):
                if casilla == 0 or casilla == 6:
                    #Actualiza la posicion del personaje
                    self.personaje_fila = indice_fila
                    self.personaje_columna = indice_columna
                    return

    def verificarCajas(self) -> bool:
        #Cuenta las cajas y las metas del nivel
        cantidad_cajas = sum(casilla == 1 or casilla == 5 for fila in self.mapa for casilla in fila)
        cantidad_metas = sum(casilla == 3 or casilla == 5 or casilla == 6 for fila in self.mapa for casilla in fila)
        #Comprueba que el nivel tenga la misma cantidad de cajas y metas
        if cantidad_cajas == 0 or cantidad_cajas != cantidad_metas:
            print("El nivel no es valido, faltan cajas.")
            return False

        #Comprueba si quedan metas pendientes
        hay_metas_pendientes = any(casilla == 3 or casilla == 6 for fila in self.mapa for casilla in fila)
        if not hay_metas_pendientes:
            self.imprimirMapa()
            print("Nivel completado.")
            #Carga el siguiente nivel si esta disponible
            if self.nivel_actual + 1 < len(self.niveles):
                self.nivel_actual += 1
                self.cargarNivel()
                print(f"Nivel {self.nivel_actual + 1}.")
                return True
            #Indica que se completaron todos los niveles
            print("Juego completado.")
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
         
    def derecha(self) -> None:
        if (
            self.posicionPersonaje() == 0
            and ((self.posicionPersonaje(0,1) == 4 or self.posicionPersonaje(0,1) == 3)
            or ((self.posicionPersonaje(0,1) == 1 or self.posicionPersonaje(0,1) == 5)
            and (self.posicionPersonaje(0,2) == 4 or self.posicionPersonaje(0,2) == 3)))
        ):
            if self.posicionPersonaje(0,1) == 4:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,1,0)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            elif self.posicionPersonaje(0,1) == 3:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,1,6)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            elif self.posicionPersonaje(0,1) == 1:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba la caja
                self.posicionPersonaje(0,1,0)
                if self.posicionPersonaje(0,2) == 3:
                    #Coloca la caja donde estaba la meta
                    self.posicionPersonaje(0,2,5)
                elif self.posicionPersonaje(0,2) == 4:
                    #Coloca la caja donde estaba el camino
                    self.posicionPersonaje(0,2,1)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            else:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba la caja en la meta
                self.posicionPersonaje(0,1,6)
                if self.posicionPersonaje(0,2) == 3:
                    #Coloca la caja donde estaba la meta
                    self.posicionPersonaje(0,2,5)
                else:
                    #Coloca la caja donde estaba el camino
                    self.posicionPersonaje(0,2,1)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1

        elif(
             self.posicionPersonaje() == 6
               and ((self.posicionPersonaje(0,1) == 4 or self.posicionPersonaje(0,1) == 3)
               or ((self.posicionPersonaje(0,1) == 1 or self.posicionPersonaje(0,1) == 5)
               and (self.posicionPersonaje(0,2) == 4 or self.posicionPersonaje(0,2) == 3)))
        ):
            if self.posicionPersonaje(0,1) == 4:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,1,0)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            elif self.posicionPersonaje(0,1) == 3:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,1,6)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            elif self.posicionPersonaje(0,1) == 1:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba la caja
                self.posicionPersonaje(0,1,0)
                if self.posicionPersonaje(0,2) == 3:
                    #Coloca la caja donde estaba la meta
                    self.posicionPersonaje(0,2,5)
                else:
                    #Coloca la caja donde estaba el camino
                    self.posicionPersonaje(0,2,1)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            else:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba la caja en la meta
                self.posicionPersonaje(0,1,6)
                if self.posicionPersonaje(0,2) == 3:
                    #Coloca la caja donde estaba la meta
                    self.posicionPersonaje(0,2,5)
                else:
                    #Coloca la caja donde estaba el camino
                    self.posicionPersonaje(0,2,1)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1

    def izquierda(self) -> None:
        if (
            self.posicionPersonaje() == 0
            and ((self.posicionPersonaje(0,-1) == 4 or self.posicionPersonaje(0,-1) == 3)
            or ((self.posicionPersonaje(0,-1) == 1 or self.posicionPersonaje(0,-1) == 5)
            and (self.posicionPersonaje(0,-2) == 4 or self.posicionPersonaje(0,-2) == 3)))
        ):
            if self.posicionPersonaje(0,-1) == 4:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,-1,0)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            elif self.posicionPersonaje(0,-1) == 3:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,-1,6)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            elif self.posicionPersonaje(0,-1) == 1:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba la caja
                self.posicionPersonaje(0,-1,0)
                if self.posicionPersonaje(0,-2) == 3:
                    #Coloca la caja donde estaba la meta
                    self.posicionPersonaje(0,-2,5)
                elif self.posicionPersonaje(0,-2) == 4:
                    #Coloca la caja donde estaba el camino
                    self.posicionPersonaje(0,-2,1)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            else:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba la caja en la meta
                self.posicionPersonaje(0,-1,6)
                if self.posicionPersonaje(0,-2) == 3:
                    #Coloca la caja donde estaba la meta
                    self.posicionPersonaje(0,-2,5)
                else:
                    #Coloca la caja donde estaba el camino
                    self.posicionPersonaje(0,-2,1)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
        elif(
             self.posicionPersonaje() == 6
               and ((self.posicionPersonaje(0,-1) == 4 or self.posicionPersonaje(0,-1) == 3)
               or ((self.posicionPersonaje(0,-1) == 1 or self.posicionPersonaje(0,-1) == 5)
               and (self.posicionPersonaje(0,-2) == 4 or self.posicionPersonaje(0,-2) == 3)))
        ):
            if self.posicionPersonaje(0,-1) == 4:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,-1,0)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            elif self.posicionPersonaje(0,-1) == 3:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,-1,6)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1  
            elif self.posicionPersonaje(0,-1) == 1:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba la caja
                self.posicionPersonaje(0,-1,0)
                if self.posicionPersonaje(0,-2) == 3:
                    #Coloca la caja donde estaba la meta
                    self.posicionPersonaje(0,-2,5)
                else:
                    #Coloca la caja donde estaba el camino
                    self.posicionPersonaje(0,-2,1)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            else:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba la caja en la meta
                self.posicionPersonaje(0,-1,6)
                if self.posicionPersonaje(0,-2) == 3:
                    #Coloca la caja donde estaba la meta
                    self.posicionPersonaje(0,-2,5)
                else:
                    #Coloca la caja donde estaba el camino
                    self.posicionPersonaje(0,-2,1)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1

    def abajo(self) -> None:
            if (
                self.posicionPersonaje() == 0
                and ((self.posicionPersonaje(1,0) == 4 or self.posicionPersonaje(1,0) == 3)
                or ((self.posicionPersonaje(1,0) == 1 or self.posicionPersonaje(1,0) == 5)
                and (self.posicionPersonaje(2,0) == 4 or self.posicionPersonaje(2,0) == 3)))
            ):
                if self.posicionPersonaje(1,0) == 4:
                    #Coloca un camino donde estaba el personaje
                    self.posicionPersonaje(0,0,4)
                    #Coloca el personaje donde estaba el camino
                    self.posicionPersonaje(1,0,0)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
                elif self.posicionPersonaje(1,0) == 3:
                    #Coloca un camino donde estaba el personaje
                    self.posicionPersonaje(0,0,4)
                    #Coloca el personaje donde estaba la meta
                    self.posicionPersonaje(1,0,6)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
                elif self.posicionPersonaje(1,0) == 1:
                    #Coloca un camino donde estaba el personaje
                    self.posicionPersonaje(0,0,4)
                    #Coloca el personaje donde estaba la caja
                    self.posicionPersonaje(1,0,0)
                    if self.posicionPersonaje(2,0) == 3:
                        #Coloca la caja donde estaba la meta
                        self.posicionPersonaje(2,0,5)
                    elif self.posicionPersonaje(2,0) == 4:
                        #Coloca la caja donde estaba el camino
                        self.posicionPersonaje(2,0,1)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
                else:
                    #Coloca un camino donde estaba el personaje
                    self.posicionPersonaje(0,0,4)
                    #Coloca el personaje donde estaba la caja en la meta
                    self.posicionPersonaje(1,0,6)
                    if self.posicionPersonaje(2,0) == 3:
                        #Coloca la caja donde estaba la meta
                        self.posicionPersonaje(2,0,5)
                    else:
                        #Coloca la caja donde estaba el camino
                        self.posicionPersonaje(2,0,1)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
            elif(
                 self.posicionPersonaje() == 6
                  and ((self.posicionPersonaje(1,0) == 4 or self.posicionPersonaje(1,0) == 3)
                  or ((self.posicionPersonaje(1,0) == 1 or self.posicionPersonaje(1,0) == 5)
                  and (self.posicionPersonaje(2,0) == 4 or self.posicionPersonaje(2,0) == 3)))
            ):
                if self.posicionPersonaje(1,0) == 4:
                    #Coloca una meta donde estaba el personaje
                    self.posicionPersonaje(0,0,3)
                    #Coloca el personaje donde estaba el camino
                    self.posicionPersonaje(1,0,0)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
                elif self.posicionPersonaje(1,0) == 3:
                    #Coloca una meta donde estaba el personaje
                    self.posicionPersonaje(0,0,3)
                    #Coloca el personaje donde estaba la meta
                    self.posicionPersonaje(1,0,6)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
                elif self.posicionPersonaje(1,0) == 1:
                    #Coloca una meta donde estaba el personaje
                    self.posicionPersonaje(0,0,3)
                    #Coloca el personaje donde estaba la caja
                    self.posicionPersonaje(1,0,0)
                    if self.posicionPersonaje(2,0) == 3:
                        #Coloca la caja donde estaba la meta
                        self.posicionPersonaje(2,0,5)
                    else:
                        #Coloca la caja donde estaba el camino
                        self.posicionPersonaje(2,0,1)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
                else:
                    #Coloca una meta donde estaba el personaje
                    self.posicionPersonaje(0,0,3)
                    #Coloca el personaje donde estaba la caja en la meta
                    self.posicionPersonaje(1,0,6)
                    if self.posicionPersonaje(2,0) == 3:
                        #Coloca la caja donde estaba la meta
                        self.posicionPersonaje(2,0,5)
                    else:
                        #Coloca la caja donde estaba el camino
                        self.posicionPersonaje(2,0,1)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1

    def arriba(self) -> None:
                if (
                    self.posicionPersonaje() == 0
                    and ((self.posicionPersonaje(-1,0) == 4 or self.posicionPersonaje(-1,0) == 3)
                    or ((self.posicionPersonaje(-1,0) == 1 or self.posicionPersonaje(-1,0) == 5)
                    and (self.posicionPersonaje(-2,0) == 4 or self.posicionPersonaje(-2,0) == 3)))
                ):
                    if self.posicionPersonaje(-1,0) == 4:
                        #Coloca un camino donde estaba el personaje
                        self.posicionPersonaje(0,0,4)
                        #Coloca el personaje donde estaba el camino
                        self.posicionPersonaje(-1,0,0)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                    elif self.posicionPersonaje(-1,0) == 3:
                        #Coloca un camino donde estaba el personaje
                        self.posicionPersonaje(0,0,4)
                        #Coloca el personaje donde estaba la meta
                        self.posicionPersonaje(-1,0,6)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                    elif self.posicionPersonaje(-1,0) == 1:
                        #Coloca un camino donde estaba el personaje
                        self.posicionPersonaje(0,0,4)
                        #Coloca el personaje donde estaba la caja
                        self.posicionPersonaje(-1,0,0)
                        if self.posicionPersonaje(-2,0) == 3:
                            #Coloca la caja donde estaba la meta
                            self.posicionPersonaje(-2,0,5)
                        elif self.posicionPersonaje(-2,0) == 4:
                            #Coloca la caja donde estaba el camino
                            self.posicionPersonaje(-2,0,1)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                    else:
                        #Coloca un camino donde estaba el personaje
                        self.posicionPersonaje(0,0,4)
                        #Coloca el personaje donde estaba la caja en la meta
                        self.posicionPersonaje(-1,0,6)
                        if self.posicionPersonaje(-2,0) == 3:
                            #Coloca la caja donde estaba la meta
                            self.posicionPersonaje(-2,0,5)
                        else:
                            #Coloca la caja donde estaba el camino
                            self.posicionPersonaje(-2,0,1)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                elif(
                     self.posicionPersonaje() == 6
                     and ((self.posicionPersonaje(-1,0) == 4 or self.posicionPersonaje(-1,0) == 3)
                     or ((self.posicionPersonaje(-1,0) == 1 or self.posicionPersonaje(-1,0) == 5)
                     and (self.posicionPersonaje(-2,0) == 4 or self.posicionPersonaje(-2,0) == 3)))
                ):
                    if self.posicionPersonaje(-1,0) == 4:
                        #Coloca una meta donde estaba el personaje
                        self.posicionPersonaje(0,0,3)
                        #Coloca el personaje donde estaba el camino
                        self.posicionPersonaje(-1,0,0)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                    elif self.posicionPersonaje(-1,0) == 3:
                        #Coloca una meta donde estaba el personaje
                        self.posicionPersonaje(0,0,3)
                        #Coloca el personaje donde estaba la meta
                        self.posicionPersonaje(-1,0,6)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                    elif self.posicionPersonaje(-1,0) == 1:
                        #Coloca una meta donde estaba el personaje
                        self.posicionPersonaje(0,0,3)
                        #Coloca el personaje donde estaba la caja
                        self.posicionPersonaje(-1,0,0)
                        if self.posicionPersonaje(-2,0) == 3:
                            #Coloca la caja donde estaba la meta
                            self.posicionPersonaje(-2,0,5)
                        else:
                            #Coloca la caja donde estaba el camino
                            self.posicionPersonaje(-2,0,1)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                    else:
                        #Coloca una meta donde estaba el personaje
                        self.posicionPersonaje(0,0,3)
                        #Coloca el personaje donde estaba la caja en la meta
                        self.posicionPersonaje(-1,0,6)
                        if self.posicionPersonaje(-2,0) == 3:
                            #Coloca la caja donde estaba la meta
                            self.posicionPersonaje(-2,0,5)
                        else:
                            #Coloca la caja donde estaba el camino
                            self.posicionPersonaje(-2,0,1)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1

    def jugar(self) -> None:
        """
            a - Izquierda
            d - Derecha
            w - Arriba
            s - Abajo
            r - Reiniciar nivel
        """
        #Imprime el mapa antes del movimiento
        self.imprimirMapa()
        #Solicita la direccion del movimiento
        movimiento = input("Movimiento: ")
        #Ejecuta el movimiento seleccionado
        if movimiento == "d":
            self.derecha()
        elif movimiento == "a":
            self.izquierda()
        elif movimiento == "w":
            self.arriba()
        elif movimiento == "s":
            self.abajo()
        elif movimiento == "r":
            #Reinicia el nivel actual
            self.cargarNivel()
        #Limpia la consola despues del movimiento
        os.system("cls" if os.name == "nt" else "clear")


soko = Sokoban()
while soko.verificarCajas():
    soko.jugar()