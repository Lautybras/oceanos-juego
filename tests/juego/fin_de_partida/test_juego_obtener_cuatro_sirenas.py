import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, JuegoException, SIRENAS_INF

def test_SiAlRobarDelDescarteSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._descarte[0].pop()
	juego._descarte[0].append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.robarDelDescarte(0)
	
	assert juego.rondaEnCurso() == False
	assert juego.haTerminado() == True
	assert juego.jugadorGanador == 0
	assert juego.puntajes[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)


def test_SiAlRobarDelMazoSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._mazo[-1] = Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	assert juego.rondaEnCurso() == False
	assert juego.haTerminado() == True
	assert juego.jugadorGanador == 0
	assert juego.puntajes[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiAlJugarDúoDePecesSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)] += 1
	juego._mazo[-1] = Carta(Carta.Tipo.PEZ, Carta.Color.NARANJA)
	juego._mazo[-3] = Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDePeces(Multiset([
		Carta(Carta.Tipo.PEZ, Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ, Carta.Color.NARANJA)
	]))
	
	assert juego.rondaEnCurso() == False
	assert juego.haTerminado() == True
	assert juego.jugadorGanador == 0
	assert juego.puntajes[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiAlJugarDúoDeCangrejosSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.ROSA)] += 1
	juego._descarte[0].pop()
	juego._descarte[0].append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego._mazo[-1] = Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDeCangrejos(Multiset([
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.ROSA)
	]), 0, 0)
	
	assert juego.rondaEnCurso() == False
	assert juego.haTerminado() == True
	assert juego.jugadorGanador == 0
	assert juego.puntajes[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiAlJugarDúoDeNadadorYTiburónSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.ROSA)] += 1
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 1
	juego._mazo[-1] = Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDeNadadorYTiburón(Multiset([
		Carta(Carta.Tipo.TIBURON, Carta.Color.ROSA),
		Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)
	]), 1)
	
	assert juego.rondaEnCurso() == False
	assert juego.haTerminado() == True
	assert juego.jugadorGanador == 0
	assert juego.puntajes[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)
