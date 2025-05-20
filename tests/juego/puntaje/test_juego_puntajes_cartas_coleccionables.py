import pytest
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos

def test_SiSeTieneUnPinguino_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1 

def test_SiSeTieneUnPinguinoYOtraCarta_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1 

def test_SiSeTienenDosPinguinos_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3

def test_SiSeTienenTresPinguinos_ElPuntajeEsCinco():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 5

def test_SiSeTieneUnAncla_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTienenDosAnclas_ElPuntajeEsCinco():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 5

def test_SiSeTienenDosAnclasYUnPinguino_ElPuntajeEsSeis():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO)] += 2
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 5 + 1

def test_SiSeTieneUnaConcha_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTienenDosConchas_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2

def test_SiSeTienenTresConchas_ElPuntajeEsCuatro():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 4

def test_SiSeTienenCuatroConchas_ElPuntajeEsSeis():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO)] += 4
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 6

def test_SiSeTienenCincoConchas_ElPuntajeEsOcho():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO)] += 5
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 8

def test_SiSeTienenSeisConchas_ElPuntajeEsDiez():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO)] += 6
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 10

def test_SiSeTieneUnPuplo_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTienenDosPulpos_ElPuntajeEsTres():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 3

def test_SiSeTienenTresPulpos_ElPuntajeEsSeis():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 6

def test_SiSeTienenCuatroPulpos_ElPuntajeEsNueve():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO)] += 4
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 9

def test_SiSeTienenCincoPulpos_ElPuntajeEsDoce():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO)] += 5
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 12

