import numpy as np
import face_recognition
import math
from rtree import index
from extraccion_de_caracteristicas import load_json


def rtree_index(n, dataset):
    #1- borrando archivos anteriores
    pathFolder = "./knn/rtree/"
    if os.path.exists(pathFolder+"rtree_feat_vector_"+str(n)+".dat"):
        os.remove(pathFolder+"rtree_feat_vector_"+str(n)+".dat")
    if os.path.exists(pathFolder+"rtree_feat_vector_"+str(n)+".idx"):
        os.remove(pathFolder+"rtree_feat_vector_"+str(n)+".idx") 

    # Configurar las propiedades del índice R-tree
    properties = rtree.index.Property()
    properties.dimension = 128  # Tamaño del vector característico
    properties.buffering_capacity = 8
    # Crear el índice R-tree
    idx = rtree.index.Index(pathFolder+"rtree_feat_vector_"+str(n), properties=properties)

    # Construir el índice si está vacío
    if idx.get_size() < 1:
        c = 0
        for path, matrix_vector_faces in dataset[:n]:
            q = tuple(matrix_vector_faces)
            idx.insert(c, q)
            #for vector in matrix_vector_faces:
            #    q = tuple(vector)
            #    idx.insert(c, q)
            c+=1
    idx.close()

def knn_rtree(faces_encoding, k, n, dataset):
    '''
    #1- borrando archivos anteriores
    if os.path.exists(index_name+"feature_vector.dat"):
        os.remove(index_name+"feature_vector.dat")
    if os.path.exists(index_name+"feature_vector.idx"):
        os.remove(index_name+"feature_vector.idx") 
    '''
    # Configurar las propiedades del índice R-tree
    properties = rtree.index.Property()
    properties.dimension = 128  # Tamaño del vector característico
    properties.buffering_capacity = 8
    # Crear el índice R-tree
    idx = rtree.index.Index("./knn/rtree/rtree_feat_vector_"+str(n), properties=properties)

    # Construir el índice si está vacío
    if idx.get_size() < 1:
        c = 0
        for path, matrix_vector_faces in dataset:
            q = tuple(matrix_vector_faces)
            idx.insert(c, q)
            #for vector in matrix_vector_faces:
            #    q = tuple(vector)
            #    idx.insert(c, q)
            c+=1

    # Realizar la consulta kNN
    query = tuple(faces_encoding[0])
    results = list(idx.nearest(coordinates=query, num_results=k))
    # Obtener las rutas de los resultados
    return [formateoPath(dataset[i][0], ERES_VALERIA) for i in results[:k]]