import numpy as np
import math
from rtree import index

def knn_rtree(faces_encoding, k , dataset):
    name = 'knn/rtree_index'

    p = index.Property()
    p.dimension = 128  # D
    p.buffering_capacity = 4  # M
    p.dat_extension = 'data'
    p.idx_extension = 'index'
    idx = index.Index(name, properties=p)

    if idx.count == 0:
        c = 0
        for path, matrix_vector_faces in dataset:
            for vector in matrix_vector_faces:
                q = tuple(vector)
                idx.insert(c, q)
            c += 1

    query = tuple(faces_encoding[0])

    lres = list(idx.nearest(coordinates=query, num_results=k))

    return [dataset[i][0] for i in lres[:k]]
