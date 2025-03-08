import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_image(root) -> typing.List["ImagenMedica"]:
    response = requests.get(f'https://5001-jvillada97-scalablemind-5s4upqot80m.ws-us118.gitpod.io/imagen-medica')
    imagenes_medicas = []
    for imagenes in response:
        imagenes_medicas.append(ImagenMedica(
            data=imagenes
        ))
    return imagenes_medicas

@strawberry.type
class ImagenMedica:
    data: str

@strawberry.type
class ImagenMedicaRespuesta:
    mensaje: str
    codigo: int






