import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, JuegoException

def test_SiNoHayCartasEnElMazo_AlPasarTurno_LaRondaTerminaYNadieObtienePuntos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._mazo = []
	
	juego.pasarTurno()
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajes[0] == 0
	assert juego.puntajes[1] == 0
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoHayCartasEnElMazo_AlDecirÚltimaChance_LaRondaTerminaYNadieObtienePuntos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.CELESTE)] += 4
	juego._mazo = []
	
	juego.decirÚltimaChance()
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajes[0] == 0
	assert juego.puntajes[1] == 0
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoHayCartasEnElMazo_AlJugarDúoDeBarcos_LaRondaTerminaYNadieObtienePuntos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.CELESTE)] += 2
	juego.robarDelDescarte(0)
	juego._mazo = []
	
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO, Carta.Color.CELESTE), Carta(Carta.Tipo.BARCO, Carta.Color.CELESTE)
	]))
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajes[0] == 0
	assert juego.puntajes[1] == 0
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	assert "No hay una ronda en curso" in str(excepcion.value)



def test_SiNoHayCartasEnElMazo_AlDecirBasta_LaRondaTerminaYCadaJugadorObtieneSuPuntajeDeRonda():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano.clear()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.CELESTE)] += 4
	juego._mazo = []
	
	juego.decirBasta()
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajes[0] == 9
	assert juego.puntajes[1] == 0
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	assert "No hay una ronda en curso" in str(excepcion.value)