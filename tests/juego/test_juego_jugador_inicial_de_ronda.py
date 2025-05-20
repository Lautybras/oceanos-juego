import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, cartasDelJuego, JuegoException

def test_SiSeDijoBastaYNoSeAlcanzóElPuntajeRequerido_AlIniciarRonda_ElJugadorInicialEsElSiguienteAlQueDijoBasta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano.clear()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	juego.iniciarRonda()
	
	assert juego._deQuiénEsTurno == 1
	assert juego.rondaEnCurso() == True

def test_SiSeDijoÚltimaChanceYNoSeAlcanzóElPuntajeRequerido_AlIniciarRonda_ElJugadorInicialEsElSiguienteAlQueDijoÚltimaChance():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	juego.iniciarRonda()
	
	assert juego._deQuiénEsTurno == 1
	assert juego.rondaEnCurso() == True

def test_SiSeTerminóLaRondaPorNoQuedarCartasEnElMazo_AlIniciarRonda_ElJugadorInicialEsElSiguienteAlQueJugóElÚltimoTurno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=3)
	juego.iniciarRonda()
	juego._mazo = [Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)]
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	
	juego.iniciarRonda()
	
	assert juego._deQuiénEsTurno == 2
	assert juego.rondaEnCurso() == True