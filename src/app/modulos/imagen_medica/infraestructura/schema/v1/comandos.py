from pulsar.schema import *
from dataclasses import dataclass, field
from app.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearImagenMedicaPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoCrearImagenMedica(ComandoIntegracion):
    data = ComandoCrearImagenMedicaPayload() 
    
   
    