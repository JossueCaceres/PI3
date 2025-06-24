import React from 'react';

// Componente para mostrar la lista de proyectos sugeridos
function ListaProyectos({ proyectos }) {
  if (!proyectos) return null;
  if (proyectos.length === 0) return <p>No hay proyectos sugeridos.</p>;
  return (
    <div>
      <h2>Proyectos sugeridos:</h2>
      <ul>
        {proyectos.map((proy, idx) => (
          <li key={idx}>
            <pre>{JSON.stringify(proy, null, 2)}</pre>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListaProyectos;
