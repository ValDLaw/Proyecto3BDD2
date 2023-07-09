import numpy as np
import math
import rtree
import time



# Calcular la distancia de cada punto a la query
def calcular_distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia



start = time.time()
# 2- Configurar el índice en memoria
prop = rtree.index.Property()
prop.dimension = 2
prop.buffering_capacity = 3

ind = rtree.index.Index(properties=prop)

objetos = [] # imagenes

# 3- Insertar los puntos en el índice
for i, objeto in enumerate(objetos):
    ind.insert(i, objeto)

end = time.time()
print("Tiempo: ", end - start)




