from pulsar.schema import Record, String
from app.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ProveedorCreadaPayload(Record):
    id = String()
    url_imagen = String()

class EventoProveedorCreada(EventoIntegracion):
    data = ProveedorCreadaPayload()        
    