import React, { useState } from 'react';
import UploadComponentes from './components/UploadComponentes';
import ListaProyectos from './components/ListaProyectos';
import DetalleProyecto from './components/DetalleProyecto';
import { fetchProyectos } from './api';

function App() {
  const [componentes, setComponentes] = useState(null);
  const [proyectos, setProyectos] = useState(null);
  const [loadingProyectos, setLoadingProyectos] = useState(false);
  const [selectedProyecto, setSelectedProyecto] = useState(null);

  // Called when components are detected
  const handleComponentesDetectados = (result) => {
    setComponentes(result.componentes);
    setProyectos(null); // Reset projects if new components
    setSelectedProyecto(null);
  };

  // Called when user wants to get projects
  const handleSolicitarProyectos = async () => {
    if (!componentes) return;
    setLoadingProyectos(true);
    try {
      const data = await fetchProyectos(componentes);
      setProyectos(data.proyectos);
      setSelectedProyecto(null);
    } catch (err) {
      alert('Error al obtener proyectos. Limite diario alcanzado. Intente de nuevo más tarde.');
    }
    setLoadingProyectos(false);
  };

  return (
    <div>
      <h1>Generador de Circuitos Automáticos</h1>
      <UploadComponentes
        onResult={handleComponentesDetectados}
        onSolicitarProyectos={handleSolicitarProyectos}
        componentesDetectados={componentes}
        loadingProyectos={loadingProyectos}
      />
      {!selectedProyecto && (
        <ListaProyectos proyectos={proyectos} onSelect={setSelectedProyecto} />
      )}
      {selectedProyecto && (
        <DetalleProyecto proyecto={selectedProyecto} onBack={() => setSelectedProyecto(null)} />
      )}
    </div>
  );
}

export default App;
