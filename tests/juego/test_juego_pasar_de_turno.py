import pytest
from juego.juego import EstadoDelJuego, JuegoException

def test_001_SiSeInicióRondaYSeRobóDelDescarte_AlPasarDeTurno_EsTurnoDelJugadorUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)

	juego.pasarTurno()
	
	assert juego.deQuienEsTurno == 1

def test_002_SiSeInicióRonda_NoSePuedePasarTurno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No se puede pasar de turno sin antes haber robado" in str(excepcion.value)
	
def test_003_SiSeInicióRondaYSePasóDeTurno_NoSePuedePasarTurno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No se puede pasar de turno sin antes haber robado" in str(excepcion.value)

def test_004_SiSeInicióRondaParaDosJugadoresYSePasóDeTurnoYSeRobóDelDescarte_AlPasarTurno_EsTurnoDelJugadorCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelDescarte(1)
	
	juego.pasarTurno()
	
	assert juego.deQuienEsTurno == 0

def test_005_SiSeInicióRondaParaTresJugadoresYSePasóDeTurnoYSeRobóDelDescarte_AlPasarTurno_EsTurnoDelJugadorDos():
	juego = EstadoDelJuego(cantidadDeJugadores=3)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelDescarte(1)
	
	juego.pasarTurno()
	
	assert juego.deQuienEsTurno == 2
