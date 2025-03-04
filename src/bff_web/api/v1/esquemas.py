import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_image(root) -> typing.List["Reserva"]:
    imagenes_medicas = requests.get(f'http://localhost:5001/imagen-medica').json()
    return [ImagenMedica(**imagen) for imagen in imagenes ]
    

@strawberry.type
class ImagenMedica:
    data: str

@strawberry.type
class ImagenMedicaRespuesta:
    mensaje: str
    codigo: int






