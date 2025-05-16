import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoException
from collections import Counter as Multiset

def test_SiSeInicióRonda_NoSePuedeJugarDúosAntesDeRobar():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset())
	
	assert "No se puede jugar dúos sin antes haber robado" in str(excepcion.value)

def test_NoSePuedeJugarUnDúoDeCeroCartas():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset())
	
	assert "Se necesitan dos cartas para jugar un dúo" in str(excepcion.value)

def test_NoSePuedeJugarUnDúoDeUnaCarta():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset([Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)]))
	
	assert "Se necesitan dos cartas para jugar un dúo" in str(excepcion.value)

def test_NoSePuedeJugarUnDúoDeMásDeDosCartas():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset([
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO),
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO),
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)
	]))
	
	assert "Se necesitan dos cartas para jugar un dúo" in str(excepcion.value)
	
def test_NoSePuedeJugarUnDúoDeCartasQueNoSeanDeTipoDúo():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset([
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO),
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)
	]))
	
	assert "Se necesitan cartas dúo para jugar un dúo" in str(excepcion.value)

def test_NoSePuedeJugarUnDúoDeCartasQueNoSeanDelMismoTipo():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset([
			Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO),
			Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)
	]))
	
	assert "Se necesitan cartas del mismo tipo dúo para jugar un dúo" in str(excepcion.value)

def test_NoSePuedeJugarUnDúoDeCartasQueNoEsténEnLaManoDelJugador():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset([
			Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO),
			Carta(Carta.Tipo.BARCO, Carta.Color.AZUL)
	]))
	
	assert "Las cartas seleccionadas no están en la mano" in str(excepcion.value)

def test_SiSeTieneUnDúo_AlJugarDúo_LasCartasDelDúoNoEstánEnLaMano():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AMARILLO)
	]))
	
	assert juego.estadoDelJugador[0].mano.total() == 0
	
def test_SiSeTieneUnDúo_AlJugarDúo_ElRestoDeLaManoQuedaIgual():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	cartaEnMano = juego.mazo[-1]
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(1,1)
	juego.pasarTurno()
	juego.robarDelDescarte(1)
	
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AMARILLO)
	]))
	
	assert juego.estadoDelJugador[0].mano == Multiset([cartaEnMano])
	
def test_SiSeTieneUnDúo_AlJugarDúo_LasCartasDelDúoEstánEnLaZonaDeDúos():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AMARILLO)
	]))
	
	assert juego.estadoDelJugador[0].zonaDeDuos == Multiset([(
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AMARILLO)
	)])
	
	