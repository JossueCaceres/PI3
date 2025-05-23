# 🛠️ Proyecto: Generador de Circuitos Automáticos a partir de Componentes Reconocidos

## 🎯 Objetivo General

Diseñar e implementar una plataforma que, a partir del reconocimiento visual de componentes electrónicos, sea capaz de sugerir circuitos posibles, generar automáticamente el código de programación (`sketch.ino`), el diagrama de conexiones (`diagram.json`) y permitir su visualización y prueba mediante una interfaz web interactiva o con simuladores como **Wokwi**.

---

## 🧩 Componentes Iniciales Disponibles

El sistema debe reconocer y trabajar inicialmente con los siguientes elementos:

- Arduino UNO  
- Protoboard  
- Jumpers  
- Resistencias (sin valor detectado)  
- LEDs (1 a 3)  
- Sensor de temperatura (LM35)  
- Sensor ultrasónico (HC-SR04)  
- Fotoresistor (LDR)  
- Motor DC con ruedas  
- Baterías y porta baterías  

---

## 🧠 Flujo del Sistema

1. El usuario toma la foto de los componentes.
2. El software reconoce los elementos y la cantidad de cada uno.
3. El backend genera 3 circuitos (fácil, medio, difícil) según los componentes detectados.
4. El usuario ve 3 títulos, cada uno con su dificultad, breve descripción y, si es posible, imagen del circuito (generada por la API de Wokwi).
5. Al seleccionar una opción, la plataforma muestra:
   - Los archivos generados (`sketch.ino`, `diagram.json`)
   - Un README con instrucciones y tips
   - El circuito funcional (simulación Wokwi)

---

### 1. Reconocimiento de Componentes

El sistema detecta los componentes presentes y genera un JSON como:

```json
{
  "componentes_detectados": ["Arduino UNO", "LM35", "Protoboard", "Jumpers", "LED"]
}
```

---

### 2. Backend Inteligente

El backend realiza:
- Generación de 3 circuitos por dificultad (fácil, medio, difícil)
- Para cada circuito:
  - Descripción del circuito
  - Código comentado y detallado (`sketch.ino`)
  - Diagrama de conexiones (`diagram.json`)
  - README con instrucciones y tips
  - Enlace e imagen de simulación Wokwi
- Los archivos y anotaciones de cada usuario se almacenan de forma personalizable

---

### 3. Endpoints de la API

#### 1. Subir componentes detectados
- **POST** `/api/componentes`
  - Recibe el JSON con los componentes detectados y sus cantidades.
  - Responde con los proyectos sugeridos (id, dificultad, descripción).

#### 2. Obtener detalles de un proyecto sugerido
- **GET** `/api/proyectos/{id}`
  - Devuelve descripción, archivos generados, README y enlaces de simulación.

#### 3. Guardar anotaciones/código personalizado del usuario
- **POST** `/api/proyectos/{id}/anotaciones`
  - Permite guardar comentarios, versiones personalizadas del código o diagramas por usuario.

#### 4. Listar proyectos guardados por usuario
- **GET** `/api/usuarios/{usuario}/proyectos`
  - Devuelve la lista de proyectos personalizados/guardados por el usuario.

---

## 🌐 Interfaz Web (Frontend)

- Aplicación web responsive (HTML o React)
- Permite al usuario:
  - Subir o pegar la lista de componentes
  - Ver proyectos sugeridos
  - Visualizar código y diagrama
  - Ejecutar simulaciones (Wokwi)

---

## 📦 Estructura del Proyecto

```
backend/
  app.py
  config.py
  requirements.txt
  controllers/
    circuitos.py
    usuarios.py
  services/
    openai_service.py
    wokwi_service.py
    generador.py
  models/
    proyecto.py
  storage/
  database/
frontend/
  public/
    index.html
  src/
    App.js
    api.js
    components/
      UploadComponentes.js
      ListaProyectos.js
      ProyectoDetalle.js
      SimuladorWokwi.js
    styles/
      global.css
  package.json
docs/
  README_Proyecto_Circuitos.md
README.md
```

---

## 🔧 Requerimientos Técnicos

- **Backend**: Python (Flask) o Node.js 
- **Frontend**: HTML/JS o React
- **IA**: OpenAI GPT-4 / GPT-3.5 turbo
- **Simulador**: Wokwi (compatibilidad con `diagram.json`)
- **Almacenamiento**: Sistema de archivos local, Firebase o S3
- **Base de datos**: JSON local o MongoDB para proyectos

---

## 🎓 Requisitos Educativos

- Todo código generado debe incluir **comentarios paso a paso**.
- El sistema servirá como una herramienta **didáctica** para estudiantes.

---

## ✨ Créditos

Proyecto desarrollado por el equipo de visión computacional, backend y electrónica educativa.
