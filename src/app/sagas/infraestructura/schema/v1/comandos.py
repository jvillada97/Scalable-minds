from pulsar.schema import *
from seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearProveedorSagaPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoCrearProveedorSaga(ComandoIntegracion):
    data = ComandoCrearProveedorSagaPayload()