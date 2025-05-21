export default function Controles(jugador){
    return (      <div>
        <button className="bg-blue-500 text-white px-4 py-2 rounded">Pasar</button>
        <div className="mt-2 space-x-2">
          <button className="bg-red-500 text-white px-3 py-1 rounded">Basta</button>
          <button className="bg-yellow-500 text-black px-3 py-1 rounded">Última chance</button>
        </div>
        <p className="mt-4">Puntaje actual : 20</p>
      </div>)
}