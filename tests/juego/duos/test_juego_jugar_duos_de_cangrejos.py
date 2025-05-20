import pytest
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, JuegoException
from collections import Counter as Multiset

def test_NoSePuedeJugarDúoDeCangrejosConDúoDeOtroTipo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)] += 2
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeCangrejos(Multiset([
			Carta(Carta.Tipo.PEZ, Carta.Color.AZUL), Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)
		]), 0, 0)
	
	assert "Ese tipo de dúo no es válido para esta acción" in str(excepcion.value)

def test_SiElDescarteEstáVacío_AlJugarDúoDeCangrejos_NoSeRobaNingunaCarta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AMARILLO)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego._descarte = ([], [])
	
	cartaRobada = juego.jugarDuoDeCangrejos(Multiset([
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL), Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
	]), 0, 0)
	
	assert cartaRobada == None
	assert juego._estadosDeJugadores[0].mano.total() == 0
	assert juego._estadosDeJugadores[0].zonaDeDuos.total() == 1
	assert juego._deQuiénEsTurno == 0

def test_SiElDescarteNoEstáVacío_NoSePuedeJugarDúoDeCangrejosEnPilaDeDescarteVacía():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AMARILLO)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego._descarte[1].pop()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeCangrejos(Multiset([
			Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL), Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
		]), 1, 0)
	
	assert "La selección de robo con el dúo de cangrejos es inválida" in str(excepcion.value)
	
def test_SiElDescarteNoEstáVacío_NoSePuedeJugarDúoDeCangrejosEnÍndiceInexistenteDePilaDeDescarte():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AMARILLO)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeCangrejos(Multiset([
			Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL), Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
		]), 0, 3)
	
	assert "La selección de robo con el dúo de cangrejos es inválida" in str(excepcion.value)
	
def test_SiElDescarteNoEstáVacío_AlJugarDúoDeCangrejos_SeRobaLaCartaSeleccionada():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AZUL)
	juego._mazo[-5] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AMARILLO)
	cartaARobarConDúoDeCangrejo = juego._mazo[-2]
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,1)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	descarteAntesDelDúo = (juego._descarte[0].copy(), juego._descarte[1].copy())
	
	cartaRobada = juego.jugarDuoDeCangrejos(Multiset([
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL), Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
	]), 0, 1)
	
	assert cartaRobada == cartaARobarConDúoDeCangrejo
	assert juego._estadosDeJugadores[0].mano == Multiset([cartaARobarConDúoDeCangrejo])
	assert juego._estadosDeJugadores[0].zonaDeDuos.total() == 1
	assert juego._deQuiénEsTurno == 0
	assert juego._descarte[1] == descarteAntesDelDúo[1]
	assert juego._descarte[0] == descarteAntesDelDúo[0][0:1] + descarteAntesDelDúo[0][2:]
