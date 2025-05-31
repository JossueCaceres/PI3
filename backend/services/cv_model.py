import requests
import os

ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")  # Add this to your .env
ROBOFLOW_WORKSPACE = "your-workspace"
ROBOFLOW_PROJECT = "your-project"
ROBOFLOW_VERSION = "1"
ROBOFLOW_URL = f"https://detect.roboflow.com/{ROBOFLOW_PROJECT}/{ROBOFLOW_VERSION}"

def predict_components(images):
    """
    images: list of file-like objects (e.g., from Flask's request.files.getlist('images'))
    Returns: list of detected components with counts
    """
    headers = {"Authorization": f"Bearer {ROBOFLOW_API_KEY}"}
    all_predictions = []
    for image in images:
        response = requests.post(
            ROBOFLOW_URL,
            params={"api_key": ROBOFLOW_API_KEY},
            files={"file": image}
        )
        result = response.json()
        all_predictions.append(result)
    # TODO: Parse all_predictions to extract component names and counts
    return all_predictions

def parse_predictions(predictions): 
    """
    predictions: list of predictions from Roboflow
    Returns: dict with component names and their counts
    """
    ids = set()
    for prediction in predictions:
        for item in prediction.get("predictions", []):
            if "id" in item:
                ids.add(item["id"])
    # Dictionary to store component names and their counts
    components = {}
    for prediction in predictions:
        for item in prediction.get("predictions", []):
            name = item["class"]
            components[name] = components.get(name, 0) + 1
    return components, ids