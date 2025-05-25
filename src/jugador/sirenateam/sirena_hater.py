from random import choice
from collections import Counter as Multiset
from administrador.acción import Acción
from juego.carta import Carta
from juego.partida import PartidaDeOcéanos
from ..base import JugadorBase

class SirenaHater(JugadorBase):
	def __init__(self):
		self._juego = None
		self._númeroDeJugador = None
	
	def configurarParaJuego(self, juego, númeroDeJugador, listaDeEventos):
		self._juego = juego
		self._númeroDeJugador = númeroDeJugador
		self._listaDeEventos = listaDeEventos
	
	def decidirAcciónDeRobo(self):
		return Acción.Robo.DEL_MAZO
	
	def decidirCómoRobarDelMazo(self, opcionesDeRobo):
		if len(opcionesDeRobo) == 1:
			return (0, None)
		else:
			cartaARobar = 0 if opcionesDeRobo[0].tipo != Carta.Tipo.SIRENA else 1
			pilaDondeDescartar = None
			if self._juego.cantidadDeCartasEnDescarte[0] == 0 and self._juego.cantidadDeCartasEnDescarte[1] > 0:
				pilaDondeDescartar = 0
			elif self._juego.cantidadDeCartasEnDescarte[1] == 0 and self._juego.cantidadDeCartasEnDescarte[0] > 0:
				pilaDondeDescartar = 1
			else:
				pilaDondeDescartar = 0 if self._juego.cantidadDeCartasEnDescarte[0] == 0 or self._juego.topeDelDescarte[0].tipo != Carta.Tipo.SIRENA else 1
			return (cartaARobar, pilaDondeDescartar)
	
	def decidirAcciónDeDúos(self):
		return (Acción.Dúos.NO_JUGAR, None, None)
	
	def decidirAcciónDeFinDeTurno(self):
		if self._juego.cantidadDeCartasEnMazo < 2 and self._juego.puntajeDeRonda >= 7 and (not self._juego.últimaChanceEnCurso()):
			return Acción.FinDeTurno.DECIR_BASTA
		return Acción.FinDeTurno.PASAR_TURNO
	
	def configurarFinDeRonda(self, manos, puntajesDeRonda):
		pass
	