import pytest
from juego.carta import Carta
from juego.partida import PartidaDeOcéanos, JuegoException
from collections import Counter as Multiset

def test_NoSePuedeJugarDúoDeBarcosConDúoDeOtroTipo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)] += 2
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
	
		juego.jugarDúoDeBarcos(Multiset([
			Carta(Carta.Tipo.PEZ, Carta.Color.AZUL), Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)
		]))
	
	assert "Ese tipo de dúo no es válido para esta acción" in str(excepcion.value)

def test_SiSePuedeJugarDúoDeBarcos_AlJugarDúoDeBarcos_SigueSiendoTurnoDelJugadorQueJugóElDúo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)	
	
	
	juego.jugarDúoDeBarcos(Multiset([
			Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
			Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
		]))
	
	assert juego._deQuiénEsTurno == 0


def test_SiSePuedeJugarDúoDeBarcos_AlJugarDúoDeBarcos_NoSePuedePasarTurno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)	
	
	juego.jugarDúoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	]))
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No se puede terminar el turno sin antes haber robado" in str(excepcion.value)
	
def test_SiSeJugóUnDúoDeBarcos_SePuedeRobarDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.jugarDúoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	]))
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,1)
	
	assert juego._estadosDeJugadores[0].mano.total() == 1
	assert juego._estadosDeJugadores[0].zonaDeDúos.total() == 1
	assert juego._deQuiénEsTurno == 0

def test_SiSeJugóUnDúoDeBarcos_SePuedeRobarDelDescarte():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.jugarDúoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	]))
	
	juego.robarDelDescarte(1)
	
	assert juego._estadosDeJugadores[0].mano.total() == 1
	assert juego._estadosDeJugadores[0].zonaDeDúos.total() == 1
	assert juego._deQuiénEsTurno == 0

def test_SiSeJugóUnDúoDeBarcos_NoSePuedeJugarOtroDúoSinAntesRobar():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA)
	juego._mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.VERDE)
	juego._mazo[-5] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego._mazo[-7] = Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	
	for _ in range(3):
		juego.verCartasParaRobarDelMazo()
		juego.robarDelMazo(0,0)
		juego.pasarTurno()
		juego.robarDelDescarte(0)
		juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	juego.jugarDúoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA),
		Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	]))
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDúoDeBarcos(Multiset([
			Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
			Carta(Carta.Tipo.BARCO,Carta.Color.VERDE)
		]))
	
	assert "No se puede jugar dúos sin antes haber robado" in str(excepcion.value)
	
def test_SiSeJugóUnDúoDeBarcosYSeRobó_SePuedePasarTurno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.jugarDúoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	]))
	juego.robarDelDescarte(1)
	
	
	juego.pasarTurno()
	
	assert juego._estadosDeJugadores[0].mano.total() == 1
	assert juego._estadosDeJugadores[0].zonaDeDúos.total() == 1
	assert juego._deQuiénEsTurno == 1

def test_SiSeJugóUnDúoDeBarcosYSeRobó_SePuedeJugarUnDúoDeOtroTipo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA)
	juego._mazo[-3] = Carta(Carta.Tipo.PEZ,Carta.Color.VERDE)
	juego._mazo[-5] = Carta(Carta.Tipo.PEZ,Carta.Color.AZUL)
	juego._mazo[-7] = Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	
	for _ in range(3):
		juego.verCartasParaRobarDelMazo()
		juego.robarDelMazo(0,0)
		juego.pasarTurno()
		juego.robarDelDescarte(0)
		juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.jugarDúoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA),
		Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	]))
	juego.robarDelDescarte(0)
	
	juego.jugarDúoDePeces(Multiset([
		Carta(Carta.Tipo.PEZ,Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ,Carta.Color.VERDE)
	]))
	
	assert juego._estadosDeJugadores[0].mano.total() == 1 + 1
	assert juego._estadosDeJugadores[0].zonaDeDúos.total() == 2
	assert juego._deQuiénEsTurno == 0

def test_SiSeJugóUnDúoDeBarcosYSeRobó_SePuedeJugarOtroDúoDeBarcos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA)
	juego._mazo[-3] = Carta(Carta.Tipo.BARCO,Carta.Color.VERDE)
	juego._mazo[-5] = Carta(Carta.Tipo.BARCO,Carta.Color.AZUL)
	juego._mazo[-7] = Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	
	for _ in range(3):
		juego.verCartasParaRobarDelMazo()
		juego.robarDelMazo(0,0)
		juego.pasarTurno()
		juego.robarDelDescarte(0)
		juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.jugarDúoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.NARANJA),
		Carta(Carta.Tipo.BARCO,Carta.Color.VIOLETA)
	]))
	juego.robarDelDescarte(0)
	
	juego.jugarDúoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO,Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO,Carta.Color.VERDE)
	]))
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	
	assert juego._estadosDeJugadores[0].mano.total() == 1 + 1
	assert juego._estadosDeJugadores[0].zonaDeDúos.total() == 2
	assert juego._deQuiénEsTurno == 0