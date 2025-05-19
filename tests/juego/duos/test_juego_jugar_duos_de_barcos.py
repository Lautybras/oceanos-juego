import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoException
from collections import Counter as Multiset

def test_NoSePuedeJugarDúoDeBarcosConDúoDeOtroTipo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)] += 2
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
	
		juego.jugarDuoDeBarcos(Multiset([
			Carta(Carta.Tipo.PEZ, Carta.Color.AZUL), Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)
		]))
	
	assert "Ese tipo de dúo no es válido para esta acción" in str(excepcion.value)

def test_SiSePuedeJugarDúoDeBarcos_AlJugarDúoDeBarcos_SigueSiendoTurnoDelJugadorQueJugóElDúo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)	
	
	
	juego.jugarDuoDeBarcos(Multiset([
			Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
			Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
		]))
	
	assert juego.deQuienEsTurno == 0


def test_SiSePuedeJugarDúoDeBarcos_AlJugarDúoDeBarcos_NoSePuedePasarTurno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)	
	
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	]))
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No se puede terminar el turno sin antes haber robado" in str(excepcion.value)
	
def test_SiSeJugóUnDúoDeBarcos_SePuedeRobarDelMazo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	]))
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,1)
	
	assert juego.estadoDelJugador[0].mano.total() == 1
	assert juego.estadoDelJugador[0].zonaDeDuos.total() == 1
	assert juego.deQuienEsTurno == 0

def test_SiSeJugóUnDúoDeBarcos_SePuedeRobarDelDescarte():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	]))
	
	juego.robarDelDescarte(1)
	
	assert juego.estadoDelJugador[0].mano.total() == 1
	assert juego.estadoDelJugador[0].zonaDeDuos.total() == 1
	assert juego.deQuienEsTurno == 0

def test_SiSeJugóUnDúoDeBarcos_NoSePuedeJugarOtroDúoSinAntesRobar():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.VERDE)
	juego.mazo[-5] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-7] = Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	
	for _ in range(3):
		juego.robarDelMazo()
		juego.elegirRoboDelMazo(0,0)
		juego.pasarTurno()
		juego.robarDelDescarte(0)
		juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA),
		Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	]))
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset([
			Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
			Carta(Carta.Tipo.BARCO,Carta.Color.VERDE)
		]))
	
	assert "No se puede jugar dúos sin antes haber robado" in str(excepcion.value)
	
def test_SiSeJugóUnDúoDeBarcosYSeRobó_SePuedePasarTurno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	]))
	juego.robarDelDescarte(1)
	
	
	juego.pasarTurno()
	
	assert juego.estadoDelJugador[0].mano.total() == 1
	assert juego.estadoDelJugador[0].zonaDeDuos.total() == 1
	assert juego.deQuienEsTurno == 1

def test_SiSeJugóUnDúoDeBarcosYSeRobó_SePuedeJugarUnDúoDeOtroTipo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA)
	juego.mazo[-3] = Carta(Carta.Tipo.PEZ,Carta.Color.VERDE)
	juego.mazo[-5] = Carta(Carta.Tipo.PEZ,Carta.Color.AZUL)
	juego.mazo[-7] = Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	
	for _ in range(3):
		juego.robarDelMazo()
		juego.elegirRoboDelMazo(0,0)
		juego.pasarTurno()
		juego.robarDelDescarte(0)
		juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA),
		Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	]))
	juego.robarDelDescarte(0)
	
	juego.jugarDuoDePeces(Multiset([
		Carta(Carta.Tipo.PEZ,Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ,Carta.Color.VERDE)
	]))
	
	assert juego.estadoDelJugador[0].mano.total() == 1 + 1
	assert juego.estadoDelJugador[0].zonaDeDuos.total() == 2
	assert juego.deQuienEsTurno == 0

def test_SiSeJugóUnDúoDeBarcosYSeRobó_SePuedeJugarOtroDúoDeBarcos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA)
	juego.mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.VERDE)
	juego.mazo[-5] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego.mazo[-7] = Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	
	for _ in range(3):
		juego.robarDelMazo()
		juego.elegirRoboDelMazo(0,0)
		juego.pasarTurno()
		juego.robarDelDescarte(0)
		juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA),
		Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	]))
	juego.robarDelDescarte(0)
	
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.VERDE)
	]))
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	
	assert juego.estadoDelJugador[0].mano.total() == 1 + 1
	assert juego.estadoDelJugador[0].zonaDeDuos.total() == 2
	assert juego.deQuienEsTurno == 0