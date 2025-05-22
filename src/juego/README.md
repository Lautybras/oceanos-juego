
# Módulo de Juego

## Partida de Océanos
La clase `PartidaDeOcéanos` modela el estado y acciones posibles a lo largo de una única partida del juego (con múltiples rondas) entre 2-4 jugadores. Tiene métodos para realizar las acciones correspondientes en cada momento, y expone las propiedades que el jugador actual debería concoer en una partida real.

### Métodos de acción
Los métodos disponibles públicamente que "hacen algo en el juego" son los siguientes:

* `iniciarRonda()`: inicia una nueva ronda desde cero.
* `robarDelDescarte(índicePilaDeDescarte)`: el jugador activo roba la carta superior de la pila de descarte indicada.
* `verCartasParaRobarDelMazo()`: el jugador activo decide que va a robar cartas del mazo, por lo que se le deja ver las dos cartas superiores del mazo. Esta acción obliga al jugador a robar del mazo.
* `robarDelMazo(índiceDeCartaARobar, índiceDePilaDondeDescartar)`: el jugador activo elige cuál de las cartas vistas quedarse, y en qué pila de descarte dejar la otra.
* `jugarDúoDePeces(cartasAJugar)`: el jugador activo juega un dúo de peces desde su mano.
* `jugarDúoDeBarcos(cartasAJugar)`: el jugador activo juega un dúo de barcos desde su mano.
* `jugarDúoDeCangrejos(cartasAJugar, pilaDeDescarteARobar, índiceDeCartaARobar)`: el jugador activo juega un dúo de cangrejos desde su mano, y roba la carta elegida.
* `jugarDúoDeNadadorYTiburón(cartasAJugar, jugadorARobar)`: el jugador activo juega un dúo de nadador y tiburón desde su mano, y roba una carta al azar de la mano del jugador elegido.
* `pasarTurno()`: el jugador activo pasa de turno.
* `decirBasta()`: el jugador activo dice ¡Basta!. La ronda termina y cada jugador suma el puntaje de ronda.
* `decirÚltimaChance()`: el jugador activo dice ¡Última Chance!. Su turno termina y la ronda terminará cuando vuelva a ser su turno.

Estos métodos NO DEBEN SER USADOS DESDE LOS BOTS, sino que serán invocados acorde a lo retornado por cada uno de los métodos de la interfaz de `JugadorBase`.