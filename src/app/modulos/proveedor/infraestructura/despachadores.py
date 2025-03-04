import pulsar
from pulsar.schema import *

from app.modulos.proveedor.infraestructura.schema.v1.eventos import EventoProveedorCreada, ProveedorCreadaPayload
from app.modulos.proveedor.infraestructura.schema.v1.comandos import ComandoCrearProveedor, ComandoCrearProveedorPayload
from app.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoProveedorCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ProveedorCreadaPayload(
            id=evento.id,
            name=evento.name
        )
        evento_integracion = EventoProveedorCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoProveedorCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearProveedorPayload(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoCrearProveedor(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearProveedor))
