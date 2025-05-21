class JuegoInvalidoException(Exception):
	def __init__(self, message="Se intentó crear un juego con atributos inválidos"):
		super().__init__(message)

class JuegoException(Exception):
	def __init__(self, message="Ha ocurrido alguna violacion a las reglas del juego"):
		super().__init__(message)
