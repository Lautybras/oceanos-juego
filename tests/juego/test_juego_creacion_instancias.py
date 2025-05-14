import pytest
from juego.juego import EstadoDelJuego, JuegoInvalidoException

def test_AlCrearJuegoParaDosJugadores_JuegoNoHaTerminado():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	assert juego.haTerminado == False

def test_AlCrearJuegoParaDosJugadores_LosPuntajesDeJuegoInicianEnCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	
	assert len(juego.puntajesDeJuego) == 2
	assert juego.puntajesDeJuego[0] == 0
	assert juego.puntajesDeJuego[1] == 0

def test_AlCrearJuegoParaDosJugadores_ElPuntajeParaGanarEsCuarenta():
	juego = EstadoDelJuego(cantidadDeJugadores=2)

	assert juego.puntajeParaGanar() == 40

def test_AlCrearJuegoParaTresJugadores_ElPuntajeParaGanarEsTreintaYCinco():
	juego = EstadoDelJuego(cantidadDeJugadores=3)

	assert juego.puntajeParaGanar() == 35

def test_AlCrearJuegoParaTresJugadores_ElPuntajeParaGanarEsTreinta():
	juego = EstadoDelJuego(cantidadDeJugadores=4)

	assert juego.puntajeParaGanar() == 30

def test_NoSePuedeCrearJuegoParaMenosDeDosJugadores():
	with pytest.raises(JuegoInvalidoException):
		juego = EstadoDelJuego(cantidadDeJugadores=1)
	
	with pytest.raises(JuegoInvalidoException):
		juego = EstadoDelJuego(cantidadDeJugadores=0)

def test_NoSePuedeCrearJuegoParaMásDeCuatroJugadores():
	with pytest.raises(JuegoInvalidoException) as excepcion:
		juego = EstadoDelJuego(cantidadDeJugadores=5)
	
	assert "La cantidad de jugadores es inválida" in str(excepcion.value)
