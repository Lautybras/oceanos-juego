import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoException
from collections import Counter as Multiset

def test_NoSePuedeJugarUnDúoDeCeroCartas():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuo(Multiset())
	
	assert "Se necesitan dos cartas para jugar un dúo" in str(excepcion.value)

def test_NoSePuedeJugarUnDúoDeUnaCarta():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuo(Multiset([Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)]))
	
	assert "Se necesitan dos cartas para jugar un dúo" in str(excepcion.value)

def test_NoSePuedeJugarUnDúoDeMásDeDosCartas():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuo(Multiset([
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO),
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO),
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)
	]))
	
	assert "Se necesitan dos cartas para jugar un dúo" in str(excepcion.value)
	
def test_NoSePuedeJugarUnDúoDeCartasQueNoSeanDeTipoDúo():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuo(Multiset([
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO),
			Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)
	]))
	
	assert "Se necesitan cartas dúo para jugar un dúo" in str(excepcion.value)

def test_NoSePuedeJugarUnDúoDeCartasQueNoSeanDelMismoTipo():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuo(Multiset([
			Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO),
			Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)
	]))
	
	assert "Se necesitan cartas del mismo tipo dúo para jugar un dúo" in str(excepcion.value)

def test_NoSePuedeJugarUnDúoDeCartasQueNoEsténEnLaManoDelJugador():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuo(Multiset([
			Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO),
			Carta(Carta.Tipo.BARCO, Carta.Color.AZUL)
	]))
	
	assert "Las cartas seleccionadas no están en la mano" in str(excepcion.value)

#TODO test de orden de acciones

def test_SiSeTienenDosPeces_AlJugarDúoDePeces_LosPecesVanALaZonaDeDúos():
	
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.PEZ,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.PEZ,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	
	juego.jugarDuo(Multiset([
		Carta(Carta.Tipo.PEZ,Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ,Carta.Color.AMARILLO)
	]))
	
	assert juego.estadoDelJugador[0].mano.total() == 0
	
