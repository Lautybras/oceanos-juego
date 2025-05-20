import pytest
from juego.juego import PartidaDeOcéanos, JuegoInvalidoException

def test_AlCrearJuegoParaDosJugadores_JuegoNoHaTerminado():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	assert juego.haTerminado() == False

def test_AlCrearJuegoParaDosJugadores_LosPuntajesDeJuegoInicianEnCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	
	assert len(juego.puntajes) == 2
	assert juego.puntajes[0] == 0
	assert juego.puntajes[1] == 0

def test_AlCrearJuegoParaDosJugadores_ElPuntajeParaGanarEsCuarenta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)

	assert juego.puntajeParaGanar == 40

def test_AlCrearJuegoParaTresJugadores_ElPuntajeParaGanarEsTreintaYCinco():
	juego = PartidaDeOcéanos(cantidadDeJugadores=3)

	assert juego.puntajeParaGanar == 35

def test_AlCrearJuegoParaTresJugadores_ElPuntajeParaGanarEsTreinta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=4)

	assert juego.puntajeParaGanar == 30

def test_NoSePuedeCrearJuegoParaMenosDeDosJugadores():
	with pytest.raises(JuegoInvalidoException):
		juego = PartidaDeOcéanos(cantidadDeJugadores=1)
	
	with pytest.raises(JuegoInvalidoException):
		juego = PartidaDeOcéanos(cantidadDeJugadores=0)

def test_NoSePuedeCrearJuegoParaMásDeCuatroJugadores():
	with pytest.raises(JuegoInvalidoException) as excepcion:
		juego = PartidaDeOcéanos(cantidadDeJugadores=5)
	
	assert "La cantidad de jugadores es inválida" in str(excepcion.value)
