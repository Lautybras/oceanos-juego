import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import EstadoDelJuego, cartasDelJuego, JuegoException

def test_SiSeDijoBastaYNoSeAlcanzóElPuntajeRequerido_AlIniciarRonda_ElJugadorInicialEsElSiguienteAlQueDijoBasta():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.estadoDelJugador[0].mano.clear()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	juego.iniciarRonda()
	
	assert juego.deQuienEsTurno == 1
	assert juego.rondaEnCurso == True

def test_SiSeDijoÚltimaChanceYNoSeAlcanzóElPuntajeRequerido_AlIniciarRonda_ElJugadorInicialEsElSiguienteAlQueDijoÚltimaChance():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	juego.iniciarRonda()
	
	assert juego.deQuienEsTurno == 1
	assert juego.rondaEnCurso == True

def test_SiSeTerminóLaRondaPorNoQuedarCartasEnElMazo_AlIniciarRonda_ElJugadorInicialEsElSiguienteAlQueJugóElÚltimoTurno():
	juego = EstadoDelJuego(cantidadDeJugadores=3)
	juego.iniciarRonda()
	juego.mazo = [Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)]
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	
	juego.iniciarRonda()
	
	assert juego.deQuienEsTurno == 2
	assert juego.rondaEnCurso == True