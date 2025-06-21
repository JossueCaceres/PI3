# PI3

Summary of technical part of the project. 
## Backend (backend)
Core Files
### *app.py*
Starts the Flask server and registers API endpoints (blueprints). Handles global errors (like rate limits).

### config.py
Loads environment variables (like API tokens) and sets configuration constants for the backend.

### requirements.txt
Lists Python dependencies (Flask, OpenAI, etc.) needed to run the backend.

## Controllers (controllers/)

### circuitos.py
Defines API endpoints related to circuits.
Receives component lists (from frontend or CV model).
Calls the project generator and returns suggested projects.

### usuarios.py
Placeholder for user-related endpoints (e.g., saving user projects, annotations).
Services (services/)

### generador.py
- Main logic to generate circuit projects based on detected components.
- Calls the AI model (via OpenAI API) to generate descriptions, code, diagrams, and README files for each difficulty level.
- Saves generated files to disk.
- Create the prompts that are inserted to OpenIA API. 

### openai_service.py
Handles communication with the OpenAI API (or a proxy endpoint) to generate text/code based on prompts.

### wokwi_service.py
Placeholder for integration with the Wokwi simulator API (to generate circuit diagrams or simulation links).

### cv_model.py
(Currently empty)
This is where you should load and run your computer vision model to detect components from uploaded images.

## Models (models/)

### proyecto.py
- Placeholder for data models (e.g., project schema for database or serialization).
Storage (storage)
- Stores generated files (Arduino code, diagrams, README, etc.) for each project.

## Database (database/)
Placeholder for database files or scripts (e.g., MongoDB, JSON files).

## Frontend (frontend)
### index.html
Main HTML file for the React app.

### App.js
Main React component; will render your UI.

### api.js
Placeholder for functions to interact with your backend API.

src/components/

### UploadComponentes.js: 
For uploading or pasting component lists (or images).
### ListaProyectos.js: 
To display the list of suggested projects.
### ProyectoDetalle.js: 
To show details of a selected project.
### SimuladorWokwi.js: 
To embed or link to the Wokwi simulator.

### global.css: 
Global CSS styles for the frontend.

## Docs (docs)
### README_Proyecto_Circuitos.md
Detailed documentation of your project’s goals, flow, API, and structure.

# Project Flow (End-to-End Purpose)
1. User uploads images (via frontend).
2. Backend receives images, uses the CV model (to be implemented in **cv_model.py**) to detect components.
3. Detected components are sent to the project generator (**generador.py**), which uses AI to suggest possible circuits.
4. Generated projects (with code, diagrams, instructions) are returned to the frontend.
5. Frontend displays the projects, lets the user view details, and possibly simulate circuits in Wokwi.

# Summary:
Each file and folder is organized to separate concerns:

Controllers handle API endpoints,
Services contain business logic (AI, CV, Wokwi),
Models define data structures,
Frontend shows the UI,
Docs explain the project.


Your next step is to implement your CV model in cv_model.py and connect it to your API so users can upload images and get component predictions

# Dependencias y librerias a instalar
## Backend
1. Flask
2. PIL
3. inference_sdk
4. io(creo que ya esta predeterminado)
5. openia
6. dotenv
7. flask cors: pip install Flask-Cors
8. Postman: Pagina Web que te sirve para generar HTTP Requests

## Frontend 
1. npm (No chocolateley): [Nodejs](https://nodejs.org/es) 


# Pasos para encendido de la aplicacion 
1. Run app.py
Se runea app.py en algun terminal 1. Este archivo genera el servidor Backend que necesitamos para obtener los resultados del modelo de Vision Computacional y los resultados de la API de OpenIA(sus respuestas). 

Activa los endpoints del backend para que un cliente puede accerder a estas funciones. Es necesario su ruta HTTP. 

### Carpeta test 
Esta carpeta contiene una carpeta de imagenes y un archivo .py. El archivo .py simula ser un cliente y pide un request para el servidor ya activado. 

2. Run npm start
Insertamos este comando en un terminal de preferencia (yo utilice Git Bash). Es importante que se runee este comando en la carpeta "frontend", sino no funciona. Este comando nos redireccionara a nuestro browser con la pagina web creada.   

# Recordatorio
Instala las librerias que necesites en el interprete de python correcto. Puede que lo estes instalando en otro que no uses en tu IDE.