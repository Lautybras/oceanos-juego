import React, { useRef, useEffect, useState } from "react";
import Carta from "./Carta";

export default function ZonaMazo({mazos, fase, turno, onAgregar1Carta, onAgregar2Cartas, onRobarDescarte1, onRobarDescarte2}) {
  const contenedorRef = useRef(null);
  const [dimensiones, setDimensiones] = useState({ width: 0, height: 0 });

  useEffect(() => {
    if (contenedorRef.current) {
      const rect = contenedorRef.current.getBoundingClientRect();
      setDimensiones({ width: rect.width, height: rect.height });
    }
  }, []);

  return (
    <div
      className="flex items-center border-2 border-gray-700 p-4 gap-6 w-[600px] h-[200px] bg-gray-50"
      ref={contenedorRef}
    >
      {/* Mazo */}
      <div className="flex-1 border-2 border-dashed border-gray-500 min-w-[150px] h-full flex justify-center items-center relative">
        <Carta
          tipo="DECK"
          color="NULL"
          contenedorRef={contenedorRef}
          width={150}
          height={200}
        />
        
      </div>
        <button
          onClick={onAgregar2Cartas}
          className="mt-2 bg-blue-600 hover:bg-blue-800 text-white font-bold py-2 px-4 rounded shadow"
        >
          Robar 2 cartas
        </button>
        <button
          onClick={onAgregar1Carta}
          className="mt-2 bg-blue-600 hover:bg-blue-800 text-white font-bold py-2 px-4 rounded shadow"
        >
          Robar 1 carta
        </button>
      {/* Contenedor descartes */}
      <div className="flex flex-col items-center justify-center flex-1 h-full relative gap-2">
        <div className="flex flex-row gap-4">
          {[0, 1].map((_, idx) => (
            <div
              key={idx}
              className="relative w-[80px] h-[120px] pointer-events-none"
            >
              {mazos["D1"].map((carta) => (
          <Carta key={carta.id} {...carta} modo="movil" />
        ))}
            </div>
          ))}
        </div>


      </div>
    </div>
  );
}
