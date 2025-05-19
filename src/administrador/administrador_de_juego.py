from .enums import Acción
from juego.juego import EstadoDelJuego
from bots.randy import RandyBot

def faseDeRobo():
	#* ============================ Fase de robo ============================
	acciónDeRobo = jugadores[juego.deQuienEsTurno].decidirAcciónDeRobo()
	
	if acciónDeRobo == Acción.Robo.DEL_MAZO:
		# Robar del mazo
		opcionesDeRobo = juego.robarDelMazo()
		(indiceDeCartaARobar, indiceDePilaDondeDescartar) = jugadores[juego.deQuienEsTurno].decidirCómoRobarDelMazo(opcionesDeRobo)
		cartaRobada = juego.elegirRoboDelMazo(indiceDeCartaARobar, indiceDePilaDondeDescartar)
		print(f"Roba del mazo una {cartaRobada}")
		
	elif acciónDeRobo == Acción.Robo.DEL_DESCARTE_0:
		cartaRobada = juego.robarDelDescarte(0)
		print(f"Roba del descarte 0 una {cartaRobada}")
	elif acciónDeRobo == Acción.Robo.DEL_DESCARTE_1:
		cartaRobada = juego.robarDelDescarte(1)
		print(f"Roba del descarte 1 una {cartaRobada}")
	else:
		#! ERROR
		raise Exception("Error")

def faseDeDúos():
	#* ============================ Fase de dúos ============================
	noSeQuierenJugarMásDúos = False
	
	while not noSeQuierenJugarMásDúos and not juego.haTerminado:
		(acciónDeDúos, cartasAJugar, parametrosDelDúo) = jugadores[juego.deQuienEsTurno].decidirAcciónDeDúos()
		if acciónDeDúos == Acción.Dúos.JUGAR_PECES:
			# Jugar dúo de peces
			cartaRobada = juego.jugarDuoDePeces(cartasAJugar)
			print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]} y roba una {cartaRobada}")
			
		elif acciónDeDúos == Acción.Dúos.JUGAR_BARCOS:
			# Jugar dúo de barcos
			print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]}")
			juego.jugarDuoDeBarcos(cartasAJugar)
			faseDeRobo()
			faseDeDúos()
			noSeQuierenJugarMásDúos = True
			
		elif acciónDeDúos == Acción.Dúos.JUGAR_CANGREJOS:
			# Jugar dúo de cangrejos
			(pilaDeDescarteARobar, indiceDeCartaARobar) = parametrosDelDúo
			cartaRobada = juego.jugarDuoDeCangrejos(cartasAJugar, pilaDeDescarteARobar, indiceDeCartaARobar)
			print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]} para robar una {cartaRobada}")
			
		elif acciónDeDúos == Acción.Dúos.JUGAR_NADADOR_Y_TIBURÓN:
			# Jugar dúo de nadador y tiburón
			jugadorARobar = parametrosDelDúo[0]
			cartaRobada = juego.jugarDuoDeNadadorYTiburón(cartasAJugar, jugadorARobar)
			print(f"Juega un dúo de {list(cartasAJugar.elements())[0]} y {list(cartasAJugar.elements())[1]} para robarle al jugador {jugadorARobar}, y roba una {cartaRobada}")
			
		elif acciónDeDúos == Acción.Dúos.NO_JUGAR:
			# No jugar dúos
			noSeQuierenJugarMásDúos = True
			print("No juega ningún dúo")
			
		else:
			#! ERROR
			raise Exception("Error")

def faseDeFin():
	#* ============================ Fase de fin de ronda ============================
	if juego.haTerminado:
		#* Cuatro sirenas!
		print("################### CUATRO SIRENAS ###################")
		print(f"Ganador: {juego.ganador}")
		for j in range(juego.cantidadDeJugadores):
			print(f"Jugador {j}: +{juego.estadoDelJugador[j].puntajeDeRonda()} ({juego.puntajesDeJuego[j]}/{juego.puntajeParaGanar()})")
		print("######################################################")
	else:
	
		acciónDeRobo = jugadores[juego.deQuienEsTurno].decidirAcciónDeFinDeRonda()

		if acciónDeRobo == Acción.FinDeRonda.PASAR_TURNO:
			# Pasar el turno normalmente
			juego.pasarTurno()
			print("Pasa de turno")
		elif acciónDeRobo == Acción.FinDeRonda.DECIR_BASTA:
			# Decir basta y terminar la ronda
			juego.decirBasta()
			print("¡¡¡Basta!!!")
		elif acciónDeRobo == Acción.FinDeRonda.DECIR_ÚLTIMA_CHANCE:
			# Decir última chance y pasar el turno
			juego.decirÚltimaChance()
			print("¡¡¡Última Chance!!!")
		else:
			#! ERROR
			raise Exception("Error")


juego = EstadoDelJuego(cantidadDeJugadores=2)
jugadores = [RandyBot(juego, 0), RandyBot(juego, 1)]

while not juego.haTerminado:
	juego.iniciarRonda()
	print("~~~~~~~~~~~~~~~~~~~~~ Inicia Ronda ~~~~~~~~~~~~~~~~~~~~~~")
	print(f"Jugador inicial: {juego.deQuienEsTurno}")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

	while juego.rondaEnCurso:
		print(f"~~~~~~~~~~~~~~~~~~~ Turno del jugador {juego.deQuienEsTurno} ~~~~~~~~~~~~~~~~~~~~")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print(f"El descarte 0 es {(juego.descarte[0])}")
		print(f"El descarte 1 es {(juego.descarte[1])}")
		
		faseDeRobo()
		faseDeDúos()
		faseDeFin()
	
	print("******************** Ronda terminada ********************")
	for j in range(juego.cantidadDeJugadores):
		print(f"Jugador {j}: +{juego.estadoDelJugador[j].puntajeDeRonda()} ({juego.puntajesDeJuego[j]}/{juego.puntajeParaGanar()})")
	print("*********************************************************")

print("!!!!!!!!!!!!!!!!!!! Partida Terminada !!!!!!!!!!!!!!!!!!!")
print(f"Ganador: {juego.ganador}")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")