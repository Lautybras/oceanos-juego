import pytest
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos

def test_SiSeTieneUnCapitán_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CAPITAN, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTieneUnCapitánYUnAncla_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CAPITAN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 0

def test_SiSeTieneUnCapitánYDosAnclas_ElPuntajeEsOnce():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CAPITAN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 6 + 5



def test_SiSeTieneUnCardumen_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0


def test_SiSeTieneUnCardumenYUnPezEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1 + 0

def test_SiSeTieneUnCardumenYDosPecesEnLaMano_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2 + 1

def test_SiSeTieneUnCardumenYTresPecesEnLaMano_ElPuntajeEsCuatro():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 1

def test_SiSeTieneUnCardumenYCuatroPecesEnLaMano_ElPuntajeEsSeis():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 4
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 4 + 2
	

def test_SiSeTieneUnCardumenYUnDuoDePeces_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2 + 1
	
def test_SiSeTieneUnCardumenYDosDuosDePeces_ElPuntajeEsSeis():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))))
	] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 4 + 2





def test_SiSeTieneUnFaro_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.FARO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0


def test_SiSeTieneUnFaroYUnBarcoEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.FARO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1 + 0

def test_SiSeTieneUnFaroYDosBarcosEnLaMano_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.FARO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2 + 1

def test_SiSeTieneUnFaroYTresBarcosEnLaMano_ElPuntajeEsCuatro():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.FARO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 1

def test_SiSeTieneUnFaroYCuatroBarcosEnLaMano_ElPuntajeEsSeis():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.FARO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 4
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 4 + 2
	

def test_SiSeTieneUnFaroYUnDuoDeBarcos_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.FARO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2 + 1
	
def test_SiSeTieneUnFaroYDosDuosDeBarcos_ElPuntajeEsSeis():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.FARO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 4 + 2




def test_SiSeTieneUnaColonia_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTieneUnaColoniaYUnPingüino_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2 + 1

def test_SiSeTieneUnaColoniaYDosPingüinos_ElPuntajeEsSiete():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 4 + 3

def test_SiSeTieneUnaColoniaYTresPingüinos_ElPuntajeEsOnce():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 6 + 5