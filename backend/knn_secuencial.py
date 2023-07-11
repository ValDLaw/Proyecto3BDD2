import face_recognition
import heapq as pq
from extraccion_de_caracteristicas import formateoPath
import numpy as np

'''
VALERIA:
def knn_pq(faces_encoding, dataset, k):
    result = []
    pq.heapify(result)
    for path, matrix_vector_faces in dataset:
        for distance in face_recognition.face_distance(matrix_vector_faces, faces_encoding):
            result.append((path, distance))

    resultK=[]
    for n in range(k):
        if n <= k:
            resultK.append(heapq.heappop(result))
        else:
            break
    res = pq.nsmallest(k , result)
    print(result)
    print(res)
    return [path for path, distance in resultK]


def range_search(faces_encoding, dataset, radio):
    result = []
    for path, matrix_vector_faces in dataset:
        for distance in face_recognition.face_distance(matrix_vector_faces, faces_encoding[0]):
            if distance < radio:
                result.append((path, distance))

    result = sorted(result, key = lambda x: x[1])
    return [path for path, dis in result]
'''

ERES_VALERIA = False

def knn_pq(faces_encoding, dataset, k):
    result = []
    for path, matrix_vector_faces in dataset:
        for distance in face_recognition.face_distance(matrix_vector_faces, faces_encoding):
            #result.append((os.path.basename(path), distance))
            pq.heappush(result, (distance, formateoPath(path, ERES_VALERIA)))

    resultK = pq.nsmallest(k , result)

    return [formateoPath(path, ERES_VALERIA) for distance, path in resultK]

def select_representative_radio(mean_distance, std_distance):
    # regla empírica
    r1 = mean_distance - std_distance
    r2 = mean_distance - 2 * std_distance
    r3 = mean_distance - 3 * std_distance

    return [r1, r2, r3]

def distances(faces_encoding, dataset):
    vector_dist = []
    for path, matrix_vector_faces in dataset:
        for distance in face_recognition.face_distance(matrix_vector_faces, faces_encoding):
            vector_dist.append(distance)

    return list((np.mean(vector_dist), np.std(vector_dist)))

def range_search(faces_encoding, dataset, radio):
    result = []
    for path, matrix_vector_faces in dataset:
        for distance in face_recognition.face_distance(matrix_vector_faces, faces_encoding):
            if distance < radio:
                result.append(( formateoPath(path, ERES_VALERIA), distance))

    if len(result):
        result = sorted(result, key = lambda x: x[1])
        return [path for path, dis in result]