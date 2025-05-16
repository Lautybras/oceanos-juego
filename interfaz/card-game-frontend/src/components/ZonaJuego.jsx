import React, { useRef, useEffect, useState } from "react";


function ZonaJuego({ children }) {
  return (
    <div
      id="tablero"
      style={{
        width: "100vw",   // ancho = 100% ventana
        height: "100vh",  // alto = 100% ventana
        position: "relative",
        overflow: "hidden",
        backgroundColor: "#0a0a0a", // opcional: para que se note
      }}
    >
      {children}
    </div>
  );
}


export default ZonaJuego;
