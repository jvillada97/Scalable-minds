from pulsar.schema import Record, String
from app.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ProveedorCreadaPayload(Record):
    id = String()
    name = String()

class EventoProveedorCreada(EventoIntegracion):
    data = ProveedorCreadaPayload()        
    