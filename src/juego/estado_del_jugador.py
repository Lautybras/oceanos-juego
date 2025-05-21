from collections import Counter as Multiset
from .carta import Carta
from .excepciones import JuegoException, JuegoInvalidoException

class EstadoDeJugador():
	def __init__(self):
		self.mano = Multiset()
		self.zonaDeDúos = Multiset()
		
	def puntajeDeRonda(self):
		cantidadDeCartasEnManoDeTipo = {tipo: 0 for tipo in Carta.Tipo}
		cantidadDeDúosEnJuegoDeTipo = {
			Carta.Tipo.PEZ: 0,
			Carta.Tipo.BARCO: 0,
			Carta.Tipo.CANGREJO: 0,
			Carta.Tipo.NADADOR: 0    # noo maldito enum que no me deja poner nombres declarativos!
		}
		cantidadDeCartasDeColor = {color: 0 for color in Carta.Color}
		
		for claveDeCarta in self.mano:
			cantidadDeCartasEnManoDeTipo[claveDeCarta.tipo] += self.mano[claveDeCarta]
			cantidadDeCartasDeColor[claveDeCarta.color] += self.mano[claveDeCarta]
		
		for claveDeDúo in self.zonaDeDúos:
			cantidadDeDúosEnJuegoDeTipo[claveDeDúo[0].tipo] += self.zonaDeDúos[claveDeDúo]
			cantidadDeCartasDeColor[claveDeDúo[0].color] += self.zonaDeDúos[claveDeDúo]
			cantidadDeCartasDeColor[claveDeDúo[1].color] += self.zonaDeDúos[claveDeDúo]
		
		return (
			self._puntajePorDúosEnMano(cantidadDeCartasEnManoDeTipo) +
			self._puntajePorDúosJugados() + 
			self._puntajePorColeccionables(cantidadDeCartasEnManoDeTipo) +
			self._puntajePorMultiplicadores(cantidadDeCartasEnManoDeTipo, cantidadDeDúosEnJuegoDeTipo) +
			self._puntajePorSirenas(cantidadDeCartasEnManoDeTipo[Carta.Tipo.SIRENA], cantidadDeCartasDeColor)
		)
	
	def _puntajePorDúosEnMano(self, cantidadDeCartasDúos):
		return (
			(cantidadDeCartasDúos[Carta.Tipo.PEZ] // 2) +  
			(cantidadDeCartasDúos[Carta.Tipo.BARCO] // 2) +  
			(cantidadDeCartasDúos[Carta.Tipo.CANGREJO] // 2) +  
			min(cantidadDeCartasDúos[Carta.Tipo.NADADOR], cantidadDeCartasDúos[Carta.Tipo.TIBURÓN])
		)
	
	def _puntajePorDúosJugados(self):
		return self.zonaDeDúos.total()
	
	def _puntajePorColeccionables(self, cantidadDeColeccionables):
		return (
			self._puntajePorAnclas(cantidadDeColeccionables[Carta.Tipo.ANCLA]) +
			self._puntajePorConchas(cantidadDeColeccionables[Carta.Tipo.CONCHA]) +
			self._puntajePorPinguinos(cantidadDeColeccionables[Carta.Tipo.PINGUINO]) +
			self._puntajePorPulpos(cantidadDeColeccionables[Carta.Tipo.PULPO])
		)
	
	def _puntajePorMultiplicadores(self, cantidadDeCartasEnManoDeTipo, cantidadDeDúosEnJuegoDeTipo):
		return (
			(cantidadDeCartasEnManoDeTipo[Carta.Tipo.CAPITÁN] * 3 * cantidadDeCartasEnManoDeTipo[Carta.Tipo.ANCLA]) +
			(cantidadDeCartasEnManoDeTipo[Carta.Tipo.COLONIA] * 2 * cantidadDeCartasEnManoDeTipo[Carta.Tipo.PINGUINO]) +
			(
				cantidadDeCartasEnManoDeTipo[Carta.Tipo.CARDUMEN] * 1 *
				(cantidadDeCartasEnManoDeTipo[Carta.Tipo.PEZ] + 2 * cantidadDeDúosEnJuegoDeTipo[Carta.Tipo.PEZ])
			) +
			(
				cantidadDeCartasEnManoDeTipo[Carta.Tipo.FARO] * 1 *
				(cantidadDeCartasEnManoDeTipo[Carta.Tipo.BARCO] + 2 * cantidadDeDúosEnJuegoDeTipo[Carta.Tipo.BARCO])
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
		
		for claveDeDúo in self.zonaDeDúos:
			cantidadDeCartasDeColor[claveDeDúo[0].color] += self.zonaDeDúos[claveDeDúo]
			cantidadDeCartasDeColor[claveDeDúo[1].color] += self.zonaDeDúos[claveDeDúo]
		
		return sum(
			(sorted(list(cantidadDeCartasDeColor.values()), reverse=True))[0:1]
		)
