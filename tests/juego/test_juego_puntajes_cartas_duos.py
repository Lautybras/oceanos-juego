import pytest
from juego.carta import Carta
from juego.juego import EstadoDelJuego

def test_SiSeTieneUnPezEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_SiSeTienenDosPecesEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 2
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTienenTresPecesEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 3
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTienenCuatroPecesEnLaMano_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 4
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2
	

def test_SiSeTieneUnDuoDePeces_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1
	
def test_SiSeTienenDosDuosDePeces_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))))
	] += 2
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_SiSeTienenDosPecesEnLaManoYUnDuoDePeces_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2




def test_SiSeTieneUnBarcoEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_SiSeTienenDosBarcosEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTienenTresBarcosEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTienenCuatroBarcosEnLaMano_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2
	

def test_SiSeTieneUnDuoDeBarcos_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1
	
def test_SiSeTienenDosDuosDeBarcos_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 1
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2



def test_SiSeTienenDosPecesEnLaManoYUnDuoDePeces_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2



def test_SiSeTieneUnCangrejoEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_SiSeTienenDosCangrejosEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTienenTresCangrejosEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTienenCuatroCangrejosEnLaMano_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2
	

def test_SiSeTieneUnDuoDeCangrejos_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1
	
def test_SiSeTienenDosDuosDeCangrejos_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))))
	] += 1
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_SiSeTienenDosPecesEnLaManoYUnDuoDePeces_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2




def test_SiSeTieneUnNadadorEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_SiSeTieneUnTiburónEnLaMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0

def test_SiSeTieneUnNadadorYUnTiburónEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTienenDosNadadoresYUnTiburónEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTieneUnNadadorYDosTiburonesEnLaMano_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTienenDosNadadoresYDosTiburonesEnLaMano_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_SiSeTieneUnDuoDeNadadorYTiburón_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 1

def test_SiSeTienenDosDuosDeNadadorYTiburón_ElPuntajeEsUno():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))))
	] += 1
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2

def test_SiSeTieneUnNadadorYUnTiburónEnLaManoYUnDuoDeNadadorYTiburón_ElPuntajeEsDos():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].zonaDeDuos[
		tuple(sorted((Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO))))
	] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 2




def test_SiSeTieneUnBarcoYUnCangrejoEnMano_ElPuntajeEsCero():
	juego = EstadoDelJuego(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego.estadoDelJugador[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego.estadoDelJugador[0].puntajeDeRonda() == 0