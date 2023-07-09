import face_recognition

def knn_pq(faces_encoding, dataset, k):
    result = []
    for path, matrix_vector_faces in dataset:
        for distance in face_recognition.face_distance(matrix_vector_faces, faces_encoding[0]):
            result.append((path, distance))

    result = sorted(result, key = lambda x: x[1])
    return [path for path, distance in result[:k]]


def range_search(faces_encoding, dataset, radio):
    result = []
    for path, matrix_vector_faces in dataset:
        for distance in face_recognition.face_distance(matrix_vector_faces, faces_encoding[0]):
            if distance < radio:
                result.append((path, distance))

    result = sorted(result, key = lambda x: x[1])
    return [path for path, dis in result]