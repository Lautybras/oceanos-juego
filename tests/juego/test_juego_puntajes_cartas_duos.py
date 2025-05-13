import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego

def test_001_SiSeTieneUnPezEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_002_SiSeTienenDosPecesEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_003_SiSeTienenTresPecesEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_004_SiSeTienenCuatroPecesEnLaMano_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2
	

def test_005_SiSeTieneUnDuoDePeces_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1
	
def test_006_SiSeTienenDosDuosDePeces_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	)
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_007_SiSeTienenDosPecesEnLaManoYUnDuoDePeces_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2




def test_008_SiSeTieneUnBarcoEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_009_SiSeTienenDosBarcosEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_010_SiSeTienenTresBarcosEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_011_SiSeTienenCuatroBarcosEnLaMano_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2
	

def test_012_SiSeTieneUnDuoDeBarcos_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1
	
def test_013_SiSeTienenDosDuosDeBarcos_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	)
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2



def test_014_SiSeTienenDosPecesEnLaManoYUnDuoDePeces_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2



def test_015_SiSeTieneUnCangrejoEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_016_SiSeTienenDosCangrejosEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_017_SiSeTienenTresCangrejosEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_018_SiSeTienenCuatroCangrejosEnLaMano_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2
	

def test_019_SiSeTieneUnDuoDeCangrejos_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1
	
def test_020_SiSeTienenDosDuosDeCangrejos_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	)
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_021_SiSeTienenDosPecesEnLaManoYUnDuoDePeces_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2




def test_022_SiSeTieneUnNadadorEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_023_SiSeTieneUnTiburónEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_024_SiSeTieneUnNadadorYUnTiburónEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_024_SiSeTienenDosNadadoresYUnTiburónEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_024_SiSeTieneUnNadadorYDosTiburonesEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_024_SiSeTienenDosNadadoresYDosTiburonesEnLaMano_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_025_SiSeTieneUnDuoDeNadadorYTiburón_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_026_SiSeTienenDosDuosDeNadadorYTiburón_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	)
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_027_SiSeTieneUnNadadorYUnTiburónEnLaManoYUnDuoDeNadadorYTiburón_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].zonaDeDuos.append(
		(Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))
	)
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2




def test_028_SiSeTieneUnBarcoYUnCangrejoEnMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0