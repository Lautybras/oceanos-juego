import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, cartasDelJuego, JuegoException

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_LosPuntajesDeRondaInicianEnCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0
	assert juego._estadosDeJugadores[1].puntajeDeRonda() == 0

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_EsTurnoDeJugadorCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert juego._deQuiénEsTurno == 0


def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_HayDosPilasDeDescarte():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego._descarte) == 2
	

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_LasPilasDeDescarteTienenUnaCartaCadaUna():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego._descarte[0]) == 1
	assert len(juego._descarte[1]) == 1
	assert isinstance(juego._descarte[0][0], Carta) == True
	assert isinstance(juego._descarte[1][0], Carta) == True
	

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_ElMazoTieneCincuentaYSeisCartas():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego._mazo) == 56

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_ElMazoYLasPilasDeDescarteConformanElConjuntoDeCartasDelJuego():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert Multiset(juego._mazo + juego._descarte[0] + juego._descarte[1]) == Multiset(cartasDelJuego())

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_HayUnEstadoDelJugadorPorCadaJugador():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego._estadosDeJugadores) == 2

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_LaManoDeCadaJugadorEstáVacía():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert juego._estadosDeJugadores[0].mano.total() == 0
	assert juego._estadosDeJugadores[1].mano.total() == 0

def test_SiSeCreóJuegoParaDosJugadores_AlIniciarRonda_LaZonaDeDuosDeCadaJugadorEstáVacía():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	juego.iniciarRonda()

	assert len(juego._estadosDeJugadores[0].zonaDeDuos) == 0
	assert len(juego._estadosDeJugadores[1].zonaDeDuos) == 0



def test_SiNoSeInicióLaPrimeraRonda_NoSePuedeRobarDelMazo():
	
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.verCartasParaRobarDelMazo()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoSeInicióLaPrimeraRonda_NoSePuedeElegirRoboDelMazo():
	
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo(0,0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoSeInicióLaPrimeraRonda_NoSePuedeRobarDelDescarte():
	
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoSeInicióLaPrimeraRonda_NoSePuedePasarTurno():
	
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoSeInicióLaPrimeraRonda_NoSePuedeJugarUnDúo():
	
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO),
		Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)
	]))
	
	assert "No hay una ronda en curso" in str(excepcion.value)
