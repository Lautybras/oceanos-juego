import pytest
import collections
from juego.carta import Carta
from juego.juego import EstadoDelJuego, cartasDelJuego

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_LosPuntajesDeRondaInicianEnCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0
	assert juego.estadoDelJugador[1].puntajeDeRonda() == 0

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_EsTurnoDeJugadorCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert juego.deQuienEsTurno == 0


def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_HayDosPilasDeDescarte():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego.descarte) == 2
	

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_LasPilasDeDescarteTienenUnaCartaCadaUna():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego.descarte[0]) == 1
	assert len(juego.descarte[1]) == 1
	assert isinstance(juego.descarte[0][0], Carta) == True
	assert isinstance(juego.descarte[1][0], Carta) == True
	

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_ElMazoTieneCincuentaYSeisCartas():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego.mazo) == 56

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_ElMazoYLasPilasDeDescarteConformanElConjuntoDeCartasDelJuego():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert collections.Counter(juego.mazo + juego.descarte[0] + juego.descarte[1]) == collections.Counter(cartasDelJuego())

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_HayUnEstadoDelJugadorPorCadaJugador():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego.estadoDelJugador) == 2

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_LaManoDeCadaJugadorEstáVacía():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego.estadoDelJugador[0].mano) == 0
	assert len(juego.estadoDelJugador[1].mano) == 0

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_LaZonaDeDuosDeCadaJugadorEstáVacía():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego.estadoDelJugador[0].zonaDeDuos) == 0
	assert len(juego.estadoDelJugador[1].zonaDeDuos) == 0

