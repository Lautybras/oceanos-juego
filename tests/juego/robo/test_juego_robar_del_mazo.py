import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, JuegoInvalidoException, JuegoException, cartasDelJuego

def test_SiSeInicióRonda_AlElegirRobarLaPrimeraCartaYDescartarEnLaPrimeraPila_LaManoDelJugadorCeroTieneLaCartaSeleccionada():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartaElegida = juego._mazo[-1]
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	assert juego._estadosDeJugadores[0].mano.total() == 1
	assert list(juego._estadosDeJugadores[0].mano.elements())[0] == cartaElegida

def test_SiSeInicióRonda_AlElegirRobarLaSegundaCartaYDescartarEnLaPrimeraPila_LaManoDelJugadorCeroTieneLaCartaSeleccionada():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartaElegida = juego._mazo[-2]
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(1,0)
	
	assert juego._estadosDeJugadores[0].mano.total() == 1
	assert list(juego._estadosDeJugadores[0].mano.elements())[0] == cartaElegida

def test_SiSeInicióRonda_AlElegirRobarLaPrimeraCartaYDescartarEnLaPrimeraPila_LaPrimeraPilaDeDescarteTieneLaCartaNoSeleccionada():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartaNoElegida = juego._mazo[-2]
	
	pilaDeDescarteElegida = juego._descarte[0].copy()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	assert juego._descarte[0] == (pilaDeDescarteElegida + [cartaNoElegida])

def test_SiSeInicióRondaYElJugadorCeroRobóDelMazoYPasóDeTurno_AlElegirRobarLaPrimeraCartaYDescartarEnLaPrimeraPila_LaManoDelJugadorUnoTieneLaCartaSeleccionada():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	
	cartaElegida = juego._mazo[-1]
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	assert juego._estadosDeJugadores[1].mano.total() == 1
	assert list(juego._estadosDeJugadores[1].mano.elements())[0] == cartaElegida
	
def test_SiSeInicióRondaYSeIntentóRobarDelMazo_NoSePuedeRobarUnaCartaFueraDelRangoDeDosCartas():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo(2,0)
	
	assert "No se puede elegir una carta para robar fuera del rango" in str(excepcion.value)

def test_SiSeInicióRondaYSeIntentóRobarDelMazo_NoSePuedeDescartarEnUnaPilaNoExistente():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo(0,2)
	
	assert "Pila de descarte no existente" in str(excepcion.value)

def test_SiSeInicióRondaYExactamenteUnaPilaDeDescarteEstáVacíaYSeIntentóRobarDelMazo_NoSePuedeDescartarEnLaPilaNoVacía():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._descarte[0].pop()
	juego.verCartasParaRobarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo(0,1)
	
	assert "No se puede descartar en una pila no vacía mientras la otra se encuentre vacía" in str(excepcion.value)

def test_SiElMazoTieneUnaCartaYSeIntentóRobarDelMazo_NoSePuedeRobarUnaCartaFueraDelRangoDeUnaCarta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo = [juego._mazo[0]]
	juego.verCartasParaRobarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo(1,0)
	
	assert "No se puede elegir una carta para robar fuera del rango" in str(excepcion.value)

def test_SiElJugadorCeroYaTeníaOtrasCartasEnLaMano_AlElegirRobarDelMazoLaPrimerCarta_LaManoDelJugadorCeroTieneSusCartasYLaRobada():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano = Multiset([
		Carta(Carta.Tipo.BARCO, Carta.Color.NARANJA),
		Carta(Carta.Tipo.ANCLA, Carta.Color.AMARILLO)
	])
	cartaARobar = juego._mazo[-1]
	juego.verCartasParaRobarDelMazo()
	
	juego.robarDelMazo(0,0)
	
	assert juego._estadosDeJugadores[0].mano == Multiset([
		Carta(Carta.Tipo.BARCO, Carta.Color.NARANJA),
		Carta(Carta.Tipo.ANCLA, Carta.Color.AMARILLO),
		cartaARobar
	])

def test_SiNoSeRobóDelMazo_NoSePuedeElegirRobarDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo(0,0)
	
	assert "Debe confirmarse que se va a robar del mazo" in str(excepcion.value)

def test_SiYaSeEligióRobarDelMazo_NoSePuedeElegirRobarDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo(0,0)
	
	assert "Debe confirmarse que se va a robar del mazo" in str(excepcion.value)
	