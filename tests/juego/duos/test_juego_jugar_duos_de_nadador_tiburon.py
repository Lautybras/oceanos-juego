import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego, JuegoException
from collections import Counter as Multiset

def test_NoSePuedeJugarDúoDeNadadorYTiburónConDúoDeOtroTipo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)] += 2
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeNadadorYTiburón(Multiset([
			Carta(Carta.Tipo.PEZ, Carta.Color.AZUL), Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)
		]), 0)
	
	assert "Ese tipo de dúo no es válido para esta acción" in str(excepcion.value)

def test_NoSePuedeJugarDúoDeNadadorYTiburónConObjetivoFueraDeRangoDeJugadores():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.NADADOR,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.TIBURON,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeNadadorYTiburón(Multiset([
			Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL), Carta(Carta.Tipo.TIBURON, Carta.Color.AMARILLO)
		]), 2)
		
	assert "La selección de jugador a robar con el dúo de nadador y tiburón es inválida" in str(excepcion.value)

def test_NoSePuedeJugarDúoDeNadadorYTiburónConObjetivoElJugadorActual():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.NADADOR,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.TIBURON,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeNadadorYTiburón(Multiset([
			Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL), Carta(Carta.Tipo.TIBURON, Carta.Color.AMARILLO)
		]), 0)
		
	assert "La selección de jugador a robar con el dúo de nadador y tiburón es inválida" in str(excepcion.value)
	

def test_SiLaManoDelJugadorObjetivoEstáVacía_AlJugarDúoDeNadadorYTiburón_NoSeRobaNingunaCarta():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.NADADOR,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.TIBURON,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.estadoDelJugador[1].mano = Multiset()
	
	cartaRobada = juego.jugarDuoDeNadadorYTiburón(Multiset([
		Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL), Carta(Carta.Tipo.TIBURON, Carta.Color.AMARILLO)
	]), 1)
	
	assert cartaRobada == None
	assert juego.estadoDelJugador[0].mano.total() == 0
	assert juego.estadoDelJugador[1].mano.total() == 0
	assert juego.estadoDelJugador[0].zonaDeDuos.total() == 1
	assert juego.deQuienEsTurno == 0

def test_SiLaManoDelJugadorObjetivoNoEstáVacía_AlJugarDúoDeNadadorYTiburón_SeRobaUnaCartaDelJugadorObjetivo():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.mazo[-1] = Carta(Carta.Tipo.NADADOR,Carta.Color.AZUL)
	juego.mazo[-3] = Carta(Carta.Tipo.TIBURON,Carta.Color.AMARILLO)
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.estadoDelJugador[1].mano = Multiset([
		Carta(Carta.Tipo.ANCLA, Carta.Color.VIOLETA),
		Carta(Carta.Tipo.COLONIA, Carta.Color.GRIS),
		Carta(Carta.Tipo.PEZ, Carta.Color.AMARILLO)
	])
	manoOriginalJugadorObjetivo = juego.estadoDelJugador[1].mano.copy()
	
	cartaRobada = juego.jugarDuoDeNadadorYTiburón(Multiset([
		Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL), Carta(Carta.Tipo.TIBURON, Carta.Color.AMARILLO)
	]), 1)
	
	assert cartaRobada in manoOriginalJugadorObjetivo
	assert juego.estadoDelJugador[0].mano == Multiset([cartaRobada])
	assert juego.estadoDelJugador[1].mano + Multiset([cartaRobada]) == manoOriginalJugadorObjetivo
	assert juego.estadoDelJugador[0].zonaDeDuos.total() == 1
	assert juego.deQuienEsTurno == 0
