from pulsar.schema import *
from seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ProveedorSagaCreadoPayload(Record):
    id = String()
    name = String()



class EventoSagaProveedorCreado(EventoIntegracion):
    data = ProveedorSagaCreadoPayload()