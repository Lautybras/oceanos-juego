import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.partida import PartidaDeOcéanos, JuegoException

def test_SiSeTerminóUnaRondaYNoSeAlcanzóElPuntajeRequerido_SePuedeIniciarRonda():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano.clear()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA)] += 2
	juego.decirBasta()
	
	juego.iniciarRonda()
	
	assert juego.rondaEnCurso() == True
	assert juego.haTerminado() == False
	assert juego.puntajes[0] == 9
	assert juego.puntajes[1] == 2
	
	assert len(juego._descarte[0]) == 1
	assert len(juego._descarte[1]) == 1
	assert isinstance(juego._descarte[0][0], Carta) == True
	assert isinstance(juego._descarte[1][0], Carta) == True
	assert len(juego._mazo) == 56

def test_SiSeTerminóUnaRonda_AlAlcanzarElPuntajeRequeridoSinEmpates_ElJugadorConMásPuntosGanaLaPartida():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego._puntajes[0] = 38
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano.clear()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA)] += 2
	
	juego.decirBasta()
	
	assert juego.rondaEnCurso() == False
	assert juego.haTerminado() == True
	assert juego.jugadorGanador == 0
	assert juego.puntajes[0] == 38 + 9
	assert juego.puntajes[1] == 2


def test_SiSeTerminóUnaRonda_AlAlcanzarElPuntajeRequeridoConEmpates_ElJugadorConMásPuntosYQueCuyoÚltimoTurnoHayaEstadoMásCercaDelFinalGanaLaPartida():
	juego = PartidaDeOcéanos(cantidadDeJugadores=3)
	juego._puntajes[0] = 33
	juego._puntajes[1] = 28
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelDescarte(1)
	juego._estadosDeJugadores[0].mano.clear()
	juego._estadosDeJugadores[1].mano.clear()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA)] += 2
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 3
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.VERDE)] += 1
	
	juego.decirBasta()
	
	assert juego.haTerminado() == True
	assert juego.rondaEnCurso() == False
	assert juego.jugadorGanador == 1
	assert juego.puntajes[0] == 35
	assert juego.puntajes[1] == 35

