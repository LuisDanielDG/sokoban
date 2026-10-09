# SOKOBAN

## 1. Objetivo

### 1.1 General

Desarrollar una version retro de Sokoban para consola usando Python.

### 1.2 Especificos

- Aplicar conceptos de programacion orientada a objetos: clases, objetos y metodos.
- Utilizar listas bidimensionales, ciclos, condiciones y entrada desde el teclado.
- Representar un juego por turnos y validar sus reglas.
- Organizar el desarrollo mediante tareas y estados Kanban.
- Documentar el funcionamiento del juego.

## 2. Reglas del juego

Sokoban consiste en mover cajas por un laberinto hasta colocarlas sobre todas las metas.

1. El personaje se mueve hacia arriba, abajo, izquierda o derecha.
2. El personaje puede empujar una caja a la vez.
3. Una caja solo se puede empujar si la casilla que sigue es camino o meta.
4. No se puede atravesar una pared ni empujar una caja contra una pared u otra caja.
5. El nivel termina cuando todas las metas tienen una caja.
6. Para que un nivel sea valido, debe tener la misma cantidad de cajas y metas, y al menos una caja.
7. Al completar un nivel se carga el siguiente. Al completar el ultimo nivel termina el juego.

## 3. Elementos del juego

### 3.1 Mapa de juego

Cada nivel se representa con una lista bidimensional de numeros. Los tres niveles estan definidos en `self.niveles` dentro de `sokoban.py`.

```python
self.mapa = [
	[2, 2, 2, 2, 2, 2, 2, 2],
	[2, 4, 4, 0, 4, 4, 4, 2],
	[2, 4, 4, 4, 3, 1, 4, 2],
	[2, 4, 4, 1, 4, 3, 4, 2],
	[2, 4, 4, 4, 4, 4, 4, 2],
	[2, 2, 2, 2, 2, 2, 2, 2],
]
```

### 3.2 Elementos

| Numero | Significado | Representacion |
| --- | --- | --- |
| 0 | Personaje | 🙉 |
| 1 | Caja | 📦 |
| 2 | Pared | 🧱 |
| 3 | Meta vacia | 🔳 |
| 4 | Camino | Espacio vacio |
| 5 | Caja sobre una meta | ✅ |
| 6 | Personaje sobre una meta | 🙈 |

## 4. Controles

| Tecla | Accion |
| --- | --- |
| `a` | Mover a la izquierda |
| `d` | Mover a la derecha |
| `w` | Mover hacia arriba |
| `s` | Mover hacia abajo |
| `r` | Reiniciar el nivel actual |

## 5. Ejecucion y modo de juego

Se requiere Python 3. Desde una terminal, ejecutar:

```bash
python sokoban.py
```

El juego muestra el mapa y solicita una tecla. Despues de procesar cada entrada limpia la consola y vuelve a mostrar el tablero. Los movimientos que no cumplen las reglas no cambian el mapa.

La tecla `r` vuelve a cargar una copia del nivel actual y restaura la posicion inicial del personaje. Las cajas y metas se conservan en su estado original para poder reiniciar el mismo nivel.

Al iniciar y durante el juego se comprueba que la cantidad de cajas coincida con la cantidad de metas. Las cajas sobre metas (`5`) cuentan como caja y como meta. Cuando todas las metas estan ocupadas, el juego carga el siguiente nivel; despues del ultimo, termina.

## 6. Funciones implementadas

Los estados Kanban usados para el seguimiento son:

| Estado | Significado |
| --- | --- |
| ToDo | Por hacer |
| Doing | En desarrollo y validacion |
| Done | Implementada y comprobada |

### 6.1 Funciones generales

| Funcion | Descripcion | Kanban |
| --- | --- | --- |
| `imprimirMapa()` | Imprime el tablero con sus representaciones visuales. | Done |
| `cargarNivel()` | Carga una copia del nivel actual y encuentra la posicion inicial del personaje. | Done |
| `verificarCajas()` | Valida la cantidad de cajas y metas, detecta el final del nivel y carga el siguiente. | Done |
| `posicionPersonaje()` | Consulta o modifica una casilla respecto a la posicion del personaje. | Done |
| `jugar()` | Lee el control, ejecuta la accion y limpia la consola. | Done |

### 6.2 Condiciones generales de movimiento

En las tablas, `P` representa la casilla ocupada por el personaje antes del movimiento. `D1` es la primera casilla en la direccion del movimiento y `D2` es la casilla que sigue despues de `D1`. Los numeros corresponden a los elementos definidos en la seccion 3.2.

