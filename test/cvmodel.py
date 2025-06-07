import requests

url = "http://localhost:5000/api/imagenes"
# Ensure the server is running before executing this code -> Run app.py

# Modify the paths to your images accordingly to your local setup
files = [
    ('imagenes', open("C:/Users/diego/OneDrive/Escritorio/Git Projects/PI3-copy/test/images/x5.jpg", 'rb')),
    ('imagenes', open("C:/Users/diego/OneDrive/Escritorio/Git Projects/PI3-copy/test/images/640px-Protoboard_circuito_multivibradores.jpg", 'rb'))
]
response = requests.post(url, files=files)
print(response.json())