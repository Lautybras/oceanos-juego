import { useState } from 'react';
import './App.css';
import Carta from './components/Carta';
import ZonaJugador from './components/ZonaJugador';
import ZonaMazo from './components/ZonaMazo';

let Esturno = 1

function App() {
  
  return (
    <div className="grid grid-cols-3 grid-rows-3 gap-4 min-h-screen p-4 bg-gray-100">
      {/* Posición 1 */}
      <div></div>

      {/* Posición 2 */}
     
      <ZonaJugador posicion="arriba" jugador="2" turno = {Esturno} >
        <Carta tipo="BARCO" color="NEGRO" modo = "movil"/>
      </ZonaJugador>

      {/* Posición 3 */}
      <div></div>

      {/* Posición 4 */}
      <div className="bg-purple-500 text-white flex justify-center items-center">
        04
      </div>

      {/* Posición 5 */}
      <div>
        <ZonaMazo>
         
        </ZonaMazo>
      </div>

      {/* Posición 6 */}
      <div className="bg-purple-500 text-white flex justify-center items-center">
        06
      </div>

      {/* Posición 7 */}
      <div></div>

      {/* Posición 8 */}

      <ZonaJugador posicion="abajo" jugador="1" turno = {Esturno}>
        <Carta tipo="BARCO" color="NEGRO" modo = "movil"/>
      </ZonaJugador>


      {/* Posición 9 */}
      <div>
        <button>Pasar</button>
        <div>
          <button>Basta</button>
          <button>Última chance</button>
        </div>
        <p>Puntaje actual : 20</p>
      </div>
    </div>
  );
}

export default App;
