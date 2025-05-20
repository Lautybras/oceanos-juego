from random import shuffle, choice
from enum import Enum, auto
from copy import deepcopy
from .carta import Carta
from collections import Counter as Multiset

SIRENAS_INF = 999

def cartasDelJuego():
	return list([
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AZUL),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.CELESTE),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.CELESTE),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.NEGRO),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.VERDE),
		Carta(Carta.Tipo.CANGREJO, Carta.Color.GRIS),
		
		Carta(Carta.Tipo.BARCO, Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO, Carta.Color.AZUL),
		Carta(Carta.Tipo.BARCO, Carta.Color.CELESTE),
		Carta(Carta.Tipo.BARCO, Carta.Color.CELESTE),
		Carta(Carta.Tipo.BARCO, Carta.Color.NEGRO),
		Carta(Carta.Tipo.BARCO, Carta.Color.NEGRO),
		Carta(Carta.Tipo.BARCO, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.BARCO, Carta.Color.AMARILLO),
		
		Carta(Carta.Tipo.PEZ, Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ, Carta.Color.AZUL),
		Carta(Carta.Tipo.PEZ, Carta.Color.CELESTE),
		Carta(Carta.Tipo.PEZ, Carta.Color.NEGRO),
		Carta(Carta.Tipo.PEZ, Carta.Color.NEGRO),
		Carta(Carta.Tipo.PEZ, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.PEZ, Carta.Color.VERDE),
		
		Carta(Carta.Tipo.NADADOR, Carta.Color.AZUL),
		Carta(Carta.Tipo.NADADOR, Carta.Color.CELESTE),
		Carta(Carta.Tipo.NADADOR, Carta.Color.NEGRO),
		Carta(Carta.Tipo.NADADOR, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.NADADOR, Carta.Color.NARANJA_CLARO),
		
		Carta(Carta.Tipo.TIBURON, Carta.Color.AZUL),
		Carta(Carta.Tipo.TIBURON, Carta.Color.CELESTE),
		Carta(Carta.Tipo.TIBURON, Carta.Color.NEGRO),
		Carta(Carta.Tipo.TIBURON, Carta.Color.VERDE),
		Carta(Carta.Tipo.TIBURON, Carta.Color.VIOLETA),
		
		Carta(Carta.Tipo.CONCHA, Carta.Color.AZUL),
		Carta(Carta.Tipo.CONCHA, Carta.Color.CELESTE),
		Carta(Carta.Tipo.CONCHA, Carta.Color.NEGRO),
		Carta(Carta.Tipo.CONCHA, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.CONCHA, Carta.Color.VERDE),
		Carta(Carta.Tipo.CONCHA, Carta.Color.GRIS),
		
		Carta(Carta.Tipo.PULPO, Carta.Color.CELESTE),
		Carta(Carta.Tipo.PULPO, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.PULPO, Carta.Color.VERDE),
		Carta(Carta.Tipo.PULPO, Carta.Color.VIOLETA),
		Carta(Carta.Tipo.PULPO, Carta.Color.GRIS),
		
		Carta(Carta.Tipo.PINGUINO, Carta.Color.VIOLETA),
		Carta(Carta.Tipo.PINGUINO, Carta.Color.NARANJA_CLARO),
		Carta(Carta.Tipo.PINGUINO, Carta.Color.ROSA),
		
		Carta(Carta.Tipo.ANCLA, Carta.Color.ROSA),
		Carta(Carta.Tipo.ANCLA, Carta.Color.NARANJA),
		
		Carta(Carta.Tipo.COLONIA, Carta.Color.VERDE),
		Carta(Carta.Tipo.FARO, Carta.Color.VIOLETA),
		Carta(Carta.Tipo.CARDUMEN, Carta.Color.GRIS),
		Carta(Carta.Tipo.CAPITAN, Carta.Color.NARANJA_CLARO),
		
		Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO),
		Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO),
		Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO),
		Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)
	])

