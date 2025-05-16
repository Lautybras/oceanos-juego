import random
from .carta import Carta
from collections import Counter as Multiset

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

class EstadoDelJuego():
	def __init__(self, cantidadDeJugadores=2):
		if(not (2 <= cantidadDeJugadores and cantidadDeJugadores <= 4)):
			raise JuegoInvalidoException("La cantidad de jugadores es inválida")
		
		self.cantidadDeJugadores = cantidadDeJugadores 
		self.puntajesDeJuego = [0] * cantidadDeJugadores
		self.estadoDelJugador = None
		self.mazo = None
		self.descarte = None
		self.haTerminado = False
		self.deQuienEsTurno = None
		self.seHaRobadoEsteTurno = None
		self.hayQueTomarDecisionesDeRoboDelMazo = None
		self.rondaEnCurso = False
	
	def iniciarRonda(self):
		self.estadoDelJugador = [EstadoDeJugador() for _ in range(self.cantidadDeJugadores)]
		self.mazo = list(cartasDelJuego())
		random.shuffle(self.mazo)
		self.descarte = ([self.mazo.pop(0)], [self.mazo.pop(0)])
		self.deQuienEsTurno = 0
		self.seHaRobadoEsteTurno = False
		self.hayQueTomarDecisionesDeRoboDelMazo = False
		self.rondaEnCurso = True
	
	def robarDelDescarte(self, indicePilaDeDescarte):
		if not self.rondaEnCurso:
			raise JuegoException("No hay una ronda en curso")
		if self.hayQueTomarDecisionesDeRoboDelMazo:
			raise JuegoException("No se ha concretado el robo del mazo (¡falta elegir!)")
		if self.seHaRobadoEsteTurno:
			raise JuegoException("Ya se ha robado en este turno")
		if not (0 <= indicePilaDeDescarte and indicePilaDeDescarte < len(self.descarte)):
			raise JuegoException("Pila de descarte no existente")
		if len(self.descarte[indicePilaDeDescarte]) == 0:
			raise JuegoException("No se puede robar de una pila de descarte vacía")
		
		cartaRobada = self.descarte[indicePilaDeDescarte].pop()
		
		self.estadoDelJugador[self.deQuienEsTurno].mano[cartaRobada] += 1
		
		self.seHaRobadoEsteTurno = True
		
		return cartaRobada
	
	def robarDelMazo(self):
		if not self.rondaEnCurso:
			raise JuegoException("No hay una ronda en curso")
		if self.hayQueTomarDecisionesDeRoboDelMazo:
			raise JuegoException("No se ha concretado el robo del mazo (¡falta elegir!)")
		if self.seHaRobadoEsteTurno:
			raise JuegoException("Ya se ha robado en este turno")
		if len(self.mazo) == 0:
			raise JuegoException("No se puede robar de un mazo vacío")
		
		self.hayQueTomarDecisionesDeRoboDelMazo = True
		if len(self.mazo) == 1:
			return [self.mazo[-1]]
		return [self.mazo[-1], self.mazo[-2]]
	
	def elegirRoboDelMazo(self, indiceDeCartaARobar, indiceDePilaDondeDescartar):
		if not self.rondaEnCurso:
			raise JuegoException("No hay una ronda en curso")
		
		if not (0 <= indiceDePilaDondeDescartar and indiceDePilaDondeDescartar <= 1):
			raise JuegoException("Pila de descarte no existente")
		elif len(self.descarte[indiceDePilaDondeDescartar]) == 0 and len(self.descarte[1 - indiceDePilaDondeDescartar]) > 0:
			raise JuegoException("No se puede descartar en una pila no vacía mientras la otra se encuentre vacía")
		elif not (0 <= indiceDeCartaARobar and indiceDeCartaARobar < min(2, len(self.mazo))):
			raise JuegoException("No se puede elegir una carta para robar fuera del rango")
		
		cartasRobadasDelMazo = [self.mazo.pop()]
		if len(self.mazo) > 1:
			cartasRobadasDelMazo.append(self.mazo.pop())
			self.descarte[indiceDePilaDondeDescartar].append(cartasRobadasDelMazo[1 - indiceDeCartaARobar])
		self.estadoDelJugador[self.deQuienEsTurno].mano[cartasRobadasDelMazo[indiceDeCartaARobar]] += 1
		
		self.hayQueTomarDecisionesDeRoboDelMazo = False
		self.seHaRobadoEsteTurno = True
	
	def jugarDuo(self, cartasAJugar):
		if not self.rondaEnCurso:
			raise JuegoException("No hay una ronda en curso")
		if self.hayQueTomarDecisionesDeRoboDelMazo:
			raise JuegoException("No se ha concretado el robo del mazo (¡falta elegir!)")
		if not self.seHaRobadoEsteTurno:
			raise JuegoException("No se puede jugar dúos sin antes haber robado")
		
		if cartasAJugar.total() != 2:
			raise JuegoException("Se necesitan dos cartas para jugar un dúo")
		
		for carta in cartasAJugar.elements():
			if not carta.esDuo():
				raise JuegoException("Se necesitan cartas dúo para jugar un dúo")
		
		tipoDeDuo = next(iter(cartasAJugar)).tipo
		for carta in cartasAJugar.elements():
			if carta.tipo != tipoDeDuo:
				raise JuegoException("Se necesitan cartas del mismo tipo dúo para jugar un dúo")
			
		if not (cartasAJugar <= self.estadoDelJugador[self.deQuienEsTurno].mano):
			raise JuegoException("Las cartas seleccionadas no están en la mano")
		
		
		for clave in cartasAJugar:
			self.estadoDelJugador[self.deQuienEsTurno].mano[clave] -= cartasAJugar[clave]
			if self.estadoDelJugador[self.deQuienEsTurno].mano[clave] == 0:
				del self.estadoDelJugador[self.deQuienEsTurno].mano[clave]
		
		self.estadoDelJugador[self.deQuienEsTurno].zonaDeDuos[
			tuple(sorted((list(cartasAJugar.elements())[0], list(cartasAJugar.elements())[1])))
		] += 1
		
	def pasarTurno(self):
		if not self.rondaEnCurso:
			raise JuegoException("No hay una ronda en curso")
		if self.hayQueTomarDecisionesDeRoboDelMazo:
			raise JuegoException("No se ha concretado el robo del mazo (¡falta elegir!)")
		if not self.seHaRobadoEsteTurno:
			raise JuegoException("No se puede pasar de turno sin antes haber robado")
		
		self.deQuienEsTurno = (self.deQuienEsTurno + 1) % self.cantidadDeJugadores
		self.seHaRobadoEsteTurno = False
	

	def puntajeParaGanar(self):
		return self._obtenerPuntajeParaGanarParaCantidadDeJugadores(self.cantidadDeJugadores)
	
	def _obtenerPuntajeParaGanarParaCantidadDeJugadores(self, cantidadDeJugadores):
		if cantidadDeJugadores == 2:
			return 40
		elif cantidadDeJugadores == 3:
			return 35
		elif cantidadDeJugadores == 4:
			return 30
		else:
			raise JuegoException("La cantidad de jugadores no es válida")