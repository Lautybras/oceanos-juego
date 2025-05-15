import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import EstadoDelJuego, cartasDelJuego, JuegoException

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

	assert Multiset(juego.mazo + juego.descarte[0] + juego.descarte[1]) == Multiset(cartasDelJuego())

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



def test_SiNoSeInicióLaPrimeraRonda_NoSePuedeRobarDelMazo():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoSeInicióLaPrimeraRonda_NoSePuedeElegirRoboDelMazo():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.elegirRoboDelMazo(0,0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoSeInicióLaPrimeraRonda_NoSePuedeRobarDelDescarte():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoSeInicióLaPrimeraRonda_NoSePuedePasarTurno():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoSeInicióLaPrimeraRonda_NoSePuedeJugarUnDúo():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuo(Multiset([
		Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO),
		Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)
	]))
	
	assert "No hay una ronda en curso" in str(excepcion.value)
