import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoException

def test_SiSeTerminóUnaRondaYNoSeAlcanzóElPuntajeRequerido_SePuedeIniciarRonda():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.estadoDelJugador[0].mano.clear()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.estadoDelJugador[1].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA)] += 2
	juego.decirBasta()
	
	juego.iniciarRonda()
	
	assert juego.rondaEnCurso() == True
	assert juego.haTerminado() == False
	assert juego.puntajesDeJuego[0] == 9
	assert juego.puntajesDeJuego[1] == 2
	
	assert len(juego.descarte[0]) == 1
	assert len(juego.descarte[1]) == 1
	assert isinstance(juego.descarte[0][0], Carta) == True
	assert isinstance(juego.descarte[1][0], Carta) == True
	assert len(juego.mazo) == 56

def test_SiSeTerminóUnaRonda_AlAlcanzarElPuntajeRequeridoSinEmpates_ElJugadorConMásPuntosGanaLaPartida():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.puntajesDeJuego[0] = 38
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.estadoDelJugador[0].mano.clear()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.estadoDelJugador[1].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA)] += 2
	
	juego.decirBasta()
	
	assert juego.rondaEnCurso() == False
	assert juego.haTerminado() == True
	assert juego.ganador == 0
	assert juego.puntajesDeJuego[0] == 38 + 9
	assert juego.puntajesDeJuego[1] == 2


def test_SiSeTerminóUnaRonda_AlAlcanzarElPuntajeRequeridoConEmpates_ElJugadorConMásPuntosYQueCuyoÚltimoTurnoHayaEstadoMásCercaDelFinalGanaLaPartida():
	juego = EstadoDelJuego(cantidadDeJugadores=3)
	juego.puntajesDeJuego[0] = 33
	juego.puntajesDeJuego[1] = 28
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelDescarte(1)
	juego.estadoDelJugador[0].mano.clear()
	juego.estadoDelJugador[1].mano.clear()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA)] += 2
	juego.estadoDelJugador[1].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 3
	juego.estadoDelJugador[1].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.VERDE)] += 1
	
	juego.decirBasta()
	
	assert juego.haTerminado() == True
	assert juego.rondaEnCurso() == False
	assert juego.ganador == 1
	assert juego.puntajesDeJuego[0] == 35
	assert juego.puntajesDeJuego[1] == 35

