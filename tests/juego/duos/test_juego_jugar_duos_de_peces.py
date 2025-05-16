import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoException
from collections import Counter as Multiset

def test_NoSePuedeJugarDúoDePecesConDúoDeOtroTipo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.AZUL)] += 2
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
	
		juego.jugarDuoDePeces(Multiset([
			Carta(Carta.Tipo.BARCO, Carta.Color.AZUL), Carta(Carta.Tipo.BARCO, Carta.Color.AZUL)
		]))
	
	assert "Ese tipo de dúo no es válido para esta acción" in str(excepcion.value)

def test_SiSePuedeJugarDúoDePecesYQuedanCartasEnElMazo_AlJugarDúoDePeces_SeRobaLaCartaSuperiorDelMazo():
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
	cartaSuperiorDelMazo = juego.mazo[-1]
	
	
	cartaRobada = juego.jugarDuoDePeces(Multiset([
		Carta(Carta.Tipo.PEZ,Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ,Carta.Color.AMARILLO)
	]))
	
	assert juego.estadoDelJugador[0].mano == Multiset([cartaSuperiorDelMazo])
	assert cartaRobada == cartaSuperiorDelMazo
	assert len(juego.mazo) == 56 - 2 - 0 - 2 - 1

def test_SiSePuedeJugarDúoDePecesYNoQuedanCartasEnElMazo_AlJugarDúoDePeces_NoSeRobanCartas():
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
	juego.mazo = []
	

	cartaRobada = juego.jugarDuoDePeces(Multiset([
		Carta(Carta.Tipo.PEZ,Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ,Carta.Color.AMARILLO)
	]))
	
	assert juego.estadoDelJugador[0].mano == Multiset()
	assert len(juego.mazo) == 0
	assert cartaRobada == None