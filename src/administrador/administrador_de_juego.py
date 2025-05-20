from .enums import Acción
from juego.juego import PartidaDeOcéanos
from bots.randy import RandyBot

class AdministradorDeJuego():
	def __init__(self, jugadoresDePartida, verbose=False):
		self._jugadores = jugadoresDePartida
		self._juego = None
		self._verbose = verbose
	
	def jugarPartida(self):
		self._juego = PartidaDeOcéanos(cantidadDeJugadores=len(self._jugadores))
		
		for j in range(len(self._jugadores)):
			self._jugadores[j].configurarParaJuego(self._juego, j)
		
		while not self._juego.haTerminado():
			self._juego.iniciarRonda()
			if self._verbose:
				print("~~~~~~~~~~~~~~~~~~~~~ Inicia Ronda ~~~~~~~~~~~~~~~~~~~~~~")
				print(f"Jugador inicial: {self._juego._deQuiénEsTurno}")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

			while self._juego.rondaEnCurso():
				if self._verbose:
					print(f"~~~~~~~~~~~~~~~~~~~ Turno del jugador {self._juego._deQuiénEsTurno} ~~~~~~~~~~~~~~~~~~~~")
					print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
					print(f"El descarte 0 es {(self._juego._descarte[0])}")
					print(f"El descarte 1 es {(self._juego._descarte[1])}")
				
				self._faseDeRobo()
				self._faseDeDúos()
				self._faseDeFin()
			
			if self._verbose:
				print("******************** Ronda terminada ********************")
				for j in range(self._juego.cantidadDeJugadores):
					print(f"Jugador {j}: +{self._juego._estadosDeJugadores[j].puntajeDeRonda()} ({self._juego.puntajes[j]}/{self._juego.puntajeParaGanar})")
				print("*********************************************************")
		
		if self._verbose:
			print("!!!!!!!!!!!!!!!!!!! Partida Terminada !!!!!!!!!!!!!!!!!!!")
			print(f"Ganador: {self._juego._jugadorGanador}")
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		return self._juego._jugadorGanador
	
	def _faseDeRobo(self):
		acciónDeRobo = self._jugadores[self._juego._deQuiénEsTurno].decidirAcciónDeRobo()
		
		if acciónDeRobo == Acción.Robo.DEL_MAZO:
			# Robar del mazo
			opcionesDeRobo = self._juego.verCartasParaRobarDelMazo()
			(indiceDeCartaARobar, indiceDePilaDondeDescartar) = self._jugadores[self._juego._deQuiénEsTurno].decidirCómoRobarDelMazo(opcionesDeRobo)
			cartaRobada = self._juego.robarDelMazo(indiceDeCartaARobar, indiceDePilaDondeDescartar)
			if self._verbose:
				print(f"Roba del mazo una {cartaRobada}")
			
		elif acciónDeRobo == Acción.Robo.DEL_DESCARTE_0:
			cartaRobada = self._juego.robarDelDescarte(0)
			if self._verbose:
				print(f"Roba del descarte 0 una {cartaRobada}")
		elif acciónDeRobo == Acción.Robo.DEL_DESCARTE_1:
			cartaRobada = self._juego.robarDelDescarte(1)
			if self._verbose:
				print(f"Roba del descarte 1 una {cartaRobada}")
		else:
			#! ERROR
			raise Exception("Error")

	def _faseDeDúos(self):
		noSeQuierenJugarMásDúos = False
		
		while not noSeQuierenJugarMásDúos and not self._juego.haTerminado():
			(acciónDeDúos, cartasAJugar, parametrosDelDúo) = self._jugadores[self._juego._deQuiénEsTurno].decidirAcciónDeDúos()
			if acciónDeDúos == Acción.Dúos.JUGAR_PECES:
				# Jugar dúo de peces
				cartaRobada = self._juego.jugarDuoDePeces(cartasAJugar)
				if self._verbose:
					print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]} y roba una {cartaRobada}")
				
			elif acciónDeDúos == Acción.Dúos.JUGAR_BARCOS:
				# Jugar dúo de barcos
				if self._verbose:
					print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]}")
				self._juego.jugarDuoDeBarcos(cartasAJugar)
				self._faseDeRobo()
				self._faseDeDúos()
				noSeQuierenJugarMásDúos = True
				
			elif acciónDeDúos == Acción.Dúos.JUGAR_CANGREJOS:
				# Jugar dúo de cangrejos
				(pilaDeDescarteARobar, indiceDeCartaARobar) = parametrosDelDúo
				cartaRobada = self._juego.jugarDuoDeCangrejos(cartasAJugar, pilaDeDescarteARobar, indiceDeCartaARobar)
				if self._verbose:
					print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]} para robar una {cartaRobada}")
				
			elif acciónDeDúos == Acción.Dúos.JUGAR_NADADOR_Y_TIBURÓN:
				# Jugar dúo de nadador y tiburón
				jugadorARobar = parametrosDelDúo[0]
				cartaRobada = self._juego.jugarDuoDeNadadorYTiburón(cartasAJugar, jugadorARobar)
				if self._verbose:
					print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]} para robarle al jugador {jugadorARobar}, y roba una {cartaRobada}")
				
			elif acciónDeDúos == Acción.Dúos.NO_JUGAR:
				# No jugar dúos
				noSeQuierenJugarMásDúos = True
				if self._verbose:
					print("No juega ningún dúo")
				
			else:
				#! ERROR
				raise Exception("Error")

	def _faseDeFin(self):
		if self._juego.haTerminado():
			if self._verbose:
				print("################### CUATRO SIRENAS ###################")
				print(f"Ganador: {self._juego._jugadorGanador}")
				for j in range(self._juego.cantidadDeJugadores()):
					print(f"Jugador {j}: +{self._juego._estadosDeJugadores[j].puntajeDeRonda()} ({self._juego.puntajes[j]}/{self._juego.puntajeParaGanar})")
				print("######################################################")
		else:
		
			acciónDeRobo = self._jugadores[self._juego._deQuiénEsTurno].decidirAcciónDeFinDeRonda()

			if acciónDeRobo == Acción.FinDeRonda.PASAR_TURNO:
				# Pasar el turno normalmente
				self._juego.pasarTurno()
				if self._verbose:
					print("Pasa de turno")
			elif acciónDeRobo == Acción.FinDeRonda.DECIR_BASTA:
				# Decir basta y terminar la ronda
				self._juego.decirBasta()
				if self._verbose:
					print("¡¡¡Basta!!!")
			elif acciónDeRobo == Acción.FinDeRonda.DECIR_ÚLTIMA_CHANCE:
				# Decir última chance y pasar el turno
				self._juego.decirÚltimaChance()
				if self._verbose:
					print("¡¡¡Última Chance!!!")
			else:
				#! ERROR
				raise Exception("Error")

if __name__ == '__main__':
	administrador = AdministradorDeJuego([RandyBot(), RandyBot()], verbose=True)
	ganador = administrador.jugarPartida()
	print(f"Ganador: {ganador}")
