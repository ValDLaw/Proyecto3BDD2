import faiss
from extraccion_de_caracteristicas import formateoPath
import numpy as np
import os

ERES_VALERIA = False

def buildFaissIndex(n, dataset):
    #1- borrando archivos anteriores
    pathFolder = "./knn/faiss/"
    if os.path.exists(pathFolder+"faiss_feat_vector_"+str(n)+".idx"):
        os.remove(pathFolder+"faiss_feat_vector_"+str(n)+".idx") 
        
    sample_dict = {}

    for path, matrix_vector_faces in dataset:
        sample_dict[formateoPath(path, ERES_VALERIA)]= matrix_vector_faces

    # FAISS BUILD
    vector = []
    faces= []
    for key in sample_dict: 
        vector.append(np.array(sample_dict[key], dtype='f'))
        faces.append(key)
    vector = np.array(vector, dtype='f')
    M = 32
    ef_search = 8
    d = 128      # 128

    # FAISS CPU
    ind  = faiss.IndexHNSWFlat(d,M)
    ind.hnsw.efConstruction = 40
    ind.hnsw.efSearch = ef_search

    ind.add(vector)

    faiss.write_index(ind, "./knn/faiss/faiss_feat_vector_"+str(n)+".idx")

def FaissIndex_Search(query, dataset, k, n):
    q = np.reshape(np.array(query,dtype='f'), (1,128))
    ind = faiss.read_index("./knn/faiss/faiss_feat_vector_"+str(n)+".idx")
    n, indx = ind.search(q, k=k)
    indx = indx[0].astype(int)
    results = []
    for i in indx: #Considerar que pasa si subes una foto de alguien que ya esta en la bd
        pathToSave = formateoPath(dataset[i][0], ERES_VALERIA)
        results.append(pathToSave)
    return results