import { useState } from 'react';
import './App.css';
import Carta from './components/Carta';
import ZonaJugador from './components/ZonaJugador';
import ZonaMazo from './components/ZonaMazo';
import Controles from './components/Controles';


let Esturno = 1;
const fases = ["inicio","elegirCarta","jugarDuo", "pasarODecirBasta"];
let fase = fases[1];

let cTipo = "BARCO"
let cColor = "NEGRO"

function App() {
  const [mazos, setMazos] = useState({
    1: [],
    2: [],
    3: [],
    4: [],
    D1: [],
    D2: []
  });

  const agregarCarta = (cant = 1,jugadorId,cTipo,cColor) => {
    for (let i = 0; i < cant; i++) {
      const nuevaCarta = {
      tipo: cTipo,
      color: cColor,
      id: Date.now(),
    };
    setMazos((prev) => ({
      ...prev,
      [jugadorId]: [...prev[jugadorId], nuevaCarta],
    }));
    }

  };

  const robarDecarte = (mazo) => {
    
    return 1;
  }

  return (
    <div className="grid grid-cols-3 grid-rows-3 gap-4 min-h-screen p-4 bg-gray-100">
      {/* Posición 1: */}
      <Controles jugador = "4"></Controles>


      {/* Posición 2: jugador arriba */}
      <ZonaJugador posicion="arriba" jugador="2" turno={Esturno}>
        {mazos[2].map((carta) => (
          <Carta key={carta.id} {...carta} modo="movil" />
        ))}
      </ZonaJugador>

      {/* Posición 3:  */}
      <Controles jugador = "3"></Controles>



      {/* Posición 4: izq */}
      
      <ZonaJugador posicion="izq" jugador="4" turno={Esturno}>
        {mazos[4].map((carta) => (
          <Carta key={carta.id} {...carta} modo="movil" />
        ))}
      </ZonaJugador>
      {/* Posición 5: mazo con botón para agregar carta al jugador 1 por ahora */}
      <ZonaMazo mazos = {mazos} fase={fase} turno={Esturno} onAgregar1Carta={() => agregarCarta(1,1,cTipo,cColor)} onAgregar2Cartas={() => agregarCarta(2,1,cTipo,cColor) } />

      {/* Posición 6: derecha */}
      <ZonaJugador posicion="der" jugador="3" turno={Esturno}>
        {mazos[3].map((carta) => (
          <Carta key={carta.id} {...carta} modo="movil" />
        ))}
      </ZonaJugador>

      {/* Posición 7: vacía */}
      <Controles jugador = "2"></Controles>


      {/* Posición 8: jugador abajo */}
      <ZonaJugador posicion="abajo" jugador="1" turno={Esturno}>
        {mazos[1].map((carta) => (
          <Carta key={carta.id} {...carta} modo="movil" />
        ))}
      </ZonaJugador>

      {/* Posición 9: controles */}
      <Controles jugador = "1"></Controles>


    </div>
  );
}

export default App;
