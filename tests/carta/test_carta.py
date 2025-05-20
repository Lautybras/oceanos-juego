import pytest
from juego.carta import Carta, CartaInvalidaException

def test_SePuedeCrearCartaDeAnclaBlanca():
	carta = Carta(tipo=Carta.Tipo.ANCLA, color=Carta.Color.BLANCO)
	
	assert carta.tipo == Carta.Tipo.ANCLA
	assert carta.color == Carta.Color.BLANCO

def test_NoSePuedeCrearCartaSinTipo():
	with pytest.raises(CartaInvalidaException):
		carta = Carta(tipo=None, color=Carta.Color.BLANCO)

def test_NoSePuedeCrearCartaSinColor():
	with pytest.raises(CartaInvalidaException):
		carta = Carta(tipo=None, color=Carta.Color.BLANCO)
		
def test_NoSePuedeCrearCartaConTipoQueNoEsClaseTipo():
	with pytest.raises(CartaInvalidaException):
		carta = Carta(tipo='Ancla', color=Carta.Color.BLANCO)

def test_NoSePuedeCrearCartaConColorQueNoEsClaseColor():
	with pytest.raises(CartaInvalidaException):
		carta = Carta(tipo=Carta.Tipo.ANCLA, color='Blanco')

def test_CartasDúo_SabenQueSonDúo():
	assert Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO).esDúo() == True
	assert Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO).esDúo() == True
	assert Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO).esDúo() == True
	assert Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO).esDúo() == True
	assert Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO).esDúo() == True

def test_CartasNoDúo_SabenQueNoSonDúo():
	assert Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO).esDúo() == False
	assert Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO).esDúo() == False
	assert Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO).esDúo() == False
	assert Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO).esDúo() == False
	assert Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO).esDúo() == False
	assert Carta(Carta.Tipo.FARO, Carta.Color.BLANCO).esDúo() == False
	assert Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO).esDúo() == False
	assert Carta(Carta.Tipo.CAPITÁN, Carta.Color.BLANCO).esDúo() == False
	assert Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO).esDúo() == False

def test_CartasColeccionables_SabenQueSonColeccionables():
	assert Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO).esColeccionable() == True
	assert Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO).esColeccionable() == True
	assert Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO).esColeccionable() == True
	assert Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO).esColeccionable() == True

def test_CartasNoColeccionables_SabenQueNoSonColeccionables():
	assert Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.FARO, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.CAPITÁN, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO).esColeccionable() == False

def test_CartasMultiplicador_SabenQueSonMultiplicador():
	assert Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO).esMultiplicador() == True
	assert Carta(Carta.Tipo.FARO, Carta.Color.BLANCO).esMultiplicador() == True
	assert Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO).esMultiplicador() == True
	assert Carta(Carta.Tipo.CAPITÁN, Carta.Color.BLANCO).esMultiplicador() == True

def test_CartasNoMultiplicador_SabenQueNoSonMultiplicador():
	assert Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.TIBURÓN, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO).esMultiplicador() == False
	