1. El mapa solo cambia cuando se cumple una de las condiciones de las tablas. Si no se cumple, el movimiento no se realiza.
2. Para caminar, `D1` debe ser camino (`4`) o meta vacia (`3`).
3. Para empujar, `D1` debe contener una caja (`1`) o una caja sobre meta (`5`). Ademas, `D2` debe ser camino (`4`) o meta vacia (`3`).
4. Solo se empuja la caja que esta en `D1`; no se pueden empujar varias cajas a la vez.
5. Las paredes (`2`) bloquean el paso. Una caja no se puede empujar contra una pared ni contra otra caja.
6. Cuando `P` es camino (`0`), la casilla de origen queda como camino (`4`). Cuando `P` es personaje sobre meta (`6`), la casilla de origen vuelve a ser meta (`3`).
7. Al entrar en una casilla de camino, el personaje queda como `0`. Al entrar en una meta, queda como `6`.
8. Si una caja llega a camino, queda como `1`; si llega a una meta, queda como `5`.
9. Si el personaje empuja una caja que estaba sobre meta (`5`), ocupa esa meta y queda como `6`.
10. Cada movimiento valido actualiza la fila o columna del personaje en una casilla, en la direccion correspondiente.
11. `r` no es un movimiento del personaje: vuelve a cargar el nivel actual y restaura el tablero y la posicion inicial.

### 6.3 Derecha

Para esta tabla, `D1` esta a la derecha del personaje y `D2` es la casilla siguiente hacia la derecha.

| No. | Condicion inicial | Resultado del movimiento | Kanban |
| --- | --- | --- | --- |
| 1 | `P=0`, `D1=4` | `P` pasa a `4`, `D1` pasa a `0`; la columna aumenta en 1. | Done |
| 2 | `P=0`, `D1=3` | `P` pasa a `4`, `D1` pasa a `6`; la columna aumenta en 1. | Done |
| 3 | `P=0`, `D1=1`, `D2=4` | `P` pasa a `4`, `D1` pasa a `0`, `D2` pasa a `1`; la columna aumenta en 1. | Done |
| 4 | `P=0`, `D1=1`, `D2=3` | `P` pasa a `4`, `D1` pasa a `0`, `D2` pasa a `5`; la columna aumenta en 1. | Done |
| 5 | `P=0`, `D1=5`, `D2=4` | `P` pasa a `4`, `D1` pasa a `6`, `D2` pasa a `1`; la columna aumenta en 1. | Done |
| 6 | `P=0`, `D1=5`, `D2=3` | `P` pasa a `4`, `D1` pasa a `6`, `D2` pasa a `5`; la columna aumenta en 1. | Done |
| 7 | `P=6`, `D1=4` | `P` pasa a `3`, `D1` pasa a `0`; la columna aumenta en 1. | Done |
| 8 | `P=6`, `D1=3` | `P` pasa a `3`, `D1` pasa a `6`; la columna aumenta en 1. | Done |
| 9 | `P=6`, `D1=1`, `D2=4` | `P` pasa a `3`, `D1` pasa a `0`, `D2` pasa a `1`; la columna aumenta en 1. | Done |
| 10 | `P=6`, `D1=1`, `D2=3` | `P` pasa a `3`, `D1` pasa a `0`, `D2` pasa a `5`; la columna aumenta en 1. | Done |
| 11 | `P=6`, `D1=5`, `D2=4` | `P` pasa a `3`, `D1` pasa a `6`, `D2` pasa a `1`; la columna aumenta en 1. | Done |
| 12 | `P=6`, `D1=5`, `D2=3` | `P` pasa a `3`, `D1` pasa a `6`, `D2` pasa a `5`; la columna aumenta en 1. | Done |

### 6.4 Izquierda

Para esta tabla, `D1` esta a la izquierda del personaje y `D2` es la casilla siguiente hacia la izquierda.

| No. | Condicion inicial | Resultado del movimiento | Kanban |
| --- | --- | --- | --- |
| 1 | `P=0`, `D1=4` | `P` pasa a `4`, `D1` pasa a `0`; la columna disminuye en 1. | Done |
| 2 | `P=0`, `D1=3` | `P` pasa a `4`, `D1` pasa a `6`; la columna disminuye en 1. | Done |
| 3 | `P=0`, `D1=1`, `D2=4` | `P` pasa a `4`, `D1` pasa a `0`, `D2` pasa a `1`; la columna disminuye en 1. | Done |
| 4 | `P=0`, `D1=1`, `D2=3` | `P` pasa a `4`, `D1` pasa a `0`, `D2` pasa a `5`; la columna disminuye en 1. | Done |
| 5 | `P=0`, `D1=5`, `D2=4` | `P` pasa a `4`, `D1` pasa a `6`, `D2` pasa a `1`; la columna disminuye en 1. | Done |
| 6 | `P=0`, `D1=5`, `D2=3` | `P` pasa a `4`, `D1` pasa a `6`, `D2` pasa a `5`; la columna disminuye en 1. | Done |
| 7 | `P=6`, `D1=4` | `P` pasa a `3`, `D1` pasa a `0`; la columna disminuye en 1. | Done |
| 8 | `P=6`, `D1=3` | `P` pasa a `3`, `D1` pasa a `6`; la columna disminuye en 1. | Done |
| 9 | `P=6`, `D1=1`, `D2=4` | `P` pasa a `3`, `D1` pasa a `0`, `D2` pasa a `1`; la columna disminuye en 1. | Done |
| 10 | `P=6`, `D1=1`, `D2=3` | `P` pasa a `3`, `D1` pasa a `0`, `D2` pasa a `5`; la columna disminuye en 1. | Done |
| 11 | `P=6`, `D1=5`, `D2=4` | `P` pasa a `3`, `D1` pasa a `6`, `D2` pasa a `1`; la columna disminuye en 1. | Done |
| 12 | `P=6`, `D1=5`, `D2=3` | `P` pasa a `3`, `D1` pasa a `6`, `D2` pasa a `5`; la columna disminuye en 1. | Done |

