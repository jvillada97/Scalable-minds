from pulsar.schema import Record, String
from dataclasses import dataclass, field
from app.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearImagenMedicaPayload(Record):
    id_usuario = String()

class ComandoCrearImagenMedica(ComandoIntegracion):
    data = ComandoCrearImagenMedicaPayload() 
    
   
    