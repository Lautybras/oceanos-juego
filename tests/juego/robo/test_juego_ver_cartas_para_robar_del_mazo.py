import pytest
from collections import Counter as Multiset
from juego.partida import PartidaDeOcéanos, JuegoException

def test_SiSeInicióRonda_AlRobarDelMazo_SeDevuelvenDosCartas():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartasParaRobarDelMazo = juego.verCartasParaRobarDelMazo()
	
	assert len(cartasParaRobarDelMazo) == 2

def test_SiSeInicióRonda_AlRobarDelMazo_LasCartasDevueltasSonLasDelTopeDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartasParaRobarDelMazo = juego.verCartasParaRobarDelMazo()
	
	assert cartasParaRobarDelMazo[0] == juego._mazo[-1]
	assert cartasParaRobarDelMazo[1] == juego._mazo[-2]

def test_SiElMazoTieneUnaCarta_AlRobarDelMazo_SeDevuelveUnaCarta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo = [juego._mazo[0]]
	
	cartasParaRobarDelMazo = juego.verCartasParaRobarDelMazo()
	
	assert len(cartasParaRobarDelMazo) == 1

def test_SiElMazoTieneUnaCarta_AlRobarDelMazo_LaCartaDevueltaEsLaDelTopeDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	cartasParaRobarDelMazo = juego.verCartasParaRobarDelMazo()
	
	assert cartasParaRobarDelMazo[0] == juego._mazo[-1]

def test_SiElMazoNoTieneCartas_NoSePuedeRobarDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo = []
	
	with pytest.raises(JuegoException) as excepcion:
		juego.verCartasParaRobarDelMazo()
	
	assert "No se puede robar de un mazo vacío" in str(excepcion.value)

def test_SiSeIntentóRobarDelMazoSinElegir_NoSePuedeRobarDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.verCartasParaRobarDelMazo()
	
	assert "No se ha concretado el robo del mazo (¡falta elegir!)" in str(excepcion.value)

def test_SiSeIntentóRobarDelMazoSinElegir_NoSePuedeJugarDúos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDúoDeBarcos(Multiset())
	
	assert "No se ha concretado el robo del mazo (¡falta elegir!)" in str(excepcion.value)

def test_SiSeIntentóRobarDelMazoSinElegir_NoSePuedePasarDeTurno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No se ha concretado el robo del mazo (¡falta elegir!)" in str(excepcion.value)

def test_SiSeIntentóRobarDelMazoSinElegir_NoSePuedeRobarDelDescarte():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(0)
	
	assert "No se ha concretado el robo del mazo (¡falta elegir!)" in str(excepcion.value)

def test_SiSeInicióRondaYSeRobóDelMazo_NoSePuedeDecirBasta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirBasta()
	
	assert "No se ha concretado el robo del mazo (¡falta elegir!)" in str(excepcion.value)

def test_SiSeInicióRondaYSeRobóDelMazo_NoSePuedeRobarDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.verCartasParaRobarDelMazo()
	
	assert "Ya se ha robado en este turno" in str(excepcion.value)