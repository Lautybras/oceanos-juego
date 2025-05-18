import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoException, SIRENAS_INF

def test_SiAlRobarDelDescarteSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego.descarte[0].pop()
	juego.descarte[0].append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.robarDelDescarte(0)
	
	assert juego.rondaEnCurso == False
	assert juego.haTerminado == True
	assert juego.ganador == 0
	assert juego.puntajesDeJuego[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)


def test_SiAlRobarDelMazoSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego.mazo[-1] = Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	assert juego.rondaEnCurso == False
	assert juego.haTerminado == True
	assert juego.ganador == 0
	assert juego.puntajesDeJuego[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiAlJugarDúoDePecesSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)] += 1
	juego.mazo[-1] = Carta(Carta.Tipo.PEZ, Carta.Color.NARANJA)
	juego.mazo[-3] = Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDePeces(Multiset([
		Carta(Carta.Tipo.PEZ, Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ, Carta.Color.NARANJA)
	]))
	
	assert juego.rondaEnCurso == False
	assert juego.haTerminado == True
	assert juego.ganador == 0
	assert juego.puntajesDeJuego[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiAlJugarDúoDeCangrejosSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.ROSA)] += 1
	juego.descarte[0].pop()
	juego.descarte[0].append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.mazo[-1] = Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO)
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDeCangrejos(Multiset([
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.ROSA)
	]), 0, 0)
	
	assert juego.rondaEnCurso == False
	assert juego.haTerminado == True
	assert juego.ganador == 0
	assert juego.puntajesDeJuego[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiAlJugarDúoDeNadadorYTiburónSeConsiguenCuatroSirenas_ElJugadorConLasSirenasGanaLaPartida():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.ROSA)] += 1
	juego.estadoDelJugador[1].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 1
	juego.mazo[-1] = Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.jugarDuoDeNadadorYTiburón(Multiset([
		Carta(Carta.Tipo.TIBURON, Carta.Color.ROSA),
		Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)
	]), 1)
	
	assert juego.rondaEnCurso == False
	assert juego.haTerminado == True
	assert juego.ganador == 0
	assert juego.puntajesDeJuego[0] == SIRENAS_INF
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	assert "No hay una ronda en curso" in str(excepcion.value)
