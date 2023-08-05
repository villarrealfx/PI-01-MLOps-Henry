from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn

from typing import Dict, List
import numpy as np

from funtions.funtions import Movies

path = 'datasets/movies_reduced.csv'

# Crear instancia de clase películas
movie = Movies(path=path)
app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')

@app.get("/")
def root():
    return {"message": "Sistema de Recomendación de Películas",
            "Alumno":"Carlos Villarreal",
            "Cohorte":'PT-02'}


@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma:str):
    '''
    Retornar la cantidad de peliculas producidas en el mismo idioma
    '''
    idioma = idioma.strip().lower()
    language = movie.get_lang(idioma)
    if language == False:
        return JSONResponse(
                            status_code=400,
                            content={"message": "El Idioma ingresado no es válido."},
                         )
    
    resul = movie.peliculas_idioma(language[0])
    if  resul > 0:
        return {'Idioma':f'{language[0]} - {language[1]}', 'cantidad':resul} 
    else:
        raise HTTPException(status_code=400, message=f"Ocurrio una excepción, no existen películas registradas en {idioma}.")


@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    '''
    retornar la duracion y el año de estreno de la pelicula pasada por parámetro
    '''
    pelicula = pelicula.strip().lower()
    resul = movie.peliculas_duracion(pelicula=pelicula)

    if  resul == False:
        return JSONResponse(status_code=400,
                            content={'message': f"Ocurrio una excepción, La película {pelicula} no se encuentra registradas en la BBDD ."})
    else:
        return {'Película':pelicula, 'Duración': resul[0], 'Año de Estreno':resul[1]}
    
@app.get('/franquicia/{franquicia}')
async def franquicia(franquicia:str):
    '''
   Retornar la cantidad de peliculas, ganancia total y promedio de la franquicia pasada por parámetros
    
    '''
    franquicia = franquicia.strip().lower()
    resul = movie.franquicia(franquicia)
    if  resul == False:
        return JSONResponse(status_code=400,
                            content={'message': f"Ocurrio una excepción, La franquicia {franquicia} no se encuentra registradas en la BBDD ."})
    else:
        return {'franquicia':franquicia, 'cantidad':resul[0], 'ganancia_total_MM$':resul[1], 'ganancia_promedio_MM$':resul[2]}
    

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    '''
    Retornar la cantidad de peliculas producidas en el pais pasado como parámetro
    
    '''
    pais = pais.strip().lower()
    resul = movie.peliculas_pais(pais)

    return {'pais':pais, 'cantidad':resul}


@app.get('/productoras_exitosas/{productora}')
async def productoras_exitosas(productora:str):
    '''
    Ingresas la productora, entregandote el revunue total y la cantidad de peliculas que realizo 
    
    '''

    productora = productora.strip().lower()

    resul = movie.productoras_exitosas(productora)

    return {'productora':productora, 'revenue_total_MM$': resul[0],'cantidad':resul[1]}


@app.get('/director/{nombre_director}')
def director(nombre_director:str):
    '''
    retorna el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma. En formato lista

    '''
    nombre_director.strip().lower()

    resul = movie.director(nombre_director)
    
    if  resul == False:
        return JSONResponse(status_code=400,
                            content={'message': f"Ocurrio una excepción, El Director {nombre_director} no se encuentra registradas en la BBDD ."})
    else:
        return {'director':nombre_director, 'retorno_total_director': resul[0], 'movies': resul[1]}