from enum import Enum, auto

class Acción():
	class Robo(Enum):
		DEL_MAZO = auto()
		DEL_DESCARTE_0 = auto()
		DEL_DESCARTE_1 = auto()
	
	class Dúos(Enum):
		JUGAR_PECES = auto()
		JUGAR_BARCOS = auto()
		JUGAR_CANGREJOS = auto()
		JUGAR_NADADOR_Y_TIBURÓN = auto()
		NO_JUGAR = auto()
	
	class FinDeRonda(Enum):
		PASAR_TURNO = auto()
		DECIR_BASTA = auto()
		DECIR_ÚLTIMA_CHANCE = auto()
			