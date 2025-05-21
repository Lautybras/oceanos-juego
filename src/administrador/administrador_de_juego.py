from copy import copy, deepcopy
from .acción import Acción
from .evento import Evento
from juego.carta import Carta
from juego.partida import PartidaDeOcéanos, SIRENAS_INF
from jugador.randy import RandyBot

class AdministradorDeJuego():
	def __init__(self, clasesDeJugadores, verbose=False):
		self._clasesDeJugadores = clasesDeJugadores
		self._jugadores = [None] * len(clasesDeJugadores)
		self._juego = None
		self._verbose = verbose
		self._eventos = []
		
		self._cantidadDeCartasPorTipoPorJugador = {tipo: [0] * len(self._jugadores) for tipo in Carta.Tipo}
		
		self._dúosJugadosPorTipoPorJugador = {
			Carta.Tipo.PEZ: [0] * len(self._jugadores),
			Carta.Tipo.BARCO: [0] * len(self._jugadores),
			Carta.Tipo.CANGREJO: [0] * len(self._jugadores),
			Carta.Tipo.NADADOR: [0] * len(self._jugadores)
		}
		
		self._dúosEnManoPorTipoPorJugador = {
			Carta.Tipo.PEZ: [0] * len(self._jugadores),
			Carta.Tipo.BARCO: [0] * len(self._jugadores),
			Carta.Tipo.CANGREJO: [0] * len(self._jugadores),
			Carta.Tipo.NADADOR: [0] * len(self._jugadores)
		}
		
		self._motivosFinDeRonda = {
			"0_CARTAS": 0,
			"BASTA": 0,
			"ÚLTIMA_CHANCE": 0,
			"4_SIRENAS": 0,
		}
		
		self._motivosFinDeRondaPorJugador = [{
			"BASTA": 0,
			"ÚLTIMA_CHANCE_GANADA": 0,
			"ÚLTIMA_CHANCE_PERDIDA": 0,
			"4_SIRENAS": 0,
		} for _ in range(len(self._jugadores))]
	
	def jugarPartida(self):
		self._juego = PartidaDeOcéanos(cantidadDeJugadores=len(self._jugadores))
		for j in range(len(self._clasesDeJugadores)):
			self._jugadores[j] = (self._clasesDeJugadores[j])()
			self._jugadores[j].configurarParaJuego(self._juego, j, self._eventos)
		
		while not self._juego.haTerminado():
			self._eventos.clear()
			
			self._juego.iniciarRonda()
			if self._verbose:
				print("~~~~~~~~~~~~~~~~~~~~~ Inicia Ronda ~~~~~~~~~~~~~~~~~~~~~~")
				print(f"Jugador inicial: {self._juego.deQuiénEsTurno}")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

			while self._juego.rondaEnCurso():
				if self._verbose:
					print(f"~~~~~~~~~~~~~~~~~~~ Turno del jugador {self._juego.deQuiénEsTurno} ~~~~~~~~~~~~~~~~~~~~")
					print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
					print(f"El descarte 0 es {(self._juego._descarte[0])}")
					print(f"El descarte 1 es {(self._juego._descarte[1])}")
				
				self._faseDeRobo()
				self._faseDeDúos()
				self._faseDeFin()
			
			self._finDeRonda()
		
		if self._verbose:
			print("!!!!!!!!!!!!!!!!!!! Partida Terminada !!!!!!!!!!!!!!!!!!!")
			print(f"Ganador: {self._juego.jugadorGanador}")
			print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		return self._juego.jugadorGanador
	
	def _faseDeRobo(self):
		acciónDeRobo = self._jugadores[self._juego.deQuiénEsTurno].decidirAcciónDeRobo()
		
		if acciónDeRobo == Acción.Robo.DEL_MAZO:
			# Robar del mazo
			opcionesDeRobo = self._juego.verCartasParaRobarDelMazo()
			(indiceDeCartaARobar, indiceDePilaDondeDescartar) = self._jugadores[self._juego.deQuiénEsTurno].decidirCómoRobarDelMazo(opcionesDeRobo)
			cartaRobada = self._juego.robarDelMazo(indiceDeCartaARobar, indiceDePilaDondeDescartar)
			
			self._eventos.append(Evento(self._juego.deQuiénEsTurno, Acción.Robo.DEL_MAZO,
				{
					"cartaDescartada": copy(self._juego.topeDelDescarte[indiceDePilaDondeDescartar]),
					"pilaDondeDescartó": indiceDePilaDondeDescartar
				}
			))
			if self._verbose:
				print(f"Roba del mazo una {cartaRobada}")
			
		elif acciónDeRobo == Acción.Robo.DEL_DESCARTE_0:
			cartaRobada = self._juego.robarDelDescarte(0)
			
			self._eventos.append(Evento(self._juego.deQuiénEsTurno, Acción.Robo.DEL_DESCARTE_0,
				{
					"cartaRobada": copy(cartaRobada)
				}
			))
			if self._verbose:
				print(f"Roba del descarte 0 una {cartaRobada}")
		elif acciónDeRobo == Acción.Robo.DEL_DESCARTE_1:
			cartaRobada = self._juego.robarDelDescarte(1)
			
			self._eventos.append(Evento(self._juego.deQuiénEsTurno, Acción.Robo.DEL_DESCARTE_1,
				{
					"cartaRobada": copy(cartaRobada)
				}
			))
			if self._verbose:
				print(f"Roba del descarte 1 una {cartaRobada}")
		else:
			#! ERROR
			raise Exception("Error")

	def _faseDeDúos(self):
		noSeQuierenJugarMásDúos = False
		
		while not noSeQuierenJugarMásDúos and not self._juego.haTerminado():
			(acciónDeDúos, cartasAJugar, parametrosDelDúo) = self._jugadores[self._juego.deQuiénEsTurno].decidirAcciónDeDúos()
			if acciónDeDúos == Acción.Dúos.JUGAR_PECES:
				# Jugar dúo de peces
				self._eventos.append(Evento(self._juego.deQuiénEsTurno, acciónDeDúos,
					{
						"cartasJugadas": deepcopy(sorted(cartasAJugar.elements()))
					}
				))
				
				cartaRobada = self._juego.jugarDúoDePeces(cartasAJugar)
				if self._verbose:
					print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]} y roba una {cartaRobada}")
				
			elif acciónDeDúos == Acción.Dúos.JUGAR_BARCOS:
				# Jugar dúo de barcos
				self._eventos.append(Evento(self._juego.deQuiénEsTurno, acciónDeDúos,
					{
						"cartasJugadas": deepcopy(sorted(cartasAJugar.elements()))
					}
				))
				
				if self._verbose:
					print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]}")
				self._juego.jugarDúoDeBarcos(cartasAJugar)
				if self._juego.rondaEnCurso():
					self._faseDeRobo()
					self._faseDeDúos()
				noSeQuierenJugarMásDúos = True
				
			elif acciónDeDúos == Acción.Dúos.JUGAR_CANGREJOS:
				# Jugar dúo de cangrejos
				(pilaDeDescarteARobar, indiceDeCartaARobar) = parametrosDelDúo
				
				self._eventos.append(Evento(self._juego.deQuiénEsTurno, acciónDeDúos,
					{
						"cartasJugadas": deepcopy(sorted(cartasAJugar.elements())),
						"pilaDondeRobó": pilaDeDescarteARobar
					}
				))
				
				cartaRobada = self._juego.jugarDúoDeCangrejos(cartasAJugar, pilaDeDescarteARobar, indiceDeCartaARobar)
				if self._verbose:
					print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]} para robar una {cartaRobada}")
				
			elif acciónDeDúos == Acción.Dúos.JUGAR_NADADOR_Y_TIBURÓN:
				# Jugar dúo de nadador y tiburón
				jugadorARobar = parametrosDelDúo[0]
				cartaRobada = self._juego.jugarDúoDeNadadorYTiburón(cartasAJugar, jugadorARobar)
				
				self._eventos.append(Evento(self._juego.deQuiénEsTurno, acciónDeDúos,
					{
						"cartasJugadas": deepcopy(sorted(cartasAJugar.elements())),
						"jugadorRobado": jugadorARobar,
						"cartaRobada": cartaRobada # ! SOLO VER SI FUISTE EL JUGADOR ROBADO!!!
					}
				))
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
		if not self._juego.haTerminado() and self._juego.rondaEnCurso():
			acciónDeFinDeRonda = self._jugadores[self._juego.deQuiénEsTurno].decidirAcciónDeFinDeRonda()
			self._eventos.append(Evento(self._juego.deQuiénEsTurno, acciónDeFinDeRonda, None))
			
			if acciónDeFinDeRonda == Acción.FinDeRonda.PASAR_TURNO:
				# Pasar el turno normalmente				
				self._juego.pasarTurno()
				if self._verbose:
					print("Pasa de turno")
			elif acciónDeFinDeRonda == Acción.FinDeRonda.DECIR_BASTA:
				# Decir basta y terminar la ronda
				self._juego.decirBasta()
				if self._verbose:
					print("¡¡¡Basta!!!")
			elif acciónDeFinDeRonda == Acción.FinDeRonda.DECIR_ÚLTIMA_CHANCE:
				# Decir última chance y pasar el turno
				self._juego.decirÚltimaChance()
				if self._verbose:
					print("¡¡¡Última Chance!!!")
			else:
				#! ERROR
				raise Exception("Error")
	
	def _finDeRonda(self):
		if max(self._juego.puntajes) == SIRENAS_INF:
			self._motivosFinDeRonda["4_SIRENAS"] += 1
			self._motivosFinDeRondaPorJugador[self._juego.jugadorGanador]["4_SIRENAS"] += 1
			if self._verbose:
				print("################### CUATRO SIRENAS ###################")
				print(f"Ganador: {self._juego.jugadorGanador}")
				for j in range(self._juego.cantidadDeJugadores):
					if self._juego.puntajes[j] == SIRENAS_INF:
						print(f"Jugador {j}: +INF (INF/{self._juego.puntajeParaGanar})")
					else:
						print(f"Jugador {j}: +0 ({self._juego.puntajes[j]}/{self._juego.puntajeParaGanar})")
				print("######################################################")
		elif self._juego.rondaAnulada():
			self._motivosFinDeRonda["0_CARTAS"] += 1
			if self._verbose:
				print("********* Ronda anulada por cero cartas en mazo *********")
				for j in range(self._juego.cantidadDeJugadores):
					print(f"Jugador {j}: +0 ({self._juego.puntajes[j]}/{self._juego.puntajeParaGanar})")
				print("*********************************************************")
		elif self._juego.útlimaChanceEnCurso():
			self._motivosFinDeRonda["ÚLTIMA_CHANCE"] += 1
			if self._juego.últimaChanceGanada():
				self._motivosFinDeRondaPorJugador[self._juego.jugadorQueDijoÚltimaChance]["ÚLTIMA_CHANCE_GANADA"] += 1
			else:
				self._motivosFinDeRondaPorJugador[self._juego.jugadorQueDijoÚltimaChance]["ÚLTIMA_CHANCE_PERDIDA"] += 1
			if self._verbose:
				print("*********** Ronda terminada por última chance ***********")
				if self._juego.últimaChanceGanada():
					print("¡Apuesta ganada!")
					for j in range(self._juego.cantidadDeJugadores):
						if j == self._juego.jugadorQueDijoÚltimaChance:
							print(f"Jugador {j}: +{self._juego._estadosDeJugadores[j].puntajeDeRonda() + self._juego._estadosDeJugadores[j]._bonificacionPorColor()} ({self._juego.puntajes[j]}/{self._juego.puntajeParaGanar})")
						else:
							print(f"Jugador {j}: +{self._juego._estadosDeJugadores[j]._bonificacionPorColor()} ({self._juego.puntajes[j]}/{self._juego.puntajeParaGanar})")
				else:
					print("Apuesta perdida...")
					for j in range(self._juego.cantidadDeJugadores):
						if j == self._juego.jugadorQueDijoÚltimaChance:
							print(f"Jugador {j}: +{self._juego._estadosDeJugadores[j]._bonificacionPorColor()} ({self._juego.puntajes[j]}/{self._juego.puntajeParaGanar})")
						else:
							print(f"Jugador {j}: +{self._juego._estadosDeJugadores[j].puntajeDeRonda()} ({self._juego.puntajes[j]}/{self._juego.puntajeParaGanar})")
				print("*********************************************************")
		else:
			self._motivosFinDeRonda["BASTA"] += 1
			self._motivosFinDeRondaPorJugador[(self._juego.deQuiénEsTurno - 1) % self._juego.cantidadDeJugadores]["BASTA"] += 1
			if self._verbose:
				print("*************** Ronda terminada por basta ***************")
				for j in range(self._juego.cantidadDeJugadores):
					print(f"Jugador {j}: +{self._juego._estadosDeJugadores[j].puntajeDeRonda()} ({self._juego.puntajes[j]}/{self._juego.puntajeParaGanar})")					
				print("*********************************************************")
		
		self._calcularEstadísticasDeRonda()
		
		quiénArranca = self._juego._deQuiénEsTurno
		manos = [deepcopy(self._juego._estadosDeJugadores[j].mano) for j in range(len(self._jugadores))]
		puntajesDeRonda = [ int(self._juego._estadosDeJugadores[j].puntajeDeRonda()) for j in range(len(self._jugadores))]
		for j in range(len(self._jugadores)):
			self._juego._deQuiénEsTurno = j
			self._jugadores[j].configurarFinDeRonda(manos, puntajesDeRonda)
		self._juego._deQuiénEsTurno = quiénArranca
		
		self._eventos = []
	
	def _calcularEstadísticasDeRonda(self):
		for j in range(len(self._jugadores)):
			# Cálculos auxiliares...
			cantidadDeCartasEnManoDeTipo = {tipo: 0 for tipo in Carta.Tipo}
			cantidadDeCartasEnZonaDeDúosDeTipo = {tipo: 0 for tipo in Carta.Tipo}
			cantidadDeDúosEnJuegoDeTipo = {
				Carta.Tipo.PEZ: 0,
				Carta.Tipo.BARCO: 0,
				Carta.Tipo.CANGREJO: 0,
				Carta.Tipo.NADADOR: 0    # noo maldito enum que no me deja poner nombres declarativos!
			}
			
			for claveDeCarta in self._juego._estadosDeJugadores[j].mano:
				cantidadDeCartasEnManoDeTipo[claveDeCarta.tipo] += self._juego._estadosDeJugadores[j].mano[claveDeCarta]
			
			for claveDeDúo in self._juego._estadosDeJugadores[j].zonaDeDúos:
				cantidadDeDúosEnJuegoDeTipo[claveDeDúo[0].tipo] += self._juego._estadosDeJugadores[j].zonaDeDúos[claveDeDúo]
				cantidadDeCartasEnZonaDeDúosDeTipo[claveDeDúo[0].tipo] += self._juego._estadosDeJugadores[j].zonaDeDúos[claveDeDúo]
				cantidadDeCartasEnZonaDeDúosDeTipo[claveDeDúo[1].tipo] += self._juego._estadosDeJugadores[j].zonaDeDúos[claveDeDúo]
			
			
			# Calcular dúos en juego del jugador en esta ronda
			for tipoDúo in [Carta.Tipo.PEZ, Carta.Tipo.BARCO, Carta.Tipo.CANGREJO, Carta.Tipo.NADADOR]:
				self._dúosJugadosPorTipoPorJugador[tipoDúo][j] += cantidadDeDúosEnJuegoDeTipo[tipoDúo]
			
			# Calcular dúos en mano del jugador en esta ronda
			self._dúosEnManoPorTipoPorJugador[Carta.Tipo.PEZ][j] += cantidadDeCartasEnManoDeTipo[Carta.Tipo.PEZ] // 2
			self._dúosEnManoPorTipoPorJugador[Carta.Tipo.BARCO][j] += cantidadDeCartasEnManoDeTipo[Carta.Tipo.BARCO] // 2
			self._dúosEnManoPorTipoPorJugador[Carta.Tipo.CANGREJO][j] += cantidadDeCartasEnManoDeTipo[Carta.Tipo.CANGREJO] // 2
			self._dúosEnManoPorTipoPorJugador[Carta.Tipo.NADADOR][j] += min(cantidadDeCartasEnManoDeTipo[Carta.Tipo.NADADOR], cantidadDeCartasEnManoDeTipo[Carta.Tipo.TIBURÓN])
			
			# Calcular cartas poseídas de cada tipo en esta ronda
			for tipo in Carta.Tipo:
				self._cantidadDeCartasPorTipoPorJugador[tipo][j] += cantidadDeCartasEnManoDeTipo[tipo] + cantidadDeCartasEnZonaDeDúosDeTipo[tipo]
	
if __name__ == '__main__':
	administrador = AdministradorDeJuego([RandyBot, RandyBot], verbose=True)
	ganador = administrador.jugarPartida()
	print(f"Ganador: {ganador}")
