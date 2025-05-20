import React, { useRef, useEffect, useState } from "react";
import styles from "./ZonaJugador.module.css";
import Carta from './Carta';

function ZonaJugador({ posicion, jugador, children, turno}) {
  const zonaRef = useRef(null);
  const [zonaSize, setZonaSize] = useState({ width: 600, height: 300 }); // valores por defecto

  // Calcular el tamaño de la zona y actualizarlo en el estado
  useEffect(() => {
    if (zonaRef.current) {
      const { width, height } = zonaRef.current.getBoundingClientRect();
      setZonaSize({ width, height });
    }
  }, []);
  if (turno == jugador){
    return esMiTurno(zonaRef,posicion,children,zonaSize)
  }else{
    return <div
        ref={zonaRef}
        className={`${styles.zona} ${styles[posicion]}`}
      >
        <p className="text-cyan-500">no es tu turno maquinola </p>
      </div>
  }


}

function esMiTurno(zonaRef,posicion,children,zonaSize){


    return (
  <div>
    <p className="text-blue-500 text-lg font-semibold bg-white bg-opacity-70 px-4 rounded-lg shadow-md border border-blue-300">
  Tu turno
    </p>
  <div
    ref={zonaRef}
    className={`${styles.zona} ${styles[posicion]}`}
  >
    {React.Children.map(children, (child) =>
      React.cloneElement(child, {
        contenedorRef: zonaRef,
        width: zonaSize.width,
        height: zonaSize.height,
      })
    )}
  </div>
  
  </div>
);
}
export default ZonaJugador;