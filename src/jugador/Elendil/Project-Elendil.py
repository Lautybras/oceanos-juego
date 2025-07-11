from collections import Counter as Multiset
from administrador.acción import Acción
from juego.carta import Carta
from juego.partida import PartidaDeOcéanos
from administrador.evento import Evento
from ..base import JugadorBase

class Elendil(JugadorBase):
	#Que atributos quiero?
	#Idea, muchisimos atributos y decidir aleatoriamente con respecto a ellos que hacer
	#Por ahora, colores, winconditions (2, con una no alcanza) cardumen, faro, etc.


	# ========================= INTERFAZ DE JUEGO =========================
	def __init__(self) -> None:
		super().__init__()
		self._win_Conditions: int
		self._tengo_Sirena: bool
		self._tengo_Cardumen: bool
		self._tengo_Faro: bool
		self._tengo_Ancla: bool
		self._ultima_Chance: bool
		



		##Contadores de colores, ojo con el coleccionar colores, reescribir todo arriba y copia
		##repetir codigo es re diverrrrr, numero 500 a revisar
		self._ColeccionarColores = max(int(self._tengo_Sirena),  500*int(self._ultima_Chance))
		self._contadorNegro: int
		##seguir despeus con todos, hay que ver si los uso



		#* Acá se pueden hacer más cosas, como definir variables del Bot
	
	def configurarParaJuego(self, juego: PartidaDeOcéanos, númeroDeJugador: int, listaDeEventos: list[Evento]) -> None:
		super().configurarParaJuego(juego, númeroDeJugador, listaDeEventos)
		#* Acá se pueden hacer más cosas, como cambiar el comportamiento según el número de jugadores
	
	def decidirAcciónDeRobo(self) -> Acción.Robo:
		# !Implementar y borrar la línea de abajo! 
		raise Exception("¡Implementame!")
	
	def decidirCómoRobarDelMazo(self, opcionesDeRobo: list[Carta]) -> tuple[int, int|None]:
		# !Implementar y borrar la línea de abajo! 
		raise Exception("¡Implementame!")
	
	def decidirAcciónDeDúos(self) -> tuple[Acción.Dúos, Multiset[Carta]|None, tuple[any]|None]:
		# !Implementar y borrar la línea de abajo! 
		raise Exception("¡Implementame!")
	
	def decidirQuéRobarConDúoDeCangrejos(self, descarteElegido: list[Carta]) -> int:
		# !Implementar y borrar la línea de abajo! 
		raise Exception("¡Implementame!")
	
	def decidirAcciónDeFinDeTurno(self) -> Acción.FinDeTurno:
		# !Implementar y borrar la línea de abajo! 
		raise Exception("¡Implementame!")
	
	def configurarInicioDeRonda(self, cartasInicialesDelDescarte: tuple[Carta, Carta]) -> None:
		# !Implementar y borrar la línea de abajo! 
		raise Exception("¡Implementame!")
	
	def configurarFinDeRonda(self, manos: list[Multiset[Carta]], puntajesDeRonda: list[int]) -> None:
		# !Implementar y borrar la línea de abajo! 
		raise Exception("¡Implementame!")
	
	def configurarInicioDeTurno(self) -> None:
		# !Implementar y borrar la línea de abajo! 
		raise Exception("¡Implementame!")
	
	# ============================ AUXILIARES =============================
	#* Acá se pueden definir más auxiliares para ser usados por tu Bot!
	def miAuxiliarFachero(self, soyFachero: bool) -> str:
		if soyFachero:
			return "Soy fachero!"
		else:
			return "No soy tan fachero..."