from random import choice
from collections import Counter as Multiset
from administrador.acción import Acción
from juego.carta import Carta
from juego.partida import PartidaDeOcéanos
from ..base import JugadorBase

class SirenaEnjoyer(JugadorBase):
	def __init__(self):
		self._juego = None
		self._númeroDeJugador = None
	
	def configurarParaJuego(self, juego, númeroDeJugador, listaDeEventos):
		self._juego = juego
		self._númeroDeJugador = númeroDeJugador
		self._listaDeEventos = listaDeEventos
	
	def decidirAcciónDeRobo(self):
		if self._juego.cantidadDeCartasEnDescarte[0] > 0 and self._juego.topeDelDescarte[0].tipo == Carta.Tipo.SIRENA:
			return Acción.Robo.DEL_DESCARTE_0
		if self._juego.cantidadDeCartasEnDescarte[1] > 0 and self._juego.topeDelDescarte[1].tipo == Carta.Tipo.SIRENA:
			return Acción.Robo.DEL_DESCARTE_1
		return Acción.Robo.DEL_MAZO
	
	def decidirCómoRobarDelMazo(self, opcionesDeRobo):
		if len(opcionesDeRobo) == 1:
			return (0, None)
		else:
			pilaVálida = 0 if self._juego.cantidadDeCartasEnDescarte[0] == 0 else 1
			if opcionesDeRobo[0].tipo == Carta.Tipo.SIRENA:
				return (0, pilaVálida)
			else:
				return (1, pilaVálida)
	
	def decidirAcciónDeDúos(self):
		return (Acción.Dúos.NO_JUGAR, None, None)
	
	def decidirAcciónDeFinDeTurno(self):
		#if self._juego.cantidadDeCartasEnMazo < 2 and self._juego.puntajeDeRonda >= 7:
		#	return Acción.FinDeTurno.DECIR_BASTA
		return Acción.FinDeTurno.PASAR_TURNO
	
	def configurarFinDeRonda(self, manos, puntajesDeRonda):
		pass
	