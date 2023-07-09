import numpy as np
import face_recognition
import math
from rtree import index
from extraccion_de_caracteristicas import load_json


def knn_rtree(faces_encoding, k, dataset):
    #index_name = 'knn/rtree_index'

    # Configurar las propiedades del índice R-tree
    properties = index.Property()
    properties.dimension = 128  # Tamaño del vector característico
    properties.buffering_capacity = 4
    properties.dat_extension = 'data'
    properties.idx_extension = 'index'

    # Crear el índice R-tree
    idx = index.Index(properties=properties)

    # Construir el índice si está vacío
    if idx.get_size() < 1:
        c = 0
        for path, matrix_vector_faces in dataset:
            for vector in matrix_vector_faces:
                q = tuple(vector)
                idx.insert(c, q)
            c+=1

    # Realizar la consulta kNN
    query = tuple(faces_encoding[0])
    results = list(idx.nearest(coordinates=query, num_results=k))

    # Obtener las rutas de los resultados
    return [dataset[i][0] for i in results[:k]]