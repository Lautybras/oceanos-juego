import pytest
from juego.carta import Carta, CartaInvalidaException

def test_001_SePuedeCrearCartaDeAnclaBlanca():
	carta = Carta(tipo=Carta.Tipo.ANCLA, color=Carta.Color.BLANCO)
	
	assert carta.tipo == Carta.Tipo.ANCLA
	assert carta.color == Carta.Color.BLANCO

def test_002_NoSePuedeCrearCartaSinTipo():
	with pytest.raises(CartaInvalidaException):
		carta = Carta(tipo=None, color=Carta.Color.BLANCO)

def test_003_NoSePuedeCrearCartaSinColor():
	with pytest.raises(CartaInvalidaException):
		carta = Carta(tipo=None, color=Carta.Color.BLANCO)
		
def test_004_NoSePuedeCrearCartaConTipoQueNoEsClaseTipo():
	with pytest.raises(CartaInvalidaException):
		carta = Carta(tipo='Ancla', color=Carta.Color.BLANCO)

def test_005_NoSePuedeCrearCartaConColorQueNoEsClaseColor():
	with pytest.raises(CartaInvalidaException):
		carta = Carta(tipo=Carta.Tipo.ANCLA, color='Blanco')

def test_006_CartasDuo_SabenQueSonDuo():
	assert Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO).esDuo() == True
	assert Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO).esDuo() == True
	assert Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO).esDuo() == True
	assert Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO).esDuo() == True
	assert Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO).esDuo() == True

def test_007_CartasNoDuo_SabenQueNoSonDuo():
	assert Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO).esDuo() == False
	assert Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO).esDuo() == False
	assert Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO).esDuo() == False
	assert Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO).esDuo() == False
	assert Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO).esDuo() == False
	assert Carta(Carta.Tipo.FARO, Carta.Color.BLANCO).esDuo() == False
	assert Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO).esDuo() == False
	assert Carta(Carta.Tipo.CAPITAN, Carta.Color.BLANCO).esDuo() == False
	assert Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO).esDuo() == False

def test_008_CartasColeccionables_SabenQueSonColeccionables():
	assert Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO).esColeccionable() == True
	assert Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO).esColeccionable() == True
	assert Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO).esColeccionable() == True
	assert Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO).esColeccionable() == True

def test_009_CartasNoColeccionables_SabenQueNoSonColeccionables():
	assert Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.FARO, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.CAPITAN, Carta.Color.BLANCO).esColeccionable() == False
	assert Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO).esColeccionable() == False

def test_010_CartasMultiplicador_SabenQueSonMultiplicador():
	assert Carta(Carta.Tipo.COLONIA, Carta.Color.BLANCO).esMultiplicador() == True
	assert Carta(Carta.Tipo.FARO, Carta.Color.BLANCO).esMultiplicador() == True
	assert Carta(Carta.Tipo.CARDUMEN, Carta.Color.BLANCO).esMultiplicador() == True
	assert Carta(Carta.Tipo.CAPITAN, Carta.Color.BLANCO).esMultiplicador() == True

def test_011_CartasNoMultiplicador_SabenQueNoSonMultiplicador():
	assert Carta(Carta.Tipo.CONCHA, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.PULPO, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.PINGUINO, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.ANCLA, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.CANGREJO, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.BARCO, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.PEZ, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.NADADOR, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.TIBURON, Carta.Color.BLANCO).esMultiplicador() == False
	assert Carta(Carta.Tipo.SIRENA, Carta.Color.BLANCO).esMultiplicador() == False
	