import pytest
from juego.partida import PartidaDeOcéanos, JuegoException

def test_SiSeInicióRondaYSeRobóDelDescarte_AlPasarDeTurno_EsTurnoDelJugadorUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)

	juego.pasarTurno()
	
	assert juego._deQuiénEsTurno == 1

def test_SiSeInicióRonda_NoSePuedePasarTurno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No se puede terminar el turno sin antes haber robado" in str(excepcion.value)
	
def test_SiSeInicióRondaYSePasóDeTurno_NoSePuedePasarTurno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No se puede terminar el turno sin antes haber robado" in str(excepcion.value)

def test_SiSeInicióRondaParaDosJugadoresYSePasóDeTurnoYSeRobóDelDescarte_AlPasarTurno_EsTurnoDelJugadorCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelDescarte(1)
	
	juego.pasarTurno()
	
	assert juego._deQuiénEsTurno == 0

def test_SiSeInicióRondaParaTresJugadoresYSePasóDeTurnoYSeRobóDelDescarte_AlPasarTurno_EsTurnoDelJugadorDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=3)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelDescarte(1)
	
	juego.pasarTurno()
	
	assert juego._deQuiénEsTurno == 2
