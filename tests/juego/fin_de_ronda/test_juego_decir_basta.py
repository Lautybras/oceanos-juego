import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, JuegoException

def test_SiNoSeRobó_NoSePuedeDecirBasta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirBasta()
	
	assert "No se puede terminar el turno sin antes haber robado" in str(excepcion.value)

def test_SiNoSeTienenSietePuntos_NoSePuedeDecirBasta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirBasta()
	
	assert "No se puede terminar la ronda si no se tienen al menos siete puntos" in str(excepcion.value)
	
def test_SiSeTienenAlMenosSietePuntosYSeRobó_AlDecirBasta_LaRondaTerminaYCadaJugadorObtieneSuPuntajeDeRonda():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	
	puntajesEsperados = (juego._estadosDeJugadores[0].puntajeDeRonda(), juego._estadosDeJugadores[1].puntajeDeRonda())
	
	juego.decirBasta()
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajes[0] == puntajesEsperados[0]
	assert juego.puntajes[1] == puntajesEsperados[1]

def test_SiSeDijoBasta_NoSePuedeRobarDelDescarte():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoBasta_NoSePuedeRobarDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.verCartasParaRobarDelMazo()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoBasta_NoSePuedeElegirRoboDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo(0,0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)
	
def test_SiSeDijoBasta_NoSePuedeJugarDúoDePeces():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDePeces(Multiset())
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoBasta_NoSePuedeJugarDúoDeBarcos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset())
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoBasta_NoSePuedeJugarDúoDeCangrejos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeCangrejos(Multiset(), 0, 0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoBasta_NoSePuedeJugarDuoDeNadadorYTiburón():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeNadadorYTiburón(Multiset(), 0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoBasta_NoSePuedePasarTurno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoBasta_NoSePuedeDecirBasta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirBasta()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoBasta_NoSePuedeDecirÚltimaChance():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirBasta()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirÚltimaChance()
	
	assert "No hay una ronda en curso" in str(excepcion.value)