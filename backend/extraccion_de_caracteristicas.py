import os
import json
import face_recognition
from json import JSONEncoder
import numpy as np

class NAEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def encode_faces(directory):
    encoded_faces = {}

    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)

            image = face_recognition.load_image_file(path)
            faces = face_recognition.face_encodings(image)

            if len(faces) > 0:
                encoded_faces[path] = faces

    return encoded_faces

def save_encoded_faces(encoded_faces, output_file):
    with open(output_file, "w") as json_file:
        json.dump(encoded_faces, json_file, cls=NAEncoder)

# Directorio de imágenes
image_directory = "..images/"

# Codificar los rostros en las imágenes del directorio
encoded_faces = encode_faces(image_directory)

# Guardar los rostros codificados en un archivo JSON
output_file = "encoded_faces.json"
save_encoded_faces(encoded_faces, output_file)



def extract_features(image_path):
    # Cargar la imagen y convertirla a un arreglo
    image = face_recognition.load_image_file(image_path)

    # Encontrar ubicaciones de los rostros en la imagen
    face_locations = face_recognition.face_locations(image)

    # Extraer características de los rostros encontrados
    face_encodings = face_recognition.face_encodings(image, face_locations)

    return face_encodings

def extract_features_from_folder(folder_path, k):
    # Obtener la lista de subcarpetas (nombres de personas)
    person_folders = os.listdir(folder_path)

    # Lista para almacenar los vectores característicos
    features_list = []

    # Contador global para el número de imágenes procesadas
    count = 0

    for person_folder in person_folders:
        # Construir la ruta completa de la subcarpeta de persona
        person_folder_path = os.path.join(folder_path, person_folder)

        if os.path.isdir(person_folder_path):
            # Obtener la lista de archivos en la subcarpeta de persona
            file_list = os.listdir(person_folder_path)

            for file_name in file_list:
                if count == k:
                    break

                # Construir la ruta completa de la imagen
                image_path = os.path.join(person_folder_path, file_name)

                # Extraer características de la imagen
                features = extract_features(image_path)

                # Agregar las características a la lista
                features_list.extend(features)

                count += 1

                if count == k:
                    break

        if count == k:
            break

    return features_list

# Ruta de la carpeta de imágenes
folder_path = "../images"

# Número máximo de imágenes a procesar
k = 2

# Extraer características de las imágenes en la carpeta
image_features = extract_features_from_folder(folder_path, k)
for i in image_features:
    print(i)

# Imprimir el número de vectores característicos generados
print("Se extrajeron", len(image_features), "vectores característicos de tamaño 128.")