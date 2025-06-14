import React from 'react';
import UploadComponentes from './components/UploadComponentes';

function App() {
  const [result, setResult] = React.useState(null);

  return (
    <div>
      <h1>Generador de Circuitos Automáticos</h1>
      <UploadComponentes onResult={setResult} />
      {/* Aquí se integrarán los componentes principales */
      result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;
