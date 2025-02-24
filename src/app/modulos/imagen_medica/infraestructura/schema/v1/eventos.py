from pulsar.schema import *
from app.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ImagenMedicaCreadaPayload(Record):
    id = String()
    url_imagen = String()
    archivo_imagen = String()

class EventoImagenMedicaCreada(EventoIntegracion):
    data = ImagenMedicaCreadaPayload()    
    