import face_recognition
import os
import json
import numpy as np
import random

def formateoPath(path):
    parts = path.split('/')
    startIndex = len(parts) - 3 
    result = "../"+('/'.join(parts[startIndex:]))
    return result

def initialize():
    images_directory = os.path.join(os.path.dirname(__file__), "../images")
    with open("encoded_faces.json", "w") as json_file:
        dictionary = {}
        for root, subdirectories, files in os.walk(images_directory):
            for file in files:
                path = os.path.join(root, file)
                if os.path.basename(file) != ".DS_Store":
                    image = face_recognition.load_image_file(path)
                    face_encod_vector = face_recognition.face_encodings(image)

                    if len(face_encod_vector) > 0:
                        path = formateoPath(path)
                        dictionary[path] = (face_encod_vector[0]).tolist()
        json.dump(dictionary, json_file)

#initialize()

def load_json():
    #Open and load the json file
    file = open("encoded_faces.json", "r")
    decodedJson = json.load(file)

    #Dataset of each image and its vectors
    dataset = []
    for path, matrix_vector_faces in decodedJson.items():
        dataset.append((path, np.asarray(decodedJson[path])))
    
    return dataset
