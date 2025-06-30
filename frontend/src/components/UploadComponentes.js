import React, { useState } from 'react';
import { uploadImages } from '../api';

function UploadComponentes({ onResult, onSolicitarProyectos, componentesDetectados, loadingProyectos }) {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [backendResult, setBackendResult] = useState(null);
  const [showComponents, setShowComponents] = useState(false);

  // Called when files are selected
  const handleFileChange = async (e) => {
    const files = Array.from(e.target.files);
    setSelectedFiles(files);
    setShowComponents(false);
    setBackendResult(null);
    if (files.length > 0) {
      setLoading(true);
      try {
        const result = await uploadImages(files);
        setBackendResult(result);
        onResult && onResult(result);
      } 
      catch (err) {
        alert('Error uploading images');
      }
      setLoading(false);
    }
  };

  // Restart: clear everything
  const handleRestart = () => {
    setSelectedFiles([]);
    setBackendResult(null);
    setShowComponents(false);
    // Also clear the file input value
    document.getElementById('file-input').value = '';
  };

  // Show components when button is clicked
  const handleShowComponents = () => {
    setShowComponents(true);
  };

  return (
    <div className="d-flex justify-content-center align-items-center mt-5">
      <div className="card shadow p-4" style={{ maxWidth: 420, width: '100%' }}>
        <h2 className="mb-4 text-center text-primary">Subir imágenes de componentes</h2>
        <form>
          <input
            id="file-input"
            className="form-control mb-3"
            type="file"
            accept="image/*"
            multiple
            onChange={handleFileChange}
            disabled={loading}
          />
          <div className="d-flex justify-content-between">
            <button type="button" className="btn btn-secondary" onClick={handleRestart} disabled={loading && !selectedFiles.length}>
              Reiniciar
            </button>
          </div>
        </form>
        {loading && <p className="text-info mt-3">Subiendo imágenes...</p>}
        {backendResult && (
          <button type="button" className="btn btn-outline-primary mt-3 w-100" onClick={handleShowComponents}>
            Mostrar Componentes
          </button>
        )}
        {showComponents && backendResult && (
          <div className="mt-4">
            <h5 className="text-primary">Componentes detectados:</h5>
            {backendResult.componentes && Object.keys(backendResult.componentes).length > 0 ? (
              <table className="table table-bordered table-sm mt-2">
                <thead className="table-light">
                  <tr>
                    <th>Componente</th>
                    <th>Cantidad</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(backendResult.componentes).map(([nombre, cantidad]) => (
                    <tr key={nombre}>
                      <td>{nombre}</td>
                      <td>{cantidad}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div className="alert alert-warning">No se detectaron componentes.</div>
            )}
            {backendResult.componentes && (
              <button
                type="button"
                className="btn btn-success w-100 mt-2"
                onClick={onSolicitarProyectos}
                disabled={loadingProyectos}
              >
                {loadingProyectos ? 'Buscando proyectos...' : 'Obtener Proyectos Recomendados'}
              </button>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default UploadComponentes;
