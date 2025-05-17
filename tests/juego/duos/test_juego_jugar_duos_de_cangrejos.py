import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoException
from collections import Counter as Multiset

def test_NoSePuedeJugarDúoDeCangrejosConDúoDeOtroTipo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)] += 2
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeCangrejos(Multiset([
			Carta(Carta.Tipo.PEZ, Carta.Color.AZUL), Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)
		]), 0, 0)
	
	assert "Ese tipo de dúo no es válido para esta acción" in str(excepcion.value)

def test_SiElDescarteEstáVacío_AlJugarDúoDeCangrejos_NoSeRobaNingunaCarta():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.descarte = ([], [])
	
	cartaRobada = juego.jugarDuoDeCangrejos(Multiset([
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL), Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
	]), 0, 0)
	
	assert cartaRobada == None
	assert juego.estadoDelJugador[0].mano.total() == 0
	assert juego.estadoDelJugador[0].zonaDeDuos.total() == 1
	assert juego.deQuienEsTurno == 0

def test_SiElDescarteNoEstáVacío_NoSePuedeJugarDúoDeCangrejosEnPilaDeDescarteVacía():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.descarte[1].pop()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeCangrejos(Multiset([
			Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL), Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
		]), 1, 0)
	
	assert "La selección de robo con el dúo de cangrejos es inválida" in str(excepcion.value)
	
def test_SiElDescarteNoEstáVacío_NoSePuedeJugarDúoDeCangrejosEnÍndiceInexistenteDePilaDeDescarte():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeCangrejos(Multiset([
			Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL), Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
		]), 0, 3)
	
	assert "La selección de robo con el dúo de cangrejos es inválida" in str(excepcion.value)
	
def test_SiElDescarteNoEstáVacío_AlJugarDúoDeCangrejos_SeRobaLaCartaSeleccionada():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AZUL)
	juego.mazo[-5] = Carta(Carta.Tipo.CANGREJO,Carta.Color.AMARILLO)
	cartaARobarConDúoDeCangrejo = juego.mazo[-2]
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,1)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	descarteAntesDelDúo = (juego.descarte[0].copy(), juego.descarte[1].copy())
	
	cartaRobada = juego.jugarDuoDeCangrejos(Multiset([
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL), Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
	]), 0, 1)
	
	assert cartaRobada == cartaARobarConDúoDeCangrejo
	assert juego.estadoDelJugador[0].mano == Multiset([cartaARobarConDúoDeCangrejo])
	assert juego.estadoDelJugador[0].zonaDeDuos.total() == 1
	assert juego.deQuienEsTurno == 0
	assert juego.descarte[1] == descarteAntesDelDúo[1]
	assert juego.descarte[0] == descarteAntesDelDúo[0][0:1] + descarteAntesDelDúo[0][2:]
