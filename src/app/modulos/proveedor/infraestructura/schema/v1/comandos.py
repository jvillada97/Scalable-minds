from pulsar.schema import Record, String
from dataclasses import dataclass, field
from app.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearProveedorPayload(Record):
    id_usuario = String()

class ComandoCrearProveedor(ComandoIntegracion):
    data = ComandoCrearProveedorPayload() 
    
   
    