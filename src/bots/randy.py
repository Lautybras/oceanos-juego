from random import choice
from administrador.enums import Acción
from juego.carta import Carta
from juego.juego import EstadoDelJuego, EstadoDeJugador

class RandyBot():
	def __init__(self, juego, númeroDeJugador):
		self._juego = juego
		self._númeroDeJugador = númeroDeJugador
	
	def decidirAcciónDeRobo(self):
		accionesPosibles = [Acción.Robo.DEL_MAZO]
		if len(self._juego.descarte[0]) > 0:
			accionesPosibles.append(Acción.Robo.DEL_DESCARTE_0)
		if len(self._juego.descarte[1]) > 0:
			accionesPosibles.append(Acción.Robo.DEL_DESCARTE_1)
		return choice(accionesPosibles)
			
	def decidirCómoRobarDelMazo(self, opcionesDeRobo):
		if len(opcionesDeRobo) == 1:
			return (0, None)
		else:
			indiceDeCartaARobar = choice([0,1])
			indiceDePilaDondeDescartar = None
			if len(self._juego.descarte[0]) > 0 and len(self._juego.descarte[1]) == 0:
				indiceDePilaDondeDescartar = 1
			elif len(self._juego.descarte[1]) > 0 and len(self._juego.descarte[0]) == 0:
				indiceDePilaDondeDescartar = 0
			else:
				indiceDePilaDondeDescartar = choice([0,1])			
			return (indiceDeCartaARobar, indiceDePilaDondeDescartar)
	
	def decidirAcciónDeDúos(self):
		return Acción.Dúos.NO_JUGAR
	
	def decidirAcciónDeFinDeRonda(self):
		if self._juego.estadoDelJugador[self._númeroDeJugador].puntajeDeRonda() >= 7:
			return Acción.FinDeRonda.DECIR_BASTA
		else:
			return Acción.FinDeRonda.PASAR_TURNO
