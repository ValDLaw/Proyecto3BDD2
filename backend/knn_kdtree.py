from sklearn.neighbors import KDTree
from extraccion_de_caracteristicas import formateoPath

ERES_VALERIA = False

def KDTree_index(dataset):
    # 1- construccion del indice
    lst = []
    for path, matrix_vector_faces in dataset:
        lst.append(matrix_vector_faces)
    ind = KDTree(lst, leaf_size=2)
    return ind

def KDTree_search(faces_encoding, dataset, k, indKD):
    # 2- busqueda KNN
    results = []
    result_dist, result_id = indKD.query(faces_encoding, k=k)
    for id, dist in zip(result_id[0], result_dist[0]):
        pathToSave = formateoPath(dataset[id][0], ERES_VALERIA)
        results.append(pathToSave)
        print(pathToSave,"=>", dist)
    return results