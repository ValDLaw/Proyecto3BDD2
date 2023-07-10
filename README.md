# PROYECTO 3 : Base de Datos Multimedia  
### Integrantes
* Valeria Espinoza Tarazona (202110109)
* Enzo Camizán Vidal (202110047)
* Diego Guerra Chevarría (202010137)
* Valentín Quezada Amour (202120570)
* Sofía García Quintana (202110567)

## KNN-Secuencial
### Using Priority Queue
### Range Search  
Para el análisis de la distribución de las distancias, empleamos la regla empírica, también conocida como la regla de los 68-95-99.7, la cual se basa en la distribución normal y establece que aproximadamente el 68% de los datos se encuentran dentro de una desviación estándar de la media, el 95% se encuentran dentro de dos desviaciones estándar y el 99.7% se encuentran dentro de tres desviaciones estándar. En base a ello calculamos el promedio y desviación estándar de todas las distancias, considerando la imagen en 'test/teofilo.png' como base.  

** Calculamos la media y la desviación estándar **  
```python
def distances(dataset):
    vector_dist = []
    for path, matrix_vector_faces in dataset:
        for distance in face_recognition.face_distance(matrix_vector_faces, faces_encoding[0]):
            vector_dist.append(distance)
    print("AQUIIIII")
    print(vector_dist)

    return list((np.mean(vector_dist), np.std(vector_dist)))
```

** Calculamos los tres radios **
```python
def select_representative_radii(mean_distance, std_distance):
    # regla empírica
    r1 = mean_distance - std_distance
    r2 = mean_distance - 2 * std_distance
    r3 = mean_distance - 3 * std_distance

    return [r1, r2, r3]
```

Obtuvimos los siguientes tres radios:  
```python
[0.7091430536563229, 0.6196988488962061, 0.5302546441360892]
```

## KNN-HighD
## Experimento  
Manteniendo un valor de K = 8

| N size   | KNN-SecuencialPQ | KNN-RTree   | KNN-HighD  |
|----------|------------------|-------------|------------|
| N=100    | 0.00078297       | 0.03930998  | Cell 3     |
| N=200    | 0.00146412       | 0.07666993  | Cell 6     |
| N=400    | 0.00354099       | 0.15550327  | Cell 6     |
| N=800    | 0.00677585       | 0.39572525  | Cell 6     |
| N=1600   | 0.01195478       | 0.80968094  | Cell 6     |
| N=3200   | 0.02157902       | 1.80910420  | Cell 6     |
| N=6400   | 0.03880596       | 3.98084021  | Cell 6     |
| N=12800  | 0.07779407       | 8.69529390  | Cell 6     |

Para la búsqueda por rango, los resultados con los tres radios diferentes fueron los siguientes:  

| N size   | R=0.709143053656 | R=0.6196988489  | R=0.53025464414|
|----------|------------------|-----------------|----------------|
| N=100    | 0.00034403801    | 0.00055289268   | 0.00029206276  |
| N=200    | 0.00058722496    | 0.00089192390   | 0.00054407120  |
| N=400    | 0.00118684769    | 0.00143218040   | 0.00104498863  |
| N=800    | 0.00397062302    | 0.00341296196   | 0.00213003159  |
| N=1600   | 0.00618696213    | 0.00604581833   | 0.00469493866  |
| N=3200   | 0.01186585426    | 0.01106381416   | 0.00871992111  |
| N=6400   | 0.02130794525    | 0.02114367485   | 0.01680111885  |
| N=12800  | 0.03789687157    | 0.04025101662   | 0.03456902504  |


## KNN-RTree
