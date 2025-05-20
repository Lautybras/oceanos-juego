import pytest
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, JuegoException
from collections import Counter as Multiset

def test_NoSePuedeJugarDúoDeNadadorYTiburónConDúoDeOtroTipo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)] += 2
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeNadadorYTiburón(Multiset([
			Carta(Carta.Tipo.PEZ, Carta.Color.AZUL), Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)
		]), 0)
	
	assert "Ese tipo de dúo no es válido para esta acción" in str(excepcion.value)

def test_NoSePuedeJugarDúoDeNadadorYTiburónConObjetivoFueraDeRangoDeJugadores():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.NADADOR,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.TIBURON,Carta.Color.AMARILLO)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeNadadorYTiburón(Multiset([
			Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL), Carta(Carta.Tipo.TIBURON, Carta.Color.AMARILLO)
		]), 2)
		
	assert "La selección de jugador a robar con el dúo de nadador y tiburón es inválida" in str(excepcion.value)

def test_NoSePuedeJugarDúoDeNadadorYTiburónConObjetivoElJugadorActual():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.NADADOR,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.TIBURON,Carta.Color.AMARILLO)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeNadadorYTiburón(Multiset([
			Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL), Carta(Carta.Tipo.TIBURON, Carta.Color.AMARILLO)
		]), 0)
		
	assert "La selección de jugador a robar con el dúo de nadador y tiburón es inválida" in str(excepcion.value)
	

def test_SiLaManoDelJugadorObjetivoEstáVacía_AlJugarDúoDeNadadorYTiburón_NoSeRobaNingunaCarta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.NADADOR,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.TIBURON,Carta.Color.AMARILLO)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego._estadosDeJugadores[1].mano = Multiset()
	
	cartaRobada = juego.jugarDuoDeNadadorYTiburón(Multiset([
		Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL), Carta(Carta.Tipo.TIBURON, Carta.Color.AMARILLO)
	]), 1)
	
	assert cartaRobada == None
	assert juego._estadosDeJugadores[0].mano.total() == 0
	assert juego._estadosDeJugadores[1].mano.total() == 0
	assert juego._estadosDeJugadores[0].zonaDeDuos.total() == 1
	assert juego._deQuiénEsTurno == 0

def test_SiLaManoDelJugadorObjetivoNoEstáVacía_AlJugarDúoDeNadadorYTiburón_SeRobaUnaCartaDelJugadorObjetivo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego._mazo[-1] = Carta(Carta.Tipo.NADADOR,Carta.Color.AZUL)
	juego._mazo[-3] = Carta(Carta.Tipo.TIBURON,Carta.Color.AMARILLO)
	
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego.pasarTurno()
	juego.robarDelDescarte(0)
	juego.pasarTurno()
	juego.verCartasParaRobarDelMazo()
	juego.robarDelMazo(0,0)
	juego._estadosDeJugadores[1].mano = Multiset([
		Carta(Carta.Tipo.ANCLA, Carta.Color.VIOLETA),
		Carta(Carta.Tipo.COLONIA, Carta.Color.GRIS),
		Carta(Carta.Tipo.PEZ, Carta.Color.AMARILLO)
	])
	manoOriginalJugadorObjetivo = juego._estadosDeJugadores[1].mano.copy()
	
	cartaRobada = juego.jugarDuoDeNadadorYTiburón(Multiset([
		Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL), Carta(Carta.Tipo.TIBURON, Carta.Color.AMARILLO)
	]), 1)
	
	assert cartaRobada in manoOriginalJugadorObjetivo
	assert juego._estadosDeJugadores[0].mano == Multiset([cartaRobada])
	assert juego._estadosDeJugadores[1].mano + Multiset([cartaRobada]) == manoOriginalJugadorObjetivo
	assert juego._estadosDeJugadores[0].zonaDeDuos.total() == 1
	assert juego._deQuiénEsTurno == 0
