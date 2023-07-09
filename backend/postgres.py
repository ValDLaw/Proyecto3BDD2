import psycopg2
import numpy as np
from extraccion_de_caracteristicas import *

# Ruta de la carpeta de imágenes
folder_path = "../images"

# Número máximo de imágenes a procesar
k = 2

# Extraer características de las imágenes en la carpeta
image_features = extract_features_from_folder(folder_path, k)
#print(image_features)

# Imprimir el número de vectores característicos generados
print("Se extrajeron", len(image_features), "vectores característicos de tamaño 128.")

def insert_points(feature_vectors):
    # Conexión a la base de datos
    conn = psycopg2.connect(database="Proyecto3", user="postgres", password="onepiecelaw", host="localhost", port="5432")
    cursor = conn.cursor()

    sql = "INSERT INTO points (p) VALUES (point%s)"

    try:
        # Insertar cada vector característico en la base de datos
        for vector in feature_vectors:
            vector_tuple = tuple(vector)  # Convertir el vector característico en una lista
            print(vector_tuple)
            cursor.execute(sql, (vector_tuple,))

        conn.commit()
        print("Los vectores característicos se han insertado correctamente en la base de datos.")
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print("Error al insertar los vectores característicos en la base de datos:", error)
    finally:
        cursor.close()
        conn.close()


insert_points(image_features)