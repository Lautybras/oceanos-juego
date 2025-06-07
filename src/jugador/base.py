from collections import Counter as Multiset
from administrador.acción import Acción
from juego.carta import Carta
from juego.partida import PartidaDeOcéanos
from administrador.evento import Evento

class JugadorBase():
	# ========================= INTERFAZ DE JUEGO =========================
	def __init__(self) -> None:
		self._juego: PartidaDeOcéanos = None
		self._númeroDeJugador: int = None
		self._listaDeEventos: list[Evento]
	
	def configurarParaJuego(self, juego: PartidaDeOcéanos, númeroDeJugador: int, listaDeEventos: list[Evento]) -> None:
		self._juego = juego
		self._númeroDeJugador = númeroDeJugador
		self._listaDeEventos = listaDeEventos
	
	def decidirAcciónDeRobo(self) -> Acción.Robo:
		raise Exception("¡Implementame!")
	
	def decidirCómoRobarDelMazo(self, opcionesDeRobo: list[Carta]) -> tuple[int, int|None]:
		raise Exception("¡Implementame!")
	
	def decidirAcciónDeDúos(self) -> tuple[Acción.Dúos, Multiset[Carta]|None, tuple[any]|None]:
		raise Exception("¡Implementame!")
	
	def decidirQuéRobarConDúoDeCangrejos(self, descarteElegido: list[Carta]) -> int:
		raise Exception("¡Implementame!")
	
	def decidirAcciónDeFinDeTurno(self) -> Acción.FinDeTurno:
		raise Exception("¡Implementame!")
	
	def configurarInicioDeRonda(self, cartasInicialesDelDescarte: tuple[Carta, Carta]) -> None:
		raise Exception("¡Implementame!")
	
	def configurarFinDeRonda(self, manos: list[Multiset[Carta]], puntajesDeRonda: list[int]) -> None:
		raise Exception("¡Implementame!")
	
	def configurarInicioDeTurno(self) -> None:
		raise Exception("¡Implementame!")
	
	# ============================ AUXILIARES =============================
	def _buscarDúoParaJugar(self, tipo: Carta.Tipo) -> Multiset[Carta]|None:
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