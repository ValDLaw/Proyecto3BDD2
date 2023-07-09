import face_recognition
from extraccion_de_caracteristicas import load_json
from knn_rtree import *
import time

N_values = [100,200,400,800,1600,3200,6400,12800]
k = 8   # fijo
image_path = "test/teofilo.png"
query_image = face_recognition.load_image_file(image_path) 
faces_encoding = face_recognition.face_encodings(query_image)

dataset = load_json()

''' Testeando KNN-RTree '''
print("KNN-Rtree TEST")
for n in N_values:
    print("N =",n)
    start_time = time.time()
    knn_rtree(faces_encoding, k, dataset[:n])
    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    print(tiempo_ejecucion)