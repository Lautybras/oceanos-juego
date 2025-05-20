import pytest
from collections import Counter as Multiset
from juego.carta import Carta
from juego.juego import PartidaDeOcéanos, JuegoException

def test_SiNoSeRobó_NoSePuedeDecirÚltimaChance():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirÚltimaChance()
	
	assert "No se puede terminar el turno sin antes haber robado" in str(excepcion.value)

def test_SiNoSeTienenSietePuntos_NoSePuedeDecirÚltimaChance():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirÚltimaChance()
	
	assert "No se puede terminar la ronda si no se tienen al menos siete puntos" in str(excepcion.value)
	
def test_SiSeTienenAlMenosSietePuntosYSeRobó_AlDecirÚltimaChance_ElTurnoTerminaYLaRondaContinúa():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	
	juego.decirÚltimaChance()
	
	assert juego.rondaEnCurso() == True
	assert juego._deQuiénEsTurno == 1

def test_SiSeTienenAlMenosSietePuntosYSeRobó_AlDecirÚltimaChance_ElSiguienteJugadorPuedeJugarUnTurnoCompleto():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)] += 2
	juego.decirÚltimaChance()
	
	juego.robarDelDescarte(1)
	juego.jugarDuoDePeces(Multiset([
		Carta(Carta.Tipo.PEZ, Carta.Color.AZUL),Carta(Carta.Tipo.PEZ, Carta.Color.AZUL)
	]))
	juego.pasarTurno()
	
	
	assert juego._estadosDeJugadores[0].mano.total() == 5
	assert juego._estadosDeJugadores[1].mano.total() == 2
	assert juego._estadosDeJugadores[1].zonaDeDuos.total() == 1

def test_SiSeDijoÚltimaChance_SiJuegaElSiguienteJugador_LaManoDelJugadorOriginalPuedeSerRobada():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego._estadosDeJugadores[0].mano.clear()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.NARANJA_CLARO)] += 1
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.ROSA)] += 1
	
	cartaRobada = juego.jugarDuoDeNadadorYTiburón(Multiset([
		Carta(Carta.Tipo.TIBURON, Carta.Color.NARANJA_CLARO),
		Carta(Carta.Tipo.NADADOR, Carta.Color.ROSA)
	]), 0)
	
	assert cartaRobada == Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)
	assert cartaRobada in juego._estadosDeJugadores[1].mano
	assert juego._estadosDeJugadores[0].mano == Multiset([cartaRobada, cartaRobada, cartaRobada])
	assert juego._estadosDeJugadores[1].mano.total() == 2
	assert juego._estadosDeJugadores[1].zonaDeDuos.total() == 1
	assert juego._deQuiénEsTurno == 1

def test_SiSeDijoÚltimaChance_AlJugarUnTurnoCompletoElSiguienteJugador_SuManoNoPuedeSerRobada():
	juego = PartidaDeOcéanos(cantidadDeJugadores=3)
	juego.iniciarRonda()
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego.pasarTurno()
	
	juego.robarDelMazo()
	juego.elegirRoboDelMazo(0,0)
	juego._estadosDeJugadores[2].mano[Carta(Carta.Tipo.TIBURON, Carta.Color.NARANJA_CLARO)] += 1
	juego._estadosDeJugadores[2].mano[Carta(Carta.Tipo.NADADOR, Carta.Color.ROSA)] += 1
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeNadadorYTiburón(Multiset([
			Carta(Carta.Tipo.TIBURON, Carta.Color.NARANJA_CLARO),
			Carta(Carta.Tipo.NADADOR, Carta.Color.ROSA)
		]), 1)
	
	assert "La selección de jugador a robar con el dúo de nadador y tiburón es inválida" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_LaRondaTermina():
	
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	assert juego.rondaEnCurso() == False


