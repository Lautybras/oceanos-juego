import pytest
from juego.juego import EstadoDelJuego, JuegoException

def test_SiSeInicióRonda_AlRobarDelDescarte_LaPilaDeDescarteRobadaEstáVacía():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()

	juego.robarDelDescarte(0)

	assert len(juego.descarte[0]) == 0

def test_SiSeInicióRonda_AlRobarDelDescarte_LaPilaDeDescarteNoRobadaTieneUnaCarta():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()

	juego.robarDelDescarte(0)

	assert len(juego.descarte[1]) == 1

def test_SiSeInicióRonda_AlRobarDelDescarte_LaCartaRobadaEstáEnLaManoDelJugadorCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()

	cartaEnDescarte = juego.descarte[0][0]
	juego.robarDelDescarte(0)

	assert juego.estadoDelJugador[0].mano.total() == 1
	assert list(juego.estadoDelJugador[0].mano.elements())[0] == cartaEnDescarte

def test_SiSeInicióRonda_NoSePuedeRobarDeUnaPilaDescarteNoExistente():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()

	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(2)
	
	assert "Pila de descarte no existente" in str(excepcion.value)

def test_SiSeInicióRonda_NoSePuedeRobarDeUnaPilaDescarteVacía():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.descarte[0].pop()

	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(0)
	
	assert "No se puede robar de una pila de descarte vacía" in str(excepcion.value)

def test_SiSeInicióRonda_AlRobarDelDescarte_LaCartaRobadaEsDevueltaPorElMétodo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	cartaEnDescarte = juego.descarte[0][0]

	cartaDevuelta = juego.robarDelDescarte(0)
	
	assert cartaDevuelta == cartaEnDescarte

def test_SiSeInicióRonda_AlRobarDelDescarte_LaManoDelJugadorUnoQuedaIgual():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()

	manoJugadorUno = juego.estadoDelJugador[1].mano
	juego.robarDelDescarte(0)

	assert juego.estadoDelJugador[1].mano == manoJugadorUno

def test_SiSeInicióRondaYSeRobóDelDescarte_NoSePuedeRobarDelDescarte():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	
	assert "Ya se ha robado en este turno" in str(excepcion.value)