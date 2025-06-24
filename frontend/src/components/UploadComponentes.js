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
    <div>
      <form>
        <input
          id="file-input"
          type="file"
          accept="image/*"
          multiple
          onChange={handleFileChange}
          disabled={loading}
        />
        <button type="button" onClick={handleRestart} disabled={loading && !selectedFiles.length}>
          Reiniciar
        </button>
      </form>
      {loading && <p>Subiendo imágenes...</p>}
      {backendResult && (
        <button type="button" onClick={handleShowComponents}>
          Mostrar Componentes
        </button>
      )}
      {showComponents && backendResult && (
        <div>
          <h3>Componentes detectados:</h3>
          <pre>{JSON.stringify(backendResult.componentes, null, 2)}</pre>
          {backendResult.componentes && (
            <button
              type="button"
              onClick={onSolicitarProyectos}
              disabled={loadingProyectos}
            >
              {loadingProyectos ? 'Buscando proyectos...' : 'Obtener Proyectos Recomendados'}
            </button>
          )}
        </div>
      )}
    </div>
  );
}

export default UploadComponentes;
