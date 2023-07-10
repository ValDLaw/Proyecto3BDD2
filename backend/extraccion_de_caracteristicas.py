import face_recognition
import os
import json
import numpy as np
import random
from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def initialize():
    images_directory = os.path.join(os.path.dirname(__file__), "../images")
    with open("encoded_faces.json", "w") as json_file:
        dictionary = {}
        for root, subdirectories, files in os.walk(images_directory):
            for file in files:
                path = os.path.join(root, file)
                if os.path.basename(file) != ".DS_Store":
                    image = face_recognition.load_image_file(path)
                    faces_on_image = face_recognition.face_encodings(image)

                    if len(faces_on_image) > 0:
                        dictionary[path] = faces_on_image
                    
        json.dump(dictionary, json_file)

def initialize2(): #Para no usar eso del NumpyArray Encoder
    images_directory = os.path.join(os.path.dirname(__file__), "../images")
    with open("encoded_faces.json", "w") as json_file:
        dictionary = {}
        for root, subdirectories, files in os.walk(images_directory):
            for file in files:
                path = os.path.join(root, file)
                if os.path.basename(file) != ".DS_Store":
                    image = face_recognition.load_image_file(path)
                    face_encod_vector = (face_recognition.face_encodings(image)[0]).tolist()

                    if len(face_encod_vector) > 0:
                        dictionary[path] = face_encod_vector
                    
    json.dump(dictionary, json_file)

initialize2()

def load_json():
    #Open and load the json file
    file = open("encoded_faces.json", "r")
    decodedJson = json.load(file)

    #Dataset of each image and its vectors
    dataset = []
    for path, matrix_vector_faces in decodedJson.items():
        dataset.append((path, np.asarray(decodedJson[path])))
    
    return dataset
