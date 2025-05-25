# Módulo Administrador

## Administrador de Juego
La clase `AdministradorDeJuego` actúa como puente entre instancias de `PartidaDeOcéanos` y los Bots. Su tarea es invocar los métodos correspondientes que los Bots implementan y usar sus respuestas para resolver las diferentes fases del juego con llamadas a métodos de `PartidaDeOcéanos`.

Esta clase espera ser creada con un arreglo de las CLASES de los Bots que van a jugar (es decir, se invoca como `AdministradorDeJuego(clasesDeJugadores=[RandyBot, SirenaEnjoyer])`), y expone un método `jugarPartida()`. Cuando este método es llamado, el administrador se encarga de simular una partida de principio a fin entre instancias de las clases de Bots, y retorna el número de jugador del Bot ganador. `jugarPartida()` puede ser llamada múltiples veces para jugar muchas partidas.

El parámetro `verbosidad` en el constructor de la clase controla si se imprime en pantalla texto sobre cada acción ocurrida en la partida.

El administrador también recolecta diversas estadísticas de la partida, como cantidad de rondas jugadas, dúos por jugador, etc. Esta información puede ser accedida en cualquier momento a través de los atributos privados de la clase.

## Tipos de Acción
Para que los Bots puedan comunicarle al administrador qué tipo de acción desean realizar en cada fase de la partida, se utiliza la clase `Acción`, es un [Enum](https://docs.python.org/3/library/enum.html) con los siguientes valores:

* `Acción.Robo.DEL_MAZO`: representa la acción de robar del mazo
* `Acción.Robo.DEL_DESCARTE_0`: representa la acción de robar de la pila de descarte izquierda (índice 0)
* `Acción.Robo.DEL_DESCARTE_1`: representa la acción de robar de la pila de descarte derecha (índice 1)
* `Acción.Dúos.NO_JUGAR`: representa la intención de no jugar ningún dúo (más) en esta ronda
* `Acción.Dúos.JUGAR_PECES`: representa la acción de jugar un dúo de peces de la mano
* `Acción.Dúos.JUGAR_BARCOS`: representa la acción de jugar un dúo de barcos de la mano
* `Acción.Dúos.JUGAR_CANGREJOS`: representa la acción de jugar un dúo de cangrejos de la mano
* `Acción.Dúos.JUGAR_NADADOR_Y_TIBURÓN`: representa la acción de jugar un dúo de nadador y tiburón de la mano
* `Acción.FinDeTurno.PASAR_TURNO`: representa la intención de pasar el turno de manera convencional
* `Acción.FinDeTurno.DECIR_BASTA`: representa la acción de decir ¡Basta!
* `Acción.FinDeTurno.ÚLTIMA_CHANCE`:  representa la acción de decir ¡Última Chance!

Los métodos de los Bots que el administrador invoca durante el juego usualmente devuelven alguna `Acción` que tenga sentido para ese método (por ejemplo, `decidirAcciónDeRobo` debe devolver algún valor de `Acción.Robo`).

## Sistema de Eventos
En una partida real, ocurren situaciones en las cuales los jugadores obtienen información por acciones fuera de su turno, pero que no es inferible cuando es su turno (por ejemplo, si alguien descarta una Sirena y otra persona la tapa con un Cangrejo, cuando sea mi turno no tengo derecho a ver qué cartas hay abajo del Cangrejo, pero "sé" que hay una Sirena abajo si presté atención). Para modelar esto, el `AdministradorDeJuego` les provee a los Bots acceso a un atributo `_eventos`.

El atributo `_eventos` es un arreglo de objetos de tipo `Evento`. Cada `Evento` es una tripla con campos:

* `jugador`: el número del jugador activo que generó el evento
* `acción`: el tipo de `Acción` del evento
* `parámetros`: un diccionario con información adicional según el tipo de acción. Estos son los parámetros de cada acción registrada:
  * `Acción.Robo.DEL_MAZO`: `"cartaDescartada"` (copia de la `Carta`) y `"pilaDondeDescartó"` (índice de la pila, 0 o 1). PUEDEN SER `None` SI NO SE DESCARTÓ CARTA!
  * `Acción.Robo.DEL_DESCARTE_0|1`: `"cartaRobada"` (copia de la `Carta`)
  * `Acción.Dúos.JUGAR_PECES`: `"cartasJugadas"` (tupla con dos `Carta`s)
  * `Acción.Dúos.JUGAR_BARCOS`: `"cartasJugadas"` (tupla con dos `Carta`s)
  * `Acción.Dúos.JUGAR_CANGREJOS`: `"cartasJugadas"` (tupla con dos `Carta`s) y `"pilaDondeRobó"` (índice de la pila, 0 o 1)
  * `Acción.Dúos.JUGAR_NADADOR_Y_TIBURÓN`: `"cartasJugadas"` (tupla con dos `Carta`s), `"jugadorRobado"` (número de jugador) y `"cartaRobada"` (copia de la `Carta`). ESTE ÚLTIMO PARÁMETRO SÓLO DEBERÍA VERSE SI EL BOT ROBADO SOY YO. NO SER MALO/A PLIS!!!
  * `Acción.Dúos.PASAR_TURNO`: el diccionario es `None`, no hay parámetros.
  * `Acción.Dúos.DECIR_BASTA`: el diccionario es `None`, no hay parámetros.
  * `Acción.Dúos.PASAR_ÚLTIMA_CHANCE`: el diccionario es `None`, no hay parámetros.

El arreglo de Eventos se limpia al inicio de cada ronda. Es responsabilidad de los Bots calcular qué eventos son nuevos y cuáles ya fueron vistos de alguna manera.