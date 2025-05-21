from random import choice
from collections import Counter as Multiset
from administrador.enums import Acción
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos

class JugadorBase():
	# ========================= INTERFAZ DE JUEGO =========================
	def __init__(self):
		self._juego = None
		self._númeroDeJugador = None
		
		# * Se pueden definir más variables de instancia acá! *
	
	def decidirAcciónDeRobo(self):
		# !Implementar!
		raise Exception("¡Implementame!")
	
	def decidirCómoRobarDelMazo(self, opcionesDeRobo):
		# !Implementar!
		raise Exception("¡Implementame!")
	
	def decidirAcciónDeDúos(self):
		# !Implementar!
		raise Exception("¡Implementame!")
	
	def decidirAcciónDeFinDeRonda(self):
		# !Implementar!
		raise Exception("¡Implementame!")
	
	def configurarFinDeRonda(self, manos, puntajesDeRonda):
		# !Implementar!
		raise Exception("¡Implementame!")
	
	# ============================ AUXILIARES =============================
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