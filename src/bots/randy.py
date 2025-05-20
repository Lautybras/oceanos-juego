from random import choice
from collections import Counter as Multiset
from administrador.enums import Acción
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos

class RandyBot():
	def __init__(self):
		self._juego = None
		self._númeroDeJugador = None
	
	def configurarParaJuego(self, juego, númeroDeJugador):
		self._juego = juego
		self._númeroDeJugador = númeroDeJugador
	
	def decidirAcciónDeRobo(self):
		accionesPosibles = [Acción.Robo.DEL_MAZO]
		if self._juego.cantidadDeCartasEnDescarte[0] > 0:
			accionesPosibles.append(Acción.Robo.DEL_DESCARTE_0)
		if self._juego.cantidadDeCartasEnDescarte[1] > 0:
			accionesPosibles.append(Acción.Robo.DEL_DESCARTE_1)
		return choice(accionesPosibles)
			
	def decidirCómoRobarDelMazo(self, opcionesDeRobo):
		if len(opcionesDeRobo) == 1:
			return (0, None)
		else:
			indiceDeCartaARobar = choice([0,1])
			indiceDePilaDondeDescartar = None
			
			if self._juego.cantidadDeCartasEnDescarte[0] > 0 and self._juego.cantidadDeCartasEnDescarte[1] == 0:
				indiceDePilaDondeDescartar = 1
			elif self._juego.cantidadDeCartasEnDescarte[1] > 0 and self._juego.cantidadDeCartasEnDescarte[0] == 0:
				indiceDePilaDondeDescartar = 0
			else:
				indiceDePilaDondeDescartar = choice([0,1])
			return (indiceDeCartaARobar, indiceDePilaDondeDescartar)
	
	def decidirAcciónDeDúos(self):
		
		accionesPosibles = [Acción.Dúos.NO_JUGAR]
		
		
		posibleDúoDePeces = self._buscarDúoParaJugar(Carta.Tipo.PEZ)
		if posibleDúoDePeces != None:
			accionesPosibles.append(Acción.Dúos.JUGAR_PECES)
		
		posibleDúoDeBarcos = self._buscarDúoParaJugar(Carta.Tipo.BARCO)
		if posibleDúoDeBarcos != None:
			accionesPosibles.append(Acción.Dúos.JUGAR_BARCOS)
			
		posibleDúoDeCangrejos = self._buscarDúoParaJugar(Carta.Tipo.CANGREJO)
		if posibleDúoDeCangrejos != None and (self._juego.cantidadDeCartasEnDescarte[0] > 0 or self._juego.cantidadDeCartasEnDescarte[1] > 0):
			accionesPosibles.append(Acción.Dúos.JUGAR_CANGREJOS)
		
		posibleDúoDeNadadorYTiburón = self._buscarDúoParaJugar(Carta.Tipo.NADADOR)
		if posibleDúoDeNadadorYTiburón != None:
			accionesPosibles.append(Acción.Dúos.JUGAR_NADADOR_Y_TIBURÓN)
		
		acciónElegida = choice(accionesPosibles)
		if acciónElegida == Acción.Dúos.JUGAR_PECES:
			return (acciónElegida, posibleDúoDePeces, None)
		
		elif acciónElegida == Acción.Dúos.JUGAR_BARCOS:
			return (acciónElegida, posibleDúoDeBarcos, None)
		
		elif acciónElegida == Acción.Dúos.JUGAR_CANGREJOS:
			pilasPosibles = []
			if (self._juego.cantidadDeCartasEnDescarte[0] > 0):
				pilasPosibles.append(0)
			if (self._juego.cantidadDeCartasEnDescarte[1] > 0):
				pilasPosibles.append(1)
			pilaElegida = choice(pilasPosibles)
			indiceElegido = choice(list(range(self._juego.cantidadDeCartasEnDescarte[pilaElegida])))
			return (acciónElegida, posibleDúoDeCangrejos, (pilaElegida, indiceElegido))
		
		elif acciónElegida == Acción.Dúos.JUGAR_NADADOR_Y_TIBURÓN:
			jugadorARobar = list(range(self._juego.cantidadDeJugadores))
			del jugadorARobar[self._númeroDeJugador]
			return (acciónElegida, posibleDúoDeNadadorYTiburón, (jugadorARobar))
		
		elif acciónElegida == Acción.Dúos.NO_JUGAR:
			return (Acción.Dúos.NO_JUGAR, None, None)
			
	
	def decidirAcciónDeFinDeRonda(self):
		accionesDeFinDeRondaPosibles = [Acción.FinDeRonda.PASAR_TURNO]
		
		if self._juego.puntajeDeRonda >= 7 and (not self._juego.útlimaChanceEnCurso()):
			accionesDeFinDeRondaPosibles.append(Acción.FinDeRonda.DECIR_BASTA)
			accionesDeFinDeRondaPosibles.append(Acción.FinDeRonda.DECIR_ÚLTIMA_CHANCE)
		
		return choice(accionesDeFinDeRondaPosibles)
		
	
	def _buscarDúoParaJugar(self, tipo):
		cartasDelDúoEnMano = Multiset([])
		nadadorEncontrado = False
		tiburónEncontrado = False
		for cartaEnMano in self._juego.mano.elements():
			if tipo in [Carta.Tipo.NADADOR, Carta.Tipo.TIBURÓN]:
				if (cartaEnMano.tipo == Carta.Tipo.NADADOR and not nadadorEncontrado) or (cartaEnMano.tipo == Carta.Tipo.TIBURÓN and not tiburónEncontrado):
					cartasDelDúoEnMano[cartaEnMano] += 1
					if cartaEnMano.tipo == Carta.Tipo.NADADOR:
						nadadorEncontrado = True
					else:
						tiburónEncontrado = True
			else: 
				if cartaEnMano.tipo == tipo:
					cartasDelDúoEnMano[cartaEnMano] += 1
			if cartasDelDúoEnMano.total() == 2:
				return cartasDelDúoEnMano
		return None