import React, { useRef, useEffect, useState } from "react";
import IMG from "../assets/cartas.png";

const margenX = 16;
const margenY = 20;

const offsetBlanco = 20

const anchoCarta = 676 + offsetBlanco *2;
const altoCarta = 967 + offsetBlanco *2
// const altoCarta = 1000 + 20;
const radioBorde = 30;


const espacioX = 30;
// const espacioY = 20;
const espacioY = 33



function filaCarta(tipo, color) {
  return 0
}

function colCarta(tipo, color) {
  return 0
}

function Carta({ tipo, color }) {
  const col = colCarta(tipo, color);
  const fila = filaCarta(tipo, color);

  const offsetX = margenX + col * (anchoCarta + espacioX);
  const offsetY = margenY + fila * (altoCarta + espacioY);

  const [pos, setPos] = useState({ x: 100, y: 100 });
  const posRef = useRef({ x: 100, y: 100 });

  const velocityRef = useRef({ x: 0, y: 0 });
  const draggingRef = useRef(false);
  const offsetRef = useRef({ x: 0, y: 0 });

  const animationRef = useRef(null);

  // Para escala responsiva opcional
  const scale = Math.min(window.innerWidth / 3000, 1);

  // Referencia al contenedor tablero
  const contenedorRef = useRef(null);

  // Función para limitar posición dentro del contenedor
  const limitarPosicion = (x, y) => {
    if (!contenedorRef.current) return { x, y };

    const contenedorRect = contenedorRef.current.getBoundingClientRect();

    // Limites en base a contenedor y tamaño carta escalada
    const maxX = contenedorRect.width - anchoCarta * scale;
    const maxY = contenedorRect.height - altoCarta * scale;

    let nx = x;
    let ny = y;

    if (nx < 0) nx = 0;
    else if (nx > maxX) nx = maxX;

    if (ny < 0) ny = 0;
    else if (ny > maxY) ny = maxY;

    return { x: nx, y: ny };
  };

  const updatePosition = (newPos) => {
    // Limitar posición aquí
    const limitedPos = limitarPosicion(newPos.x, newPos.y);
    posRef.current = limitedPos;
    setPos(limitedPos);
  };

  const handleMouseDown = (e) => {
    draggingRef.current = true;
    offsetRef.current = {
      x: e.clientX - posRef.current.x,
      y: e.clientY - posRef.current.y,
    };
    cancelAnimationFrame(animationRef.current);
  };

  const handleMouseMove = (e) => {
    if (!draggingRef.current) return;

    const newX = e.clientX - offsetRef.current.x;
    const newY = e.clientY - offsetRef.current.y;

    velocityRef.current = {
      x: newX - posRef.current.x,
      y: newY - posRef.current.y,
    };

    updatePosition({ x: newX, y: newY });
  };

  const handleMouseUp = () => {
    draggingRef.current = false;
    applyInertia();
  };

  const applyInertia = () => {
    const friction = 0.92;

    const step = () => {
      velocityRef.current.x *= friction;
      velocityRef.current.y *= friction;

      const speed =
        Math.abs(velocityRef.current.x) + Math.abs(velocityRef.current.y);

      if (speed < 0.5) return; // Detener cuando sea lento

      let newX = posRef.current.x + velocityRef.current.x;
      let newY = posRef.current.y + velocityRef.current.y;

      // Limitar posición para que no salga
      const limitedPos = limitarPosicion(newX, newY);
      newX = limitedPos.x;
      newY = limitedPos.y;

      // Si tocamos bordes, invertir velocidad para "rebotar" (opcional)
      if (newX === 0 || newX === (contenedorRef.current.getBoundingClientRect().width - anchoCarta * scale)) {
        velocityRef.current.x *= -0.1;
      }
      if (newY === 0 || newY === (contenedorRef.current.getBoundingClientRect().height - altoCarta * scale)) {
        velocityRef.current.y *= -0.2;
      }

      updatePosition({ x: newX, y: newY });
      animationRef.current = requestAnimationFrame(step);
    };

    animationRef.current = requestAnimationFrame(step);
  };

  useEffect(() => {
    window.addEventListener("mousemove", handleMouseMove);
    window.addEventListener("mouseup", handleMouseUp);

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("mouseup", handleMouseUp);
      cancelAnimationFrame(animationRef.current);
    };
  }, []);

  useEffect(() => {
    contenedorRef.current = document.getElementById("tablero");
  }, []);

  return (
    <div
      onMouseDown={handleMouseDown}
      style={{
        position: "absolute",
        top: `${pos.y}px`,
        left: `${pos.x}px`,
        width: `${anchoCarta}px`,
        height: `${altoCarta}px`,
        backgroundImage: `url(${IMG})`,
        backgroundPosition: `-${offsetX}px -${offsetY}px`,
        backgroundRepeat: "no-repeat",
        borderRadius: `${radioBorde}px`,
        border: "1px solid black",
        cursor: draggingRef.current ? "grabbing" : "grab",
        userSelect: "none",
        transform: `scale(${scale})`,
        transformOrigin: "top left",
        boxShadow: "0 4px 12px rgba(0,0,0,0.3)",
        transition: draggingRef.current ? "none" : "transform 0.1s",
      }}
      draggable={false}
    ></div>
  );
}

export default Carta;
