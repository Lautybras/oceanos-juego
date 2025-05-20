import React, { useRef, useEffect, useState } from "react";
import IMG from "../assets/cartas.png";

const IMG_WIDTH = 7450
const IMG_HEIGHT = 7280

const margenX = 16;
const margenY = 20;
const offsetBlanco = 20;
const anchoCarta = 674 + offsetBlanco * 2;
const altoCarta = 967 + offsetBlanco * 2;
const radioBorde = 30;
const espacioX = 31;
const espacioY = 33;

// Enums
const Colores = Object.freeze({
  AZUL: 0,
  CELESTE: 1,
  NEGRO: 2,
  AMARILLO: 3,
  VERDE: 4,
  BLANCO: 5,
  VIOLETA: 6,
  GRIS: 7,
  NARANJA_CLARO: 8,
  ROSA: 9,
  NARANJA: 10,
});

const Tipo = Object.freeze({
  CANGREJO: 0,
  BARCO: 1,
  PEZ: 2,
  NADADOR: 3,
  TIBURON: 4,
  CONCHA: 5,
  PULPO: 6,
  PINGUINO: 7,
  ANCLA: 8,
  COLONIA: 9,
  FARO: 10,
  CARDUMEN: 11,
  CAPITAN: 12,
  SIRENA: 13,
});

const cartas = {
  BARCO: {
    NEGRO: [0, 0],
    AZUL: [0, 5],
    AMARILLO: [1, 5],
    CELESTE: [1, 8],
    NEGRO_2: [2, 7],
    CELESTE_2: [2, 3],
    AZUL_2: [0, 8],
  },
  CANGREJO: {
    AZUL: [0, 2],
    GRIS: [0, 7],
    CELESTE: [2, 4],
  },
  PEZ: {
    NEGRO: [1, 6],
    CELESTE: [2, 0],
    AZUL: [2, 1],
    NEGRO_2: [2, 2],
    AZUL_2: [3, 1],
  },
  TIBURON: {
    VIOLETA: [2, 5],
    NEGRO: [2, 6],
  },
  NADADOR: {
    AZUL: [0, 6],
    AMARILLO: [1, 7],
    NARANJA_CLARO: [1, 9],
  },
  CONCHA: {
    VERDE: [0, 4],
    AZUL: [0, 9],
    AMARILLO: [2, 9],
  },
  PULPO: {
    VERDE: [0, 3],
    VIOLETA: [1, 4],
    GRIS: [3, 0],
  },
  PINGUINO: {
    NARANJA_CLARO: [1, 3],
  },
  ANCLA: {
    ROSA: [2, 8],
    NARANJA: [3, 2],
  },
  COLONIA: {
    VERDE: [3, 1],
  },
  FARO: {
    NEGRO: [2, 0],
    BLANCO: [2, 1],
  },
  CARDUMEN: {
    GRIS: [1, 1],
  },
  CAPITAN: {
    NEGRO: [2, 0],
    BLANCO: [2, 1],
  },
  SIRENA: {
    BLANCO: [1, 2],
  },
  DECK: {
    NULL: [6,9]
  }
};


function Carta({ tipo, color, width, height, modo = "fija", contenedorRef }) {
  const filaCol = cartas[tipo][color];
  const fila = filaCol[0];
  const col = filaCol[1];

  const offsetX = margenX + col * (anchoCarta + espacioX);
  const offsetY = margenY + fila * (altoCarta + espacioY);

  const scaleX = width / anchoCarta;
  const scaleY = height / altoCarta;
  const scale = Math.min(scaleX, scaleY, 1) * 0.3;

  const [pos, setPos] = useState({ x: 0, y: 0 });
  const draggingRef = useRef(false);
  const offsetRef = useRef({ x: 0, y: 0 });

  // Limita la posición para que la carta no salga del contenedor
  const limitarPosicion = (x, y) => {
    if (!contenedorRef?.current) return { x: Math.max(0, x), y: Math.max(0, y) };

    const rect = contenedorRef.current.getBoundingClientRect();

    // Tamaño visible del contenedor en "unidades carta sin escalar"
    const maxX = Math.max(0, rect.width / scale - anchoCarta);
    const maxY = Math.max(0, rect.height / scale - altoCarta);

    return {
      x: Math.min(Math.max(0, x), maxX),
      y: Math.min(Math.max(0, y), maxY),
    };
  };

  const handleMouseDown = (e) => {
    if (modo !== "movil") return;
    draggingRef.current = true;
    offsetRef.current = {
      x: e.clientX - pos.x * scale,
      y: e.clientY - pos.y * scale,
    };
    window.addEventListener("mousemove", handleMouseMove);
    window.addEventListener("mouseup", handleMouseUp);
  };

  const handleMouseMove = (e) => {
    if (!draggingRef.current) return;
    const newX = (e.clientX - offsetRef.current.x) / scale;
    const newY = (e.clientY - offsetRef.current.y) / scale;
    setPos(limitarPosicion(newX, newY));
  };

  const handleMouseUp = () => {
    draggingRef.current = false;
    window.removeEventListener("mousemove", handleMouseMove);
    window.removeEventListener("mouseup", handleMouseUp);
  };

  const estiloPosicion =
    modo === "movil"
      ? {
          position: "absolute",
          top: `${pos.y * scale}px`,
          left: `${pos.x * scale}px`,
          cursor: draggingRef.current ? "grabbing" : "grab",
          zIndex: 1000, // para que quede encima
        }
      : {
          position: "relative",
          cursor: "default",
          margin: "auto",
        };

  return (
    <div
      className="carta"
      onMouseDown={handleMouseDown}
      style={{
        ...estiloPosicion,
        width: `${anchoCarta * scale}px`,
        height: `${altoCarta * scale}px`,
        backgroundImage: `url(${IMG})`,
        backgroundPosition: `-${offsetX * scale}px -${offsetY * scale}px`,
        backgroundSize: `${IMG_WIDTH * scale}px ${IMG_HEIGHT * scale}px`,
        backgroundRepeat: "no-repeat",
        borderRadius: `${radioBorde * scale}px`,
        border: "1px solid black",
        boxShadow: "0 4px 12px rgba(0,0,0,0.3)",
        userSelect: "none",
        transition: modo === "fija" ? "transform 0.1s" : "none",
      }}
    />
  );
}

export default Carta;