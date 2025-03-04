from pulsar.schema import Record, String, Long
from app.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from app.seedwork.infraestructura.utils import time_millis
import uuid

class AnonimizacionCreadaPayload(Record):
    id = String()
    url_imagen = String()

class EventoAnonimizacionCreada(EventoIntegracion):
    
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = AnonimizacionCreadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
         
    