### 6.5 Arriba

Para esta tabla, `D1` esta arriba del personaje y `D2` es la casilla siguiente hacia arriba.

| No. | Condicion inicial | Resultado del movimiento | Kanban |
| --- | --- | --- | --- |
| 1 | `P=0`, `D1=4` | `P` pasa a `4`, `D1` pasa a `0`; la fila disminuye en 1. | Done |
| 2 | `P=0`, `D1=3` | `P` pasa a `4`, `D1` pasa a `6`; la fila disminuye en 1. | Done |
| 3 | `P=0`, `D1=1`, `D2=4` | `P` pasa a `4`, `D1` pasa a `0`, `D2` pasa a `1`; la fila disminuye en 1. | Done |
| 4 | `P=0`, `D1=1`, `D2=3` | `P` pasa a `4`, `D1` pasa a `0`, `D2` pasa a `5`; la fila disminuye en 1. | Done |
| 5 | `P=0`, `D1=5`, `D2=4` | `P` pasa a `4`, `D1` pasa a `6`, `D2` pasa a `1`; la fila disminuye en 1. | Done |
| 6 | `P=0`, `D1=5`, `D2=3` | `P` pasa a `4`, `D1` pasa a `6`, `D2` pasa a `5`; la fila disminuye en 1. | Done |
| 7 | `P=6`, `D1=4` | `P` pasa a `3`, `D1` pasa a `0`; la fila disminuye en 1. | Done |
| 8 | `P=6`, `D1=3` | `P` pasa a `3`, `D1` pasa a `6`; la fila disminuye en 1. | Done |
| 9 | `P=6`, `D1=1`, `D2=4` | `P` pasa a `3`, `D1` pasa a `0`, `D2` pasa a `1`; la fila disminuye en 1. | Done |
| 10 | `P=6`, `D1=1`, `D2=3` | `P` pasa a `3`, `D1` pasa a `0`, `D2` pasa a `5`; la fila disminuye en 1. | Done |
| 11 | `P=6`, `D1=5`, `D2=4` | `P` pasa a `3`, `D1` pasa a `6`, `D2` pasa a `1`; la fila disminuye en 1. | Done |
| 12 | `P=6`, `D1=5`, `D2=3` | `P` pasa a `3`, `D1` pasa a `6`, `D2` pasa a `5`; la fila disminuye en 1. | Done |

### 6.6 Abajo

Para esta tabla, `D1` esta abajo del personaje y `D2` es la casilla siguiente hacia abajo.

| No. | Condicion inicial | Resultado del movimiento | Kanban |
| --- | --- | --- | --- |
| 1 | `P=0`, `D1=4` | `P` pasa a `4`, `D1` pasa a `0`; la fila aumenta en 1. | Done |
| 2 | `P=0`, `D1=3` | `P` pasa a `4`, `D1` pasa a `6`; la fila aumenta en 1. | Done |
| 3 | `P=0`, `D1=1`, `D2=4` | `P` pasa a `4`, `D1` pasa a `0`, `D2` pasa a `1`; la fila aumenta en 1. | Done |
| 4 | `P=0`, `D1=1`, `D2=3` | `P` pasa a `4`, `D1` pasa a `0`, `D2` pasa a `5`; la fila aumenta en 1. | Done |
| 5 | `P=0`, `D1=5`, `D2=4` | `P` pasa a `4`, `D1` pasa a `6`, `D2` pasa a `1`; la fila aumenta en 1. | Done |
| 6 | `P=0`, `D1=5`, `D2=3` | `P` pasa a `4`, `D1` pasa a `6`, `D2` pasa a `5`; la fila aumenta en 1. | Done |
| 7 | `P=6`, `D1=4` | `P` pasa a `3`, `D1` pasa a `0`; la fila aumenta en 1. | Done |
| 8 | `P=6`, `D1=3` | `P` pasa a `3`, `D1` pasa a `6`; la fila aumenta en 1. | Done |
| 9 | `P=6`, `D1=1`, `D2=4` | `P` pasa a `3`, `D1` pasa a `0`, `D2` pasa a `1`; la fila aumenta en 1. | Done |
| 10 | `P=6`, `D1=1`, `D2=3` | `P` pasa a `3`, `D1` pasa a `0`, `D2` pasa a `5`; la fila aumenta en 1. | Done |
| 11 | `P=6`, `D1=5`, `D2=4` | `P` pasa a `3`, `D1` pasa a `6`, `D2` pasa a `1`; la fila aumenta en 1. | Done |
| 12 | `P=6`, `D1=5`, `D2=3` | `P` pasa a `3`, `D1` pasa a `6`, `D2` pasa a `5`; la fila aumenta en 1. | Done |