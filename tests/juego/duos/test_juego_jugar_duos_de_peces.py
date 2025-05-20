import pytest
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, JuegoException
from collections import Counter as Multiset

def test_NoSePuedeJugarDúoDePecesConDúoDeOtroTipo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.AZUL)] += 2
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
	
		juego.jugarDuoDePeces(Multiset([
			Carta(Carta.Tipo.BARCO, Carta.Color.AZUL), Carta(Carta.Tipo.BARCO, Carta.Color.AZUL)
		]))
	
	assert "Ese tipo de dúo no es válido para esta acción" in str(excepcion.value)

def test_SiSePuedeJugarDúoDePecesYQuedanCartasEnElMazo_AlJugarDúoDePeces_SeRobaLaCartaSuperiorDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.PEZ,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.PEZ,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	cartaSuperiorDelMazo = juego._mazo[-1]
	
	
	cartaRobada = juego.jugarDuoDePeces(Multiset([
		Carta(Carta.Tipo.PEZ,Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ,Carta.Color.AMARILLO)
	]))
	
	assert juego._estadosDeJugadores[0].mano == Multiset([cartaSuperiorDelMazo])
	assert cartaRobada == cartaSuperiorDelMazo
	assert len(juego._mazo) == 56 - 2 - 0 - 2 - 1

def test_SiSePuedeJugarDúoDePecesYNoQuedanCartasEnElMazo_AlJugarDúoDePeces_NoSeRobanCartas():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.PEZ,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.PEZ,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego._mazo = []
	

	cartaRobada = juego.jugarDuoDePeces(Multiset([
		Carta(Carta.Tipo.PEZ,Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ,Carta.Color.AMARILLO)
	]))
	
	assert juego._estadosDeJugadores[0].mano == Multiset()
	assert len(juego._mazo) == 0
	assert cartaRobada == None