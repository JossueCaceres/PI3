from PIL import Image 
import os
from inference_sdk import InferenceHTTPClient
from io import BytesIO

ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")  # Add this to your .env
ROBOFLOW_WORKSPACE = "cv-laboratory"
ROBOFLOW_ID = "detect-count-and-visualize"


def predecir_componentes(imagenes): #Imagen debe ser un objeto tipo archivo (file-like object)(".jpg")
    """
    imagen: file-like object (URL, File Path, np.ndarray, PIL.Image) 
    Returns: list of detected components with counts
    """
    client = InferenceHTTPClient(
        api_url="https://serverless.roboflow.com",
        api_key= ROBOFLOW_API_KEY
    )

    predicciones = []

    for imagen in imagenes:
        if not imagen:
            raise ValueError("No image provided")
        if not hasattr(imagen, 'read'):
            raise ValueError("Image must be a file-like object")
        # Convert FileStorage to PIL Image
        imagen.seek(0)
        pil_image = Image.open(imagen)
        result = client.run_workflow(
            workspace_name=ROBOFLOW_WORKSPACE,
            workflow_id=ROBOFLOW_ID,
            images={"image": pil_image}, 
            use_cache=True
        )
        predicciones.append(result)
    
    componentes, ids = parse_predictions(predicciones)
    
    return componentes, ids


def parse_predictions(predictions): 
    """
    predictions: list of dictionaries containing prediction results
    Parses the predictions to extract component names and their counts and ids.

    Also, we can return the predicted image by the model 
    """
    ids = set()
    for result in predictions: #if prediction is a dict 
        for num_ids in result[0]["count_objects"]: # Just for our workflow, it returns a list of ids
            num_ids = int(num_ids) 
            ids.add(num_ids)
    # Dictionary to store component names and their counts(may be repeated)
    components = {}
    for result in predictions:
        for object in result[0]["predictions"]["predictions"]:
            name = object["class"]
            if name not in components:
                components[name] = 0
            components[name] = components[name] + 1
    return components, ids
    
    #componentes = {"Led": 2, "Arduino_uno": 1}
    #ids = [1, 2]