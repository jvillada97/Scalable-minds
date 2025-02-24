import uuid

from pulsar.schema import *
from app.seedwork.infraestructura.utils import time_millis
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica


class Mensaje(ImagenMedica):
    id = String(default=str(uuid.uuid4()))   
    url_imagen = String()