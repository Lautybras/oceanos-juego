import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego

def test_001_SiSeTieneUnaSirena_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_002_SiSeTieneUnaSirenaYUnaCartaDeUnColor_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_003_SiSeTieneUnaSirenaYDosCartasDeUnColor_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_004_SiSeTieneUnaSirenaYDosCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_005_SiSeTieneUnaSirenaYTresCartasDeUnColor_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3

def test_006_SiSeTieneUnaSirenaYTresCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3

def test_007_SiSeTieneUnaSirenaYTresCartasDeUnColorYDosCartasDeOtroColor_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3





def test_008_SiSeTienenDosSirenas_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2 + 0

def test_009_SiSeTienenDosSirenasYUnaCartaDeUnColor_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2 + 1

def test_010_SiSeTienenDosSirenasYDosCartasDeUnColor_ElPuntajeEsCuatro():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2 + 2

def test_011_SiSeTienenDosSirenasYDosCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsCuatro():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2 + 2

def test_012_SiSeTienenDosSirenasYTresCartasDeUnColor_ElPuntajeEsCinco():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 2

def test_013_SiSeTienenDosSirenasYTresCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsCinco():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 2

def test_014_SiSeTienenDosSirenasYTresCartasDeUnColorYDosCartasDeOtroColor_ElPuntajeEsCinco():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 2




def test_015_SiSeTienenTresSirenas_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 0 + 0

def test_016_SiSeTienenTresSirenasYUnaCartaDeUnColor_ElPuntajeEsCuatro():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 1 + 0

def test_017_SiSeTienenTresSirenasYDosCartasDeUnColor_ElPuntajeEsCinco():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 2 + 0

def test_018_SiSeTienenTresSirenasYDosCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsSeis():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 2 + 1

def test_019_SiSeTienenTresSirenasYTresCartasDeUnColor_ElPuntajeEsSeis():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 3 + 0

def test_020_SiSeTienenTresSirenasYTresCartasDeUnColorYUnaCartaDeOtroColor_ElPuntajeEsSiete():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 3 + 1

def test_021_SiSeTienenTresSirenasYTresCartasDeUnColorYDosCartasDeOtroColor_ElPuntajeEsOcho():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3 + 3 + 2
