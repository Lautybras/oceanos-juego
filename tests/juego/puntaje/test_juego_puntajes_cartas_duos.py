import pytest
from juego.carta import Carta
from juego.partida import PartidaDeOcéanos

def test_SiSeTieneUnPezEnLaMano_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTienenDosPecesEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTienenTresPecesEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 3
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTienenCuatroPecesEnLaMano_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 4
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2
	

def test_SiSeTieneUnDúoDePeces_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1
	
def test_SiSeTienenDosDúosDePeces_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))))
	] += 2
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2

def test_SiSeTienenDosPecesEnLaManoYUnDúoDePeces_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO), Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2




def test_SiSeTieneUnBarcoEnLaMano_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTienenDosBarcosEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTienenTresBarcosEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTienenCuatroBarcosEnLaMano_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2
	

def test_SiSeTieneUnDúoDeBarcos_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1
	
def test_SiSeTienenDosDúosDeBarcos_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 1
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2



def test_SiSeTienenDosPecesEnLaManoYUnDúoDePeces_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO), Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2



def test_SiSeTieneUnCangrejoEnLaMano_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTienenDosCangrejosEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTienenTresCangrejosEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTienenCuatroCangrejosEnLaMano_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2
	

def test_SiSeTieneUnDúoDeCangrejos_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1
	
def test_SiSeTienenDosDúosDeCangrejos_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))))
	] += 1
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2

def test_SiSeTienenDosPecesEnLaManoYUnDúoDePeces_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO), Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2




def test_SiSeTieneUnNadadorEnLaMano_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTieneUnTiburónEnLaMano_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0

def test_SiSeTieneUnNadadorYUnTiburónEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTienenDosNadadoresYUnTiburónEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTieneUnNadadorYDosTiburónesEnLaMano_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTienenDosNadadoresYDosTiburónesEnLaMano_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2

def test_SiSeTieneUnDúoDeNadadorYTiburón_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 1

def test_SiSeTienenDosDúosDeNadadorYTiburón_ElPuntajeEsUno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO))))
	] += 1
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2

def test_SiSeTieneUnNadadorYUnTiburónEnLaManoYUnDúoDeNadadorYTiburón_ElPuntajeEsDos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].zonaDeDúos[
		tuple(sorted((Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO), Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO))))
	] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 2




def test_SiSeTieneUnBarcoYUnCangrejoEnMano_ElPuntajeEsCero():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO)] += 1
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO)] += 1
	
	assert juego._estadosDeJugadores[0].puntajeDeRonda() == 0