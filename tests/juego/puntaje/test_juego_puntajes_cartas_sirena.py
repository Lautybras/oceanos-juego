import pytest
from juego.carta import Carta
from juego.partida import PartidaDeOcéanos

def test_SiSeTieneUnaSirena_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTieneUnaSirenaYUnaCartaDeUnColor_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTieneUnaSirenaYDosCartasDeUnColor_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2

def test_SiSeTieneUnaSirenaYDosCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2

def test_SiSeTieneUnaSirenaYTresCartasDeUnColor_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3

def test_SiSeTieneUnaSirenaYTresCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3

def test_SiSeTieneUnaSirenaYTresCartasDeUnColorYDosCartasDeOtroColor_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3





def test_SiSeTienenDosSirenas_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2 + 0

def test_SiSeTienenDosSirenasYUnaCartaDeUnColor_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2 + 1

def test_SiSeTienenDosSirenasYDosCartasDeUnColor_ElPuntajeEsCuatro():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2 + 2

def test_SiSeTienenDosSirenasYDosCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsCuatro():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2 + 2

def test_SiSeTienenDosSirenasYTresCartasDeUnColor_ElPuntajeEsCinco():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 2

def test_SiSeTienenDosSirenasYTresCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsCinco():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 2

def test_SiSeTienenDosSirenasYTresCartasDeUnColorYDosCartasDeOtroColor_ElPuntajeEsCinco():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 2




def test_SiSeTienenTresSirenas_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 0 + 0

def test_SiSeTienenTresSirenasYUnaCartaDeUnColor_ElPuntajeEsCuatro():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 1 + 0

def test_SiSeTienenTresSirenasYDosCartasDeUnColor_ElPuntajeEsCinco():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 2 + 0

def test_SiSeTienenTresSirenasYDosCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsSeis():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 2 + 1

def test_SiSeTienenTresSirenasYTresCartasDeUnColor_ElPuntajeEsSeis():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 3 + 0

def test_SiSeTienenTresSirenasYTresCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsSiete():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 3 + 1

def test_SiSeTienenTresSirenasYTresCartasDeUnColorYDosCartasDeOtroColor_ElPuntajeEsOcho():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL)] += 3
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3 + 3 + 2
