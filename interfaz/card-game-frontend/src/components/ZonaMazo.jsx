import React, { useRef, useEffect, useState } from "react";
import Carta from "./Carta";

export default function ZonaMazo() {
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
            width={150}   // tamaño fijo adecuado
            height={200}  // tamaño fijo adecuado
          />
    </div>

      {/* Contenedor descartes (ahora horizontal) */}
      <div className="flex flex-row gap-4 flex-1 h-full justify-center items-center relative">
        {[0, 1].map((_, idx) => (
        <div key={idx} className="relative w-[80px] h-[120px] pointer-events-none">
        <Carta
            tipo="BARCO"
            color="NEGRO"
            contenedorRef={contenedorRef}
            width={dimensiones.width}
            height={dimensiones.height}
        />
        </div>
        ))}
      </div>
    </div>
  );
}
