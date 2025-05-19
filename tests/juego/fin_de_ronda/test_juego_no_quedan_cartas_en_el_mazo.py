import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoException

def test_SiNoHayCartasEnElMazo_AlPasarTurno_LaRondaTerminaYNadieObtienePuntos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.mazo = []
	
	juego.pasarTurno()
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajesDeJuego[0] == 0
	assert juego.puntajesDeJuego[1] == 0
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoHayCartasEnElMazo_AlDecirÚltimaChance_LaRondaTerminaYNadieObtienePuntos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.CELESTE)] += 4
	juego.mazo = []
	
	juego.decirÚltimaChance()
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajesDeJuego[0] == 0
	assert juego.puntajesDeJuego[1] == 0
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiNoHayCartasEnElMazo_AlJugarDúoDeBarcos_LaRondaTerminaYNadieObtienePuntos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.CELESTE)] += 2
	juego.robarDelDescarte(0)
	juego.mazo = []
	
	juego.jugarDuoDeBarcos(Multiset([
		Carta(Carta.Tipo.BARCO, Carta.Color.CELESTE), Carta(Carta.Tipo.BARCO, Carta.Color.CELESTE)
	]))
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajesDeJuego[0] == 0
	assert juego.puntajesDeJuego[1] == 0
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	assert "No hay una ronda en curso" in str(excepcion.value)



def test_SiNoHayCartasEnElMazo_AlDecirBasta_LaRondaTerminaYCadaJugadorObtieneSuPuntajeDeRonda():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.estadoDelJugador[0].mano.clear()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.CELESTE)] += 4
	juego.mazo = []
	
	juego.decirBasta()
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajesDeJuego[0] == 9
	assert juego.puntajesDeJuego[1] == 0
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	assert "No hay una ronda en curso" in str(excepcion.value)