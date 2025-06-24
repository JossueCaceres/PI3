// Funciones para interactuar con la API del backend
// Asegurarse de insertar la ruta correcta del backend en el fetch

// Metodo POST: Manda un conjunto de imagenes al backend y recibe un JSON con los componentes
export async function uploadImages(files) {
  const formData = new FormData();
  files.forEach(file => formData.append('imagenes', file));
  const response = await fetch('http://localhost:5000/api/imagenes', {
    method: 'POST',
    body: formData,
  });
  if (!response.ok) throw new Error('Upload failed');
  return await response.json();
}

// POST: Send detected components to backend and get suggested projects
export async function fetchProyectos(componentes) {
  const response = await fetch('http://localhost:5000/api/componentes', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ componentes }),
  });
  if (!response.ok) throw new Error('Error en HTTP request para los proyectos');
  return await response.json();
}

