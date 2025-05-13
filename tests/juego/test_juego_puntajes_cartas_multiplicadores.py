import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego

def test_001_SiSeTieneUnCapitán_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CAPITAN, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_002_SiSeTieneUnCapitánYUnAncla_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CAPITAN, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 0

def test_003_SiSeTieneUnCapitánYDosAnclas_ElPuntajeEsOnce():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CAPITAN, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 6 + 5



def test_004_SiSeTieneUnCardumen_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0


def test_005_SiSeTieneUnCardumenYUnPezEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1 + 0

def test_006_SiSeTieneUnCardumenYDosPecesEnLaMano_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2 + 1

def test_007_SiSeTieneUnCardumenYTresPecesEnLaMano_ElPuntajeEsCuatro():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 1

def test_008_SiSeTieneUnCardumenYCuatroPecesEnLaMano_ElPuntajeEsSeis():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 4 + 2
	

def test_009_SiSeTieneUnCardumenYUnDuoDePeces_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2 + 1
	
def test_010_SiSeTieneUnCardumenYDosDuosDePeces_ElPuntajeEsSeis():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	)
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 4 + 2





def test_011_SiSeTieneUnFaro_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.FARO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0


def test_012_SiSeTieneUnFaroYUnBarcoEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.FARO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1 + 0

def test_013_SiSeTieneUnFaroYDosBarcosEnLaMano_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.FARO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2 + 1

def test_014_SiSeTieneUnFaroYTresBarcosEnLaMano_ElPuntajeEsCuatro():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.FARO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 1

def test_015_SiSeTieneUnFaroYCuatroBarcosEnLaMano_ElPuntajeEsSeis():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.FARO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 4 + 2
	

def test_016_SiSeTieneUnFaroYUnDuoDeBarcos_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.FARO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2 + 1
	
def test_017_SiSeTieneUnFaroYDosDuosDeBarcos_ElPuntajeEsSeis():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.FARO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	)
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 4 + 2




def test_018_SiSeTieneUnaColonia_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_019_SiSeTieneUnaColoniaYUnPingüino_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2 + 1

def test_020_SiSeTieneUnaColoniaYDosPingüinos_ElPuntajeEsSiete():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 4 + 3

def test_021_SiSeTieneUnaColoniaYTresPingüinos_ElPuntajeEsOnce():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 6 + 5