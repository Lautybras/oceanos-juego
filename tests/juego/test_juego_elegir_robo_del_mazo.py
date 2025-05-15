import pytest
import collections
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoInvalidoException, JuegoException, cartasDelJuego

def test_SiSeInicióRonda_AlElegirRobarLaPrimeraCartaYDescartarEnLaPrimeraPila_LaManoDelJugadorCeroTieneLaCartaSeleccionada():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartaElegida = juego.mazo[-1]
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	assert len(juego.estadoDelJugador[0].mano) == 1
	assert juego.estadoDelJugador[0].mano[0] == cartaElegida

def test_SiSeInicióRonda_AlElegirRobarLaSegundaCartaYDescartarEnLaPrimeraPila_LaManoDelJugadorCeroTieneLaCartaSeleccionada():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartaElegida = juego.mazo[-2]
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(1,0)
	
	assert len(juego.estadoDelJugador[0].mano) == 1
	assert juego.estadoDelJugador[0].mano[0] == cartaElegida

def test_SiSeInicióRonda_AlElegirRobarLaPrimeraCartaYDescartarEnLaPrimeraPila_LaPrimeraPilaDeDescarteTieneLaCartaNoSeleccionada():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartaNoElegida = juego.mazo[-2]
	
	pilaDeDescarteElegida = juego.descarte[0].copy()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	assert juego.descarte[0] == (pilaDeDescarteElegida + [cartaNoElegida])

def test_SiSeInicióRondaYElJugadorCeroRobóDelMazoYPasóDeTurno_AlElegirRobarLaPrimeraCartaYDescartarEnLaPrimeraPila_LaManoDelJugadorUnoTieneLaCartaSeleccionada():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	
	cartaElegida = juego.mazo[-1]
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	assert len(juego.estadoDelJugador[1].mano) == 1
	assert juego.estadoDelJugador[1].mano[0] == cartaElegida
	
def test_SiSeInicióRondaYSeIntentóRobarDelMazo_NoSePuedeRobarUnaCartaFueraDelRangoDeDosCartas():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.elegirRoboDelMazo(2,0)
	
	assert "No se puede elegir una carta para robar fuera del rango" in str(excepcion.value)

def test_SiSeInicióRondaYSeIntentóRobarDelMazo_NoSePuedeDescartarEnUnaPilaNoExistente():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.elegirRoboDelMazo(0,2)
	
	assert "Pila de descarte no existente" in str(excepcion.value)

def test_SiSeInicióRondaYExactamenteUnaPilaDeDescarteEstáVacíaYSeIntentóRobarDelMazo_NoSePuedeDescartarEnLaPilaNoVacía():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.descarte[0].pop()
	juego.robarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.elegirRoboDelMazo(0,0)
	
	assert "No se puede descartar en una pila no vacía mientras la otra se encuentre vacía" in str(excepcion.value)

def test_SiElMazoTieneUnaCartaYSeIntentóRobarDelMazo_NoSePuedeRobarUnaCartaFueraDelRangoDeUnaCarta():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo = [juego.mazo[0]]
	juego.robarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.elegirRoboDelMazo(1,0)
	
	assert "No se puede elegir una carta para robar fuera del rango" in str(excepcion.value)

def test_SiElJugadorCeroYaTeníaOtrasCartasEnLaMano_AlElegirRobarDelMazoLaPrimerCarta_LaManoDelJugadorCeroTieneSusCartasYLaRobada():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano = [
		Carta(Carta.Tipo.BARCO, Carta.Color.NARANJA),
		Carta(Carta.Tipo.ANCLA, Carta.Color.AMARILLO)
	]
	cartaARobar = juego.mazo[-1]
	juego.robarDelMazo()
	
	juego.elegirRoboDelMazo(0,0)
	
	assert juego.estadoDelJugador[0].mano == [
		Carta(Carta.Tipo.BARCO, Carta.Color.NARANJA),
		Carta(Carta.Tipo.ANCLA, Carta.Color.AMARILLO),
		cartaARobar
	]