class JuegoInvalidoException(Exception):
	def __init__(self, message="Se intentó crear un juego con atributos inválidos"):
		super().__init__(message)

class JuegoException(Exception):
	def __init__(self, message="Ha ocurrido alguna violacion a las reglas del juego"):
		super().__init__(message)

class EstadoDeJugador():
	def __init__(self):
		self.mano = Multiset()
		self.zonaDeDuos = Multiset()
		
	def puntajeDeRonda(self):
		cantidadDeCartasEnManoDeTipo = {tipo: 0 for tipo in Carta.Tipo}
		cantidadDeDuosEnJuegoDeTipo = {
			Carta.Tipo.PEZ: 0,
			Carta.Tipo.BARCO: 0,
			Carta.Tipo.CANGREJO: 0,
			Carta.Tipo.NADADOR: 0    # noo maldito enum que no me deja poner nombres declarativos!
		}
		cantidadDeCartasDeColor = {color: 0 for color in Carta.Color}
		
		for claveDeCarta in self.mano:
			cantidadDeCartasEnManoDeTipo[claveDeCarta.tipo] += self.mano[claveDeCarta]
			cantidadDeCartasDeColor[claveDeCarta.color] += self.mano[claveDeCarta]
		
		for claveDeDuo in self.zonaDeDuos:
			cantidadDeDuosEnJuegoDeTipo[claveDeDuo[0].tipo] += self.zonaDeDuos[claveDeDuo]
			cantidadDeCartasDeColor[claveDeDuo[0].color] += self.zonaDeDuos[claveDeDuo]
			cantidadDeCartasDeColor[claveDeDuo[1].color] += self.zonaDeDuos[claveDeDuo]
		
		return (
			self._puntajePorDuosEnMano(cantidadDeCartasEnManoDeTipo) +
			self._puntajePorDuosJugados() + 
			self._puntajePorColeccionables(cantidadDeCartasEnManoDeTipo) +
			self._puntajePorMultiplicadores(cantidadDeCartasEnManoDeTipo, cantidadDeDuosEnJuegoDeTipo) +
			self._puntajePorSirenas(cantidadDeCartasEnManoDeTipo[Carta.Tipo.SIRENA], cantidadDeCartasDeColor)
		)
	
	def _puntajePorDuosEnMano(self, cantidadDeCartasDuos):
		return (
			(cantidadDeCartasDuos[Carta.Tipo.PEZ] // 2) +  
			(cantidadDeCartasDuos[Carta.Tipo.BARCO] // 2) +  
			(cantidadDeCartasDuos[Carta.Tipo.CANGREJO] // 2) +  
			min(cantidadDeCartasDuos[Carta.Tipo.NADADOR], cantidadDeCartasDuos[Carta.Tipo.TIBURON])
		)
	
	def _puntajePorDuosJugados(self):
		return self.zonaDeDuos.total()
	
	def _puntajePorColeccionables(self, cantidadDeColeccionables):
		return (
			self._puntajePorAnclas(cantidadDeColeccionables[Carta.Tipo.ANCLA]) +
			self._puntajePorConchas(cantidadDeColeccionables[Carta.Tipo.CONCHA]) +
			self._puntajePorPinguinos(cantidadDeColeccionables[Carta.Tipo.PINGUINO]) +
			self._puntajePorPulpos(cantidadDeColeccionables[Carta.Tipo.PULPO])
		)
	
	def _puntajePorMultiplicadores(self, cantidadDeCartasEnManoDeTipo, cantidadDeDuosEnJuegoDeTipo):
		return (
			(cantidadDeCartasEnManoDeTipo[Carta.Tipo.CAPITAN] * 3 * cantidadDeCartasEnManoDeTipo[Carta.Tipo.ANCLA]) +
			(cantidadDeCartasEnManoDeTipo[Carta.Tipo.COLONIA] * 2 * cantidadDeCartasEnManoDeTipo[Carta.Tipo.PINGUINO]) +
			(
				cantidadDeCartasEnManoDeTipo[Carta.Tipo.CARDUMEN] * 1 *
				(cantidadDeCartasEnManoDeTipo[Carta.Tipo.PEZ] + 2 * cantidadDeDuosEnJuegoDeTipo[Carta.Tipo.PEZ])
			) +
			(
				cantidadDeCartasEnManoDeTipo[Carta.Tipo.FARO] * 1 *
				(cantidadDeCartasEnManoDeTipo[Carta.Tipo.BARCO] + 2 * cantidadDeDuosEnJuegoDeTipo[Carta.Tipo.BARCO])
			)
		)
	
	def _puntajePorSirenas(self, cantidadDeSirenas, cantidadDeCartasDeColor):
		return sum(
			(sorted(list(cantidadDeCartasDeColor.values()), reverse=True))[0:cantidadDeSirenas]
		)
	
	
	def _puntajePorAnclas(self, cantidadDeAnclas):
		if cantidadDeAnclas == 0:
			return 0
		elif 0 < cantidadDeAnclas and cantidadDeAnclas <= 2:
			return (cantidadDeAnclas - 1) * 5
		else:
			raise JuegoException("Cantidad de anclas inválida")
	
	def _puntajePorConchas(self, cantidadDeConchas):
		if cantidadDeConchas == 0:
			return 0
		elif 0 < cantidadDeConchas and cantidadDeConchas <= 6:
			return (cantidadDeConchas - 1) * 2
		else:
			raise JuegoException("Cantidad de conchas inválida")
	
	def _puntajePorPulpos(self, cantidadDePulpos):
		if cantidadDePulpos == 0:
			return 0
		elif 0 < cantidadDePulpos and cantidadDePulpos <= 5:
			return (cantidadDePulpos - 1) * 3
		else:
			raise JuegoException("Cantidad de pulpos inválida")
		
	def _puntajePorPinguinos(self, cantidadDePinguinos):
		if cantidadDePinguinos == 0:
			return 0
		elif 0 < cantidadDePinguinos and cantidadDePinguinos <= 3:
			return 1 + ((cantidadDePinguinos - 1) * 2)
		else:
			raise JuegoException("Cantidad de pingüinos inválida")
	
	def _bonificacionPorColor(self):
		cantidadDeCartasDeColor = {color: 0 for color in Carta.Color}
		
		for claveDeCarta in self.mano:
			cantidadDeCartasDeColor[claveDeCarta.color] += self.mano[claveDeCarta]
		
		for claveDeDuo in self.zonaDeDuos:
			cantidadDeCartasDeColor[claveDeDuo[0].color] += self.zonaDeDuos[claveDeDuo]
			cantidadDeCartasDeColor[claveDeDuo[1].color] += self.zonaDeDuos[claveDeDuo]
		
		return sum(
			(sorted(list(cantidadDeCartasDeColor.values()), reverse=True))[0:1]
		)

class PartidaDeOcéanos():
	class Estado():
		PARTIDA_NO_INICIADA = auto()
		FASE_ROBO = auto()
		FASE_ROBO_DEL_MAZO = auto()
		FASE_DÚOS = auto()
		RONDA_TERMINADA = auto()
		PARTIDA_TERMINADA = auto()
	
	def rondaEnCurso(self):
		return self._estadoActual in [
			self.Estado.FASE_ROBO,
			self.Estado.FASE_ROBO_DEL_MAZO,
			self.Estado.FASE_DÚOS
		]
	
	def haTerminado(self):
		return self._estadoActual == self.Estado.PARTIDA_TERMINADA
	
	def seHaRobadoEsteTurno(self):
		return self._estadoActual == self.Estado.FASE_DÚOS
	
	def hayQueTomarDecisionesDeRoboDelMazo(self):
		return self._estadoActual == self.Estado.FASE_ROBO_DEL_MAZO
	
	def útlimaChanceEnCurso(self):
		return self._últimaChancePorJugador != None
	
	
	
	@property
	def cantidadDeJugadores(self):
		return int(self._cantidadDeJugadores)
	@property
	def deQuiénEsTurno(self):
		return int(self._deQuiénEsTurno)
	@property
	def puntajes(self):
		return list(self._puntajes.copy())
	@property
	def jugadorGanador(self):
		return int(self._jugadorGanador) if self._jugadorGanador != None else None
	@property
	def últimaChanceEnCurso(self):
		return (self._últimaChancePorJugador != None)
	@property
	def jugadorQueDijoÚltimaChance(self):
		return int(self._últimaChancePorJugador) if self._últimaChancePorJugador != None else None
	@property
	def descarte(self):
		return deepcopy(self._descarte)
	
	
	def __init__(self, cantidadDeJugadores=2):
		if(not (2 <= cantidadDeJugadores and cantidadDeJugadores <= 4)):
			raise JuegoInvalidoException("La cantidad de jugadores es inválida")
		
		self._cantidadDeJugadores = cantidadDeJugadores 
		self._deQuiénEsTurno = 0
		self._puntajes = [0] * cantidadDeJugadores
		self._jugadorGanador = None
		self._últimaChancePorJugador = None
		self._descarte = None
		self._estadosDeJugadores = None
		self._mazo = None
		self._estadoActual = self.Estado.PARTIDA_NO_INICIADA
	
	def iniciarRonda(self):
		if self.rondaEnCurso():
			raise JuegoException("Ya hay una ronda en curso!")
		
		self._estadosDeJugadores = [EstadoDeJugador() for _ in range(self._cantidadDeJugadores)]
		self._mazo = list(cartasDelJuego())
		shuffle(self._mazo)
		self._descarte = ([self._mazo.pop(0)], [self._mazo.pop(0)])
		self._estadoActual = self.Estado.FASE_ROBO
		self._últimaChancePorJugador = None
	
	def robarDelDescarte(self, indicePilaDeDescarte):
		self._assertSePuedeElegirAcciónDeRobo()
		self._assertÍndicePilaDeDescarteVálidoParaRobar(indicePilaDeDescarte)
		
		cartaRobada = self._descarte[indicePilaDeDescarte].pop()
		self._estadosDeJugadores[self._deQuiénEsTurno].mano[cartaRobada] += 1
		self._estadoActual = self.Estado.FASE_DÚOS
		
		self._calcularSiHayGanadorPorSirenas()
		
		return cartaRobada
	
	def robarDelMazo(self):
		self._assertSePuedeElegirAcciónDeRobo()
		if len(self._mazo) == 0:
			raise JuegoException("No se puede robar de un mazo vacío")
		
		self._estadoActual = self.Estado.FASE_ROBO_DEL_MAZO
		
		if len(self._mazo) == 1:
			return [self._mazo[-1]]
		return [self._mazo[-1], self._mazo[-2]]
	
	def elegirRoboDelMazo(self, indiceDeCartaARobar, indiceDePilaDondeDescartar):
		self._assertSePuedeRobarDelMazo()
		
		self._assertObjetivoDeDescarteVálido(indiceDePilaDondeDescartar, indiceDeCartaARobar)
		
		cartasRobadasDelMazo = [self._mazo.pop()]
		if len(self._mazo) > 1:
			cartasRobadasDelMazo.append(self._mazo.pop())
			self._descarte[indiceDePilaDondeDescartar].append(cartasRobadasDelMazo[1 - indiceDeCartaARobar])
		cartaRobada = cartasRobadasDelMazo[indiceDeCartaARobar]
		self._estadosDeJugadores[self._deQuiénEsTurno].mano[cartaRobada] += 1
		
		self._estadoActual = self.Estado.FASE_DÚOS
		
		self._calcularSiHayGanadorPorSirenas()
		
		return cartaRobada
	
	def jugarDuoDePeces(self, cartasAJugar):
		self._assertSePuedeJugarDuo(cartasAJugar)
		self._assertDúoEsDeTipo(cartasAJugar, Carta.Tipo.PEZ)
		
		self._moverDúoAZonaDeDúo(cartasAJugar)
		
		cartaRobada = None
		if len(self._mazo) > 0:
			cartaRobada = self._mazo.pop()
			self._estadosDeJugadores[self._deQuiénEsTurno].mano[cartaRobada] += 1
			self._calcularSiHayGanadorPorSirenas()
		
		return cartaRobada
	
	def jugarDuoDeBarcos(self, cartasAJugar):
		self._assertSePuedeJugarDuo(cartasAJugar)
		self._assertDúoEsDeTipo(cartasAJugar, Carta.Tipo.BARCO)
		
		self._moverDúoAZonaDeDúo(cartasAJugar)
		
		if len(self._mazo) == 0:
			# ronda anulada por mazo vacío
			
			self._estadoActual = self.Estado.RONDA_TERMINADA
			
			self._deQuiénEsTurno = (self._deQuiénEsTurno + 1) % self._cantidadDeJugadores
			return
		
		self._estadoActual = self.Estado.FASE_ROBO
	
	def jugarDuoDeCangrejos(self, cartasAJugar, pilaDeDescarteARobar, indiceDeCartaARobar):
		self._assertSePuedeJugarDuo(cartasAJugar)
		self._assertDúoEsDeTipo(cartasAJugar, Carta.Tipo.CANGREJO)
		
		self._assertObjetivoDeDúoDeCangrejosVálido(pilaDeDescarteARobar, indiceDeCartaARobar)
		
		self._moverDúoAZonaDeDúo(cartasAJugar)
		if len(self._descarte[0]) == 0 and len(self._descarte[1]) == 0:
			return None
		
		cartaRobada = self._descarte[pilaDeDescarteARobar][indiceDeCartaARobar]
		self._estadosDeJugadores[self._deQuiénEsTurno].mano[cartaRobada] += 1
		del self._descarte[pilaDeDescarteARobar][indiceDeCartaARobar]
		
		self._calcularSiHayGanadorPorSirenas()
		
		return cartaRobada
	
	def jugarDuoDeNadadorYTiburón(self, cartasAJugar, jugadorARobar):
		self._assertSePuedeJugarDuo(cartasAJugar)
		self._assertDúoEsDeTipo(cartasAJugar, Carta.Tipo.TIBURON)
		self._assertSelecciónDeJugadorVálida(jugadorARobar)
		
		self._moverDúoAZonaDeDúo(cartasAJugar)
		
		cartaRobada = None
		if self._estadosDeJugadores[jugadorARobar].mano.total() > 0:
			cartaRobada = choice(list(self._estadosDeJugadores[jugadorARobar].mano.elements()))
			
			self._estadosDeJugadores[self._deQuiénEsTurno].mano[cartaRobada] += 1
			
			self._estadosDeJugadores[jugadorARobar].mano[cartaRobada] -= 1
			if self._estadosDeJugadores[jugadorARobar].mano[cartaRobada] == 0:
				del self._estadosDeJugadores[jugadorARobar].mano[cartaRobada]
			
			self._calcularSiHayGanadorPorSirenas()
		
		return cartaRobada
	
	def pasarTurno(self):
		self._assertSePuedeTerminarElTurno()
		
		if len(self._mazo) == 0:
			# ronda anulada por mazo vacío
			
			self._estadoActual = self.Estado.RONDA_TERMINADA
			
			self._deQuiénEsTurno = (self._deQuiénEsTurno + 1) % self._cantidadDeJugadores
			return
		
		self._deQuiénEsTurno = (self._deQuiénEsTurno + 1) % self._cantidadDeJugadores
		
		if self._últimaChancePorJugador == self._deQuiénEsTurno:
			#calcular fin de ronda por apuesta de última chance
			if self._estadosDeJugadores[self._últimaChancePorJugador].puntajeDeRonda() == max([self._estadosDeJugadores[j].puntajeDeRonda() for j in range(self._cantidadDeJugadores)]):
				# apuesta ganada
				for jugador in range(self._cantidadDeJugadores):
					self._puntajes[jugador] += self._estadosDeJugadores[jugador]._bonificacionPorColor()
				self._puntajes[self._últimaChancePorJugador] += self._estadosDeJugadores[self._últimaChancePorJugador].puntajeDeRonda()
			else: 
				# apuesta perdida
				for jugador in range(self._cantidadDeJugadores):
					if jugador != self._últimaChancePorJugador:
						self._puntajes[jugador] += self._estadosDeJugadores[jugador].puntajeDeRonda()
				self._puntajes[self._últimaChancePorJugador] += self._estadosDeJugadores[self._últimaChancePorJugador]._bonificacionPorColor()
			
			
			self._estadoActual = self.Estado.RONDA_TERMINADA
			
			self._deQuiénEsTurno = (self._deQuiénEsTurno + 1) % self._cantidadDeJugadores
			self._calcularSiHayGanador()
		
		else:
			
			self._estadoActual = self.Estado.FASE_ROBO
	
	def decirBasta(self):
		self._assertSePuedeTerminarElTurno()
		self._assertSePuedeTerminarLaRonda()
		
		for jugador in range(self._cantidadDeJugadores):
			self._puntajes[jugador] += self._estadosDeJugadores[jugador].puntajeDeRonda()
		
		self._estadoActual = self.Estado.RONDA_TERMINADA
		
		self._deQuiénEsTurno = (self._deQuiénEsTurno + 1) % self._cantidadDeJugadores
		self._calcularSiHayGanador()
	
	def decirÚltimaChance(self):
		self._assertSePuedeTerminarElTurno()
		self._assertSePuedeTerminarLaRonda()
		
		if len(self._mazo) == 0:
			# ronda anulada por mazo vacío
			
			self._estadoActual = self.Estado.RONDA_TERMINADA
			
			self._deQuiénEsTurno = (self._deQuiénEsTurno + 1) % self._cantidadDeJugadores
			return
		
		
		self._estadoActual = self.Estado.FASE_ROBO
		
		self._últimaChancePorJugador = self._deQuiénEsTurno
		self._deQuiénEsTurno = (self._deQuiénEsTurno + 1) % self._cantidadDeJugadores
	
	def puntajeParaGanar(self):
		return self._obtenerPuntajeParaGanarParaCantidadDeJugadores(self._cantidadDeJugadores)
	
	def _assertSePuedeJugarDuo(self, cartasAJugar):
		if not self.rondaEnCurso():
			raise JuegoException("No hay una ronda en curso")
		if self.hayQueTomarDecisionesDeRoboDelMazo():
			raise JuegoException("No se ha concretado el robo del mazo (¡falta elegir!)")
		if not self.seHaRobadoEsteTurno():
			raise JuegoException("No se puede jugar dúos sin antes haber robado")
		
		if cartasAJugar.total() != 2:
			raise JuegoException("Se necesitan dos cartas para jugar un dúo")
		
		for carta in cartasAJugar.elements():
			if not carta.esDuo():
				raise JuegoException("Se necesitan cartas dúo para jugar un dúo")
		
		tipos = [list(cartasAJugar.elements())[0].tipo, list(cartasAJugar.elements())[1].tipo] if (list(cartasAJugar.elements())[0].tipo.value < list(cartasAJugar.elements())[1].tipo.value) else [list(cartasAJugar.elements())[1].tipo, list(cartasAJugar.elements())[0].tipo]
		
		if not ((
				tipos[0] == Carta.Tipo.NADADOR and
				tipos[1] == Carta.Tipo.TIBURON
			) or (
				tipos[0] != Carta.Tipo.NADADOR and
				tipos[1] == tipos[0]
		)):
			raise JuegoException("Se necesitan cartas del mismo tipo dúo para jugar un dúo")
		
		if not (cartasAJugar <= self._estadosDeJugadores[self._deQuiénEsTurno].mano):
			raise JuegoException("Las cartas seleccionadas no están en la mano")
	
	def _moverDúoAZonaDeDúo(self, cartasAJugar):
		for clave in cartasAJugar:
			self._estadosDeJugadores[self._deQuiénEsTurno].mano[clave] -= cartasAJugar[clave]
			if self._estadosDeJugadores[self._deQuiénEsTurno].mano[clave] == 0:
				del self._estadosDeJugadores[self._deQuiénEsTurno].mano[clave]
		
		self._estadosDeJugadores[self._deQuiénEsTurno].zonaDeDuos[
			tuple(sorted((list(cartasAJugar.elements())[0], list(cartasAJugar.elements())[1])))
		] += 1
	
	def _obtenerPuntajeParaGanarParaCantidadDeJugadores(self, cantidadDeJugadores):
		if cantidadDeJugadores == 2:
			return 40
		elif cantidadDeJugadores == 3:
			return 35
		elif cantidadDeJugadores == 4:
			return 30
		else:
			raise JuegoException("La cantidad de jugadores no es válida")
	
	def _jugadorMostróSuManoPorÚltimaChance(self, jugador):
		if not self.útlimaChanceEnCurso():
			return False
		else:
			for orden in range(self._últimaChancePorJugador + 1, self._últimaChancePorJugador + 1 + self._cantidadDeJugadores):
				jugadorEnOrden = orden % self._cantidadDeJugadores
				if jugadorEnOrden == self._deQuiénEsTurno:
					return False
				if jugadorEnOrden == jugador:
					return True
	
	def _calcularSiHayGanador(self):
		puntajeMáximoAlcanzado = max(self._puntajes)
		if puntajeMáximoAlcanzado >= self.puntajeParaGanar():
			
			self._estadoActual = self.Estado.PARTIDA_TERMINADA
			
			
			# calcular ganador
			for orden in range(self._cantidadDeJugadores):
				jugadorEnOrden = (self._deQuiénEsTurno - 1 - orden) % self._cantidadDeJugadores
				if self._puntajes[jugadorEnOrden] == puntajeMáximoAlcanzado:
					self._jugadorGanador = jugadorEnOrden
					break;
	
	def _calcularSiHayGanadorPorSirenas(self):
		for j in range(self._cantidadDeJugadores):
			if self._estadosDeJugadores[j].mano[Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO)] == 4:
				
				self._estadoActual = self.Estado.PARTIDA_TERMINADA
				
				self._jugadorGanador = j
				self._puntajes[j] = SIRENAS_INF
			
	def _assertSePuedeElegirAcciónDeRobo(self):
		if not self.rondaEnCurso():
			raise JuegoException("No hay una ronda en curso")
		if self.hayQueTomarDecisionesDeRoboDelMazo():
			raise JuegoException("No se ha concretado el robo del mazo (¡falta elegir!)")
		if self.seHaRobadoEsteTurno():
			raise JuegoException("Ya se ha robado en este turno")
	
	def _assertSePuedeRobarDelMazo(self):
		if not self.rondaEnCurso():
			raise JuegoException("No hay una ronda en curso")
		if not self.hayQueTomarDecisionesDeRoboDelMazo():
			raise JuegoException("Debe confirmarse que se va a robar del mazo")
		if self.seHaRobadoEsteTurno():
			raise JuegoException("Ya se ha robado en este turno")
	
	def _assertObjetivoDeDescarteVálido(self, indiceDePilaDondeDescartar, indiceDeCartaARobar):
		if not (0 <= indiceDePilaDondeDescartar and indiceDePilaDondeDescartar <= 1):
			raise JuegoException("Pila de descarte no existente")
		elif len(self._descarte[indiceDePilaDondeDescartar]) > 0 and len(self._descarte[1 - indiceDePilaDondeDescartar]) == 0:
			raise JuegoException("No se puede descartar en una pila no vacía mientras la otra se encuentre vacía")
		elif not (0 <= indiceDeCartaARobar and indiceDeCartaARobar < min(2, len(self._mazo))):
			raise JuegoException("No se puede elegir una carta para robar fuera del rango")
	
	def _assertÍndicePilaDeDescarteVálidoParaRobar(self, indicePilaDeDescarte):
		if not (0 <= indicePilaDeDescarte and indicePilaDeDescarte < len(self._descarte)):
			raise JuegoException("Pila de descarte no existente")
		if len(self._descarte[indicePilaDeDescarte]) == 0:
			raise JuegoException("No se puede robar de una pila de descarte vacía")
	
	def _assertDúoEsDeTipo(self, cartasAJugar, tipoObjetivo):
		if tipoObjetivo in [Carta.Tipo.NADADOR, Carta.Tipo.TIBURON]:
			tipos = [list(cartasAJugar.elements())[0].tipo, list(cartasAJugar.elements())[1].tipo] if (list(cartasAJugar.elements())[0].tipo.value < list(cartasAJugar.elements())[1].tipo.value) else [list(cartasAJugar.elements())[1].tipo, list(cartasAJugar.elements())[0].tipo]
			if tipos[0] != Carta.Tipo.NADADOR or tipos[1] != Carta.Tipo.TIBURON:
				raise JuegoException("Ese tipo de dúo no es válido para esta acción")
		else:
			if next(iter(cartasAJugar)).tipo !=  tipoObjetivo:
				raise JuegoException("Ese tipo de dúo no es válido para esta acción")
	
	def _assertSelecciónDeJugadorVálida(self, jugadorARobar):
		if not (
			0 <= jugadorARobar and jugadorARobar < self._cantidadDeJugadores and jugadorARobar != self._deQuiénEsTurno
			and not self._jugadorMostróSuManoPorÚltimaChance(jugadorARobar)
		):
			raise JuegoException("La selección de jugador a robar con el dúo de nadador y tiburón es inválida")
	
	def _assertObjetivoDeDúoDeCangrejosVálido(self, pilaDeDescarteARobar, indiceDeCartaARobar):
		if (len(self._descarte[0]) != 0 or len(self._descarte[1]) != 0) and (
			(not (0 <= pilaDeDescarteARobar and pilaDeDescarteARobar <= 1) )
			or (
				not (0 <= indiceDeCartaARobar and indiceDeCartaARobar < len(self._descarte[pilaDeDescarteARobar]))
			)
		):
			raise JuegoException("La selección de robo con el dúo de cangrejos es inválida")
	
	def _assertSePuedeTerminarElTurno(self):
		if not self.rondaEnCurso():
			raise JuegoException("No hay una ronda en curso")
		if self.hayQueTomarDecisionesDeRoboDelMazo():
			raise JuegoException("No se ha concretado el robo del mazo (¡falta elegir!)")
		if not self.seHaRobadoEsteTurno():
			raise JuegoException("No se puede terminar el turno sin antes haber robado")
	
	def _assertSePuedeTerminarLaRonda(self):
		if not (self._estadosDeJugadores[self._deQuiénEsTurno].puntajeDeRonda() >= 7):
			raise JuegoException("No se puede terminar la ronda si no se tienen al menos siete puntos")
		if self.útlimaChanceEnCurso():
			raise JuegoException("Ya se está jugando una ronda de última chance")