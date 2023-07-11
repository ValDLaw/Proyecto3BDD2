from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import face_recognition
import json
import requests
import os
import sys
import extraccion_de_caracteristicas
import numpy as np
from shortuuid import ShortUUID
from werkzeug.utils import secure_filename
from PIL import Image

from knn_secuencial import knn_pq
from knn_rtree import knn_rtree
from knn_kdtree import KDTree_index, KDTree_search
from knn_faiss import FaissIndex_Search

os.environ['UPLOAD_FOLDER'] = 'uploads/'

app = Flask(__name__)
CORS(app, origin="*")
dataset = extraccion_de_caracteristicas.load_json()
app.config["UPLOAD_FOLDER"] = os.environ.get("UPLOAD_FOLDER")

N = 12800


@app.route("/sequential", methods=["POST"])
def upload_image_sequential():
    file = request.files["file"]
    random_seed = ShortUUID().random(length=50)
    img_id = secure_filename(str(random_seed) + str(file.filename))
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], img_id))

    #image_path = request.form['image_path']
    query_image = face_recognition.load_image_file(file)
    face_encodings = face_recognition.face_encodings(query_image)
    k = int(request.form['k'])

    return knn_pq(face_encodings, dataset[:N], k)

@app.route("/rtree", methods=["POST"])
def upload_image_rtree():
    file = request.files["file"]
    random_seed = ShortUUID().random(length=50)
    img_id = secure_filename(str(random_seed) + str(file.filename))
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], img_id))

    #image_path = request.form['image_path']
    query_image = face_recognition.load_image_file(file)
    face_encodings = face_recognition.face_encodings(query_image)
    k = int(request.form['k'])

    return knn_rtree(face_encodings, dataset, k, N)

@app.route("/kdtree", methods=["POST"])
def upload_image_kdtree():
    file = request.files["file"]
    random_seed = ShortUUID().random(length=50)
    img_id = secure_filename(str(random_seed) + str(file.filename))
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], img_id))

    #image_path = request.form['image_path']
    query_image = face_recognition.load_image_file(file)
    face_encodings = face_recognition.face_encodings(query_image)
    k = int(request.form['k'])

    index = KDTree_index(dataset[:N])
    return KDTree_search(face_encodings, dataset, k, index)

@app.route("/faiss", methods=["POST"])
def upload_image_faiss():
    file = request.files["file"]
    random_seed = ShortUUID().random(length=50)
    img_id = secure_filename(str(random_seed) + str(file.filename))
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], img_id))

    #image_path = request.form['image_path']
    query_image = face_recognition.load_image_file(file)
    face_encodings = face_recognition.face_encodings(query_image)
    k = int(request.form['k'])

    return FaissIndex_Search(face_encodings, dataset, k, N)

@app.route("/")
def index():
    print("Ruta raíz accedida")
    return "Api para subir imágenes"

if __name__ == '__main__':
    app.run()