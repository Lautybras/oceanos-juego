import { useState } from 'react'
import './App.css'
import Carta from "./components/Carta";
import ZonaJuego from "./components/ZonaJuego";

function App() {
  const [count, setCount] = useState(0)

  return (
    <div style={{ display: "flex", gap: "10px", padding: "20px" }}>
      <ZonaJuego>
      <Carta tipo={0} color={0} />

      </ZonaJuego>
    </div>    
  )
}

export default App
