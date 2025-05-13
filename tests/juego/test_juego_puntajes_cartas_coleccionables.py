import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego

def test_001_SiSeTieneUnPinguino_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1 

def test_002_SiSeTieneUnPinguinoYOtraCarta_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1 

def test_003_SiSeTienenDosPinguinos_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3

def test_004_SiSeTienenTresPinguinos_ElPuntajeEsCinco():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 5

def test_005_SiSeTieneUnAncla_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_006_SiSeTienenDosAnclas_ElPuntajeEsCinco():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 5

def test_007_SiSeTienenDosAnclasYUnPinguino_ElPuntajeEsSeis():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 5 + 1

def test_008_SiSeTieneUnaConcha_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_009_SiSeTienenDosConchas_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_010_SiSeTienenTresConchas_ElPuntajeEsCuatro():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 4

def test_011_SiSeTienenCuatroConchas_ElPuntajeEsSeis():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 6

def test_012_SiSeTienenCincoConchas_ElPuntajeEsOcho():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 8

def test_013_SiSeTienenSeisConchas_ElPuntajeEsDiez():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 10

def test_014_SiSeTieneUnPuplo_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_015_SiSeTienenDosPulpos_ElPuntajeEsTres():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 3

def test_016_SiSeTienenTresPulpos_ElPuntajeEsSeis():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 6

def test_017_SiSeTienenCuatroPulpos_ElPuntajeEsNueve():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 9

def test_018_SiSeTienenCincoPulpos_ElPuntajeEsDoce():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	juego.estadoDelJugador[0].mano.append(Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO))
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 12

