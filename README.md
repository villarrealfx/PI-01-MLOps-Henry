

# Machine Learning Operations (MLOps)
## Proyecto Individual # 1 | Sistema de Recomendación de Películas
## Introducción:
El presente proyecto práctico forma parte del curriculum para la carrera de Ciencia de Datos impartido por **Henry** como parte del trayecto de Labs. El mismo consiste en la elaboración de un Sistema de Recomendación de películas cumpliendo cuatro (04) etapas principales
1. Trabajo de ETL **(Extract, Transform, Load)** en un conjunto de datasets (proporcionados por la institución).
2. Trabajo de EDA  **(Exploratory Data Analysis)** a los datos resultantes del procedimiento enunciado en el punto 1
3. Trabajo de ML **(machine learning)** para armar un sistema de recomendación de películas.
4. Trabajo de crear y realizar deploy de API **(Application Programming Interface)** donde quede a disposición la información necesaria para su consumo respetando y cumpliendo las características y requerimientos solicitados en el programa
## 1. El set de datos

La información recolectada se encuentra en dos (02) archivo CSV (`movies_dataset.csv` y `credits.csv`) los cuales encontraras en el enlace con las siguientes características:<br>

[Archivos `movies_dataset.csv` y `credits.csv`](https://drive.google.com/drive/folders/1hsmKrY2O-nlOF4_BJuEd7ti3MCrF_6Cz?usp=sharing)<br>
los archivos deberán colocarse dentro de la carpeta `datasets` que se encuentra en el directorio raíz del proyecto para que funcionen los path predeterminados.

* **`movies_dataset`**: 45466 filas y 24 columnas.
* **`credits`** : 45476 filas y 3 columnas.

 Las columnas para **`movies_dataset`** son:<br>
 

|Característica | Descripción|
|:-------------:|:---------- |
| adult |	Indica si la película tiene califiación X, exclusiva para adultos.|
| belongs_to_collection | Un diccionario que indica a que franquicia o serie de películas pertenece la película|
| budget |	El presupuesto de la película, en dólares |
| genres |	Un diccionario que indica todos los géneros asociados a la película|
| homepage | La página web oficial de la película|
| id | ID de la pelicula|
| imdb_id |IMDB ID de la pelicula|
| original_language | Idioma original en la que se grabo la pelicula |
| original_title | Titulo original de la pelicula |
| overview | Pequeño resumen de la película|
| popularity | Puntaje de popularidad de la película, asignado por TMDB (TheMoviesDataBase) |
| poster_path |	URL del póster de la película |
| production_companies | Lista con las compañias productoras asociadas a la película |
| production_countries | Lista con los países donde se produjo la película |
| release_date | Fecha de estreno de la película |
| revenue |	Recaudación de la pelicula, en dolares |
| runtime |	Duración de la película, en minutos |
| spoken_languages | Lista con los idiomas que se hablan en la pelicula |
| status | Estado de la pelicula actual (si fue anunciada, si ya se estreno, etc) |
| tagline |	Frase celebre asociada a la pelicula |
| title | Titulo de la pelicula |
| video | Indica si hay o no un trailer en video disponible en TMDB |
| vote_average | Puntaje promedio de reseñas de la pelicula |
| vote_count | Numeros de votos recibidos por la pelicula, en TMDB |


## 2 URLs

1. [Render: (https://recomendacion-peliculas-cv.onrender.com/docs)](https://recomendacion-peliculas-cv.onrender.com/docs)

2. [Video: https://www.loom.com/share/eb82e4350421451abb0b2f2a5fd6b62d?sid=d66369d9-bfab-4877-be42-c02eb943ac6e](https://www.loom.com/share/eb82e4350421451abb0b2f2a5fd6b62d?sid=d66369d9-bfab-4877-be42-c02eb943ac6e)

3. [GitHub: https://github.com/villarrealfx/PI-01-MLOps-Henry](https://github.com/villarrealfx/PI-01-MLOps-Henry)

## ETL - (Extract-Transform-Load) 
[ir a ETL](ETL-(Extract-Transform-Load).ipynb)

El proceso de Extracción, transformación y carga ETL, se realizó manteniendo una estructura previamente configurada en un modelo `Kanban` que permitiera desarrollar los pasos necesarios en los tiempos requeridos teniendo como hitos:

1. Visualización General de los datos de los dos (02) datasets suministrados
2. Limpieza de datos.
    * Eliminar filas Duplicadas
    * Verificar integridad de los datos
    * Adecuar los tipos de datos de las columnas que lo nesecitan.
    * Eliminar columnas innecesarias por solicitud explícita en el planteamiento del problema.
    * Eliminar registros con `id` duplicados.
    * Realizar `merge` de los Data Frames.
3. Aplanar columnas anidadas.
    * `belongs_to_collection` : Un diccionario que indica a que franquicia pertenece la película
    * `genres` : Un diccionario que indica todos los géneros asociados a la película.
    * `production_companies` : Lista con las compañias productoras asociadas a la película.
    * `production_countries` : Lista con los países donde se produjo la película.
    * `spoken_languages` : Lista con los idiomas que se hablan en la pelicula
    * `cast` : Actores de la pelicula.
    * `crew` : Directores de la pelicula
4. Imputar valores faltantes en columna `original_language` con el primer lenguaje que se encuentre en la lista de la columna `spoken_languages`.
5. Realizar imputaciones y crear columnas requeridas en el enunciado del problema.
6. Generar archivos .csv con la data limpia. 

## EDA - (Exploratory-Data-Analysis-ML)
[ir a EDA](EDA-(Exploratory-Data-Analysis-ML).ipynb)

Al igual que con el ETL se siguió un procedimiento preestablecido realizando las siguientes tareas:

1. Se revisó el planteamiento del problema de negocio.
2. Se verificó el set de datos después de la limpieza.
3. Se realizó un análisis exploratorio por variable incluyendo estadísticos básicos.
4. Se realizarón cuatro (04) análisis a variables que consideré relevantes.
    * Analisis de variable `genres` donde se intentó visualizar cuales genero de películas  fueron los más realizados.
    * Analisis de la variable `production_countries` tratando de encontrar que paises copan el mercado de producción cinematográfica.
    * Análisis de la variable `budget` observando el comportamiento histórico en cuanto a las recaudaciones.
    * Análisis de variable `overview` obteniendo las palabras que tienen mayor repeticiones en la variable estudiada.

## ML - (Machine Learning)
[ir a ML](ML-(Machine-Learning).ipynb)

El sistema de recomendación utilizado `Content Based Filtering` realizando un algoritmo que busca similitudes entre las diferentes películas.

1. Se procesaron los datos para evitar ambiguedades.
2. Se creó una sopa de palabras con las columnas seleccionadas.
3. Se generó modelo de Machine Learning.
4. Se creó función de recomendación.
5. Se realizó test de prueba manual
6. Se Crearón los archivos .pkl necesarios para llevar a producción el modelo.

## La API

La etapa final del proyecto consistió en la elaboración y deploy de una API que integrara siete (07) endpoints **obligatorios** entre los que se encuentra el sistema de recomendación realizado durante el trayecto, el mismo esta constituido de la siguiente manera:

1. def **peliculas_idioma( *`Idioma`: str* )**:<br>
    Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de películas producidas en ese idioma.

2. def **peliculas_duracion( *`Pelicula`: str* )**:<br>
    Se ingresa una pelicula. Debe devolver la duracion y el año.

3. def **franquicia( *`Franquicia`: str* )**:<br>
    Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio

4. def **peliculas_pais( *`Pais`: str* )**:<br>
    Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.

5. def **productoras_exitosas( *`Productora`: str* )**:<br>
    Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo. 

6. def **get_director( *`nombre_director`* )**:<br>
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

7. def **recomendacion( *`titulo`* )**:<br>
    Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.

La Api fué realizada utilizando el Framework `FastAPI` de python y colocado en producción en `Render` que es un servicio para despliege desde GitHub, se puede consumir la API desde el siguiente enlace https://recomendacion-peliculas-cv.onrender.com/docs.

## Recomendaciones:

Este repositorio es de acceso **público** se recomienda:
1. Realizar `git clone https://github.com/villarrealfx/PI-01-MLOps-Henry.git`.
2. Bajar los archivos `movies_dataset.csv` y `credits.csv` que se encuentran en https://drive.google.com/drive/folders/1hsmKrY2O-nlOF4_BJuEd7ti3MCrF_6Cz?usp=sharing y colocarlos dentro de la carpeta datasets.
3. Crear un entorno virtual de trabajo con alguna herramienta python tal como [venv](https://docs.python.org/3/library/venv.html).
4. instalar las dependencias que se encuentran en el archivo `requirements.txt` utilizando el comando `pip install -r requirements.txt`.

Gracias por su interés en este proyecto, para cualquier comentario o sugerencia puede comunicarse por el correo eléctronico `villarreal.fx@gmail.com`

## Bibliografía
### Libros
1. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow Concepts, Tools, and Techniques to Build Intelligent Systems (2019) Aurélien Géron Published by O’Reilly Media, Inc 
2. Pandas-Cookbook-eBook (2017) Theodore Petrou Packt Publishing
3. Data Engineering with Python (2020) Paul Crickard Packt Publishing

### Páginas web
1. [pandas-Python Data Analysis Library](https://pandas.pydata.org/)
2. [scikit-learn: machine learning in Python](https://scikit-learn.org/stable/)
3. [developers.google](https://developers.google.com/machine-learning/recommendation/content-based/basics?hl=es-419)
4. [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
