import React from 'react';

// Componente para mostrar la lista de proyectos sugeridos
function ListaProyectos({ proyectos, onSelect }) {
  if (!proyectos) return null;
  if (proyectos.length === 0) return <p>No hay proyectos sugeridos.</p>;
  return (
    <div className="container mt-4">
      <div className="row">
        {proyectos.map((proy, idx) => (
          <div className="col-md-4 mb-3" key={proy.id}>
            <div className="card h-100 shadow-sm" style={{ cursor: 'pointer' }} onClick={() => onSelect(proy)}>
              <div className="card-body">
                <h5 className="card-title text-capitalize">{proy.nivel}</h5>
                <p className="card-text">{proy.descripcion.slice(0, 100)}...</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ListaProyectos;
