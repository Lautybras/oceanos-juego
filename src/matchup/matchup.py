import matplotlib.pyplot as plt
import numpy as np
from juego.carta import Carta, apodosCartas
from jugador.RandyBot.randy import RandyBot
from jugador.PuntosBot.puntosbot_mk1 import PuntosBotMk1
from jugador.SirenaTeam.sirena_enjoyer import SirenaEnjoyer
from jugador.SirenaTeam.sirena_hater import SirenaHater
from administrador.administrador_de_juego import AdministradorDeJuego

#* vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#* vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#* vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#* vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#* vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
jugadoresDelMatchup = [
	PuntosBotMk1,
	SirenaHater,
	SirenaEnjoyer,
	RandyBot
]
nombres = [
	"PuntosBotMk1",
	"SirenaHater",
	"SirenaEnjoyer",
	"RandyBot"
]
cantidadDePartidasAJugar = 100
#* ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#* ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#* ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#* ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#* ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# =================================================== ¡¡¡¡¡MATCHUP!!!!! ===================================================
cantidadJugadores = len(jugadoresDelMatchup)
administrador = AdministradorDeJuego(jugadoresDelMatchup, verbosidad=AdministradorDeJuego.Verbosidad.NADA)


for decimo in range(1, 11):
	for _ in range(cantidadDePartidasAJugar // 10):
		administrador.jugarPartida()
	print(f"{decimo * 10}% de las {cantidadDePartidasAJugar} partidas disputadas{'...' if decimo < 10 else '!'}")

# ======================================================== GANADOR ========================================================
ganador = np.argmax(administrador._partidasGanadasPorJugador)
print("EL GANADOR ES...")
print("v" * 119)
print("v" * 119)
print("v" * 119)
print("v" * 119)
print("v" * 119)
print((">" * ((117 - len(nombres[ganador])) // 2)) + " " + nombres[ganador] + " " + ("<" * ((117 - len(nombres[ganador])) // 2 + int(len(nombres[ganador]) % 2 == 0 ))))
print("^" * 119)
print("^" * 119)
print("^" * 119)
print("^" * 119)
print("^" * 119)


# =============================================== Preprocesamiento de datos ===============================================
for j in range(cantidadJugadores):
	for e in administrador._dúosJugadosPorJugadorPorTipo[j]:
		administrador._dúosJugadosPorJugadorPorTipo[j][e] = administrador._dúosJugadosPorJugadorPorTipo[j][e] / administrador._rondasTerminadas
	
	for e in administrador._dúosEnManoPorJugadorPorTipo[j]:
		administrador._dúosEnManoPorJugadorPorTipo[j][e] = administrador._dúosEnManoPorJugadorPorTipo[j][e] / administrador._rondasTerminadas
	
	for e in administrador._cantidadDeCartasPorJugadorPorTipo[j]:
		administrador._cantidadDeCartasPorJugadorPorTipo[j][e] = administrador._cantidadDeCartasPorJugadorPorTipo[j][e] / administrador._rondasTerminadas

# =================================================== Preparación Gráficos ===================================================
fig, ((ax_motivosFinDeRonda, ax_partidasGanadas, ax_puntosPorJugador), (ax_motivosFinDeRondaJugadorCero, ax_motivosFinDeRondaJugadorUno, ax_dúosPorRonda), (ax_motivosFinDeRondaJugadorDos, ax_motivosFinDeRondaJugadorTres, ax_cartasPorTipo)) = plt.subplots(3, 3)
fig.suptitle('Estadísticas del Matchup')
fig.tight_layout()

colors = ['red', 'mediumseagreen', 'cornflowerblue', 'purple']
colors2 = ['orange', 'lime', 'darkturquoise', 'violet']
labelsMotivosFinDeRonda = ["Mazo vacío", "Basta", "Cuatro sirenas", "Última chance"]
coloresMotivosFinDeRonda = ["lightsteelblue", "tan", "lightgrey", "deeppink"]
labelsMotivosFinDeRondaPorJugador = ["Basta", "Última chance ganada", "Última chance perdida", "Cuatro sirenas"]
coloresMotivosFinDeRondaPorJugador = ["tan", "seagreen", "orangered", "lightgrey"]
labelsPartidasGanadas = nombres
labelsDúos = ['Peces', 'Barcos', 'Cangrejos', 'Ndrs&Tbns']
labelsTiposCartas = [ apodosCartas[t] for t in Carta.Tipo ]
width = None
preOff = None
if cantidadJugadores == 2:
	width = 0.25
	preOff = 0.125
elif cantidadJugadores == 3:
	width = 0.25
	preOff = 0.05
elif cantidadJugadores == 4:
	width = 0.20
	preOff = 0.025

# =================================================== Motivos Fin de Ronda ===================================================
my_pie, texts, pct_txts = ax_motivosFinDeRonda.pie(administrador._motivosFinDeRonda.values(), labels=labelsMotivosFinDeRonda, autopct='%1.1f%%', colors=coloresMotivosFinDeRonda)
ax_motivosFinDeRonda.title.set_text("Motivos Fin de Ronda")

# ================================================= Distribución de Victorias ================================================
ax_partidasGanadas.pie(administrador._partidasGanadasPorJugador, labels=labelsPartidasGanadas, autopct='%1.1f%%', colors=colors)
ax_partidasGanadas.title.set_text("Distribución de Victorias")

# ============================================== Distribución de Puntos por Ronda ============================================
for j in range(cantidadJugadores):
	counts, bins = np.histogram(administrador._puntosPorJugadorPorRonda[j], bins=np.arange(20))
	ax_puntosPorJugador.stairs(counts, bins, color=colors[j])
ax_puntosPorJugador.title.set_text("Distribución de Puntos por Ronda")

# ============================================ Motivos Fin de Ronda (Por Jugador) ============================================
ax_motivosFinDeRondaJugadorCero.pie(administrador._motivosFinDeRondaPorJugador[0].values(), labels=labelsMotivosFinDeRondaPorJugador, autopct='%1.1f%%', colors=coloresMotivosFinDeRondaPorJugador)
ax_motivosFinDeRondaJugadorCero.title.set_text(f"Motivos Fin de Ronda ({nombres[0]})")


if max(administrador._motivosFinDeRondaPorJugador[1].values()) > 0:
	ax_motivosFinDeRondaJugadorUno.pie(administrador._motivosFinDeRondaPorJugador[1].values(), labels=labelsMotivosFinDeRondaPorJugador, autopct='%1.1f%%', colors=coloresMotivosFinDeRondaPorJugador)
	ax_motivosFinDeRondaJugadorUno.title.set_text(f"Motivos Fin de Ronda ({nombres[1]})")
else:
	ax_motivosFinDeRondaJugadorUno.text(0.5, 0.5, "No disponible", ha="center", va="center", transform=ax_motivosFinDeRondaJugadorUno.transAxes)
	ax_motivosFinDeRondaJugadorUno.set_xticks([])
	ax_motivosFinDeRondaJugadorUno.set_yticks([])
	ax_motivosFinDeRondaJugadorUno.spines['top'].set_visible(False)
	ax_motivosFinDeRondaJugadorUno.spines['right'].set_visible(False)
	ax_motivosFinDeRondaJugadorUno.spines['bottom'].set_visible(False)
	ax_motivosFinDeRondaJugadorUno.spines['left'].set_visible(False)
	ax_motivosFinDeRondaJugadorUno.title.set_text(f"Motivos Fin de Ronda ({nombres[1]})")


if cantidadJugadores >= 3 and max(administrador._motivosFinDeRondaPorJugador[2].values()) > 0:
	ax_motivosFinDeRondaJugadorDos.pie(administrador._motivosFinDeRondaPorJugador[2].values(), labels=labelsMotivosFinDeRondaPorJugador, autopct='%1.1f%%', colors=coloresMotivosFinDeRondaPorJugador)
	ax_motivosFinDeRondaJugadorDos.title.set_text(f"Motivos Fin de Ronda ({nombres[2]})")
else:
	ax_motivosFinDeRondaJugadorDos.text(0.5, 0.5, "No disponible", ha="center", va="center", transform=ax_motivosFinDeRondaJugadorDos.transAxes)
	ax_motivosFinDeRondaJugadorDos.set_xticks([])
	ax_motivosFinDeRondaJugadorDos.set_yticks([])
	ax_motivosFinDeRondaJugadorDos.spines['top'].set_visible(False)
	ax_motivosFinDeRondaJugadorDos.spines['right'].set_visible(False)
	ax_motivosFinDeRondaJugadorDos.spines['bottom'].set_visible(False)
	ax_motivosFinDeRondaJugadorDos.spines['left'].set_visible(False)
	ax_motivosFinDeRondaJugadorDos.title.set_text(f"Motivos Fin de Ronda (Jugador 2)")

if cantidadJugadores == 4 and max(administrador._motivosFinDeRondaPorJugador[3].values()) > 0:
	ax_motivosFinDeRondaJugadorTres.pie(administrador._motivosFinDeRondaPorJugador[3].values(), labels=labelsMotivosFinDeRondaPorJugador, autopct='%1.1f%%', colors=coloresMotivosFinDeRondaPorJugador)
	ax_motivosFinDeRondaJugadorTres.title.set_text(f"Motivos Fin de Ronda ({nombres[3]})")
else:
	ax_motivosFinDeRondaJugadorTres.text(0.5, 0.5, "No disponible", ha="center", va="center", transform=ax_motivosFinDeRondaJugadorTres.transAxes)
	ax_motivosFinDeRondaJugadorTres.set_xticks([])
	ax_motivosFinDeRondaJugadorTres.set_yticks([])
	ax_motivosFinDeRondaJugadorTres.spines['top'].set_visible(False)
	ax_motivosFinDeRondaJugadorTres.spines['right'].set_visible(False)
	ax_motivosFinDeRondaJugadorTres.spines['bottom'].set_visible(False)
	ax_motivosFinDeRondaJugadorTres.spines['left'].set_visible(False)
	ax_motivosFinDeRondaJugadorTres.title.set_text(f"Motivos Fin de Ronda (Jugador 3)")

# ============================================ Promedio de Dúos Jugados por Ronda ============================================
x = np.arange(len(labelsDúos))

for j in range(cantidadJugadores):
	multiplier = j
	attribute = f"Jugador {j}"
	measurement = administrador._dúosJugadosPorJugadorPorTipo[j].values()
	#print(attribute)
	#print(measurement)
	offset = width * multiplier
	rects = ax_dúosPorRonda.bar(x + offset, measurement, width, label=attribute, color=colors[j])
	ax_dúosPorRonda.bar_label(rects, label_type="center", fmt="{:.2f}")
for j in range(cantidadJugadores):
	multiplier = j
	attribute = f"Jugador {j}"
	measurement = administrador._dúosEnManoPorJugadorPorTipo[j].values()
	#print(attribute)
	#print(measurement)
	offset = width * multiplier
	#print(list(administrador._dúosJugadosPorJugadorPorTipo[j].values()))
	rects = ax_dúosPorRonda.bar(x + offset, measurement, width, label=attribute, bottom=list(administrador._dúosJugadosPorJugadorPorTipo[j].values()), color=colors2[j], hatch='//')
	ax_dúosPorRonda.bar_label(rects, label_type="center", fmt="{:.2f}")
ax_dúosPorRonda.set_title('Promedio de Dúos Jugados por Ronda')
ax_dúosPorRonda.set_xticks(x + width - preOff, labelsDúos)

# =============================================== Promedio de Cartas por Ronda ===============================================
x = np.arange(len(labelsTiposCartas))

for j in range(cantidadJugadores):
	multiplier = j
	attribute = f"Jugador {j}"
	measurement = administrador._cantidadDeCartasPorJugadorPorTipo[j].values()
	#print(attribute)
	#print(measurement)
	offset = width * multiplier
	rects = ax_cartasPorTipo.bar(x + offset, measurement, width, label=attribute, color=colors[j])
	#ax_cartasPorTipo.bar_label(rects, label_type="center")

ax_cartasPorTipo.set_title('Promedio de Cartas por Ronda')
ax_cartasPorTipo.set_xticks(x + width - preOff, labelsTiposCartas)
#ax_cartasPorTipo.legend(loc='upper left', ncols=3)


# ===================================================== Mostrar Gráficos =====================================================
plt.show()