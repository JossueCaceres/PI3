import React from 'react';

function DetalleProyecto({ proyecto, onBack }) {
  if (!proyecto) return null;
  return (
    <div className="container mt-4">
      <button className="btn btn-link mb-3" onClick={onBack}>← Volver</button>
      <h2 className="mb-3 text-capitalize">{proyecto.nivel}</h2>
      <h5>Descripción</h5>
      <div className="mb-3">{proyecto.descripcion}</div>
      <h5 className="mt-3">Archivos del circuito</h5>
      <ul>
        <li>
          <a href={`http://localhost:5000/descargar/${proyecto.archivos.sketch}`} download className="btn btn-outline-primary btn-sm me-2">Descargar Código Arduino (.ino)</a>
        </li>  
        <li>
          <a href={`http://localhost:5000/descargar/${proyecto.archivos.diagrama}`} download className="btn btn-outline-primary btn-sm me-2">Descargar Diagrama Wokwi (.json)</a>
        </li>
        <li>
          <a href={`http://localhost:5000/descargar/${proyecto.archivos.readme}`} download className="btn btn-outline-primary btn-sm">Descargar README</a>
        </li>
      </ul>
    </div>
  );
}

export default DetalleProyecto;