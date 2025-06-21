import React from 'react';
import UploadComponentes from './components/UploadComponentes';

function App() {
  const [result, setResult] = React.useState(null);

  return (
    <div>
      <h1>Generador de Circuitos Automáticos</h1>
      <UploadComponentes onResult={setResult} />
      
    </div>
  );
}

export default App;