def test_SiSeDijoÚltimaChance_NoSePuedeDecirBasta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA)] += 5
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirBasta()
	
	assert "Ya se está jugando una ronda de última chance" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_NoSePuedeDecirÚltimaChance():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego._estadosDeJugadores[1].mano[Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA)] += 5
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirÚltimaChance()
	
	assert "Ya se está jugando una ronda de última chance" in str(excepcion.value)




def test_SiElJugadorQueDijoÚltimaChanceTieneElMayorPuntajeDeRonda_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_ElJugadorQueDijoÚltimaChanceObtieneSuPuntajeMásBonificaciónPorColorYElRestoDeJugadoresSoloObtienenSuBonificaciónPorColor():
	
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano.clear()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego._estadosDeJugadores[1].mano.clear()
	juego._estadosDeJugadores[1].mano = Multiset([
		Carta(Carta.Tipo.CONCHA, Carta.Color.ROSA),
		Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA),
		Carta(Carta.Tipo.CONCHA, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.BARCO, Carta.Color.AMARILLO)
	])
	puntajesDeRonda = (juego._estadosDeJugadores[0].puntajeDeRonda(), juego._estadosDeJugadores[1].puntajeDeRonda())
	
	juego.pasarTurno()
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajes[0] == puntajesDeRonda[0] + 4
	assert juego.puntajes[1] == 2

def test_SiElJugadorQueDijoÚltimaChanceNoTieneElMayorPuntajeDeRonda_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_ElJugadorQueDijoÚltimaChanceSoloObtieneSuBonificaciónPorColorYElRestoDeJugadoresObtienenSuPuntaje():
	
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano.clear()
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego._estadosDeJugadores[1].mano.clear()
	juego._estadosDeJugadores[1].mano = Multiset([
		Carta(Carta.Tipo.CONCHA, Carta.Color.ROSA),
		Carta(Carta.Tipo.CONCHA, Carta.Color.NARANJA),
		Carta(Carta.Tipo.CONCHA, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.CONCHA, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.CONCHA, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.PINGUINO, Carta.Color.AMARILLO),
		Carta(Carta.Tipo.PINGUINO, Carta.Color.AMARILLO)
	])
	puntajesDeRonda = (juego._estadosDeJugadores[0].puntajeDeRonda(), juego._estadosDeJugadores[1].puntajeDeRonda())
	
	juego.pasarTurno()
	
	assert juego.rondaEnCurso() == False
	assert juego.puntajes[0] == 4
	assert juego.puntajes[1] == puntajesDeRonda[1]





def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedeRobarDelDescarte():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelDescarte(1)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedeRobarDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.robarDelMazo()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedeElegirRoboDelMazo():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.elegirRoboDelMazo(0,0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)
	
def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedeJugarDúoDePeces():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDePeces(Multiset())
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedeJugarDúoDeBarcos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeBarcos(Multiset())
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedeJugarDúoDeCangrejos():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeCangrejos(Multiset(), 0, 0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedeJugarDuoDeNadadorYTiburón():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.jugarDuoDeNadadorYTiburón(Multiset(), 0)
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedePasarTurno():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.pasarTurno()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedeDecirBasta():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirBasta()
	
	assert "No hay una ronda en curso" in str(excepcion.value)

def test_SiSeDijoÚltimaChance_AlVolverASerTurnoDelJugadorQueDijoÚltimaChance_NoSePuedeDecirÚltimaChance():
	juego = PartidaDeOcéanos(cantidadDeJugadores=2)
	juego.iniciarRonda()
	juego.robarDelDescarte(0)
	juego._estadosDeJugadores[0].mano[Carta(Carta.Tipo.PULPO, Carta.Color.GRIS)] += 4
	juego.decirÚltimaChance()
	juego.robarDelDescarte(1)
	juego.pasarTurno()
	
	with pytest.raises(JuegoException) as excepcion:
		juego.decirÚltimaChance()
	
	assert "No hay una ronda en curso" in str(excepcion.value)
