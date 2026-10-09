class Sokoban():
    def __init__(self) -> None:
        self.niveles =[[
            [2,2,2,2,2,2,2,2],
            [2,4,4,0,4,4,4,2],
            [2,4,4,4,3,4,4,2],
            [2,4,4,1,4,3,3,2],
            [2,4,4,4,4,4,4,2],
            [2,2,2,2,2,2,2,2]
        ],
        [
            [2,2,2,2,2,2,2,2],
            [2,4,4,0,4,4,4,2],
            [2,4,1,4,3,4,4,2],
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

        self.personaje_fila = 1
        self.personaje_columna = 3

    def pruebas(self) -> None:
        for nivel in self.niveles:
            self.mapa = nivel
            self.imprimirMapa()
            print()

    def imprimirMapa(self) -> None:
        for fila in self.mapa:
            print(fila)

    

soko = Sokoban()
soko.pruebas()