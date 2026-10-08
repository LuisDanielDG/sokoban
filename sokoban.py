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
        self.mapa = [
            [2,2,2,2,2,2,2],
            [2,4,4,0,4,4,2],
            [2,4,4,4,3,4,2],
            [2,2,2,2,2,2,2]
        ]

        self.personaje_fila = 1
        self.personaje_columna = 3

    def imprimirMapa(self) -> None:
        for fila in self.mapa:
            print(fila)

    def posicionPersonaje(self, fila: int = 0, columna: int = 0, valor: int = None):
        f = self.personaje_fila + fila
        c = self.personaje_columna + columna
        if valor is None:
            return self.mapa[f][c]
        self.mapa[f][c] = valor
         
    def derecha(self) -> None:
        if (
            self.posicionPersonaje() == 0
            and (self.posicionPersonaje(0,1) == 4 or self.posicionPersonaje(0,1) == 3)
        ):
            if self.posicionPersonaje(0,1) == 4:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,1,0)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            else:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,1,6)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
        elif(
             self.posicionPersonaje() == 6
             and (self.posicionPersonaje(0,1) == 4 or self.posicionPersonaje(0,1) == 3)
        ):
            if self.posicionPersonaje(0,1) == 4:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,1,0)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1
            else:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,1,6)
                #Actualiza la posicion del personaje
                self.personaje_columna += 1

    def izquierda(self) -> None:
        if (
            self.posicionPersonaje() == 0
            and (self.posicionPersonaje(0,-1) == 4 or self.posicionPersonaje(0,-1) == 3)
        ):
            if self.posicionPersonaje(0,-1) == 4:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,-1,0)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            else:
                #Coloca un camino donde estaba el personaje
                self.posicionPersonaje(0,0,4)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,-1,6)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
        elif(
             self.posicionPersonaje() == 6
             and (self.posicionPersonaje(0,-1) == 4 or self.posicionPersonaje(0,-1) == 3)
        ):
            if self.posicionPersonaje(0,-1) == 4:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba el camino
                self.posicionPersonaje(0,-1,0)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1
            else:
                #Coloca una meta donde estaba el personaje
                self.posicionPersonaje(0,0,3)
                #Coloca el personaje donde estaba la meta
                self.posicionPersonaje(0,-1,6)
                #Actualiza la posicion del personaje
                self.personaje_columna -= 1  

    def abajo(self) -> None:
            if (
                self.posicionPersonaje() == 0
                and (self.posicionPersonaje(1,0) == 4 or self.posicionPersonaje(1,0) == 3)
            ):
                if self.posicionPersonaje(1,0) == 4:
                    #Coloca un camino donde estaba el personaje
                    self.posicionPersonaje(0,0,4)
                    #Coloca el personaje donde estaba el camino
                    self.posicionPersonaje(1,0,0)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
                else:
                    #Coloca un camino donde estaba el personaje
                    self.posicionPersonaje(0,0,4)
                    #Coloca el personaje donde estaba la meta
                    self.posicionPersonaje(1,0,6)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
            elif(
                 self.posicionPersonaje() == 6
                 and (self.posicionPersonaje(1,0) == 4 or self.posicionPersonaje(1,0) == 3)
            ):
                if self.posicionPersonaje(1,0) == 4:
                    #Coloca una meta donde estaba el personaje
                    self.posicionPersonaje(0,0,3)
                    #Coloca el personaje donde estaba el camino
                    self.posicionPersonaje(1,0,0)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1
                else:
                    #Coloca una meta donde estaba el personaje
                    self.posicionPersonaje(0,0,3)
                    #Coloca el personaje donde estaba la meta
                    self.posicionPersonaje(1,0,6)
                    #Actualiza la posicion del personaje
                    self.personaje_fila += 1

    def arriba(self) -> None:
                if (
                    self.posicionPersonaje() == 0
                    and (self.posicionPersonaje(-1,0) == 4 or self.posicionPersonaje(-1,0) == 3)
                ):
                    if self.posicionPersonaje(-1,0) == 4:
                        #Coloca un camino donde estaba el personaje
                        self.posicionPersonaje(0,0,4)
                        #Coloca el personaje donde estaba el camino
                        self.posicionPersonaje(-1,0,0)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                    else:
                        #Coloca un camino donde estaba el personaje
                        self.posicionPersonaje(0,0,4)
                        #Coloca el personaje donde estaba la meta
                        self.posicionPersonaje(-1,0,6)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                elif(
                     self.posicionPersonaje() == 6
                     and (self.posicionPersonaje(-1,0) == 4 or self.posicionPersonaje(-1,0) == 3)
                ):
                    if self.posicionPersonaje(-1,0) == 4:
                        #Coloca una meta donde estaba el personaje
                        self.posicionPersonaje(0,0,3)
                        #Coloca el personaje donde estaba el camino
                        self.posicionPersonaje(-1,0,0)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1
                    else:
                        #Coloca una meta donde estaba el personaje
                        self.posicionPersonaje(0,0,3)
                        #Coloca el personaje donde estaba la meta
                        self.posicionPersonaje(-1,0,6)
                        #Actualiza la posicion del personaje
                        self.personaje_fila -= 1

    def jugar(self) -> None:
        """
            a - Izquierda
            d - Derecha
            w - Arriba
            s - Abajo
        """
        self.imprimirMapa()
        movimiento = input("Movimiento: ")
        if movimiento == "d":
            self.derecha()
        elif movimiento == "a":
            self.izquierda()
        elif movimiento == "w":
            self.arriba()
        elif movimiento == "s":
            self.abajo()


soko = Sokoban()
while True:
    soko.jugar()