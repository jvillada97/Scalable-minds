import uuid

from pulsar.schema import *


class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))   
    url_imagen = String()